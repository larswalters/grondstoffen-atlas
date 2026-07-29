"""Werker: haal spoor 1-op-1 uit één Geofabrik-extract.

Per extract een geojson in build-cache/raw1op1/. HERVATBAAR: een extract dat al
een uitvoerbestand heeft wordt overgeslagen, dus een crash of afbreken kost
hooguit het bestand waar hij mee bezig was.

Wat er in gaat (bewust ruim — dit is de hele 1-op-1-gedachte):
  · railway=rail|narrow_gauge, INCLUSIEF service=yard|siding|spur|crossover —
    juist die sporen zijn de overlopen tussen parallelle sporen, en zonder die
    verzint de heal-pass ze zelf (Guixi: een naad van 40 m die er in OSM niet is)
Wat eruit blijft:
  · metro/tram/light rail/monorail/funicular — geen goederenspoor
  · construction/proposed/disused/abandoned/razed — ligt er niet
  · usage=tourism|military

De geometrie blijft RAUW: elk OSM-punt blijft staan en niets wordt verschoven.
Dat is de hele voorwaarde — twee ways die een node delen dragen dan exact
dezelfde coördinaat, en de exacte las in bake_landnet.bouw() reproduceert
daarmee OSM's topologie zonder één drempel.

Draaien:  python raw1op1_werker.py <shard> <aantal_shards>
"""
import os, sys, json, time, glob

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HIER))
sys.path.insert(0, HIER)
os.chdir(REPO)
import osmium
import bake_marnet as bm

BRON = os.path.join(REPO, "v2", "build-cache", "geofabrik")
UIT = os.path.join(REPO, "v2", "build-cache", "raw1op1")
os.makedirs(UIT, exist_ok=True)

HOUD = {"rail", "narrow_gauge"}
WEG = {"subway", "tram", "light_rail", "monorail", "funicular", "miniature",
       "construction", "proposed", "disused", "abandoned", "razed",
       "platform", "station", "halt", "turntable", "traverser"}


class Rail(osmium.SimpleHandler):
    def __init__(s):
        super().__init__()
        s.uit = []
        s.service = 0

    def way(s, w):
        t = dict(w.tags)
        rw = t.get("railway")
        if rw not in HOUD:
            return
        if rw in WEG or t.get("usage") in ("tourism", "military"):
            return
        try:
            pts = [[round(bm.wrap_lon(n.lon), 7), round(n.lat, 7)]
                   for n in w.nodes if n.location.valid()]
        except Exception:
            return
        if len(pts) < 2:
            return
        if "service" in t:
            s.service += 1
        s.uit.append((w.id, t.get("gauge") or "onbekend", bool(t.get("highspeed")), pts))


def doe(pbf):
    naam = os.path.basename(pbf)[:-len("-latest.osm.pbf")]
    uit_pad = os.path.join(UIT, f"{naam}.geojson")
    if os.path.exists(uit_pad):
        return naam, None, None, 0.0
    t0 = time.time()
    h = Rail()
    h.apply_file(pbf, locations=True, idx="flex_mem")
    feats = []
    for wid, gauge, hs, pts in h.uit:
        feats.append({
            "type": "Feature",
            "properties": {"label": f"spoor-{naam}-{gauge}", "regio": naam,
                           "modus": "spoor", "gauge": gauge, "hs": hs,
                           "wayId": wid},
            "geometry": {"type": "LineString", "coordinates": pts},
        })
    tmp = uit_pad + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": feats}, f,
                  separators=(",", ":"))
    os.replace(tmp, uit_pad)          # atomair: half bestand kan niet blijven staan
    return naam, len(feats), h.service, time.time() - t0


def main():
    shard, n_shards = int(sys.argv[1]), int(sys.argv[2])
    # op grootte sorteren en round-robin verdelen, zodat de zware extracts
    # (Canada 6,1 GB, Japan 2,4) niet in dezelfde werker belanden
    paden = sorted(glob.glob(os.path.join(BRON, "*.osm.pbf")),
                   key=os.path.getsize, reverse=True)
    mijn = [p for i, p in enumerate(paden) if i % n_shards == shard]
    print(f"werker {shard}/{n_shards}: {len(mijn)} extracts, "
          f"{sum(os.path.getsize(p) for p in mijn)/2**30:.1f} GB", flush=True)
    for i, p in enumerate(mijn, 1):
        naam, n, sv, dt = doe(p)
        if n is None:
            print(f"  [{i}/{len(mijn)}] {naam:<28} overgeslagen (bestaat al)", flush=True)
        else:
            print(f"  [{i}/{len(mijn)}] {naam:<28} {n:7,} ways "
                  f"({sv:,} service) · {dt:.0f} s", flush=True)
    print(f"werker {shard} KLAAR", flush=True)


main()
