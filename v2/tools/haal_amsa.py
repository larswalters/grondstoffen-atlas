# haal_amsa.py — de AUSTRALISCHE bron voor het tracknet (M28).
#
# AMSA (Australian Maritime Safety Authority) publiceert per maand alle
# AIS-posities uit haar Craft Tracking System over de hele Australische
# SAR-regio (lon 75..163, lat -86,5..-2,0) — inclusief satelliet-AIS, dus óók
# waar geen walstation staat. Dat is precies het gat dat aisstream in de
# Indische Oceaan en op de Australische noordwestkust laat vallen.
#
# Zelfde recept als haal_marinecadastre.py: bron -> collector-JSONL
# (aisstream-schema), zodat alles stroomafwaarts — bouw_tracks.py (LAR-530),
# de terminal-typering (LAR-531) — maar één formaat hoeft te kennen.
#
# Gebruik:
#   python tools/haal_amsa.py --lijst                    # id -> maand
#   python tools/haal_amsa.py 2026-03..2026-06           # download + omzetten
#   python tools/haal_amsa.py --recent 4                 # 4 nieuwste maanden
#   python tools/haal_amsa.py --velden 2026-06           # DBF-schema + sample
#   python tools/haal_amsa.py --tracks                   # -> au-landelijk
#
# Uitvoer: build-cache/ais/amsa/YYYY-MM.jsonl.gz (+ de ruwe .zip blijft ernaast
# staan zodat een rijker recept nooit een nieuwe download kost).
#
# ────────────────────────────────────────────────────────────────────────────
# ⚠️ VIJF EIGENSCHAPPEN VAN DEZE BRON DIE HET RECEPT BEPALEN. Alle vijf
#    GEMETEN op 2026-03 t/m 2026-06, niet aangenomen.
#
# 1. DE BRON IS MOEDWILLIG UITGEDUND NAAR 1 POSITIE PER SCHIP PER UUR.
#    AMSA's eigen metadata-PDF (zit in de zip), "Lineage": *a minimum time
#    interval between successive vessel position reports of 60 minutes*.
#    Nagemeten over ALLE vier de maanden (7.718.627 opeenvolgende paren
#    binnen één craft_id, niet één maand): interval p25 60 · p50 65 · p75 72 ·
#    p90 123 · p95 299 min. **99,6% van alle intervallen is > 30 min en
#    73,6% is > 60 min.** Varend (beide punten >= 0,5 kn) ligt p90 op 188 min.
#    Stapafstand varend: p50 21,3 km · p90 43,4 km.
#    ⚠️ Een eerdere versie van deze kop noemde "mediaan 60 min, 5,2% <= 30 min";
#      dat gold alleen voor 2026-06 (6% van de data) — over alles is het
#      mediaan 65 min en 0,4% <= 30 min.
#    ⇒ bouw_tracks.py knipt standaard op --knip-min 30. Met die waarde valt
#      vrijwel élk opeenvolgend paar uit elkaar en komt er NIETS uit: 0 tracks
#      uit 7.746.422 pings, gedraaid en niet beredeneerd (MIN_PUNTEN = 8
#      aaneengesloten punten wordt nooit gehaald). Dat is geen bug in
#      bouw_tracks.py — 30 min is juist voor de VS/EU-bronnen, die pings van
#      seconden tot minuten leveren. Deze bron krijgt daarom eigen waarden
#      (--knip-min 180 --stil-max 360 --gat-max-km 120); zie --tracks.
#
# 2. DE SCHEEPSIDENTITEIT IS ERUIT GESLOOPT.
#    AMSA-metadata: *vessel identification fields (i.e. MMSI number, Reg, IMO
#    number, callsign and vessel name) were deleted from the dataset*. Wat
#    overblijft is `craft_id`, een surrogaatsleutel — GEEN MMSI. Gemeten:
#    stabiel over maanden heen (2026-04 ∩ 2026-05 = 12.766 id's = 71% van de
#    kleinste maand), dus tracks over een maandgrens heen zijn zinnig.
#    ⚠️ craft_id is een GETEKENDE 32-bits waarde (gemeten bereik
#      -2.146.018.332 .. 2.146.758.065) en bouw_tracks.py pakt de MMSI als
#      unsigned ("<I") — een negatieve waarde geeft struct.error. Daarom
#      `& 0xFFFFFFFF`: een bijectie op 32 bits, dus geen enkele nieuwe
#      botsing, alleen een andere leesrichting van dezelfde bits.
#    Punten zónder craft_id kunnen per definitie geen track vormen en worden
#    overgeslagen (geteld + gerapporteerd). Ze een verzonnen id geven zou
#    schepen aan elkaar vlechten die niets met elkaar te maken hebben.
#
# 3. ER ZIJN TWEE VERSCHILLENDE SCHEMA'S, EN ZE SPREKEN ELKAAR TEGEN.
#    AMSA wisselde ergens tussen 2026-05 en 2026-06 van export.
#      OUD (t/m 2026-05, 887 byte/record): CRAFT_ID/LON/LAT/COURSE/SPEED/
#        TYPE/SUBTYPE/LENGTH/BEAM/DRAUGHT/TIMESTAMP — HOOFDLETTERS, CRAFT_ID
#        als float, TYPE 254 tekens, aparte (altijd lege) SUBTYPE.
#      NIEUW (2026-06, 261 byte/record): OBJECTID/craft_id/longitude/latitude/
#        course/speed/type/length/beam/draught/timestamp — kleine letters,
#        craft_id als int, type 71 tekens (kapt lange DG-omschrijvingen af).
#    Beide worden ondersteund via VELD_ALIAS.
#
# 4. ⚠️ HET TIJDSTEMPEL IS 12-UURS IN HET OUDE SCHEMA EN 24-UURS IN HET NIEUWE.
#    Dit is de gemeenste val van deze bron. Beide dragen een AM/PM-staart:
#      OUD  "16/05/2026 11:22:47 AM" — uren lopen 1..12, AM/PM IS BETEKENISVOL
#           (gemeten op 2026-05: uur-histogram is exact 1..12, nooit 0 of 13+).
#      NIEUW "24/06/2026 18:21:32 PM" — uren lopen 0..23, AM/PM is LOOS
#           (gemeten: het aantal records met uur 00..11 is exact gelijk aan
#           het aantal met "AM" — 1.486.722 van 2.936.215).
#    Pas je de ene regel op de andere toe, dan staat de halve dataset 12 uur
#    verkeerd — en dat is onzichtbaar in de kaart, alleen de tracks vlechten.
#    De regel hieronder klopt voor BEIDE (zie tijd_utc).
#    De dag is bovendien NIET met nullen aangevuld in het oude schema
#    ("5/03/2026 1:09:54 PM"), dus vaste tekenposities werken niet — splitsen.
#    UTC staat vast: AMSA-metadata zegt *vessel position report UTC timestamp*.
#
# 5. ⚠️ DE OUDE MAANDDUMPS ZIJN DOOR AMSA ZELF AFGEKAPT OP 2 GiB.
#    2026-03, -04 en -05 zijn alle drie EXACT 2.147.484.154 byte = 2^31 + 506:
#    de klassieke shapefile/dBASE-grens. De DBF-kop belooft meer records dan
#    er in het bestand staan:
#      2026-03: 2.421.064 van 2.713.739 -> 10,8% weg
#      2026-04: 2.421.064 van 2.601.223 ->  6,9% weg
#      2026-05: 2.421.064 van 2.618.631 ->  7,5% weg
#      2026-06: compleet (het nieuwe, compacte schema past wél)
#    Gemeten: het verlies zit NIET aan het eind van de maand — alle 31 dagen
#    van mei zijn aanwezig met 76-81k punten per dag. Het is een vrij
#    gelijkmatige uitdunning, geen ontbrekende week.
#    ⚠️ pyshp vertrouwt de kop en knalt met struct.error op het laatste,
#      halve record. Daarom lezen we tot de ECHT aanwezige recordgrens
#      (iterRecords(stop=...)), en melden we hoeveel er ontbreekt.
#
# ────────────────────────────────────────────────────────────────────────────
# ROUTE-KEUZE: pyshp, en de .shp blijft dicht.
#   `pip install pyshp` werkte (pure python, geen binaries), dus de eigen
#   minimale shapefile-lezer was niet nodig. Bijkomende vondst: de .dbf draagt
#   longitude/latitude ALS ATTRIBUUT, gelijk aan de punt-geometrie in de .shp.
#   De 82-101 MB .shp hoeft dus niet eens uitgepakt te worden; pyshp leest
#   alleen de .dbf (2,9 mln records in ~18 s).
#
# GEEN CSV-TUSSENSTAP (afwijking van het onderzoeksrecept, bewust).
#   Het recept schreef "shapefile -> CSV -> JSONL" omdat het ogr2ogr aannam,
#   en ogr2ogr kán geen collector-JSONL schrijven — CSV was daar de brug, geen
#   doel. Met pyshp lezen we de records rechtstreeks; een CSV ertussen kost
#   een extra volledige pass en ~300 MB per maand zonder iets zichtbaar te
#   maken wat de .dbf niet al is. De transparantie die de CSV moest leveren
#   zit nu in `--velden` (schema + voorbeeldrecords mét de omgerekende tijd en
#   AIS-code) en in `--csv-ook` voor wie tóch een platte tabel wil.
#
# LICENTIE: Creative Commons Attribution-Noncommercial 3.0 Australia.
#   Niet-commercieel gebruik + attributieplicht; AMSA schrijft de vorm van de
#   naamsvermelding zelf voor — zie ATTRIBUTIE hieronder.

import argparse
import csv
import gzip
import io
import json
import re
import struct
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

try:
    import shapefile  # pyshp
except ImportError:
    sys.exit("pip install pyshp")

BASIS = "https://www.operations.amsa.gov.au/spatial"
LIJST_URL = f"{BASIS}/DataServices/DigitalData"
DOWNLOAD_URL = f"{BASIS}/DataServices/Download"
CACHE = Path(__file__).resolve().parent.parent / "build-cache" / "ais" / "amsa"

# AMSA schrijft de naamsvermelding letterlijk voor op
# /spatial/DataServices/Copyright: "AMSA asserts the right to be recognized
# as author of the original material in the following manner: © AMSA 2013."
ATTRIBUTIE = "© AMSA 2013"
LICENTIE = "Creative Commons Attribution-Noncommercial 3.0 Australia"

MAANDEN = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"])}

# oud schema (HOOFDLETTERS) -> nieuw schema (kleine letters). Zie punt 3.
VELD_ALIAS = {
    "craft_id": ("craft_id", "CRAFT_ID"),
    "lat": ("latitude", "LAT"),
    "lon": ("longitude", "LON"),
    "cog": ("course", "COURSE"),
    "sog": ("speed", "SPEED"),
    "type": ("type", "TYPE"),
    "subtype": ("SUBTYPE",),
    "length": ("length", "LENGTH"),
    "beam": ("beam", "BEAM"),
    "draught": ("draught", "DRAUGHT"),
    "tijd": ("timestamp", "TIMESTAMP"),
}


# ── de id -> maand-mapping ─────────────────────────────────────────────────
# Bewust ELKE RUN opnieuw ophalen in plaats van een tabel in te bakken: AMSA
# zet er maandelijks een dump bij en de id's zijn niet af te leiden (ze lopen
# niet aaneengesloten en de "Sub-areas"-variant zit ertussen).

def haal_pagina(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0", "Referer": LIJST_URL})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read().decode("utf-8", "replace")


def scrape_ids() -> dict:
    """{'2026-06': 6529, ...} — alleen de volle maanddumps.

    ⚠️ Naast 'Vessel Traffic Data <maand> <jaar>' staat per maand een
    'Vessel Traffic Data Sub-areas <maand> <jaar>' met een NAASTLIGGEND id
    (6529 vs 6530). Dat is een ander product; pak je hem per ongeluk, dan
    download je 100+ MB die geen punt-shapefile is. Daarom fullmatch.
    """
    html = haal_pagina(LIJST_URL)
    paren = re.findall(r"<strong>(.*?)</strong>.*?openDownload\((\d+)\)",
                       html, re.S)
    uit = {}
    for titel, cid in paren:
        titel = re.sub(r"\s+", " ", titel).strip()
        m = re.fullmatch(r"Vessel Traffic Data ([A-Za-z]+) (\d{4})", titel)
        if not m:
            continue                      # Sub-areas, AUSREP, kaarten, ...
        maand = MAANDEN.get(m.group(1).lower())
        if maand:
            uit[f"{m.group(2)}-{maand:02d}"] = int(cid)
    if not uit:
        raise RuntimeError("geen maanddumps gevonden — is de pagina veranderd?")
    return uit


# ── download ───────────────────────────────────────────────────────────────

def download(maand: str, cid: int) -> Path:
    """POST met TermsAccepted; hervatbaar en met een harde groottecontrole.

    ⚠️ DE VAL HIER IS NIET DE 0-BYTE MAAR DE HALVE BYTE. Gemeten: de server
    stuurt netjes HTTP 200 met Content-Length 122.686.739 en kapt de stroom
    daarna stil af op 26 MB. Dat is een geldige download volgens élke
    statuscontrole en een kapotte zip volgens zipfile. Dus: tellen wat er
    binnenkomt, vergelijken met Content-Length, en pas dán hernoemen.
    """
    doel = CACHE / f"{maand}.zip"
    if doel.exists() and doel.stat().st_size > 1_000_000:
        print(f"  {doel.name} staat er al ({doel.stat().st_size/1e6:.0f} MB)")
        return doel
    CACHE.mkdir(parents=True, exist_ok=True)
    tijdelijk = doel.with_suffix(".tmp")
    body = urllib.parse.urlencode({"ContentItemId": str(cid),
                                   "TermsAccepted": "true"}).encode()
    for poging in range(1, 5):
        t0 = time.monotonic()
        gehad = verwacht = 0
        try:
            req = urllib.request.Request(DOWNLOAD_URL, data=body, headers={
                "User-Agent": "Mozilla/5.0", "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": LIJST_URL})
            with urllib.request.urlopen(req, timeout=300) as r, \
                    tijdelijk.open("wb") as f:
                verwacht = int(r.headers.get("Content-Length", 0))
                print(f"  downloaden id {cid} ({verwacht/1e6:.0f} MB)")
                while blok := r.read(1 << 20):
                    f.write(blok)
                    gehad += len(blok)
        except Exception as e:                       # noqa: BLE001
            print(f"  poging {poging}: {type(e).__name__} na {gehad/1e6:.1f} MB")
            continue
        if verwacht and gehad != verwacht:
            print(f"  poging {poging}: afgekapt op "
                  f"{gehad/1e6:.1f}/{verwacht/1e6:.1f} MB")
            continue
        if gehad < 1_000_000:
            print(f"  poging {poging}: verdacht klein ({gehad} byte)")
            continue
        tijdelijk.replace(doel)
        print(f"  {doel.name}: {gehad/1e6:.0f} MB in {time.monotonic()-t0:.0f}s")
        return doel
    tijdelijk.unlink(missing_ok=True)
    raise RuntimeError(f"download van {maand} mislukt na 4 pogingen")


def open_dbf(zip_pad: Path) -> io.BytesIO:
    """De zip zit in een zip: <maand>.zip -> cts_srr_MM_YYYY_pt.zip -> .dbf"""
    buiten = zipfile.ZipFile(zip_pad)
    binnen_naam = next(i.filename for i in buiten.infolist()
                       if i.filename.endswith(".zip"))
    binnen = zipfile.ZipFile(io.BytesIO(buiten.read(binnen_naam)))
    dbf_naam = next(i.filename for i in binnen.infolist()
                    if i.filename.endswith(".dbf"))
    return io.BytesIO(binnen.read(dbf_naam))


def lees_dbf(zip_pad: Path):
    """(pyshp-Reader, kolomindex, n_echt, n_belooft) — bestand boven kop.

    Zie punt 5: de oude dumps zijn op 2 GiB afgekapt, dus de recordteller in
    de DBF-kop is te hoog en pyshp loopt eroverheen. We rekenen uit hoeveel
    records er ECHT in het bestand passen en begrenzen daarop.
    """
    buf = open_dbf(zip_pad)
    ruw = buf.getvalue()
    n_belooft, kop_len, rec_len = struct.unpack("<IHH", ruw[4:12])
    n_echt = min(n_belooft, (len(ruw) - kop_len) // rec_len)
    lezer = shapefile.Reader(dbf=buf)
    namen = [f[0] for f in lezer.fields[1:]]
    kolom = {}
    for sleutel, mogelijk in VELD_ALIAS.items():
        for naam in mogelijk:
            if naam in namen:
                kolom[sleutel] = namen.index(naam)
                break
    ontbreekt = {"craft_id", "lat", "lon", "sog", "tijd"} - set(kolom)
    if ontbreekt:
        raise RuntimeError(f"onbekend DBF-schema, mist {ontbreekt}: {namen}")
    return lezer, kolom, n_echt, n_belooft


# ── AIS-scheepstype terugrekenen uit de tekst ──────────────────────────────
# AMSA schrijft het type uit als "<klasse> - <subtype>"; dat is precies de
# standaard AIS-tabel (ITU-R M.1371), dus de numerieke code is exact terug te
# rekenen — en numeriek is wat het collector-schema en LAR-531 verwachten.
#   tientallen: "Reserved" 1x · WIG 2x · HSC 4x · Passenger 6x · Cargo 7x ·
#               Tanker 8x · Other 9x
#   eenheden:   All 0 · DG-categorie A/B/C/D 1/2/3/4 · Reserved 5..8 5..8 ·
#               "No additional info" 9
# 3x en 5x zijn losse betekenissen zonder subtype (Fishing 30, Tug 52, ...).
# Gemeten op 2026-06: 93 verschillende tekstwaarden, alle door dit schema
# gedekt. "unknown code N" draagt de ruwe code al in de tekst.

KLASSE_TIENTAL = {"Reserved": 10, "WIG": 20, "HSC": 40,
                  "Passenger ship": 60, "Cargo ship": 70, "Tanker": 80,
                  "Other": 90}
SUBTYPE_EENHEID = {"All": 0, "No additional info": 9, "Reserved 5": 5,
                   "Reserved 6": 6, "Reserved 7": 7, "Reserved 8": 8}
ENKELVOUDIG = {
    "Fishing": 30, "Towing": 31, "Towing Long/Large": 32,
    "Engaged in dredging or underwater operations": 33,
    "Engaged in diving operations": 34,
    "Engaged in military operations": 35, "Sailing": 36,
    "Pleasure craft": 37, "Pilot vessel": 50, "SAR": 51, "Tug": 52,
    "Port tender": 53,
    "Vessel with anti-pollution facilities or equipment": 54,
    "Law enforcement": 55, "Local 56": 56, "Local 57": 57,
    "Medical transport": 58,
    "Ship according to RR Resolution No. 18 (Mob-83)": 59,
}


def ais_type(tekst: str, subtype: str = "") -> int:
    """AMSA-tekst -> numerieke AIS-code; 0 = 'not available' (eerlijk onbekend).

    ⚠️ Het type-veld is in het NIEUWE schema 71 tekens breed en kapt af:
    'Passenger ship - Carrying DG, HS, or MP, IMO Hazard or pollutant catego'
    verliest juist de categorieletter. Dan geven we het tiental terug (klasse
    zeker, subtype onbekend) in plaats van een letter te gokken.
    """
    tekst = (tekst or "").strip()
    subtype = (subtype or "").strip()
    if subtype and " - " not in tekst:
        tekst = f"{tekst} - {subtype}"
    if not tekst:
        return 0
    m = re.fullmatch(r"unknown code (\d+)", tekst)
    if m:
        return int(m.group(1)) & 0xFF
    if tekst in ENKELVOUDIG:
        return ENKELVOUDIG[tekst]
    if " - " in tekst:
        klasse, sub = tekst.split(" - ", 1)
        tiental = KLASSE_TIENTAL.get(klasse.strip())
        if tiental is None:
            return 0
        sub = sub.strip()
        if sub in SUBTYPE_EENHEID:
            return tiental + SUBTYPE_EENHEID[sub]
        if sub.startswith("Carrying DG"):
            m = re.search(r"category (\w)", sub)
            if m and m.group(1).upper() in "ABCD":
                return tiental + "ABCD".index(m.group(1).upper()) + 1
            return tiental          # afgekapt: klasse zeker, subtype niet
        return tiental
    return KLASSE_TIENTAL.get(tekst, 0)


def tijd_utc(stempel: str) -> str:
    """AMSA-tijd -> '2026-06-24 18:21:32.000000000 +0000 UTC'.

    ⚠️ ÉÉN REGEL DIE VOOR BEIDE SCHEMA'S KLOPT (zie punt 4):
        uur > 12            -> al 24-uurs, AM/PM is loos, laat staan
        uur == 12 en 'AM'   -> 0   (middernacht in 12-uurs notatie)
        uur <= 11 en 'PM'   -> +12 (middag in 12-uurs notatie)
    In het nieuwe (24-uurs) schema komt uur <= 11 nooit met 'PM' voor en
    uur 12 nooit met 'AM' — gemeten — dus die takken raken het niet.
    De dag is in het oude schema niet met nullen aangevuld ('5/03/2026'),
    dus splitsen op '/' en ':' in plaats van vaste tekenposities.
    """
    delen = str(stempel).strip().split()
    if len(delen) < 2:
        raise ValueError(f"onleesbaar tijdstempel: {stempel!r}")
    dag, maand, jaar = delen[0].split("/")
    uur, minuut, seconde = delen[1].split(":")
    uur = int(uur)
    staart = delen[2].upper() if len(delen) > 2 else ""
    if uur <= 12 and staart in ("AM", "PM"):
        if staart == "AM" and uur == 12:
            uur = 0
        elif staart == "PM" and uur != 12:
            uur += 12
    return (f"{int(jaar):04d}-{int(maand):02d}-{int(dag):02d} "
            f"{uur:02d}:{int(minuut):02d}:{int(seconde):02d}"
            ".000000000 +0000 UTC")


# ── omzetten naar collector-JSONL ──────────────────────────────────────────

def zet_om(zip_pad: Path, maand: str, csv_ook=False) -> Path:
    doel = CACHE / f"{maand}.jsonl.gz"
    if doel.exists() and doel.stat().st_size > 100_000:
        print(f"  {doel.name} staat er al ({doel.stat().st_size/1e6:.0f} MB)")
        return doel

    begon = time.monotonic()
    lezer, kol, n_echt, n_belooft = lees_dbf(zip_pad)
    if n_echt < n_belooft:
        print(f"  LET OP - AFGEKAPT DOOR DE BRON: {n_echt:,} van {n_belooft:,} "
              f"records aanwezig ({100*(n_belooft-n_echt)/n_belooft:.1f}% weg, "
              f"2 GiB-shapefilegrens)")

    def veld(rec, sleutel, standaard=None):
        i = kol.get(sleutel)
        if i is None:
            return standaard
        w = rec[i]
        return standaard if w is None or w == "" else w

    n_pos = n_stat = n_geen_id = n_stuk = 0
    gezien = set()
    tijdelijk = doel.with_suffix(".tmp")
    csv_uit = csv_schr = None
    if csv_ook:
        csv_uit = gzip.open(CACHE / f"{maand}.csv.gz", "wt", newline="",
                            encoding="utf-8")
        csv_schr = csv.writer(csv_uit)
        csv_schr.writerow(["craft_id", "time_utc", "latitude", "longitude",
                           "sog", "cog", "type", "length", "beam", "draught"])

    with gzip.open(tijdelijk, "wt", encoding="utf-8", compresslevel=6) as uit:
        for rec in lezer.iterRecords(stop=n_echt):
            try:
                cid = veld(rec, "craft_id")
                if cid is None:
                    n_geen_id += 1
                    continue
                lat, lon = veld(rec, "lat"), veld(rec, "lon")
                if lat is None or lon is None:
                    n_stuk += 1
                    continue
                tijd = tijd_utc(veld(rec, "tijd"))
                # oud schema levert craft_id als float -> via float naar int;
                # getekend int32 -> unsigned, want bouw_tracks pakt MMSI als "<I"
                mmsi = int(float(cid)) & 0xFFFFFFFF
                sog = veld(rec, "sog", 0.0)
                cog = veld(rec, "cog")
            except (KeyError, TypeError, ValueError, IndexError):
                n_stuk += 1
                continue

            meta = {"MMSI": mmsi, "ShipName": "", "time_utc": tijd,
                    "latitude": lat, "longitude": lon}
            # AMSA maakt géén onderscheid Class A/B — alles als PositionReport
            uit.write(json.dumps(
                {"Message": {"PositionReport": {
                    "Latitude": lat, "Longitude": lon, "Sog": sog, "Cog": cog}},
                 "MessageType": "PositionReport", "MetaData": meta},
                separators=(",", ":")) + "\n")
            n_pos += 1

            if mmsi not in gezien:
                gezien.add(mmsi)
                ssd = {"Type": ais_type(veld(rec, "type", ""),
                                        veld(rec, "subtype", "")),
                       "Name": "",
                       "Dimension": {"A": veld(rec, "length", 0), "B": 0,
                                     "C": veld(rec, "beam", 0), "D": 0},
                       "MaximumStaticDraught": veld(rec, "draught", 0)}
                uit.write(json.dumps(
                    {"Message": {"ShipStaticData": ssd},
                     "MessageType": "ShipStaticData", "MetaData": meta},
                    separators=(",", ":")) + "\n")
                n_stat += 1

            if csv_schr:
                csv_schr.writerow([cid, tijd, lat, lon, sog, cog,
                                   veld(rec, "type", ""), veld(rec, "length"),
                                   veld(rec, "beam"), veld(rec, "draught")])
    if csv_uit:
        csv_uit.close()
    tijdelijk.replace(doel)
    print(f"  {doel.name}: {n_pos:,} posities · {n_stat:,} schepen · "
          f"{doel.stat().st_size/1e6:.0f} MB in {time.monotonic()-begon:.0f}s")
    if n_geen_id or n_stuk:
        print(f"    overgeslagen: {n_geen_id:,} zonder craft_id "
              f"({100*n_geen_id/max(n_echt,1):.1f}% — identiteit door AMSA "
              f"verwijderd) · {n_stuk:,} onleesbaar")
    return doel


def toon_velden(zip_pad: Path, n=4):
    lezer, kol, n_echt, n_belooft = lees_dbf(zip_pad)
    print(f"  records: {n_echt:,} aanwezig / {n_belooft:,} in de kop")
    print("  velden:")
    for naam, soort, lengte, dec in lezer.fields[1:]:
        print(f"    {naam:<12} {soort} len={lengte:<4} dec={dec}")
    namen = [f[0] for f in lezer.fields[1:]]
    for i, rec in enumerate(lezer.iterRecords(stop=min(n, n_echt))):
        rij = dict(zip(namen, list(rec)))
        print(f"    {rij}")
        t = rij.get("timestamp") or rij.get("TIMESTAMP")
        ty = rij.get("type") or rij.get("TYPE") or ""
        print(f"      -> time_utc={tijd_utc(t)!r}  AIS-type={ais_type(ty)}")


# ── tracks ─────────────────────────────────────────────────────────────────

def bouw_tracks_au(uit_pad: Path, knip_min: int, stil_max: int, gat_max_km: float):
    """Roept bouw_tracks.py aan via zijn eigen CLI-vlaggen.

    ⚠️ WAAROM DEZE BRON ANDERE KNIP-WAARDEN KRIJGT DAN VS/DK/NO/collector.
    AMSA dunt zelf naar 1 positie per schip per uur (punt 1 in de kop), dus
    de defaults van bouw_tracks.py — geijkt op bronnen met 0,25-0,45 km
    tussen twee pings — knippen hier tussen vrijwel élk paar opeenvolgende
    punten en leveren 0 tracks uit 7,75 mln pings (gemeten). De waarden
    staan in `main()` en gaan als gewone vlaggen mee; er wordt niets in
    bouw_tracks.py gepatcht, zodat de trackset reproduceerbaar is uit het
    commando alleen.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import bouw_tracks

    oud_argv, sys.argv = sys.argv, [
        "bouw_tracks.py", "--bron", str(CACHE), "--uit", str(uit_pad),
        "--knip-min", str(knip_min), "--stil-max", str(stil_max),
        "--gat-max-km", str(gat_max_km)]
    try:
        bouw_tracks.main()
    finally:
        sys.argv = oud_argv


# ── main ───────────────────────────────────────────────────────────────────

def maanden_uit_args(args):
    uit = []
    for a in args:
        if ".." in a:
            van, tot = a.split("..")
            j, m = int(van[:4]), int(van[5:7])
            while f"{j:04d}-{m:02d}" <= tot:
                uit.append(f"{j:04d}-{m:02d}")
                m += 1
                if m > 12:
                    j, m = j + 1, 1
        else:
            uit.append(a)
    return uit


def main():
    p = argparse.ArgumentParser(
        description="AMSA-maanddumps -> collector-JSONL (M28)")
    p.add_argument("maanden", nargs="*", help="YYYY-MM of YYYY-MM..YYYY-MM")
    p.add_argument("--lijst", action="store_true",
                   help="toon de id -> maand-mapping van de site")
    p.add_argument("--recent", type=int, metavar="N",
                   help="pak de N nieuwste maanddumps")
    p.add_argument("--velden", action="store_true",
                   help="toon DBF-schema + voorbeeldrecords, zet niets om")
    p.add_argument("--csv-ook", action="store_true",
                   help="schrijf ook YYYY-MM.csv.gz (platte tabel)")
    p.add_argument("--tracks", action="store_true",
                   help="bouw tracks over alles in build-cache/ais/amsa")
    # Bron-eigen knip-waarden, gekozen op de GEMETEN korrel van deze bron
    # (7.718.627 opeenvolgende paren, alle vier de maanden) — zie punt 1 in
    # de kop. Kort: 73,6% van de intervallen is > 60 min en het varende p90
    # ligt op 188 min, dus knippen onder ~180 min knipt de normale cadans
    # zelf weg; boven ~180 min vlakt de winst af terwijl het venster waarin
    # een ongeziene koorde kan wegkruipen wél meegroeit.
    p.add_argument("--knip-min", type=int, default=180,
                   help="minuten datagat dat een track knipt (default 180; de "
                        "bron is op 60 min uitgedund, 30 levert 0 tracks)")
    p.add_argument("--stil-max", type=int, default=360,
                   help="minuten stilliggen die een track overleeft (default "
                        "360 = 6 bronmonsters; 90 is bij deze cadans niet "
                        "meetbaar)")
    p.add_argument("--gat-max-km", type=float, default=120.0,
                   help="max koorde over een datagat (default 120 = wat het "
                        "snelste schip in één knip-min-venster haalt)")
    p.add_argument("--uit", type=Path,
                   help="tracks-uitvoer (default ../tracks/au-landelijk.jsonl.gz)")
    args = p.parse_args()

    if args.lijst:
        ids = scrape_ids()
        for maand in sorted(ids, reverse=True):
            print(f"  {maand}  id={ids[maand]}")
        print(f"{len(ids)} maanddumps · {min(ids)} .. {max(ids)}")
        return

    if args.tracks:
        uit = args.uit or (CACHE.parent / "tracks" / "au-landelijk.jsonl.gz")
        if not list(CACHE.glob("*.jsonl.gz")):
            sys.exit("geen collector-JSONL in build-cache/ais/amsa")
        bouw_tracks_au(uit, args.knip_min, args.stil_max, args.gat_max_km)
        return

    maanden = maanden_uit_args(args.maanden)
    if args.recent:
        maanden = sorted(scrape_ids(), reverse=True)[:args.recent]
        print(f"nieuwste {args.recent}: {', '.join(maanden)}")
    if not maanden:
        sys.exit("geef maanden op (2026-06), of --recent N, of --lijst")

    ids = scrape_ids()
    for maand in maanden:
        print(f"{maand}:")
        if maand not in ids:
            print(f"  LET OP - geen dump voor {maand} op de site, overgeslagen")
            continue
        zip_pad = download(maand, ids[maand])
        if args.velden:
            toon_velden(zip_pad)
        else:
            zet_om(zip_pad, maand, csv_ook=args.csv_ook)

    print(f"\nBRONVERMELDING (verplicht, {LICENTIE}):")
    print(f"  {ATTRIBUTIE} — Australian Maritime Safety Authority, "
          f"Craft Tracking System")


if __name__ == "__main__":
    main()
