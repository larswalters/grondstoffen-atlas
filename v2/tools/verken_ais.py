# verken_ais.py — kijk eerst, bouw dan (de satelliet-overlay-les van Tongling).
#
# Leest vensters uit de World Bank "Global Shipping Traffic Density"-raster
# (Data Catalog 0037580, laag Commercial: BULK CARRIER/ORE CARRIER/PUSHER TUG/
# INLAND TANKER e.a., 0,005° ≈ 500 m, AIS-posities jan 2015–feb 2021) en
# schrijft per venster een log-geschaalde PNG + statistieken. Doel: empirisch
# zien hoe helder de vaargeulen in het raster staan — zee, havenaanloop én
# binnenwater — vóór we er een graaf uit afleiden (M27).
#
# De vensters zijn de zwakke plekken van het óude waternet (bewust):
#   tongling   de Yangtze-vlecht waar OSM's watervlak geen waarheid was
#   nederland  Maasvlakte→Rijn, de kolencorridor uit de routebrief
#   patache    de Chileense kust waar het oude zeenet 78–85 km miste
#   shanghai   de Yangtze-mond, drukste aanloop van de koperstroom
#
# Draaien:  python v2/tools/verken_ais.py [venster ...]

import sys
from pathlib import Path

import numpy as np
import rasterio
from rasterio.windows import from_bounds
from PIL import Image

HIER = Path(__file__).resolve().parent
AIS = HIER.parent / "build-cache" / "ais"
TIF = AIS / "commercial" / "ShipDensity_Commercial1.tif"
UIT = AIS / "verken"

# (west, zuid, oost, noord) in graden — ruim genoeg om de corridor te zien,
# klein genoeg om het beeld op pixelniveau te kunnen beoordelen.
VENSTERS = {
    "tongling":  (117.40, 30.65, 118.15, 31.35),   # beide geulen + eiland
    "nederland": (3.40, 51.20, 6.80, 52.40),        # Maasvlakte→Waal→Duitse grens
    "patache":   (-70.75, -21.30, -69.90, -20.10),  # Puerto Patache + kustaanloop
    "shanghai":  (120.60, 30.60, 122.70, 31.90),    # Yangtze-mond + Yangshan
}


def verken(naam: str, bbox, bron) -> None:
    w, z, o, n = bbox
    venster = from_bounds(w, z, o, n, bron.transform)
    data = bron.read(1, window=venster)
    nodata = bron.nodata
    if nodata is not None:
        data = np.where(data == nodata, 0, data)
    data = np.clip(data, 0, None)

    nonzero = data[data > 0]
    print(f"\n== {naam} ==  {data.shape[1]}×{data.shape[0]} cellen  "
          f"({w}..{o} lon, {z}..{n} lat)")
    if nonzero.size == 0:
        print("   LEEG — geen enkele AIS-positie in dit venster")
        return
    pct = 100.0 * nonzero.size / data.size
    p = np.percentile(nonzero, [50, 90, 99, 99.9])
    print(f"   bezet {pct:.1f}% van de cellen · max {data.max():,.0f} posities/cel")
    print(f"   percentielen (van bezette cellen): p50 {p[0]:,.0f} · p90 {p[1]:,.0f} · "
          f"p99 {p[2]:,.0f} · p99,9 {p[3]:,.0f}")

    # Log-schaal: dichtheden lopen orden van grootte uiteen; lineair is één
    # witte havenvlek op zwart. log1p + normeren op p99,9 houdt de geul leesbaar
    # zonder dat de drukste kade alles wegdrukt.
    beeld = np.log1p(data.astype(np.float64))
    top = np.log1p(p[3])
    beeld = np.clip(beeld / top, 0, 1)

    # simpele blauw→wit gradiënt op donkere ondergrond (leest als "waterdrukte")
    rgb = np.zeros((*beeld.shape, 3), dtype=np.uint8)
    rgb[..., 0] = (beeld * 235).astype(np.uint8)          # R
    rgb[..., 1] = (20 + beeld * 225).astype(np.uint8)     # G
    rgb[..., 2] = (40 + beeld * 215).astype(np.uint8)     # B
    Image.fromarray(rgb).save(UIT / f"{naam}.png")
    print(f"   → {UIT / (naam + '.png')}")


def main() -> None:
    UIT.mkdir(parents=True, exist_ok=True)
    gekozen = sys.argv[1:] or list(VENSTERS)
    with rasterio.open(TIF) as bron:
        print(f"raster: {bron.width}×{bron.height} · {bron.dtypes[0]} · "
              f"nodata {bron.nodata} · crs {bron.crs}")
        print(f"resolutie {bron.transform.a:.4f}° ≈ "
              f"{bron.transform.a * 111.32:.0f} m op de evenaar")
        for naam in gekozen:
            verken(naam, VENSTERS[naam], bron)


if __name__ == "__main__":
    main()
