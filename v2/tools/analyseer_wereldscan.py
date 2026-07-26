# analyseer_wereldscan.py — vertaal het dekkingsraster naar één bruikbaar oordeel:
# WELKE HAVENS kunnen we uit echte tracks opbouwen, en welke niet?
#
# Het raster uit `ais_wereldscan.py` zegt waar aisstream berichten levert. Dat is
# nog geen antwoord op de vraag die het project stelt — die luidt "tot welke kade
# kunnen we een spoor leggen". Daarom wordt elk van de 3.963 havens uit
# `v2/data/ports.json` gescoord tegen het raster: alle cellen waarvan het midden
# binnen --straal km van de haven ligt.
#
# ⚠️ De scan is een momentopname van een uur. Een drukke haven blijft niet leeg,
# maar een haven met drie scheepsbewegingen per dag kán leeg lijken terwijl er wél
# een station staat. "0 in dit uur" is dus geen bewijs van "geen dekking" — het
# omgekeerde wel: wat binnenkwam, is er aantoonbaar.
#
# Draaien:
#   python v2/tools/analyseer_wereldscan.py v2/build-cache/ais/wereldscan-....json

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

HIER = Path(__file__).resolve().parent
PORTS = HIER.parent / "data" / "ports.json"


def km(lat1, lon1, lat2, lon2) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = (math.sin(dp / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2)
    return 2 * r * math.asin(min(1.0, math.sqrt(a)))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("raster", type=Path)
    p.add_argument("--straal", type=float, default=30.0,
                   help="km rond de haven waarbinnen cellen meetellen")
    p.add_argument("--ports", type=Path, default=PORTS)
    p.add_argument("--top", type=int, default=40)
    p.add_argument("--uit", type=Path, default=None,
                   help="schrijf de per-haven-uitslag als JSON weg")
    args = p.parse_args()

    r = json.loads(args.raster.read_text(encoding="utf-8"))
    graden = r["raster_graden"]
    cellen = {}
    for sleutel, waarden in r["cellen"].items():
        ilat, ilon = (int(x) for x in sleutel.split(","))
        # celmidden
        cellen[(ilat, ilon)] = ((ilat + 0.5) * graden, (ilon + 0.5) * graden,
                                waarden)

    d = json.loads(args.ports.read_text(encoding="utf-8"))
    ll = d["ll"]
    straal_cellen = int(math.ceil(args.straal / (graden * 111.0))) + 1

    rijen = []
    for i, naam in enumerate(d["namen"]):
        lon, lat = ll[2 * i], ll[2 * i + 1]
        ilat, ilon = math.floor(lat / graden), math.floor(lon / graden)
        n = mm = varend = a_ber = b_ber = a_mmsi = b_mmsi = 0
        for dy in range(-straal_cellen, straal_cellen + 1):
            for dx in range(-straal_cellen, straal_cellen + 1):
                cel = cellen.get((ilat + dy, ilon + dx))
                if not cel:
                    continue
                clat, clon, w = cel
                if km(lat, lon, clat, clon) > args.straal:
                    continue
                n += w[0]
                mm += w[1]
                varend += w[2]
                if len(w) >= 7:
                    a_ber += w[3]
                    b_ber += w[4]
                    a_mmsi += w[5]
                    b_mmsi += w[6]
        rijen.append({"naam": naam, "land": d["landen"][i], "lat": lat,
                      "lon": lon, "berichten": n, "mmsi": mm, "varend": varend,
                      "klasseA": a_ber, "klasseB": b_ber,
                      "klasseA_mmsi": a_mmsi, "klasseB_mmsi": b_mmsi})

    met = [x for x in rijen if x["berichten"] > 0]
    varend_havens = [x for x in rijen if x["varend"] > 0]
    minuten = r["minuten"]

    print(f"WERELDSCAN · {minuten:.1f} min · {r['berichten']:,} berichten · "
          f"{r['unieke_mmsi']:,} unieke MMSI · {r['cellen_met_data']:,} cellen "
          f"van {graden}°")
    print(f"\nHAVENS (straal {args.straal:.0f} km, {len(rijen):,} totaal)")
    print(f"  met enig signaal      : {len(met):5,}  "
          f"({100 * len(met) / len(rijen):.1f}%)")
    print(f"  met VAREND verkeer    : {len(varend_havens):5,}  "
          f"({100 * len(varend_havens) / len(rijen):.1f}%)   "
          f"<- hieruit vallen tracks te bouwen")
    print(f"  stil in dit uur       : {len(rijen) - len(met):5,}")

    alleen_b = [x for x in rijen if x["klasseB"] and not x["klasseA"]]
    met_b = [x for x in rijen if x["klasseB"]]
    print(f"\nCLASS B — wat we zónder de omzetting gemist hadden")
    print(f"  havens met Class B-verkeer          : {len(met_b):5,}")
    print(f"  havens die UITSLUITEND Class B zijn : {len(alleen_b):5,}   "
          f"<- die waren volledig onzichtbaar")
    if alleen_b:
        print("  " + " · ".join(
            f"{x['naam']} ({x['land']}, {x['klasseB']})"
            for x in sorted(alleen_b, key=lambda x: -x["klasseB"])[:25]))

    per_land = defaultdict(lambda: [0, 0])
    for x in rijen:
        per_land[x["land"]][0] += 1
        if x["varend"] > 0:
            per_land[x["land"]][1] += 1
    print(f"\nLANDEN ZONDER ENKELE HAVEN MET VAREND VERKEER "
          f"(havens tussen haakjes):")
    leeg = sorted((l for l, (t, v) in per_land.items() if v == 0),
                  key=lambda l: -per_land[l][0])
    print("  " + " · ".join(f"{l} ({per_land[l][0]})" for l in leeg[:60]))

    print(f"\nTOP {args.top} HAVENS OP VAREND VERKEER")
    for x in sorted(rijen, key=lambda x: -x["varend"])[:args.top]:
        print(f"  {x['naam'][:28]:28} {x['land'][:18]:18} "
              f"{x['berichten']:7,} ber · {x['mmsi']:5,} MMSI · "
              f"{x['varend']:6,} varend")

    if args.uit:
        args.uit.write_text(json.dumps({
            "raster": str(args.raster.name), "minuten": minuten,
            "straal_km": args.straal, "havens": rijen,
        }, ensure_ascii=False), encoding="utf-8")
        print(f"\nper-haven-uitslag -> {args.uit}")


if __name__ == "__main__":
    main()
