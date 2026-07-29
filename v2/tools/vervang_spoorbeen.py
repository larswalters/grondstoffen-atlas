"""vervang_spoorbeen.py — vervang ÉÉN been in een gebakken stroom door een
vers geroutete lijn, zonder de andere benen aan te raken.

Waarom dit bestaat. Een gebakken `stroomroute-*.json` bevat benen uit heel
verschillende bronnen: MARNET-zee, AIS-tracks, de slurryleiding-geometrie, de
Yangtze-bulklaag én het landnet. Wordt alleen het LANDNET herbouwd, dan hoeft
maar één been opnieuw; `hecht_marnet route` opnieuw draaien zou álle benen
opnieuw routeren en daarmee ook de benen veranderen die al goedgekeurd zijn.

En met de hand in het json knippen is precies de val die dit project al eens
duur betaald heeft: een gegenereerd bestand dat met de hand is bijgewerkt loopt
stil uit de pas met zijn generator (Guixi, 741 m). Dus: één commando, in de
geschiedenis terug te vinden, met een controle op de uiteinden.

De uiteinden worden GETOETST, niet aangenomen: als het nieuwe been ergens anders
begint of eindigt dan het oude, klopt de aansluiting op het vorige/volgende been
niet meer en horen de overslagmarkers mee te verschuiven. Boven --max-schuif-km
weigert het script.

Draaien:
    python v2/tools/vervang_spoorbeen.py \
        --stroom v2/data/stroomroute-koper-escondida-guixi.json \
        --modaliteit spoor \
        --geojson v2/build-cache/ais/graaf/spoorroute-xyz.geojson
"""
import argparse
import json
import math
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import bake_marnet as bm   # noqa: E402 — gc_km


def lees_lijn(pad):
    d = json.load(open(pad, encoding="utf-8"))
    g = d["features"][0]["geometry"] if d.get("type") == "FeatureCollection" else d
    if g["type"] == "LineString":
        return [tuple(p) for p in g["coordinates"]]
    if g["type"] == "MultiLineString":
        uit = []
        for deel in g["coordinates"]:
            uit.extend(tuple(p) for p in deel)
        return uit
    raise SystemExit(f"geen (Multi)LineString in {pad}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stroom", required=True)
    ap.add_argument("--modaliteit", required=True,
                    help="welk been vervangen wordt (bv. 'spoor'); moet "
                         "precies één been raken")
    ap.add_argument("--geojson", required=True)
    ap.add_argument("--max-schuif-km", type=float, default=0.5)
    ap.add_argument("--droog", action="store_true", help="alleen rapporteren")
    args = ap.parse_args()

    d = json.load(open(args.stroom, encoding="utf-8"))
    kandidaten = [i for i, b in enumerate(d["benen"])
                  if b["modaliteit"] == args.modaliteit and not b.get("stippel")]
    if len(kandidaten) != 1:
        sys.exit(f"{len(kandidaten)} benen met modaliteit '{args.modaliteit}' "
                 f"— verwacht precies 1")
    i = kandidaten[0]
    been = d["benen"][i]
    oud = [tuple(p) for p in been["punten"]]
    nieuw = lees_lijn(args.geojson)

    # richting: de geojson kan omgekeerd lopen t.o.v. het been
    if (bm.gc_km(nieuw[0], oud[0]) + bm.gc_km(nieuw[-1], oud[-1]) >
            bm.gc_km(nieuw[-1], oud[0]) + bm.gc_km(nieuw[0], oud[-1])):
        nieuw = nieuw[::-1]

    schuif_a = bm.gc_km(nieuw[0], oud[0])
    schuif_z = bm.gc_km(nieuw[-1], oud[-1])
    km_oud = been["km"]
    km_nieuw = sum(bm.gc_km(nieuw[j - 1], nieuw[j]) for j in range(1, len(nieuw)))

    print(f"been [{been['modaliteit']}] {been['naam']}")
    print(f"  punten {len(oud):,} -> {len(nieuw):,}")
    print(f"  km     {km_oud:,.1f} -> {km_nieuw:,.1f} "
          f"({(km_nieuw-km_oud)/max(km_oud,1e-9)*100:+.2f}%)")
    print(f"  begin schuift {schuif_a*1000:,.0f} m · eind schuift "
          f"{schuif_z*1000:,.0f} m")
    if max(schuif_a, schuif_z) > args.max_schuif_km:
        sys.exit(f"GEWEIGERD: een uiteinde schuift meer dan "
                 f"{args.max_schuif_km} km — de aansluiting op het vorige of "
                 f"volgende been klopt dan niet meer, en de overslagmarker "
                 f"hoort mee te verhuizen. Controleer eerst de ankers.")
    if args.droog:
        print("  (droog — niets weggeschreven)")
        return

    been["punten"] = [[round(lo, 5), round(la, 5)] for lo, la in nieuw]
    been["km"] = round(km_nieuw, 1)
    d.setdefault("herkomst", {})[been["modaliteit"]] = {
        "bron": os.path.basename(args.geojson),
        "vervangen": True,
    }
    with open(args.stroom, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
    print(f"  weggeschreven: {args.stroom}")


if __name__ == "__main__":
    main()
