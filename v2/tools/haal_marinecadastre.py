# haal_marinecadastre.py — de VS-bron voor het tracknet (M28).
#
# MarineCadastre (NOAA + USACE) publiceert per dag alle Amerikaanse AIS-posities
# als CSV.zst — publiek domein, mét de binnenrivieren waar aisstream niets
# ontvangt (pilot 2025-07-25: mississippi-venster 768 ber/min tegen 0 bij
# aisstream, en scheepstype 31 = duwboot domineert er).
#
# Dit script downloadt dagen en zet ze om naar exact de JSONL-vorm die de
# collector op de VPS schrijft (aisstream-schema). Waarom die omweg: alles
# stroomafwaarts — de track-bouwer (LAR-530), de terminal-typering (LAR-531) —
# hoeft dan maar één formaat te kennen. De bron verschilt, het recept niet.
#
#   PositionReport                 <- transceiver A
#   StandardClassBPositionReport   <- transceiver B
#   ShipStaticData                 <- 1x per MMSI per dag (type/lengte/breedte/
#                                     diepgang staan in de CSV op élke regel)
#
# Gebruik:
#   python tools/haal_marinecadastre.py 2025-07-25 [2025-07-26 ...]
#   python tools/haal_marinecadastre.py 2025-07-01..2025-07-07
#
# Uitvoer: build-cache/ais/marinecadastre/YYYY-MM-DD.jsonl.gz (+ de ruwe .csv.zst
# blijft ernaast staan zodat een rijker recept nooit een nieuwe download kost).
#
# ⚠️ De bron loopt per kwartaal achter (geen live feed). Voor de graaf is dat
# irrelevant: een vaargeul verplaatst zich niet per kwartaal.

import csv
import gzip
import io
import json
import sys
import time
import urllib.request
from pathlib import Path

try:
    import zstandard
except ImportError:
    sys.exit("pip install zstandard")

BASIS_URL = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/{jaar}/ais-{dag}.csv.zst"
CACHE = Path(__file__).resolve().parent.parent / "build-cache" / "ais" / "marinecadastre"


def dagen_uit_args(args):
    dagen = []
    for a in args:
        if ".." in a:
            van, tot = a.split("..")
            d = __import__("datetime").date.fromisoformat(van)
            tot_d = __import__("datetime").date.fromisoformat(tot)
            while d <= tot_d:
                dagen.append(d.isoformat())
                d += __import__("datetime").timedelta(days=1)
        else:
            dagen.append(a)
    return dagen


def download(dag: str) -> Path:
    doel = CACHE / f"ais-{dag}.csv.zst"
    if doel.exists() and doel.stat().st_size > 1_000_000:
        print(f"  {doel.name} staat er al ({doel.stat().st_size/1e6:.0f} MB)")
        return doel
    url = BASIS_URL.format(jaar=dag[:4], dag=dag)
    print(f"  downloaden: {url}")
    tijdelijk = doel.with_suffix(".tmp")
    with urllib.request.urlopen(url, timeout=120) as r, tijdelijk.open("wb") as f:
        while blok := r.read(1 << 20):
            f.write(blok)
    # de 0-byte-val: controleer de grootte, niet de HTTP-status
    if tijdelijk.stat().st_size < 1_000_000:
        tijdelijk.unlink()
        raise RuntimeError(f"download van {dag} verdacht klein — bestaat de dag wel?")
    tijdelijk.replace(doel)
    print(f"  {doel.name}: {doel.stat().st_size/1e6:.0f} MB")
    return doel


def zet_om(csv_pad: Path, dag: str) -> Path:
    """CSV.zst -> collector-JSONL.gz. Statische data (type/maten) zit in de CSV
    op elke regel; we schrijven per MMSI één ShipStaticData bij de eerste keer
    dat de velden gevuld zijn."""
    doel = CACHE / f"{dag}.jsonl.gz"
    if doel.exists() and doel.stat().st_size > 1_000_000:
        print(f"  {doel.name} staat er al")
        return doel

    begon = time.monotonic()
    n_pos = n_stat = 0
    statisch_gezien = set()
    tijdelijk = doel.with_suffix(".tmp")
    with csv_pad.open("rb") as f_in, gzip.open(tijdelijk, "wt", encoding="utf-8",
                                               compresslevel=6) as f_uit:
        lezer = csv.reader(io.TextIOWrapper(
            zstandard.ZstdDecompressor().stream_reader(f_in), encoding="utf-8"))
        kop = next(lezer)
        ix = {k: i for i, k in enumerate(kop)}

        def veld(rij, naam, conv=float):
            w = rij[ix[naam]]
            if w == "":
                return None
            try:
                return conv(w)
            except ValueError:
                return None

        for rij in lezer:
            lat = veld(rij, "latitude")
            lon = veld(rij, "longitude")
            mmsi = veld(rij, "mmsi", int)
            if lat is None or lon is None or mmsi is None:
                continue
            # "2025-07-25 00:00:01" -> aisstream-vorm met fracties + zone
            tijd = rij[ix["base_date_time"]] + ".000000000 +0000 UTC"
            naam_schip = rij[ix["vessel_name"]]
            meta = {"MMSI": mmsi, "ShipName": naam_schip, "time_utc": tijd,
                    "latitude": lat, "longitude": lon}

            klasse_b = rij[ix["transceiver"]] == "B"
            positie = {"Latitude": lat, "Longitude": lon,
                       "Sog": veld(rij, "sog"), "Cog": veld(rij, "cog")}
            if klasse_b:
                soort = "StandardClassBPositionReport"
            else:
                soort = "PositionReport"
                positie["NavigationalStatus"] = veld(rij, "status", int)
            f_uit.write(json.dumps({"Message": {soort: positie},
                                    "MessageType": soort,
                                    "MetaData": meta},
                                   separators=(",", ":")) + "\n")
            n_pos += 1

            if mmsi not in statisch_gezien:
                stype = veld(rij, "vessel_type", int)
                lengte = veld(rij, "length")
                if stype is not None or lengte is not None:
                    statisch_gezien.add(mmsi)
                    ssd = {"Type": stype, "Name": naam_schip,
                           "Dimension": {"A": lengte or 0, "B": 0,
                                         "C": veld(rij, "width") or 0, "D": 0},
                           "MaximumStaticDraught": veld(rij, "draft")}
                    f_uit.write(json.dumps({"Message": {"ShipStaticData": ssd},
                                            "MessageType": "ShipStaticData",
                                            "MetaData": meta},
                                           separators=(",", ":")) + "\n")
                    n_stat += 1
    tijdelijk.replace(doel)
    print(f"  {doel.name}: {n_pos:,} posities + {n_stat:,} statisch, "
          f"{doel.stat().st_size/1e6:.0f} MB in {time.monotonic()-begon:.0f}s")
    return doel


def main():
    dagen = dagen_uit_args(sys.argv[1:])
    if not dagen:
        sys.exit("geef dagen op: 2025-07-25 of 2025-07-01..2025-07-07")
    CACHE.mkdir(parents=True, exist_ok=True)
    for dag in dagen:
        print(f"{dag}:")
        zet_om(download(dag), dag)


if __name__ == "__main__":
    main()
