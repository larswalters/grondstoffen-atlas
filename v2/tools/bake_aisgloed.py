# bake_aisgloed.py — de AIS-drukte als GLOED (M27, pilot).
#
# ⚠️ STATUS SINDS 2026-07-25 (M28, LAR-534): deze laag BLIJFT als VISUELE laag —
# hij is alleen geen routeringsbron meer. De vaargraaf komt vanaf nu uit echte
# scheepstracks (aisstream, milestone "M28 · AIS-tracknet", LAR-528 t/m LAR-535);
# het density-raster is nog fallback-bron voor corridors zonder eigen tracks.
#
# Lars' keuze (2026-07-25): niet de geëxtraheerde middellijnen maar het
# dichtheidsveld zélf op de bol — de blauwe gloed van zes jaar scheepvaart,
# zoals de verken_ais.py-PNG's die de bron bewezen. De lijnen (bake_aisnet.py)
# blijven bestaan als graaf-zaad, maar het beeld komt van deze laag.
#
# Per venster: raster lezen → artefact-gaten dichten (1-cels nullen ín een
# geuldraad, de tegelnaden uit de World Bank-verwerking) → log-schaal op de
# p99,9 van het venster → ×3 opschalen + zachte blur (gloed i.p.v. blokjes) →
# blauw→wit-kleurverloop op ZWART. De tekenlaag (aisgloed.js) rendert de PNG
# additief: zwart telt niets op en is dus vanzelf onzichtbaar — geen alpha
# nodig, en de gloed licht op boven donker water én satellietkleur.
#
# Draaien:  python v2/tools/bake_aisgloed.py

import json
from pathlib import Path

import numpy as np
import rasterio
from rasterio.windows import from_bounds
from scipy import ndimage
from PIL import Image, ImageFilter

HIER = Path(__file__).resolve().parent
TIF = HIER.parent / "build-cache" / "ais" / "commercial" / "ShipDensity_Commercial1.tif"
UIT_MAP = HIER.parent / "data" / "aisgloed"

# Dezelfde vensters als bake_aisnet.py / verken_ais.py.
VENSTERS = {
    "tongling":  (117.40, 30.65, 118.15, 31.35),
    "nederland": (3.40, 51.20, 6.80, 52.40),
    "patache":   (-70.75, -21.30, -69.90, -20.10),
    "shanghai":  (120.60, 30.60, 122.70, 31.90),
}

SCHAAL = 3          # opschaalfactor: 500 m-cellen → zachte gloed op de bol
BLUR_PX = 1.0       # Gaussische blur ná het opschalen (in opgeschaalde pixels)
RAND_CELLEN = 10    # randvervaging: het venster dooft zacht uit naar de rand


def dicht_artefacten(data: np.ndarray) -> np.ndarray:
    """Vult exacte-nul-cellen die ≥5 van hun 8 buren bezet hebben met het
    buurgemiddelde — de tegelnaad-gaten in geuldraden, niet echte leegte."""
    positief = data > 0
    buren = ndimage.uniform_filter(positief.astype(np.float64), 3) * 9 - positief
    som = ndimage.uniform_filter(data, 3) * 9 - data
    gat = (~positief) & (buren >= 5)
    uit = data.copy()
    uit[gat] = som[gat] / buren[gat]
    return uit


def bak_venster(naam: str, bbox, bron) -> dict:
    w, z, o, n = bbox
    venster = from_bounds(w, z, o, n, bron.transform)
    data = bron.read(1, window=venster).astype(np.float64)
    if bron.nodata is not None:
        data = np.where(data == bron.nodata, 0, data)
    data = np.clip(data, 0, None)
    data = dicht_artefacten(data)

    nonzero = data[data > 0]
    top = float(np.percentile(nonzero, 99.9)) if nonzero.size else 1.0
    # machtsverloop i.p.v. log: log perst álles bevaren in de topband (een
    # kanaal van 300k en een geul van 17M zaten beide boven 0,85 → één witte
    # vlek); de vierdemachtswortel spreidt kanaal → vaargeul → havenpiek
    t = np.clip(data / top, 0, 1) ** 0.25

    # randvervaging (~10 cellen): het venster dooft zacht uit i.p.v. dat de
    # drukte hard afkapt op de vensterrand
    h, b = t.shape
    rij = np.minimum(np.arange(h), np.arange(h)[::-1])[:, None]
    kol = np.minimum(np.arange(b), np.arange(b)[::-1])[None, :]
    t = t * np.clip(np.minimum(rij, kol) / RAND_CELLEN, 0, 1)

    # blauw → cyaan → wit op ZWART (additief): blauw stijgt als eerste (macht
    # 0,7), groen volgt, rood pas aan de top (macht 2,2) zodat alleen de
    # drukste kades echt wit worden.
    rgb = np.zeros((*t.shape, 3), dtype=np.uint8)
    rgb[..., 0] = (255 * t ** 2.2).astype(np.uint8)
    rgb[..., 1] = (245 * t ** 1.4).astype(np.uint8)
    rgb[..., 2] = (255 * t ** 0.7).astype(np.uint8)

    im = Image.fromarray(rgb)
    im = im.resize((im.width * SCHAAL, im.height * SCHAAL), Image.BICUBIC)
    im = im.filter(ImageFilter.GaussianBlur(BLUR_PX))
    pad = UIT_MAP / f"{naam}.png"
    im.save(pad, optimize=True)

    kb = pad.stat().st_size / 1024
    print(f"  {naam:10s} {im.width}×{im.height} px · top {top:,.0f} · {kb:,.0f} KB")
    return {"bbox": list(bbox), "file": f"aisgloed/{naam}.png", "top": round(top)}


def main() -> None:
    UIT_MAP.mkdir(exist_ok=True)
    vensters = {}
    with rasterio.open(TIF) as bron:
        print("bake_aisgloed · dichtheidsveld → gloed-texturen")
        for naam, bbox in VENSTERS.items():
            vensters[naam] = bak_venster(naam, bbox, bron)

    manifest = {
        "bron": "World Bank / IMF Global Shipping Traffic Density (0037580), "
                "laag Commercial, jan 2015 - feb 2021, CC-BY 4.0",
        "vensters": vensters,
    }
    pad = UIT_MAP / "manifest.json"
    pad.write_text(json.dumps(manifest, separators=(",", ":")), encoding="utf-8")
    print(f"→ {pad.relative_to(HIER.parent)}")


if __name__ == "__main__":
    main()
