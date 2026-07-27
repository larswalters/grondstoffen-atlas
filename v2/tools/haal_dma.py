# haal_dma.py — de Deense bron voor het tracknet (M28).
#
# De Danish Maritime Authority publiceert per dag álle AIS-berichten uit Deense
# wateren als CSV in een zip — gratis, geen registratie, en tot gisteren-min-drie.
# Dat dekt precies wat aisstream in de Oostzee-toegang mager doet: de SONT
# (Helsingør-Helsingborg), de Grote en Kleine Belt, het Kattegat en de Deense
# Noordzeekust — de enige zeepoort tussen de Oostzee en de wereld.
#
# Zelfde recept als haal_marinecadastre.py: bron -> collector-JSONL (aisstream-
# schema), zodat alles stroomafwaarts (bouw_tracks.py, LAR-531) maar één formaat
# hoeft te kennen. De bron verschilt, het recept niet.
#
#   PositionReport                 <- Class A
#   StandardClassBPositionReport   <- Class B
#   ShipStaticData                 <- 1x per MMSI per dag
#
# Gebruik:
#   python tools/haal_dma.py 2026-07-24
#   python tools/haal_dma.py 2026-06-27..2026-07-24
#   python tools/haal_dma.py --lijst          (welke dagen staan er in de bucket?)
#
# Uitvoer: build-cache/ais/dma/YYYY-MM-DD.jsonl.gz (+ de ruwe .zip blijft ernaast
# staan zodat een rijker recept nooit een nieuwe download kost).
#
# ─────────────────────────────────────────────────────────────────────────────
# ⚠️ ZES VALKUILEN, ALLE ZES GEMETEN OP DE ECHTE DATA VAN 2026-07-24 — NIET AANGENOMEN
#
# 1. HET TIJDSTEMPEL IS DEENS: "24/07/2026 00:00:00" = dd/mm/yyyy, niet ISO.
#    bouw_tracks.py leest MetaData.time_utc met strptime(t[:26], "%Y-%m-%d
#    %H:%M:%S.%f"). Schrijf je het Deense formaat door, dan gooit élke regel een
#    ValueError die bouw_tracks.py stílzwijgend opvangt (`except ... continue`) →
#    nul tracks, nul foutmeldingen. Precies de stille fout die dit project eerder
#    heeft gebeten. Daarom bouwt zet_om() de aisstream-vorm handmatig op ÉN
#    controleert toets_tijd() bij elke dag dat hij terugleest zoals bedoeld.
#
# 2. DE EERSTE KOLOM HEET "# Timestamp", mét hekje en spatie — geen "Timestamp".
#    Een index op de gestripte naam geeft een KeyError of, erger, de verkeerde kolom.
#
# 3. "Type of mobile" IS GEEN SCHEEPSKLASSE MAAR EEN OBJECTSOORT. Gemeten op één
#    dag: Class A 79,1% · Class B 10,3% · **Base Station 7,9%** · **AtoN 2,7%**
#    (boeien/bakens) · SAR Airborne 0,02%. Walstations en boeien liggen per
#    definitie stil en zouden als ligplaats-clusters in LAR-531 belanden; een
#    SAR-vliegtuig doet 145 knopen en zou als scheepstrack meetellen. Alleen
#    Class A/B gaat mee.
#
# 4. 0,8% VAN DE POSITIES IS DE AIS-"ONBEKEND"-SENTINEL — lat 91 / lon 181 (en
#    0,0). Dat zijn geen coördinaten maar "geen fix". Ongefilterd trekt elke
#    track een sprong naar de noordpool.
#
# 5. "Ship type" ÉN "Navigational status" ZIJN TEKST ("Cargo", "Moored", …) waar
#    NOAA én de aisstream-collector NUMMERS leveren. Nagekeken in de echte
#    collector-uitvoer: `"NavigationalStatus": 4` — een integer. Zou je de Deense
#    tekst doorschrijven, dan geeft een stroomafwaartse toets als
#    `NavigationalStatus == 5` (aangemeerd) voor DK-data altijd stil False,
#    terwijl hij voor VS-data werkt. SCHEEPSTYPE en NAVSTATUS vertalen daarom
#    terug naar de standaard AIS-codes, zodat een bericht uit Denemarken en uit
#    de VS letterlijk hetzelfde betekent.
#
# 6. SOG staat in KNOPEN (gemeten: 1,850 km/u per eenheid tegen 1,852 exact, over
#    15.809 opeenvolgende posistieparen) — gelijk aan NOAA, dus geen omrekening.
#
# ─────────────────────────────────────────────────────────────────────────────
# ⚠️ DE DRAGENDE ONTWERPKEUZE: ÉÉN POSITIE PER MMSI PER MINUUT.
#
# DMA levert de volle AIS-cadans (een varend schip zendt elke 2-10 seconden);
# MarineCadastre levert al gedund op één positie per minuut. Ongedund is dat
# ~20 mln posities per dag tegen ~9 mln voor héél de VS.
#
# Maar bouw_tracks.py rekent in HELE MINUTEN — `t_min = timestamp // 60` — en
# gooit binnen een minuut alles behalve het eerste punt zelf weg:
#     if huidig and huidig[-1][2] == t_min: continue
# Alles wat wij fijner aanleveren dan een minuut wordt stroomafwaarts dus
# gegarandeerd weggegooid; het kost alleen schijf, gzip-tijd en 5,8x zoveel
# json.loads in pass 1. Gemeten op de echte dag: 1.161.518 geldige posities ->
# 198.850 unieke (MMSI, minuut) = **5,8x**.
#
# Dunnen is hier dus geen verlies maar het gelijkzetten van de brongranulariteit
# aan de resolutie van de verbruiker — en het maakt de bestaande JSONL-weg snel
# genoeg, zodat bouw_tracks.py ONAANGERAAKT blijft (geen --csv-dma-vlag nodig).
# Wie de volle cadans wil: --alle-posities.
#
# De dunning gebruikt dat het bestand op tijd gesorteerd is: onthoud per MMSI de
# laatst weggeschreven minuut. Is het bestand ergens tóch niet gesorteerd, dan is
# het ergste gevolg een paar extra posities in dezelfde minuut — en die gooit
# bouw_tracks.py alsnog weg. De fout kan dus maar één kant op.

import argparse
import csv
import datetime
import gzip
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

BASIS_URL = "https://s3.eu-central-1.amazonaws.com/aisdata.ais.dk/aisdk-{dag}.zip"
BUCKET_URL = "https://s3.eu-central-1.amazonaws.com/aisdata.ais.dk/"
CACHE = Path(__file__).resolve().parent.parent / "build-cache" / "ais" / "dma"

# Een dagzip is gemeten 610-1.036 MB. Ver onder de helft = kapot/afgebroken.
MIN_ZIP_BYTE = 200_000_000

# DMA schrijft de scheepssoort als tekst; de rest van de pijplijn (en NOAA)
# rekent in AIS-typenummers. Onbekende waarden worden geteld en gemeld.
SCHEEPSTYPE = {
    "WIG": 20, "Fishing": 30, "Towing": 31, "Towing long/wide": 32,
    "Dredging": 33, "Diving": 34, "Military": 35, "Sailing": 36,
    "Pleasure": 37, "HSC": 40, "Pilot": 50, "SAR": 51, "Tug": 52,
    "Port tender": 53, "Anti-pollution": 54, "Law enforcement": 55,
    "Medical": 58, "Not party to conflict": 59, "Passenger": 60,
    "Cargo": 70, "Tanker": 80, "Other": 90,
}
# "Undefined", "Reserved" en "Spare" dragen geen informatie -> geen type.

# Idem voor de vaarstatus: DMA schrijft tekst, aisstream/NOAA een AIS-code.
NAVSTATUS = {
    "Under way using engine": 0, "At anchor": 1, "Not under command": 2,
    "Restricted maneuverability": 3, "Constrained by her draught": 4,
    "Moored": 5, "Aground": 6, "Engaged in fishing": 7,
    "Under way sailing": 8, "Reserved for future amendment [HSC]": 9,
    "Reserved for future amendment [WIG]": 10,
    "Power-driven vessel towing astern": 11,
    "Power-driven vessel pushing ahead or towing alongside": 12,
    "Reserved for future use": 13, "AIS-SART": 14,
    "AIS-SART (active)": 14, "Unknown value": None,
}
# Nagelopen op een volle dag: dit dekt ALLE 15 daar voorkomende waarden. Over de
# volle 28 dagen (688 mln regels) dook er precies één extra op — de schrijfwijze
# "AIS-SART (active)", 1 regel op 2026-07-03 — en die is hierboven toegevoegd.
# Dat is meteen het bewijs dat de meldregel in zet_om() werkt: een onbekende code
# verdwijnt niet stil als None maar komt in de log te staan.

KOLOMMEN = ["# Timestamp", "Type of mobile", "MMSI", "Latitude", "Longitude",
            "Navigational status", "SOG", "COG", "Name", "Ship type",
            "Width", "Length", "Draught", "A", "B", "C", "D"]


# ── bucket ────────────────────────────────────────────────────────────────

def bucket_dagen():
    """Welke dagen staan er ECHT in de bucket? Vraag het voordat je 28
    downloads start — een ontbrekende dag geeft een 404-achtige minipagina,
    geen nette fout."""
    dagen, token = {}, None
    while True:
        url = BUCKET_URL + "?list-type=2&max-keys=1000"
        if token:
            url += "&continuation-token=" + urllib.parse.quote(token, safe="")
        with urllib.request.urlopen(url, timeout=120) as r:
            xml = r.read().decode("utf-8")
        for m in re.finditer(r"<Key>aisdk-(\d{4}-\d{2}-\d{2})\.zip</Key>"
                             r".*?<Size>(\d+)</Size>", xml, re.S):
            dagen[m.group(1)] = int(m.group(2))
        if "<IsTruncated>true</IsTruncated>" not in xml:
            return dagen
        t = re.search(r"<NextContinuationToken>([^<]*)</NextContinuationToken>", xml)
        if not t:
            return dagen
        token = t.group(1)


def dagen_uit_args(args):
    dagen = []
    for a in args:
        if ".." in a:
            van, tot = a.split("..")
            d = datetime.date.fromisoformat(van)
            tot_d = datetime.date.fromisoformat(tot)
            while d <= tot_d:
                dagen.append(d.isoformat())
                d += datetime.timedelta(days=1)
        else:
            dagen.append(a)
    return dagen


# ── download ──────────────────────────────────────────────────────────────

def download(dag: str) -> Path:
    doel = CACHE / f"aisdk-{dag}.zip"
    if doel.exists() and doel.stat().st_size > MIN_ZIP_BYTE:
        print(f"  {doel.name} staat er al ({doel.stat().st_size/1e6:.0f} MB)")
        return doel
    url = BASIS_URL.format(dag=dag)
    print(f"  downloaden: {url}", flush=True)
    begon = time.monotonic()
    tijdelijk = doel.with_suffix(".tmp")
    with urllib.request.urlopen(url, timeout=180) as r, tijdelijk.open("wb") as f:
        while blok := r.read(1 << 20):
            f.write(blok)
    # de 0-byte-val: controleer de GROOTTE, niet de HTTP-status
    grootte = tijdelijk.stat().st_size
    if grootte < MIN_ZIP_BYTE:
        tijdelijk.unlink()
        raise RuntimeError(f"download van {dag} verdacht klein ({grootte} byte) — "
                           f"bestaat die dag wel in de bucket?")
    tijdelijk.replace(doel)
    duur = time.monotonic() - begon
    print(f"  {doel.name}: {grootte/1e6:.0f} MB in {duur:.0f}s "
          f"({grootte/1e6/max(duur, 1):.0f} MB/s)")
    return doel


# ── omzetten ──────────────────────────────────────────────────────────────

def tijd_om(ts: str) -> str:
    """'24/07/2026 00:00:00' -> '2026-07-24 00:00:00.000000000 +0000 UTC'.
    Handmatig snijden i.p.v. strptime: dit is de hete lus van miljoenen regels
    en strptime is er ~3x trager in."""
    return f"{ts[6:10]}-{ts[3:5]}-{ts[0:2]} {ts[11:19]}.000000000 +0000 UTC"


def toets_tijd(dag: str):
    """Bewijs dat ons tijdstempel terugleest zoals bouw_tracks.py hem leest.
    Zonder deze toets is een verkeerd geparste datum onzichtbaar: bouw_tracks.py
    vangt de ValueError stil op en levert een lege trackset."""
    d, m, j = dag[8:10], dag[5:7], dag[:4]
    uit = tijd_om(f"{d}/{m}/{j} 13:37:42")
    terug = datetime.datetime.strptime(uit[:26], "%Y-%m-%d %H:%M:%S.%f")
    verwacht = datetime.datetime(int(j), int(m), int(d), 13, 37, 42)
    if terug != verwacht:
        raise RuntimeError(f"tijdstempel-omzetting fout: {uit!r} -> {terug} "
                           f"i.p.v. {verwacht}")


def getal(w):
    if not w:
        return None
    try:
        return float(w)
    except ValueError:
        return None


def zet_om(zip_pad: Path, dag: str, alle_posities=False) -> Path:
    doel = CACHE / f"{dag}.jsonl.gz"
    if doel.exists() and doel.stat().st_size > 1_000_000:
        print(f"  {doel.name} staat er al ({doel.stat().st_size/1e6:.0f} MB)")
        return doel
    toets_tijd(dag)

    begon = time.monotonic()
    n_ruw = n_pos = n_stat = n_gedund = 0
    n_ongeldig = n_geen_schip = 0
    onbekend_type = {}
    onbekend_nav = {}
    laatste_minuut = {}          # mmsi -> 'dd/mm/yyyy HH:MM' (dunning)
    statisch_gezien = set()
    tijdelijk = doel.with_suffix(".tmp")

    with zipfile.ZipFile(zip_pad) as z:
        namen = [n for n in z.namelist() if n.lower().endswith(".csv")]
        if len(namen) != 1:
            raise RuntimeError(f"verwacht 1 csv in de zip, gevonden: {namen}")
        # STREAMEN: de uitgepakte CSV is ~3,5 GB per dag en raakt nooit de schijf.
        with z.open(namen[0]) as ruw_stroom, \
                gzip.open(tijdelijk, "wt", encoding="utf-8", compresslevel=6) as f_uit:
            stroom = io.TextIOWrapper(io.BufferedReader(ruw_stroom, 1 << 22),
                                      encoding="utf-8", errors="replace",
                                      newline="")
            kop = next(stroom).rstrip("\r\n").split(",")
            ix = {k: i for i, k in enumerate(kop)}
            ontbreekt = [k for k in KOLOMMEN if k not in ix]
            if ontbreekt:
                raise RuntimeError(f"kolommen ontbreken in {dag}: {ontbreekt}\n"
                                   f"kopregel: {kop}")
            # "Type of mobile" en "MMSI" worden door de voorfilter hierboven
            # rechtstreeks uit de regel gesneden, dus die indexen zijn hier niet
            # nodig — ze staan wél in KOLOMMEN zodat de kopcontrole ze eist.
            i_t = ix["# Timestamp"]
            i_la, i_lo, i_sog, i_cog = (ix["Latitude"], ix["Longitude"],
                                        ix["SOG"], ix["COG"])
            i_nav, i_naam, i_type = (ix["Navigational status"], ix["Name"],
                                     ix["Ship type"])
            i_br, i_le, i_dr = ix["Width"], ix["Length"], ix["Draught"]
            i_a, i_b, i_c, i_d = ix["A"], ix["B"], ix["C"], ix["D"]

            for regel in stroom:
                n_ruw += 1
                # ── goedkope voorfilter: knip alleen de eerste drie velden af.
                # Het tijdstempel is exact 19 tekens, dus regel[19] is de eerste
                # komma (gemeten: 100% van de dataregels). Zo hoeven de ~83%
                # regels die de dunning tóch weggooit nooit volledig gesplitst.
                if len(regel) < 40 or regel[19] != ",":
                    continue
                k1 = regel.find(",", 20)
                soort = regel[20:k1]
                if soort != "Class A" and soort != "Class B":
                    n_geen_schip += 1
                    continue
                k2 = regel.find(",", k1 + 1)
                mmsi_s = regel[k1 + 1:k2]
                if not alle_posities:
                    minuut = regel[:16]
                    if laatste_minuut.get(mmsi_s) == minuut:
                        n_gedund += 1
                        continue
                    laatste_minuut[mmsi_s] = minuut

                rij = regel.rstrip("\r\n").split(",")
                if len(rij) != len(kop):
                    # zeldzaam (0,18%): een naam/bestemming mét komma staat
                    # tussen aanhalingstekens -> alsnog echt CSV-parsen
                    try:
                        rij = next(csv.reader([regel]))
                    except (csv.Error, StopIteration):
                        continue
                    if len(rij) != len(kop):
                        continue

                lat = getal(rij[i_la])
                lon = getal(rij[i_lo])
                # de AIS-"geen fix"-sentinel (lat 91 / lon 181) en 0,0
                if (lat is None or lon is None or not -90 <= lat <= 90
                        or not -180 <= lon <= 180 or (lat == 0.0 and lon == 0.0)):
                    n_ongeldig += 1
                    continue
                try:
                    mmsi = int(mmsi_s)
                except ValueError:
                    continue

                naam_schip = rij[i_naam]
                meta = {"MMSI": mmsi, "ShipName": naam_schip,
                        "time_utc": tijd_om(rij[i_t]),
                        "latitude": lat, "longitude": lon}
                positie = {"Latitude": lat, "Longitude": lon,
                           "Sog": getal(rij[i_sog]), "Cog": getal(rij[i_cog])}
                if soort == "Class B":
                    soort_ber = "StandardClassBPositionReport"
                else:
                    soort_ber = "PositionReport"
                    nav = rij[i_nav]
                    if nav and nav not in NAVSTATUS and nav not in onbekend_nav:
                        onbekend_nav[nav] = 0
                    if nav in onbekend_nav:
                        onbekend_nav[nav] += 1
                    positie["NavigationalStatus"] = NAVSTATUS.get(nav)
                f_uit.write(json.dumps({"Message": {soort_ber: positie},
                                        "MessageType": soort_ber,
                                        "MetaData": meta},
                                       separators=(",", ":")) + "\n")
                n_pos += 1

                if mmsi not in statisch_gezien:
                    stype_tekst = rij[i_type]
                    lengte = getal(rij[i_le])
                    if (stype_tekst and stype_tekst not in ("Undefined", "Reserved")
                            ) or lengte is not None:
                        stype = SCHEEPSTYPE.get(stype_tekst)
                        if (stype is None and stype_tekst
                                and stype_tekst not in ("Undefined", "Reserved",
                                                        "Spare 1", "Spare 2")):
                            onbekend_type[stype_tekst] = \
                                onbekend_type.get(stype_tekst, 0) + 1
                        statisch_gezien.add(mmsi)
                        # DMA levert de ECHTE A/B/C/D (afstand GPS->boeg/spiegel/
                        # bak/stuurboord). Downstream telt A+B = lengte en
                        # C+D = breedte, dus die vorm blijft kloppen. Zijn ze
                        # leeg, val dan terug op Length/Width in de NOAA-vorm.
                        a, b = getal(rij[i_a]), getal(rij[i_b])
                        c, d = getal(rij[i_c]), getal(rij[i_d])
                        if a is None and b is None and c is None and d is None:
                            a, b = lengte, 0.0
                            c, d = getal(rij[i_br]), 0.0
                        # de collector schrijft A/B/C/D als hele meters -> int
                        ssd = {"Type": stype, "Name": naam_schip,
                               "Dimension": {"A": int(a or 0), "B": int(b or 0),
                                             "C": int(c or 0), "D": int(d or 0)},
                               "MaximumStaticDraught": getal(rij[i_dr])}
                        f_uit.write(json.dumps(
                            {"Message": {"ShipStaticData": ssd},
                             "MessageType": "ShipStaticData",
                             "MetaData": meta}, separators=(",", ":")) + "\n")
                        n_stat += 1

    tijdelijk.replace(doel)
    duur = time.monotonic() - begon
    print(f"  {doel.name}: {n_pos:,} posities + {n_stat:,} statisch · "
          f"{doel.stat().st_size/1e6:.0f} MB in {duur:.0f}s", flush=True)
    print(f"    ruw {n_ruw:,} regels · weggelaten: {n_geen_schip:,} niet-schip "
          f"(walstation/boei/vliegtuig) · {n_gedund:,} zelfde minuut · "
          f"{n_ongeldig:,} ongeldige positie", flush=True)
    if onbekend_type:
        print(f"    LET OP: onbekende scheepstypen (geen AIS-code gezet): "
              f"{sorted(onbekend_type.items(), key=lambda x: -x[1])[:8]}")
    if onbekend_nav:
        print(f"    LET OP: onbekende vaarstatussen (geen AIS-code gezet): "
              f"{sorted(onbekend_nav.items(), key=lambda x: -x[1])[:8]}")
    return doel


def main():
    p = argparse.ArgumentParser(
        description="DMA-dagbestanden -> collector-JSONL (M28)")
    p.add_argument("dagen", nargs="*", help="2026-07-24 of 2026-06-27..2026-07-24")
    p.add_argument("--lijst", action="store_true",
                   help="toon welke dagen er in de bucket staan en stop")
    p.add_argument("--alle-posities", action="store_true",
                   help="niet dunnen naar 1 positie per MMSI per minuut "
                        "(5,8x meer data; bouw_tracks.py gooit het tóch weg)")
    p.add_argument("--zip-weg", action="store_true",
                   help="verwijder de ruwe zip na een geslaagde omzetting")
    args = p.parse_args()

    if args.lijst:
        d = bucket_dagen()
        alle = sorted(d)
        print(f"{len(alle)} dagbestanden · oudste {alle[0]} · nieuwste {alle[-1]}")
        for k in alle[-10:]:
            print(f"  {k}  {d[k]/1e6:.0f} MB")
        return

    dagen = dagen_uit_args(args.dagen)
    if not dagen:
        sys.exit("geef dagen op: 2026-07-24 of 2026-06-27..2026-07-24 "
                 "(of --lijst)")

    # Vraag de bucket éérst welke dagen bestaan; 28 downloads starten op een
    # aanname is de dure variant van deze vraag.
    beschikbaar = bucket_dagen()
    mist = [d for d in dagen if d not in beschikbaar]
    if mist:
        sys.exit(f"deze dagen staan NIET in de bucket: {mist}\n"
                 f"nieuwste beschikbare dag: {max(beschikbaar)}")

    CACHE.mkdir(parents=True, exist_ok=True)
    for i, dag in enumerate(dagen, 1):
        print(f"{dag}  ({i}/{len(dagen)}):", flush=True)
        zip_pad = download(dag)
        zet_om(zip_pad, dag, alle_posities=args.alle_posities)
        if args.zip_weg:
            zip_pad.unlink()
            print(f"  {zip_pad.name} verwijderd")


if __name__ == "__main__":
    main()
