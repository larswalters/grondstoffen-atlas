#!/usr/bin/env python3
"""maak_luchtbeen.py — een luchtvrachtbeen als GROOTCIRKEL tussen twee luchthavens
(M31 golf 3, 2026-09-28: goud, PGM en diamant vliegen).

WAAROM EEN GROOTCIRKEL EN GEEN GEMETEN ROUTE. Voor zee, spoor en weg meet dit
project de echte lijn (MARNET, OSM 1-op-1, Overpass), want daar ligt de lading
op een net dat je kunt aanwijzen. Een vlucht heeft geen net op de grond: een
vrachtvliegtuig volgt luchtwegen die per dag verschillen, en die zijn niet vrij
beschikbaar. De grootcirkel is de kortste weg en ligt binnen de marge van wat een
lange-afstandsvlucht werkelijk vliegt. Het is dus een benadering, en dat staat in
de beennaam ("grootcirkel"). Het doorgetrokken been betekent hier "we weten van
welke luchthaven naar welke luchthaven het vliegt", niet "langs deze lijn".

WAT HET NIET IS. Geen stippel: stippel betekent in dit project "hier reikt het
net niet" (werkwijze §7). Een vlucht tussen twee gelegde vrachtterminals is geen
gat maar een gedocumenteerde verbinding, dus doorgetrokken via --been-geojson.

DE BOOG ZIT NIET IN DIT BESTAND. De punten liggen op het oppervlak; de bol tilt
een been met modaliteit "lucht" zelf op (stroomstijl.js, tiltOp). Zo blijft de
gebakken geometrie een geografische claim en is de hoogte een weergavekeuze.

Gebruik (vanuit de repo-root):
    python v2/tools/maak_luchtbeen.py \\
        --van  "OR Tambo vrachtterminal|-26.1290,28.2330" \\
        --naar "Brussels Airport Brucargo|50.9110,4.4630" \\
        --uit  v2/build-cache/ais/graaf/diamant-x-lucht.geojson

    daarna in hecht_marnet.py route:
        --been-geojson "lucht|vlucht JNB → BRU (vrachtvlucht, grootcirkel)|<uit>"

Het ankerpunt is de VRACHTTERMINAL of het vrachtplatform (satelliet-gelegd), niet
het midden van de startbaan: daar sluit het truckbeen aan.
"""
import argparse, json, math, sys
from pathlib import Path

R_KM = 6371.0088

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def punt(spec, vlag):
    """'NAAM|LAT,LON' → (naam, lat, lon)."""
    delen = [d.strip() for d in spec.split("|")]
    if len(delen) != 2 or not all(delen):
        sys.exit(f"{vlag} verwacht 'NAAM|LAT,LON', kreeg: {spec!r}")
    try:
        lat, lon = (float(x) for x in delen[1].split(","))
    except ValueError:
        sys.exit(f"{vlag}: coördinaat niet leesbaar in {spec!r}")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        sys.exit(f"{vlag}: coördinaat buiten bereik in {spec!r} (volgorde is LAT,LON)")
    return delen[0], lat, lon


def grootcirkel(lat1, lon1, lat2, lon2, stap_km):
    """Punten [lon, lat] langs de grootcirkel, hooguit stap_km uit elkaar."""
    f1, l1, f2, l2 = map(math.radians, (lat1, lon1, lat2, lon2))
    d = 2 * math.asin(math.sqrt(math.sin((f2 - f1) / 2) ** 2 +
                                math.cos(f1) * math.cos(f2) * math.sin((l2 - l1) / 2) ** 2))
    km = d * R_KM
    if d < 1e-12:
        return [[lon1, lat1], [lon2, lat2]], 0.0
    n = max(2, math.ceil(km / stap_km))
    uit = []
    for i in range(n + 1):
        t = i / n
        a = math.sin((1 - t) * d) / math.sin(d)
        b = math.sin(t * d) / math.sin(d)
        x = a * math.cos(f1) * math.cos(l1) + b * math.cos(f2) * math.cos(l2)
        y = a * math.cos(f1) * math.sin(l1) + b * math.cos(f2) * math.sin(l2)
        z = a * math.sin(f1) + b * math.sin(f2)
        uit.append([round(math.degrees(math.atan2(y, x)), 5),
                    round(math.degrees(math.atan2(z, math.hypot(x, y))), 5)])
    # Kop en staart letterlijk het anker, niet een afgeronde herberekening ervan.
    uit[0] = [round(lon1, 5), round(lat1, 5)]
    uit[-1] = [round(lon2, 5), round(lat2, 5)]
    return uit, km


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--van", required=True, help="'NAAM|LAT,LON' — vrachtterminal van vertrek")
    ap.add_argument("--naar", required=True, help="'NAAM|LAT,LON' — vrachtterminal van aankomst")
    ap.add_argument("--uit", required=True, help="pad van de GeoJSON die --been-geojson leest")
    ap.add_argument("--stap-km", type=float, default=25.0,
                    help="max. afstand tussen twee punten (default 25 km)")
    a = ap.parse_args()

    nv, la1, lo1 = punt(a.van, "--van")
    nn, la2, lo2 = punt(a.naar, "--naar")
    coords, km = grootcirkel(la1, lo1, la2, lo2, a.stap_km)
    if km < 50:
        print(f"⚠️ luchtbeen van {km:.1f} km — is dit echt een vlucht en geen truckbeen?")

    doc = {"type": "FeatureCollection", "features": [{
        "type": "Feature",
        "properties": {"modaliteit": "lucht", "van": nv, "naar": nn,
                       "km": round(km, 1), "bron": "grootcirkel (maak_luchtbeen.py)"},
        "geometry": {"type": "LineString", "coordinates": coords},
    }]}
    uit = Path(a.uit)
    uit.parent.mkdir(parents=True, exist_ok=True)
    uit.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    print(f"luchtbeen {nv} → {nn}: {km:.1f} km grootcirkel · {len(coords)} punten → {uit}")


if __name__ == "__main__":
    main()
