# bouw_tracks.py — van ruwe pings naar losse scheepstracks (LAR-530, stap 1).
#
# Twee bronnen, één recept:
#   --bron <map>  collector-JSONL(.gz) (aisstream-schema; VPS of haal_marinecadastre)
#   --csv  <map>  MarineCadastre-dagen (ais-*.csv.zst) DIRECT — bij landelijke
#                 schaal is csv-parsen 5-10x sneller dan 270 mln json.loads
#
# Het venster is OPTIONEEL. De 14-daagse pilot bakte twee rechthoeken en Lars
# zag het gevolg meteen op de bol: de rivier "hield op" bij lat 35,6 (de
# vensterrand Memphis->Cairo) terwijl de bron daar gewoon data heeft. Zonder
# --venster gaat alles mee.
#
# Track-regels (ongewijzigd):
#   - knip bij een datagat > KNIP_MIN zonder énige ping;
#   - een korte stop (<= STIL_MAX: sluis, even ankeren) knipt NIET; echt
#     aanleggen wél — en dat eindpunt is dok-materiaal voor LAR-531;
#   - een onmogelijke sprong (> MAX_KNOPEN) knipt (dubbel-MMSI-vlechten);
#   - GPS-uitschieters (te snel tegen béide buren) vallen weg;
#   - mini-tracks (< MIN_PUNTEN of < MIN_KM) vallen weg.
#
# Schaal: landelijk passen de pings niet in RAM (28 dagen VS ≈ 270 mln punten).
# Daarom twee passes via bucket-bestanden op schijf: pass 1 streamt de bron en
# schrijft elk punt als 16 bytes naar bucket mmsi % N_BUCKETS; pass 2 bouwt per
# bucket (≈ 1/64e van de data) de tracks. Geheugen blijft ~honderden MB.
#
# Uitvoer: JSONL.gz — één track per regel:
#   {"mmsi": .., "km": .., "dlat": .., "dlon": .., "punten": [[lat,lon,t_min], ..]}
# (dlat/dlon = netto verplaatsing: op-/afvaart-splitsing in de graaf-stap.)

import argparse
import csv
import gzip
import io
import json
import math
import struct
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

VENSTERS = {
    "mississippi-breed": (28.90, -92.50, 35.60, -89.00),
    "ohio-illinois":     (36.50, -90.50, 41.60, -84.00),
    "meren-seaway":      (41.00, -88.00, 47.50, -76.00),
    "rijnmond":          (51.75, 3.85, 52.05, 4.75),
    "rijn-corridor":     (51.15, 4.75, 52.10, 7.00),
}

KNIP_MIN = 30        # minuten zonder énige ping -> nieuwe track (datagat)
STIL_MAX = 90        # minuten stilliggen die een track overleeft; langer = aangelegd
VARE_GRENS = 0.5     # knopen; onder = stilliggend
MAX_KNOPEN = 40      # sneller = GPS-uitschieter of dubbel-MMSI
MIN_PUNTEN = 8
MIN_KM = 2.0
N_BUCKETS = 64

# 16 bytes per ping: mmsi u32 · t_min u32 · lat f32 · lon f32 · sog in 1/10 kn u16 pad
PUNT = struct.Struct("<IIffH2x")

POSITIE_SOORTEN = ("PositionReport", "StandardClassBPositionReport",
                   "ExtendedClassBPositionReport")


def km(lat1, lon1, lat2, lon2):
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1) * math.cos(math.radians((lat1 + lat2) / 2))
    return 6371.0 * math.hypot(dlat, dlon)


# ── pass 1: bron -> buckets ────────────────────────────────────────────────

def stream_jsonl(bron: Path):
    bestanden = sorted(bron.glob("*.jsonl.gz")) + sorted(bron.glob("*.jsonl"))
    bestanden = [b for b in bestanden if not b.name.startswith("ais-")]
    for pad in bestanden:
        opener = gzip.open if pad.suffix == ".gz" else open
        with opener(pad, "rt", encoding="utf-8", errors="replace") as fh:
            while True:
                try:
                    regel = next(fh)
                except StopIteration:
                    break
                except EOFError:
                    break            # levend gegzipt dagbestand — verwacht
                if "PositionReport" not in regel:
                    continue
                try:
                    b = json.loads(regel)
                    bericht = b["Message"]
                    for soort in POSITIE_SOORTEN:
                        if soort in bericht:
                            pr = bericht[soort]
                            break
                    else:
                        continue
                    meta = b["MetaData"]
                    tijd = datetime.strptime(meta["time_utc"][:26],
                                             "%Y-%m-%d %H:%M:%S.%f"
                                             ).replace(tzinfo=timezone.utc)
                    mmsi = meta.get("MMSI")
                    if mmsi is None:
                        continue
                    sog = pr.get("Sog") or 0.0
                    yield (int(mmsi), int(tijd.timestamp() // 60),
                           pr["Latitude"], pr["Longitude"], sog)
                except (json.JSONDecodeError, KeyError, ValueError, TypeError):
                    continue


def stream_csv(bron: Path):
    try:
        import zstandard
    except ImportError:
        sys.exit("pip install zstandard")
    bestanden = sorted(bron.glob("ais-*.csv.zst"))
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    for pad in bestanden:
        t0 = time.monotonic()
        n = 0
        with pad.open("rb") as f:
            lezer = csv.reader(io.TextIOWrapper(
                zstandard.ZstdDecompressor().stream_reader(f), encoding="utf-8"))
            kop = next(lezer)
            ix = {k: i for i, k in enumerate(kop)}
            i_m, i_t = ix["mmsi"], ix["base_date_time"]
            i_la, i_lo, i_s = ix["latitude"], ix["longitude"], ix["sog"]
            for rij in lezer:
                try:
                    # "2025-07-25 00:00:01" — handmatig parsen is ~3x sneller
                    # dan strptime en dit is de hete lus van 270 mln regels
                    ts = rij[i_t]
                    dt = datetime(int(ts[0:4]), int(ts[5:7]), int(ts[8:10]),
                                  int(ts[11:13]), int(ts[14:16]),
                                  tzinfo=timezone.utc)
                    yield (int(rij[i_m]), int((dt - epoch).total_seconds() // 60),
                           float(rij[i_la]), float(rij[i_lo]),
                           float(rij[i_s]) if rij[i_s] else 0.0)
                    n += 1
                except (ValueError, IndexError):
                    continue
        print(f"  {pad.name}: {n:,} posities in {time.monotonic()-t0:.0f}s",
              flush=True)


def vul_buckets(pings, venster, werkmap: Path):
    z = w = n_ = o = None
    if venster:
        z, w, n_, o = venster
    handles = [(werkmap / f"bucket-{i:02d}.bin").open("wb") for i in range(N_BUCKETS)]
    buffers = [bytearray() for _ in range(N_BUCKETS)]
    tot = 0
    for mmsi, t_min, lat, lon, sog in pings:
        if venster and not (z <= lat <= n_ and w <= lon <= o):
            continue
        i = mmsi % N_BUCKETS
        buffers[i] += PUNT.pack(mmsi, t_min, lat, lon,
                                min(int(sog * 10), 65535))
        tot += 1
        if len(buffers[i]) > 1 << 20:
            handles[i].write(buffers[i]); buffers[i] = bytearray()
    for h, buf in zip(handles, buffers):
        h.write(buf); h.close()
    return tot


# ── pass 2: buckets -> tracks ──────────────────────────────────────────────

def bouw_bucket(pad: Path):
    ruw = pad.read_bytes()
    perschip = {}
    for (mmsi, t_min, lat, lon, sog10) in PUNT.iter_unpack(ruw):
        perschip.setdefault(mmsi, []).append((t_min, lat, lon, sog10 / 10.0))

    for mmsi, rijen in perschip.items():
        rijen.sort()
        huidig = []
        laatste_ping = None
        stil_sinds = None

        def sluit():
            nonlocal huidig
            if huidig:
                yield_tracks.append((mmsi, huidig))
                huidig = []

        yield_tracks = []
        for t_min, lat, lon, sog in rijen:
            if sog < VARE_GRENS:
                if stil_sinds is None:
                    stil_sinds = t_min
                if huidig and t_min - stil_sinds > STIL_MAX:
                    yield_tracks.append((mmsi, huidig)); huidig = []
                laatste_ping = t_min
                continue
            if huidig and (
                    (laatste_ping is not None and t_min - laatste_ping > KNIP_MIN)
                    or (stil_sinds is not None and t_min - stil_sinds > STIL_MAX)):
                yield_tracks.append((mmsi, huidig)); huidig = []
            stil_sinds = None
            if huidig and huidig[-1][2] == t_min:
                continue
            if huidig:
                la, lo, tv = huidig[-1]
                dt_uur = max(t_min - tv, 1) / 60.0
                if km(lat, lon, la, lo) / dt_uur > MAX_KNOPEN * 1.852:
                    yield_tracks.append((mmsi, huidig)); huidig = []
            huidig.append((lat, lon, t_min))
            laatste_ping = t_min
        if huidig:
            yield_tracks.append((mmsi, huidig))

        for mmsi_, punten in yield_tracks:
            gefilterd = []
            for i, (lat, lon, t) in enumerate(punten):
                def te_snel(j):
                    la, lo, tj = punten[j]
                    dt_uur = max(abs(t - tj), 1) / 60.0
                    return km(lat, lon, la, lo) / dt_uur > MAX_KNOPEN * 1.852
                if 0 < i < len(punten) - 1 and te_snel(i - 1) and te_snel(i + 1):
                    continue
                gefilterd.append((lat, lon, t))
            lengte = sum(km(*gefilterd[i][:2], *gefilterd[i + 1][:2])
                         for i in range(len(gefilterd) - 1))
            if len(gefilterd) >= MIN_PUNTEN and lengte >= MIN_KM:
                yield {"mmsi": mmsi_, "km": round(lengte, 1),
                       "dlat": round(gefilterd[-1][0] - gefilterd[0][0], 4),
                       "dlon": round(gefilterd[-1][1] - gefilterd[0][1], 4),
                       "punten": [[round(la, 5), round(lo, 5), t]
                                  for la, lo, t in gefilterd]}


def main():
    p = argparse.ArgumentParser(description="Pings -> scheepstracks (LAR-530)")
    p.add_argument("--bron", type=Path, help="map met collector-JSONL(.gz)")
    p.add_argument("--csv", type=Path, help="map met MarineCadastre ais-*.csv.zst")
    p.add_argument("--venster", help=f"optioneel: {', '.join(VENSTERS)} of 'z,w,n,o'")
    p.add_argument("--uit", type=Path, required=True,
                   help=".jsonl.gz — één track per regel")
    args = p.parse_args()
    if not args.bron and not args.csv:
        sys.exit("geef --bron en/of --csv")

    venster = None
    if args.venster:
        venster = (VENSTERS.get(args.venster)
                   or tuple(float(x) for x in args.venster.split(",")))

    begon = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="tracks-", dir=args.uit.parent) as tmp:
        werkmap = Path(tmp)
        tot = 0
        if args.csv:
            tot += vul_buckets(stream_csv(args.csv), venster, werkmap)
        if args.bron:
            tot += vul_buckets(stream_jsonl(args.bron), venster, werkmap)
        print(f"pass 1: {tot:,} pings in {N_BUCKETS} buckets "
              f"({time.monotonic()-begon:.0f}s)", flush=True)

        n_tracks = n_punten = 0
        tot_km = 0.0
        args.uit.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(args.uit, "wt", encoding="utf-8", compresslevel=6) as uit:
            for i in range(N_BUCKETS):
                for track in bouw_bucket(werkmap / f"bucket-{i:02d}.bin"):
                    uit.write(json.dumps(track, separators=(",", ":")) + "\n")
                    n_tracks += 1
                    n_punten += len(track["punten"])
                    tot_km += track["km"]
                if (i + 1) % 16 == 0:
                    print(f"pass 2: bucket {i+1}/{N_BUCKETS} · "
                          f"{n_tracks:,} tracks", flush=True)

    print(f"{n_tracks:,} tracks · {tot_km:,.0f} km · {n_punten:,} punten · "
          f"{time.monotonic()-begon:.0f}s totaal")
    print(f"geschreven: {args.uit} ({args.uit.stat().st_size/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
