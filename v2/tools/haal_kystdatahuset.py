# haal_kystdatahuset.py — de Noorse bron voor het tracknet (M28).
#
# Kystdatahuset (Kystverket) publiceert de Noorse AIS-historie als QUERY-API,
# niet als bulk-dump. Dat stuurt de hele vorm van dit script: waar
# haal_marinecadastre.py een dagbestand binnenhaalt en omzet, moet dit script
# per corridorbox en per tijdsbrok een POST doen. Daarom is de scope bewust
# klein — drie corridorboxen, vier weken — en niet heel Noorwegen.
#
# Licentie NLOD (open), GEEN registratie, GEEN token: geverifieerd met echte
# anonieme requests (2026-07-27).
#
# ── HET CONTRACT (uitgezocht, stond niet in ons bronnenonderzoek) ───────────
# De API publiceert een OpenAPI-doc op https://kystdatahuset.no/ws/swagger/v1/
# swagger.json (118 paden). Daar staat het body-schema:
#
#   POST https://kystdatahuset.no/ws/api/ais/positions/within-bbox-time
#   {"bbox": "minLon,minLat,maxLon,maxLat",   <- LON EERST (minx,miny,maxx,maxy)
#    "start": "yyyymmddhhMM", "end": "yyyymmddhhMM", "minSpeed": 0}
#
# Antwoord: {"success": bool, "msg": str, "data": [[..12 kolommen..], ..]}
# De kolommen zijn NERGENS gedocumenteerd; empirisch afgeleid (en gecontroleerd
# door k7 ≈ k9/k8 om te rekenen naar knopen — dat klopte op elke steekproef):
#
#   0 mmsi · 1 tijd (UTC, ISO zonder zone) · 2 LON · 3 LAT · 4 cog (360=onbekend)
#   5 sog kn (102.3=onbekend) · 6 AIS-berichttype (1/2/3=Class A, 18/19=Class B)
#   7 berekende snelheid kn · 8 seconden sinds vorige ping · 9 meter sinds vorige
#   10 heading (511=onbekend) · 11 rate-of-turn
#
# ⚠️ VALKUIL 1 — HET TIJDVENSTER IS NIET WAT JE VRAAGT. Gemeten op de dichte
# Oslofjord-box (pings per seconde, dus de rand is scherp af te lezen):
#   start 2026-03-10 00:00 -> eerste rij 2026-03-09 01:00:00
#   start 2026-03-10 06:00 -> eerste rij 2026-03-09 07:00:00
#   end   2026-03-10 07:00 -> laatste rij 2026-03-10 07:59:59
# Het werkelijke venster is dus [start − 23 uur, end + 1 uur], begrensd door de
# dagtabellen die de server laadt (dag(start)−1 t/m dag(end)). Reken NOOIT op
# het gevraagde venster: dit script vraagt bewust ruim en KNIPT ZELF op de
# gewenste dagen. De extra kopdag is verspilling die we accepteren omdat hij de
# eerste gewenste dag gegarandeerd compleet maakt.
#
# ⚠️ VALKUIL 2 — EEN ONTBREKENDE DAG GEEFT HTTP 200. De server antwoordt met
# {"success": false, "msg": "42P01: relation \"ais202603.ais_20260318_unique_info\"
# does not exist"} en status 200. Dit is de 0-byte-val van deze bron: controleer
# het ANTWOORD (success + rijen), niet de HTTP-status.
#
# ⚠️ VALKUIL 3 — HET ARCHIEF LOOPT ~4 MAANDEN ACHTER. Gemeten op 2026-07-27 is
# 2026-03-17 de laatste dag met een tabel (2026-03-18 ontbreekt). Voor de graaf
# maakt dat niet uit — een vaargeul verplaatst zich niet per kwartaal — maar het
# betekent wel dat "de laatste vier weken" hier eind maart is, niet juli.
#
# Tijdzone: de tijdkolom is UTC. Bewijs langs een onafhankelijke weg: het
# zusterendpoint /ws/api/ais/realtime/geojson uit dezelfde GeoAisDB noemt exact
# dit tijdformaat `date_time_utc` en die waarde liep bij de meting ~10 min
# achter op de wandklok-UTC (= de normale feed-vertraging), niet 1 of 2 uur.
# Dat sluit aan bij valkuil 1: de server telt +1 uur (CET) bij ONZE invoer op,
# dus onze invoer wordt als lokale tijd gelezen en de uitvoer is UTC.
#
# Statische data (naam/type/maten) komt uit een tweede endpoint:
#   POST /ws/api/ais/statinfo/for-mmsis-time  {"mmsiIds":[..],"start":..,"end":..}
# Dat werkt anoniem. ⚠️ /ws/api/ship/data/ais/for-mmsis-imos NIET: dat geeft 401
# "Not authorized ... role [Kystdatahuset_ekstern_alle]" — een licentie-slot,
# geen bug. We hebben het niet nodig.
#
# Rate-limits: geen 429 en geen documentatie gezien in ~40 requests. Wees
# desondanks beleefd tegen een gratis publieke API — vandaar --pauze tussen de
# verzoeken en één verzoek tegelijk (nooit parallel).
#
# Gebruik:
#   python tools/haal_kystdatahuset.py                       # 3 boxen, 4 weken
#   python tools/haal_kystdatahuset.py --box narvik --van 2026-03-01 --tot 2026-03-17
#
# Uitvoer: build-cache/ais/kystdatahuset/<box>-<van>_<tot>.jsonl.gz in exact het
# collector-schema (aisstream) dat bouw_tracks.py leest. De ruwe API-antwoorden
# blijven gegzipt in build-cache/ais/kystdatahuset/ruw/ staan, zodat een rijker
# recept nooit een nieuwe download kost (zelfde regel als bij marinecadastre).

import argparse
import gzip
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

BASIS = "https://kystdatahuset.no/ws"
POSITIES = BASIS + "/api/ais/positions/within-bbox-time"
STATINFO = BASIS + "/api/ais/statinfo/for-mmsis-time"

CACHE = Path(__file__).resolve().parent.parent / "build-cache" / "ais" / "kystdatahuset"

# de drie corridorboxen als (zuid, west, noord, oost)
BOXEN = {
    "oslofjord": (58.90, 10.20, 59.95, 11.10),
    "bergen":    (60.15,  4.90, 60.55,  5.50),
    "narvik":    (68.30, 16.80, 68.60, 17.60),   # het ertsbeen — LKAB over Narvik
}

# vier weken die eindigen op de laatste dag die het archief heeft (zie valkuil 3)
VAN_STANDAARD = "2026-02-18"
TOT_STANDAARD = "2026-03-17"

# AIS-berichttype -> collector-soort. 1/2/3 = Class A, 18/19 = Class B.
SOORT = {1: "PositionReport", 2: "PositionReport", 3: "PositionReport",
         18: "StandardClassBPositionReport", 19: "ExtendedClassBPositionReport"}

COG_ONBEKEND = 360.0
SOG_ONBEKEND = 102.3
HDG_ONBEKEND = 511


def post(url: str, body: dict, timeout: int = 900, pogingen: int = 3):
    """POST met retry. Geeft het geparste antwoord terug; controleert het
    ANTWOORD, niet de HTTP-status (valkuil 2)."""
    data = json.dumps(body).encode()
    laatste = None
    for poging in range(1, pogingen + 1):
        try:
            verzoek = urllib.request.Request(
                url, data=data,
                headers={"Content-Type": "application/json",
                         "Accept": "application/json",
                         "User-Agent": "grondstoffen-atlas/1.0 (open data, NLOD)"})
            with urllib.request.urlopen(verzoek, timeout=timeout) as r:
                antwoord = json.loads(r.read())
            if antwoord.get("success"):
                return antwoord
            # 42P01 = tabel bestaat niet -> die dag zit niet in het archief.
            # Geen retry: opnieuw vragen maakt de tabel niet alsnog aan.
            laatste = antwoord.get("msg", "")
            if "42P01" in laatste:
                return antwoord
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError,
                ConnectionError) as fout:
            laatste = f"{type(fout).__name__}: {fout}"
        if poging < pogingen:
            wacht = 10 * poging
            print(f"    poging {poging} mislukt ({str(laatste)[:80]}) — "
                  f"{wacht}s wachten", flush=True)
            time.sleep(wacht)
    return {"success": False, "msg": str(laatste), "data": []}


def brokken(van: date, tot: date, dagen: int):
    """Deel [van, tot] op in brokken van hoogstens `dagen` dagen."""
    d = van
    while d <= tot:
        eind = min(d + timedelta(days=dagen - 1), tot)
        yield d, eind
        d = eind + timedelta(days=1)


def ruw_pad(box: str, a: date, b: date) -> Path:
    # ⚠️ één API-rij per regel (JSONL), niet één grote array: de Oslofjord-box
    # geeft ~290k rijen per dag en een json.load van een hele brok kost bijna
    # een GB. Zo streamt de omzetting met verwaarloosbaar geheugen. Het bestand
    # staat in de submap ruw/, dus bouw_tracks.py's glob raakt het nooit.
    return CACHE / "ruw" / f"{box}-{a:%Y%m%d}-{b:%Y%m%d}.rows.jsonl.gz"


def haal_brok(box: str, a: date, b: date, pauze: float,
              mag_splitsen: bool = True) -> list:
    """Eén brok ruw ophalen en gegzipt wegschrijven. Geeft een lijst
    (pad, van, tot) terug — normaal één element.

    ⚠️ Het archief heeft GATEN (gemeten: 2026-03-11 ontbreekt terwijl 03-10 en
    03-12 er zijn). Eén ontbrekende dagtabel laat de server de HELE brok
    weigeren, dus zonder terugval kost één gat vier dagen. Daarom: mislukt een
    brok van meerdere dagen, dan halen we de dagen los op. Let op dat een
    verzoek voor dag D óók tabel D−1 nodig heeft (valkuil 1), dus rond een gat
    vallen er altijd twee dagen weg, niet één."""
    (CACHE / "ruw").mkdir(parents=True, exist_ok=True)
    doel = ruw_pad(box, a, b)
    if doel.exists() and doel.stat().st_size > 200:
        print(f"    {doel.name} staat er al ({doel.stat().st_size/1e6:.1f} MB)")
        return [(doel, a, b)]

    zuid, west, noord, oost = BOXEN[box]
    # bewust ruim vragen: de server levert [start-23u, end+1u] (valkuil 1),
    # dus met start = eerste gewenste dag 00:00 is die dag gegarandeerd heel.
    body = {"bbox": f"{west},{zuid},{oost},{noord}",
            "start": f"{a:%Y%m%d}0000", "end": f"{b:%Y%m%d}2359",
            "minSpeed": 0}
    t0 = time.monotonic()
    antwoord = post(POSITIES, body)
    duur = time.monotonic() - t0
    rijen = antwoord.get("data") or []
    if not antwoord.get("success"):
        kort = " ".join(str(antwoord.get("msg") or "").split())[:110]
        print(f"    {a}..{b}: MISLUKT — {kort}")
        if mag_splitsen and b > a:
            print(f"      terugval op losse dagen ({(b-a).days + 1} stuks)")
            uit = []
            d = a
            while d <= b:
                uit += haal_brok(box, d, d, pauze, mag_splitsen=False)
                d += timedelta(days=1)
            return uit
        return []
    if not rijen:
        print(f"    {a}..{b}: 0 rijen (leeg, {duur:.0f}s)")

    tijdelijk = doel.with_suffix(".tmp")
    with gzip.open(tijdelijk, "wt", encoding="utf-8", compresslevel=6) as f:
        for rij in rijen:
            f.write(json.dumps(rij, separators=(",", ":")) + "\n")
    # 0-byte-val: controleer de grootte, niet de HTTP-status
    if tijdelijk.stat().st_size < 100:
        tijdelijk.unlink()
        print(f"    {a}..{b}: verdacht klein bestand — overgeslagen")
        return []
    tijdelijk.replace(doel)
    print(f"    {a}..{b}: {len(rijen):,} rijen · "
          f"{doel.stat().st_size/1e6:.1f} MB gz · {duur:.0f}s")
    time.sleep(pauze)
    return [(doel, a, b)]


def stream_ruw(pad: Path):
    """Ruwe brok regel voor regel — één API-rij per regel."""
    with gzip.open(pad, "rt", encoding="utf-8") as f:
        for regel in f:
            try:
                yield json.loads(regel)
            except json.JSONDecodeError:
                continue


def haal_statisch(mmsis: list, van: date, tot: date, pauze: float) -> dict:
    """Naam/type/maten per MMSI via het statinfo-endpoint (anoniem)."""
    uit = {}
    partij = 250
    for i in range(0, len(mmsis), partij):
        deel = mmsis[i:i + partij]
        antwoord = post(STATINFO, {"mmsiIds": deel,
                                   "start": f"{van:%Y%m%d}0000",
                                   "end": f"{tot:%Y%m%d}2359"}, timeout=300)
        for rij in (antwoord.get("data") or []):
            try:
                uit[int(rij["mmsi"])] = rij
            except (KeyError, TypeError, ValueError):
                continue
        print(f"    statisch {min(i+partij, len(mmsis)):,}/{len(mmsis):,} "
              f"({len(uit):,} bekend)", flush=True)
        time.sleep(pauze)
    return uit


def als_getal(w, standaard=None):
    try:
        f = float(w)
    except (TypeError, ValueError):
        return standaard
    return f


def zet_om(box: str, van: date, tot: date, brokken_lijst: list,
           statisch: dict) -> Path:
    """Ruwe brokken -> collector-JSONL.gz (aisstream-schema).

    Hier gebeurt de knip op het gewenste venster (valkuil 1). ⚠️ Elke brok wordt
    op ZIJN EIGEN dagen geknipt, niet op het hele venster: de kopdag van brok N
    is de laatste dag van brok N−1 en die zit wél in het venster. Zonder deze
    knip belandt een dag twee keer in de tracks. Wat dan nog overblijft is de
    handvol exacte duplicaten die de API zelf teruggeeft (~1 op 4.000)."""
    doel = CACHE / f"{box}-{van:%Y%m%d}_{tot:%Y%m%d}.jsonl.gz"
    tijdelijk = doel.with_suffix(".tmp")

    n_pos = n_stat = n_buiten = n_dubbel = 0
    statisch_gedaan = set()  # (mmsi, dag) — één ShipStaticData per MMSI per dag
    with gzip.open(tijdelijk, "wt", encoding="utf-8", compresslevel=6) as uit:
        for pad, a, b in brokken_lijst:
            vroegst, laatst = f"{a:%Y-%m-%d}", f"{b:%Y-%m-%d}"
            gezien = set()          # per brok — houdt het geheugen begrensd
            for rij in stream_ruw(pad):
                try:
                    mmsi = int(rij[0])
                    tijd = rij[1]              # "2026-03-10T07:14:22" (UTC)
                    lon, lat = float(rij[2]), float(rij[3])
                except (IndexError, TypeError, ValueError):
                    continue
                dag = tijd[:10]
                if dag < vroegst or dag > laatst:
                    n_buiten += 1              # de kopdag van elke brok
                    continue
                sleutel = (mmsi, tijd)
                if sleutel in gezien:
                    n_dubbel += 1
                    continue
                gezien.add(sleutel)

                cog = als_getal(rij[4])
                sog = als_getal(rij[5])
                if cog == COG_ONBEKEND:
                    cog = None                 # 360 = "niet beschikbaar"
                if sog == SOG_ONBEKEND:
                    sog = None                 # 102.3 = "niet beschikbaar"
                try:
                    soort = SOORT.get(int(rij[6]), "PositionReport")
                except (TypeError, ValueError):
                    soort = "PositionReport"

                st = statisch.get(mmsi) or {}
                naam = (st.get("name") or "").strip()
                # exact de vorm die bouw_tracks.py leest:
                #   strptime(t[:26], "%Y-%m-%d %H:%M:%S.%f")
                t_utc = tijd.replace("T", " ") + ".000000000 +0000 UTC"
                meta = {"MMSI": mmsi, "ShipName": naam, "time_utc": t_utc,
                        "latitude": lat, "longitude": lon}
                positie = {"Latitude": lat, "Longitude": lon,
                           "Sog": sog, "Cog": cog}
                if soort == "PositionReport":
                    hdg = als_getal(rij[10])
                    if hdg is not None and hdg != HDG_ONBEKEND:
                        positie["TrueHeading"] = hdg
                uit.write(json.dumps({"Message": {soort: positie},
                                      "MessageType": soort,
                                      "MetaData": meta},
                                     separators=(",", ":")) + "\n")
                n_pos += 1

                if st and (mmsi, dag) not in statisch_gedaan:
                    statisch_gedaan.add((mmsi, dag))
                    ssd = {"Type": int(als_getal(st.get("type"), 0) or 0),
                           "Name": naam,
                           "Dimension": {"A": als_getal(st.get("length"), 0) or 0,
                                         "B": 0,
                                         "C": als_getal(st.get("breadth"), 0) or 0,
                                         "D": 0},
                           "MaximumStaticDraught": als_getal(st.get("draught"))}
                    uit.write(json.dumps({"Message": {"ShipStaticData": ssd},
                                          "MessageType": "ShipStaticData",
                                          "MetaData": meta},
                                         separators=(",", ":")) + "\n")
                    n_stat += 1
    tijdelijk.replace(doel)
    print(f"  {doel.name}: {n_pos:,} posities + {n_stat:,} statisch "
          f"({n_buiten:,} buiten venster, {n_dubbel:,} dubbel weggelaten) · "
          f"{doel.stat().st_size/1e6:.1f} MB")
    return doel


def main():
    p = argparse.ArgumentParser(
        description="Kystdatahuset (Noorwegen) -> collector-JSONL")
    p.add_argument("--box", action="append",
                   help=f"herhaalbaar; keuze: {', '.join(BOXEN)} (default: alle)")
    p.add_argument("--van", default=VAN_STANDAARD, help="YYYY-MM-DD")
    p.add_argument("--tot", default=TOT_STANDAARD, help="YYYY-MM-DD")
    p.add_argument("--dagen-per-verzoek", type=int, default=4,
                   help="brokgrootte; groter = minder kopdag-verspilling, "
                        "maar meer geheugen (default 4)")
    p.add_argument("--pauze", type=float, default=3.0,
                   help="seconden tussen verzoeken — beleefd tegen een gratis API")
    p.add_argument("--alleen-omzetten", action="store_true",
                   help="niets downloaden, alleen de ruwe brokken omzetten")
    args = p.parse_args()

    boxen = args.box or list(BOXEN)
    onbekend = [b for b in boxen if b not in BOXEN]
    if onbekend:
        sys.exit(f"onbekende box(en): {onbekend}; keuze: {', '.join(BOXEN)}")
    van = date.fromisoformat(args.van)
    tot = date.fromisoformat(args.tot)
    if tot < van:
        sys.exit("--tot ligt vóór --van")
    dagen = (tot - van).days + 1
    CACHE.mkdir(parents=True, exist_ok=True)

    print(f"Kystdatahuset · {dagen} dagen ({van} t/m {tot}) · "
          f"boxen: {', '.join(boxen)}")
    begon = time.monotonic()
    for box in boxen:
        print(f"\n{box} {BOXEN[box]}:")
        brokken_lijst = []
        for a, b in brokken(van, tot, args.dagen_per_verzoek):
            if args.alleen_omzetten:
                # ook de losse dagen meenemen die uit een terugval kwamen
                pad = ruw_pad(box, a, b)
                if pad.exists():
                    brokken_lijst.append((pad, a, b))
                else:
                    d = a
                    while d <= b:
                        los = ruw_pad(box, d, d)
                        if los.exists():
                            brokken_lijst.append((los, d, d))
                        d += timedelta(days=1)
                continue
            brokken_lijst += haal_brok(box, a, b, args.pauze)
        if not brokken_lijst:
            print(f"  {box}: geen data — overgeslagen")
            continue

        # unieke MMSI's verzamelen voor de statische ronde
        mmsis = set()
        for pad, _a, _b in brokken_lijst:
            for rij in stream_ruw(pad):
                try:
                    mmsis.add(int(rij[0]))
                except (IndexError, TypeError, ValueError):
                    continue
        print(f"  {len(mmsis):,} unieke MMSI — statische data ophalen")
        statisch = haal_statisch(sorted(mmsis), van, tot, args.pauze)
        zet_om(box, van, tot, brokken_lijst, statisch)

    print(f"\nklaar in {(time.monotonic()-begon)/60:.1f} min · uitvoer in {CACHE}")


if __name__ == "__main__":
    main()
