"""Satelliet-overlay voor het SATELLIET-LEGGEN van route-ankers (routebrief-werkwijze §2).

Stitcht Esri World Imagery-tegels rond een kandidaatpunt, tekent een graden-grid en een
kruis op het punt, en schrijft een PNG naar `v2/build-cache/satcheck/`. Daarna kijk je
ernaar en schuif je het punt tot het zichtbaar op de kade/laadplek ligt.

    python v2/tools/sat_check.py <naam> <lat> <lon> [--z 16] [--tegels 5] [--grid 0.005]
    python v2/tools/sat_check.py --lijst punten.txt      # regels: naam lat lon [z] [tegels]

⚠️ Werkwijze §2: een bron- of OSM-coördinaat is een KANDIDAAT. Pas na deze pass — en pas
als je zelf op het beeld hebt gekeken — heet een laad-/overslag-/losplek een ANKER.
Route-uiteinden vragen **z16**; een haven of fabriek is kleiner dan de z13-korrel.

Herkomst: gebouwd in de ankercheck-ronde van 2026-07-28 (toen nog in een scratchpad, wat
hem na die sessie onvindbaar maakte — dezelfde klasse als de generator-drift van Guixi:
gereedschap dat het recept draagt hoort in de repo).
"""
import argparse
import math
import os
import sys
import urllib.request

from PIL import Image, ImageDraw

TEGEL = ("https://server.arcgisonline.com/ArcGIS/rest/services/"
         "World_Imagery/MapServer/tile/{z}/{y}/{x}")
# Esri Wayback: hetzelfde beeld, maar per ARCHIEFVERSIE. Nodig omdat een pass ook kan
# falen doordat de opname OUDER is dan de infrastructuur (Bunbury Shed 8-8, 2026-07-29).
# Releaselijst: https://s3-us-west-2.amazonaws.com/config.maptiles.arcgis.com/waybackconfig.json
TEGEL_WAYBACK = ("https://wayback.maptiles.arcgis.com/arcgis/rest/services/"
                 "World_Imagery/WMTS/1.0.0/default028mm/MapServer/tile/{rel}/{z}/{y}/{x}")
WAYBACK_CONFIG = ("https://s3-us-west-2.amazonaws.com/config.maptiles.arcgis.com/"
                  "waybackconfig.json")
UA = {"User-Agent": "grondstoffen-atlas/1.0 (routebrief anker-check)"}
TS = 256
WORTEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # …/v2
UIT = os.path.join(WORTEL, "build-cache", "satcheck")
CACHE = os.path.join(UIT, "tegelcache")
RELEASE = None      # None = de huidige (live) World Imagery-laag


def tegel_xy(lon, lat, z):
    n = 2 ** z
    x = (lon + 180.0) / 360.0 * n
    la = math.radians(lat)
    y = (1.0 - math.log(math.tan(la) + 1.0 / math.cos(la)) / math.pi) / 2.0 * n
    return x, y


def lon_lat(x, y, z):
    n = 2 ** z
    lon = x / n * 360.0 - 180.0
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))
    return lon, lat


def haal(z, x, y):
    tak = "live" if RELEASE is None else f"wb{RELEASE}"
    pad = os.path.join(CACHE, tak, str(z), str(y))
    os.makedirs(pad, exist_ok=True)
    bestand = os.path.join(pad, f"{x}.jpg")
    if not os.path.exists(bestand):
        url = (TEGEL.format(z=z, x=x, y=y) if RELEASE is None
               else TEGEL_WAYBACK.format(rel=RELEASE, z=z, x=x, y=y))
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r, open(bestand, "wb") as f:
            f.write(r.read())
    return Image.open(bestand).convert("RGB")


def wayback_lijst(n=12):
    """Print de n nieuwste Wayback-releases (id + datum)."""
    import json
    req = urllib.request.Request(WAYBACK_CONFIG, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        js = json.loads(r.read())
    rijen = sorted((v.get("itemTitle", ""), k) for k, v in js.items())
    for titel, rel in rijen[-n:]:
        print(f"  {rel:>7}  {titel}")


def overlay(naam, lat, lon, z=16, tegels=5, grid=0.005):
    """tegels x tegels mozaïek rond (lat, lon); grid in graden."""
    os.makedirs(UIT, exist_ok=True)
    cx, cy = tegel_xy(lon, lat, z)
    x0, y0 = int(cx) - tegels // 2, int(cy) - tegels // 2
    beeld = Image.new("RGB", (TS * tegels, TS * tegels))
    for i in range(tegels):
        for j in range(tegels):
            try:
                beeld.paste(haal(z, x0 + i, y0 + j), (i * TS, j * TS))
            except Exception as e:       # ontbrekende tegel = zwart vlak, geen crash
                print(f"  ! tegel {z}/{x0+i}/{y0+j}: {e}")
    d = ImageDraw.Draw(beeld)

    def naar_px(plon, plat):
        px, py = tegel_xy(plon, plat, z)
        return ((px - x0) * TS, (py - y0) * TS)

    lon_a, lat_a = lon_lat(x0, y0, z)
    lon_b, lat_b = lon_lat(x0 + tegels, y0 + tegels, z)
    lo1, lo2 = min(lon_a, lon_b), max(lon_a, lon_b)
    la1, la2 = min(lat_a, lat_b), max(lat_a, lat_b)

    v = math.floor(lo1 / grid) * grid
    while v <= lo2:
        px, _ = naar_px(v, lat)
        d.line([(px, 0), (px, beeld.height)], fill=(255, 230, 0), width=1)
        d.text((px + 3, 4), f"{v:.3f}", fill=(255, 230, 0))
        v += grid
    v = math.floor(la1 / grid) * grid
    while v <= la2:
        _, py = naar_px(lon, v)
        d.line([(0, py), (beeld.width, py)], fill=(255, 230, 0), width=1)
        d.text((4, py + 3), f"{v:.3f}", fill=(255, 230, 0))
        v += grid

    px, py = naar_px(lon, lat)
    r = 26
    d.line([(px - r, py), (px + r, py)], fill=(255, 40, 40), width=3)
    d.line([(px, py - r), (px, py + r)], fill=(255, 40, 40), width=3)
    d.ellipse([px - 8, py - 8, px + 8, py + 8], outline=(255, 40, 40), width=3)

    mpp = 156543.03392 * math.cos(math.radians(lat)) / (2 ** z)
    merk = "live" if RELEASE is None else f"wayback {RELEASE}"
    d.rectangle([6, beeld.height - 30, 430, beeld.height - 6], fill=(0, 0, 0))
    d.text((12, beeld.height - 24),
           f"{naam}  {lat:.5f},{lon:.5f}  z{z}  {mpp:.2f} m/px  grid {grid}deg  {merk}",
           fill=(255, 255, 255))

    achter = "" if RELEASE is None else f"-wb{RELEASE}"
    pad = os.path.join(UIT, f"sat-{naam}{achter}.png")
    beeld.save(pad)
    print(f"{pad}  ({mpp:.2f} m/px, beeld {beeld.width}px = "
          f"{beeld.width * mpp / 1000:.2f} km breed)")
    return pad


def main():
    p = argparse.ArgumentParser(description=__doc__,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("naam", nargs="?")
    p.add_argument("lat", nargs="?", type=float)
    p.add_argument("lon", nargs="?", type=float)
    p.add_argument("--z", type=int, default=16)
    p.add_argument("--tegels", type=int, default=5)
    p.add_argument("--grid", type=float, default=0.005)
    p.add_argument("--lijst", help="bestand met regels: naam lat lon [z] [tegels]")
    p.add_argument("--wayback", help="Esri Wayback-release-id i.p.v. de live laag")
    p.add_argument("--wayback-lijst", action="store_true",
                   help="toon de nieuwste Wayback-releases (id + datum) en stop")
    a = p.parse_args()

    if a.wayback_lijst:
        wayback_lijst()
        return
    if a.wayback:
        global RELEASE
        RELEASE = a.wayback

    if a.lijst:
        with open(a.lijst, encoding="utf-8") as f:
            for regel in f:
                regel = regel.split("#")[0].strip()
                if not regel:
                    continue
                d = regel.split()
                naam, lat, lon = d[0], float(d[1]), float(d[2])
                z = int(d[3]) if len(d) > 3 else a.z
                t = int(d[4]) if len(d) > 4 else a.tegels
                print(f"— {naam}")
                overlay(naam, lat, lon, z=z, tegels=t, grid=a.grid)
        return
    if not a.naam or a.lat is None or a.lon is None:
        p.error("geef naam lat lon, of --lijst")
    overlay(a.naam, a.lat, a.lon, z=a.z, tegels=a.tegels, grid=a.grid)


if __name__ == "__main__":
    sys.exit(main())
