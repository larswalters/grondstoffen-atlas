"""Meet wat een Geofabrik-regio-extract aan bruikbaar spoor bevat (M25 · LAR-491).

Waarom dit bestaat: vóór M25 gebouwd wordt moet vaststaan (a) dat het spoorfilter
de juiste lijnen overhoudt in regio's waar OSM slecht getagd is, en (b) hoeveel
knopen een compleet spoornet kost. Dit script beantwoordt allebei zonder dat er
iets gebakken hoeft te worden.

HET FILTER WERKT DOOR UITSLUITING, NIET DOOR INSLUITING. `usage=main` eisen lijkt
netjes maar sloopt precies de regio's waar de atlas z'n corridors heeft: 40%
(Myanmar) tot 43% (China) van de spoor-ways draagt géén usage-tag, en in Myanmar
dragen die ongetagde ways 843 km = 13% van het net.

Gevalideerd tegen gepubliceerde route-lengtes (2026-07-19):

    regio      ongefilterd   na filter   gepubliceerd            afwijking
    Cambodja        676 km      652 km    ~650                        ~0%
    Myanmar       7.167 km    6.643 km    6.207,6 (ministerie)        +7%
    China       352.375 km  266.146 km    109.767 (Wereldbank)      +142%

⚠️ Die +142% is GEEN meetfout maar de kern van het probleem: `tracks=2` staat in
China op maar 5.406 ways, dus vrijwel al het dubbelspoor is gemapt als twéé losse
parallelle lijnen. De lengtetoets — onze enige echte controle op land — meet daar
dus 2,4x te veel, en de graaf verdubbelt gratis mee. Parallelle sporen samenvouwen
tot één middellijn is de stap die M24 niet nodig had (rivieren komen niet in
paren). Myanmar/Cambodja vallen er niet in omdat ze enkelspoor zijn.

Gebruik:
    python v2/tools/meet_spoor.py v2/build-cache/geofabrik/china-latest.osm.pbf [...]

Extracts komen uit het Geofabrik-pad van fetch_waterways.py:
    python v2/tools/fetch_waterways.py geofabrik --download

Alleen lezen — raakt geen data en geen cache aan. 1,56 GB scant in ~34 s.
"""
import sys
import os
import math
from collections import Counter

import osmium

R_AARDE = 6371.0

# Houden: alleen wat een goederentrein kan dragen. narrow_gauge blijft erin —
# in Afrika en Zuidoost-Azië is dát het hoofdnet (TAZARA is 1067 mm).
RAIL_TYPES = {"rail", "narrow_gauge"}

# Weggooien op usage. De rest van de uitsluiting gebeurt op `service` (yard,
# siding, spur, crossover) en op de railway-waarde zelf (abandoned, disused,
# razed, construction, proposed, tram, subway, light_rail vallen buiten
# RAIL_TYPES en komen dus nooit binnen).
DROP_USAGE = {"tourism", "military"}


def km(a, b):
    """Haversine tussen (lon,lat)-paren — zelfde formule als fetch_waterways."""
    (lo1, la1), (lo2, la2) = a, b
    p1, p2 = math.radians(la1), math.radians(la2)
    dp, dl = p2 - p1, math.radians(lo2 - lo1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_AARDE * math.asin(min(1.0, math.sqrt(h)))


def lengte(pts):
    return sum(km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def meet(pad):
    railway_val = Counter()      # alle railway=* waarden die langskomen
    usage_val = Counter()        # usage=* binnen de rail-typen
    service_val = Counter()
    tracks_val = Counter()

    km_totaal = 0.0              # rail + narrow_gauge, ongefilterd
    km_houden = 0.0              # na uitsluiting
    km_per_usage = Counter()
    vertices_houden = 0
    ways_houden = 0

    fp = (osmium.FileProcessor(pad)
          .with_locations()
          .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
          .with_filter(osmium.filter.KeyFilter("railway")))

    for obj in fp:
        t = obj.tags
        rw = t.get("railway")
        railway_val[rw] += 1
        if rw not in RAIL_TYPES:
            continue

        pts = [(n.location.lon, n.location.lat) for n in obj.nodes
               if n.location.valid()]
        if len(pts) < 2:
            continue
        L = lengte(pts)
        km_totaal += L

        usage = t.get("usage")
        service = t.get("service")
        usage_val[usage or "(geen)"] += 1
        if service:
            service_val[service] += 1
        if t.get("tracks"):
            tracks_val[t["tracks"]] += 1

        if service:                       # yard / siding / spur / crossover
            continue
        if usage in DROP_USAGE:
            continue

        km_houden += L
        km_per_usage[usage or "(geen)"] += L
        vertices_houden += len(pts)
        ways_houden += 1

    return dict(railway_val=railway_val, usage_val=usage_val,
                service_val=service_val, tracks_val=tracks_val,
                km_totaal=km_totaal, km_houden=km_houden,
                km_per_usage=km_per_usage, vertices_houden=vertices_houden,
                ways_houden=ways_houden)


def rapport(naam, r):
    print(f"\n{'=' * 62}\n{naam}\n{'=' * 62}")
    print("railway=*  :", ", ".join(f"{k}={v}" for k, v in r["railway_val"].most_common(8)))
    print(f"\nrail+narrow_gauge ongefilterd : {r['km_totaal']:>10,.0f} km")
    print(f"na uitsluiting (het filter)   : {r['km_houden']:>10,.0f} km"
          f"   ({100 * r['km_houden'] / max(r['km_totaal'], 1):.0f}%)")
    print(f"  ways={r['ways_houden']:,}  vertices={r['vertices_houden']:,}"
          f"  ({r['vertices_houden'] / max(r['km_houden'], 1):.1f}/km)")

    tot_ways = sum(r["usage_val"].values())
    geen = r["usage_val"].get("(geen)", 0)
    print(f"\nusage-tag ONTBREEKT op {geen:,}/{tot_ways:,} ways "
          f"({100 * geen / max(tot_ways, 1):.0f}%)  <- daarom uitsluiten ipv insluiten")
    print("usage=*    :", ", ".join(f"{k}={v}" for k, v in r["usage_val"].most_common(6)))
    print("km per usage:", ", ".join(f"{k}={v:,.0f}" for k, v in r["km_per_usage"].most_common(6)))
    print("service=*  :", ", ".join(f"{k}={v}" for k, v in r["service_val"].most_common(5)) or "(geen)")
    # tracks=2 zegt "dubbelspoor als één lijn gemapt"; staat het er nauwelijks,
    # dan liggen de sporen als losse parallelle lijnen en meet de lengte dubbel.
    print("tracks=*   :", ", ".join(f"{k}={v}" for k, v in r["tracks_val"].most_common(4)) or "(geen)")

    print(f"\nbudget: {r['km_houden'] / 5.0:>10,.0f} knopen bij 5 km bemonstering")
    print(f"        {r['km_houden'] / 10.0:>10,.0f} knopen bij 10 km")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for pad in sys.argv[1:]:
        if not os.path.exists(pad):
            print(f"ontbreekt: {pad}")
            continue
        rapport(os.path.basename(pad), meet(pad))
