#!/usr/bin/env python3
"""fetch_service_lastmile.py — het INDUSTRIËLE LAST-MILE-SPOOR (M26).

Waarom dit bestaat: `fetch_landnet.spoor_houden()` gooit ALLE `service=`-rail weg
(yard/siding/spur/crossover). Dat is bewust — service-rail globaal insluiten blies
de China-ijking +142/+22% op en jaagt de componenten omhoog. Maar het is óók
precies het spoor dat de keten nodig heeft: de siding/spur die een smelter of
terminal aan de hoofdlijn knoopt. Gevolg (gemeten met toets_spoor_aansluiting.mjs):
22 aansluitingen staan AFGEKNIPT — een gemapte stub bij de plant, los van het
hoofdnet, precies waar de service-spur is weggefilterd (Tongling bewees het:
0,9 km `service=spur` + `service=siding` binnen 3 km, allemaal gedropt).

De veilige fix is NIET het globale filter aanzetten, maar deze ADDITIEVE pass:
`service=spur|siding`-rail insluiten ALLEEN binnen een straal van de aangewezen
aansluitingen, als extra last-mile-lijnen. Het globale hoofdnet blijft ongemoeid
(de bake leest de regio-geojsons onaangeroerd erbij), de ijking wordt niet geraakt,
en `bake_landnet` laat coïncidente vertices (~1 m) samenvallen — dus een spur die
in OSM op een gedeelde knoop aan de zijlijn hangt, verbindt vanzelf.

Uitvoer: build-cache/landnet_lastmile.geojson (label "spoor-lastmile"), die
`bake_landnet` via zijn `landnet_*.geojson`-glob vanzelf meebakt.

Draaien:  python v2/tools/fetch_service_lastmile.py
Daarna:   python v2/tools/bake_landnet.py --suffix -t   (toetsen vóór live)
"""

import json
import math
import os
import sys

import osmium

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import fetch_waterways as fw  # noqa: E402 — extract_pad

STRAAL_KM = 7.0                       # ruim: dekt de hoofdlijn (Tongling-hoofdnet op ~5,3 km van de kade)
# spur/siding zijn de connectors; yard (rangeerterrein) verbindt bij grote plants
# de siding aan de hoofdlijn (Tongling: 89 yard-ways overbruggen het 699 m-gat).
# Yard GLOBAAL insluiten blies de China-ijking +22% op — maar hier alléén binnen
# de straal van de aangewezen aansluitingen, en de drop gooit onverbonden yard weg.
SERVICE_OK = {"spur", "siding", "yard"}
RAILWAY_OK = {"rail", "narrow_gauge"}

# aansluiting-id → extract-sleutel (de Geofabrik-regio waar het punt in ligt)
PUNT_EXTRACT = {
    "cu-shanghai-kade": "china", "cu-tongling-kade": "china",
    "cu-beilun-kade": "china", "cu-guixi-spoor": "china",
    "cu-collahuasi-laad": "chili", "cu-patache-kade": "chili",
    "cu-escondida-laad": "chili", "cu-coloso-kade": "chili",
    "cu-lobito-kade": "angola",
    "cu-rotterdam-kade": "nederland", "coal-rotterdam-kade": "nederland",
    "cu-duisburg-kade": "de-nrw", "coal-duisburg-kade": "de-nrw",
    "coal-cerrejon-laad": "colombia", "coal-bolivar-kade": "colombia",
}
REGIO_VAN = {"china": "cn", "chili": "sa", "angola": "af",
             "nederland": "eu", "de-nrw": "eu", "colombia": "sa"}


def km(lo1, la1, lo2, la2):
    r = math.pi / 180
    return 6371 * math.acos(min(1, math.sin(la1 * r) * math.sin(la2 * r)
                            + math.cos(la1 * r) * math.cos(la2 * r) * math.cos((lo2 - lo1) * r)))


class Scan(osmium.SimpleHandler):
    def __init__(self, punten):
        super().__init__()
        self.punten = punten                 # [(id, lon, lat), ...] in deze extract
        self.features = []
        self.per_punt = {p[0]: 0 for p in punten}

    def way(self, w):
        if (w.tags.get("railway") or "") not in RAILWAY_OK:
            return
        if (w.tags.get("service") or "") not in SERVICE_OK:
            return
        try:
            pts = [(n.lon, n.lat) for n in w.nodes if n.location.valid()]
        except Exception:
            return
        if len(pts) < 2:
            return
        # binnen STRAAL_KM van een aansluiting?
        beste_id, beste_d = None, 1e9
        for pid, plo, pla in self.punten:
            d = min(km(plo, pla, lo, la) for lo, la in pts)
            if d < beste_d:
                beste_d, beste_id = d, pid
        if beste_d > STRAAL_KM:
            return
        self.per_punt[beste_id] += 1
        self.features.append({
            "type": "Feature",
            "properties": {
                "label": "spoor-lastmile", "regio": None, "modus": "spoor",
                "gauge": "onbekend", "service": w.tags.get("service"),
                "bijAansluiting": beste_id, "afstandKm": round(beste_d, 2),
                "wayId": w.id,
                "bron": "OSM service=spur|siding (ODbL) via Geofabrik-extract — "
                        "industriële last-mile bij een aangewezen aansluiting",
            },
            "geometry": {"type": "LineString",
                         "coordinates": [[round(lo, 6), round(la, 6)] for lo, la in pts]},
        })


def main():
    ans = json.load(open(os.path.join(V2, "data", "aansluitingen.json"), encoding="utf-8"))
    plek = {a["id"]: a["plek"] for a in ans["aansluitingen"]}

    per_extract = {}
    for pid, ext in PUNT_EXTRACT.items():
        if pid in plek:
            per_extract.setdefault(ext, []).append((pid, plek[pid][0], plek[pid][1]))

    alle_features = []
    for ext, punten in per_extract.items():
        pad = fw.extract_pad(ext)
        if not os.path.exists(pad):
            print(f"⚠️  extract ontbreekt: {ext} ({pad}) — overslaan")
            continue
        print(f"scan {ext} ({os.path.getsize(pad)/1e9:.2f} GB) voor {len(punten)} punten …", flush=True)
        h = Scan(punten)
        h.apply_file(pad, locations=True)
        for f in h.features:
            f["properties"]["regio"] = REGIO_VAN.get(ext, "xx")
        alle_features.extend(h.features)
        for pid, n in h.per_punt.items():
            print(f"    {pid:<20} {n:3} service-ways ≤ {STRAAL_KM:.0f} km")

    uit = os.path.join(V2, "build-cache", "landnet_lastmile.geojson")
    json.dump({"type": "FeatureCollection", "features": alle_features},
              open(uit, "w", encoding="utf-8"))
    tot_km = sum(sum(fw.km(f["geometry"]["coordinates"][i], f["geometry"]["coordinates"][i + 1])
                     for i in range(len(f["geometry"]["coordinates"]) - 1))
                 for f in alle_features)
    print(f"\n{len(alle_features)} last-mile-ways · {tot_km:.1f} km → {uit}")


if __name__ == "__main__":
    main()
