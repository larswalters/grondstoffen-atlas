# ais_pings_publiceren.py — de pings-debuglaag voeden (LAR-535).
#
# Draait op de VPS als systemd-timer naast de collector. Leest de recente ruwe
# JSONL, dunt hem uit tot iets wat een telefoon aankan, en schrijft één compact
# bestand dat de atlas (statische GitHub Pages) rechtstreeks kan fetchen.
#
# Waarom dit bestaat: de atlas kan niet in de JSONL op de VPS kijken, en zonder
# venster op wat er binnenkomt is dekking niet te beoordelen. Met deze laag zie
# je een leeg stuk rivier meteen als "geen station" in plaats van het pas weken
# later in de graaf te ontdekken.
#
# Vorm van de uitvoer — gegroepeerd per schip, want dan kun je én punten tekenen
# én zien welke pings bij elkaar horen (de voorloper van de echte tracks uit
# LAR-530):
#
#   {"gemaakt": "...", "vanaf": "...", "uren": 24, "korrel_min": 1,
#    "vensters": {naam: [z,w,n,o]},
#    "schepen": [[mmsi, [lat_e5, lon_e5, min_geleden, varend], ...], ...]}
#
# Coordinaten staan als integers x 1e5 (~1 m) — dat scheelt de helft aan bytes
# tegenover floats met zes decimalen, en 1 m is ruim genoeg voor een debuglaag.
# "min_geleden" is minuten terug vanaf `gemaakt`, zodat de atlas op recentheid
# kan kleuren zonder tijdstempels te parsen.
#
# Zelfregulerend: is het na uitdunnen nog te groot, dan wordt de tijdkorrel
# grover (1 -> 2 -> 5 -> 10 -> 30 min) tot het onder MAX_PUNTEN zit. Zo blijft
# het bestand hanteerbaar als er straks drukkere vensters bij komen, zonder dat
# iemand een limiet hoeft na te stellen.
#
# Draaien (VPS):
#   /opt/ais-collector/venv/bin/python /opt/ais-collector/publiceren.py \
#       --bron /var/lib/ais-collector/ais \
#       --uit /var/lib/ais-collector/publiek/pings.json \
#       --vensters /opt/ais-collector/vensters.json

import argparse
import gzip
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

MAX_PUNTEN = 120_000
KORRELS = [1, 2, 5, 10, 30]      # minuten, voor VARENDE schepen
STIL_KORREL_MIN = 60             # minuten, voor stilliggers (zie dun_uit)
VARE_GRENS = 0.5                 # knopen; onder = ligplaats


def bronbestanden(map_pad: Path, uren: float):
    """De dagbestanden die het venster kunnen raken, oud -> nieuw.

    Eén dag kan meerdere bestanden hebben: bij de omzetting naar `--live-gz`
    gaat het ongegzipte deel naar `<dag>-a.jsonl(.gz)` en schrijft de collector
    verder in `<dag>.jsonl.gz`. Beide horen bij dezelfde dag, dus pak ze allebei
    — anders vallen de uren vóór een omzetting stil uit het venster."""
    nu = datetime.now(timezone.utc)
    dagen = {(nu - timedelta(hours=h)).strftime("%Y-%m-%d")
             for h in (0, uren, uren / 2)}
    paden = []
    for dag in sorted(dagen):
        kandidaten = sorted(map_pad.glob(f"{dag}*.jsonl")) + \
                     sorted(map_pad.glob(f"{dag}*.jsonl.gz"))
        # Staat een dag zowel plat als gegzipt klaar, dan is dat dezelfde inhoud
        # (de gzip-ronde ruimt het platte bestand pas daarna op) -> plat wint.
        gezien = set()
        for pad in kandidaten:
            stam = pad.name.split(".jsonl")[0]
            if stam in gezien:
                continue
            gezien.add(stam)
            paden.append(pad)
    return paden


def open_regels(pad: Path):
    """Regels uit een dagbestand, gegzipt of plat.

    ⚠️ Het dagbestand van vandaag wordt LIVE geschreven (`--live-gz`), dus de
    laatste gzip-member heeft nog geen end-of-stream-marker. Python gooit daar
    een EOFError op nadat het alles wat er wél staat al heeft opgeleverd. Dat is
    hier de normale toestand en geen fout: lees tot waar de schrijver is en stop.
    Zonder deze vangst faalt élke publiceerronde zolang de collector draait."""
    if pad.suffix == ".gz":
        fh = gzip.open(pad, "rt", encoding="utf-8", errors="replace")
    else:
        fh = pad.open(encoding="utf-8", errors="replace")
    try:
        while True:
            try:
                regel = next(fh)
            except StopIteration:
                return
            except EOFError:
                return          # staart van het levende bestand — verwacht
            yield regel
    finally:
        fh.close()


# De drie berichtsoorten die een positie dragen. `PositionReport` is UITSLUITEND
# Class A; Class B-transponders (sleepboten, binnenvaart, kleinere schepen) komen
# binnen als de twee ClassB-varianten. Die dragen dezelfde Latitude/Longitude/Sog,
# dus alleen de sleutel verschilt — maar ze weglaten kost ruwweg de helft van de
# schepen (gemeten 2026-07-26: 9.655 ber/min mét tegen 4.465 zonder).
POSITIE_SOORTEN = ("PositionReport", "StandardClassBPositionReport",
                   "ExtendedClassBPositionReport")


def lees(paden, grens: datetime):
    """Ruwe JSONL -> (mmsi, lat, lon, tijd, varend). Alles wat niet parseert
    slaan we over: een half weggeschreven laatste regel mag niets breken."""
    for pad in paden:
        for regel in open_regels(pad):
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
                # aisstream levert "2026-07-25 20:23:17.115098352 +0000 UTC" —
                # nanoseconden, en die slikt fromisoformat niet (max 6 cijfers).
                tijd = datetime.strptime(meta["time_utc"][:26],
                                         "%Y-%m-%d %H:%M:%S.%f"
                                         ).replace(tzinfo=timezone.utc)
            except (json.JSONDecodeError, KeyError, ValueError, TypeError):
                continue
            if tijd < grens:
                continue
            sog = pr.get("Sog")
            yield (meta.get("MMSI"), pr["Latitude"], pr["Longitude"], tijd,
                   1 if (sog is not None and sog >= VARE_GRENS) else 0)


def dun_uit(rijen, nu: datetime, korrel: int):
    """Eén ping per schip per tijdkorrel, met een EIGEN, veel grovere korrel voor
    stilliggers.

    Waarom gesplitst: een schip aan de kade zendt ~30x per uur vrijwel dezelfde
    positie. Op één gedeelde korrel eten die ligplaats-pings het puntenbudget op,
    waarna de zelfregulering de korrel grover maakt en juist de trackvorm van de
    varende schepen sneuvelt — precies het omgekeerde van wat je wilt zien.
    Stilliggers dragen alleen "hier is een ligplaats"; één punt per uur zegt dat
    net zo goed."""
    stil_korrel = max(STIL_KORREL_MIN, korrel)
    perschip = {}
    for mmsi, lat, lon, tijd, varend in rijen:
        if mmsi is None:
            continue
        minuten = int((nu - tijd).total_seconds() // 60)
        # Aparte sleutelruimte per soort, anders verdringt een stilligger de
        # varende ping van dezelfde minuut (of andersom).
        sleutel = (varend, minuten // (korrel if varend else stil_korrel))
        if sleutel not in (bak := perschip.setdefault(mmsi, {})):
            bak[sleutel] = (round(lat * 1e5), round(lon * 1e5), minuten, varend)
    return perschip


def main() -> None:
    p = argparse.ArgumentParser(description="Pings-debuglaag publiceren (LAR-535)")
    p.add_argument("--bron", type=Path, required=True)
    p.add_argument("--uit", type=Path, required=True)
    p.add_argument("--vensters", type=Path, required=True)
    p.add_argument("--uren", type=float, default=24.0)
    args = p.parse_args()

    nu = datetime.now(timezone.utc)
    grens = nu - timedelta(hours=args.uren)
    paden = bronbestanden(args.bron, args.uren)
    if not paden:
        sys.exit(f"Geen dagbestanden gevonden in {args.bron}")

    begon = time.monotonic()
    rijen = list(lees(paden, grens))
    print(f"{len(rijen):,} pings gelezen uit {len(paden)} bestand(en) "
          f"in {time.monotonic() - begon:.1f}s")

    for korrel in KORRELS:
        perschip = dun_uit(rijen, nu, korrel)
        punten = sum(len(v) for v in perschip.values())
        print(f"  korrel {korrel:2d} min -> {punten:,} punten "
              f"({len(perschip):,} schepen)")
        if punten <= MAX_PUNTEN:
            break
    else:
        print(f"  ⚠️ ook op {KORRELS[-1]} min nog {punten:,} punten — "
              "toch publiceren")

    schepen = [[mmsi, *sorted(bak.values(), key=lambda r: -r[2])]
               for mmsi, bak in perschip.items()]
    schepen.sort(key=lambda s: -len(s))

    doc = {
        "gemaakt": nu.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "vanaf": grens.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "uren": args.uren,
        "korrel_min": korrel,
        "punten": punten,
        "vensters": json.loads(args.vensters.read_text(encoding="utf-8")),
        "schepen": schepen,
    }

    args.uit.parent.mkdir(parents=True, exist_ok=True)
    tijdelijk = args.uit.with_suffix(".tmp")
    tijdelijk.write_text(json.dumps(doc, separators=(",", ":")),
                         encoding="utf-8")
    # Atomair vervangen: de atlas mag nooit een half geschreven bestand fetchen.
    os.replace(tijdelijk, args.uit)

    # Voorgecomprimeerd ernaast; Traefik/nginx serveert dat direct bij
    # Accept-Encoding: gzip en scheelt de telefoon een factor ~5.
    gz_tijdelijk = args.uit.with_suffix(".json.gz.tmp")
    with gzip.open(gz_tijdelijk, "wt", encoding="utf-8", compresslevel=6) as fh:
        fh.write(json.dumps(doc, separators=(",", ":")))
    os.replace(gz_tijdelijk, str(args.uit) + ".gz")

    kb = args.uit.stat().st_size / 1024
    kb_gz = Path(str(args.uit) + ".gz").stat().st_size / 1024
    print(f"geschreven: {args.uit} — {kb:,.0f} KB ({kb_gz:,.0f} KB gegzipt) · "
          f"{punten:,} punten van {len(schepen):,} schepen")


if __name__ == "__main__":
    main()
