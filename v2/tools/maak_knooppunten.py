#!/usr/bin/env python3
"""maak_knooppunten.py — bouwt v2/data/knooppunten.json, het AANGEWEZEN register.

De overslagpunten zijn een REDACTIEBESLUIT, geen afleiding: geen enkele
afstandsdrempel kan havens classificeren (Manaus is een échte oceaanhaven op
1.084 km zee-snap, Duisburg wordt door geen zeeschip aangelopen op 152 km — het
interval is leeg, zie `v2/design/overslag-ontwerp.md` §2.2). Deze tool wijst dus
niets aan; hij MEET alleen wat de redacteur heeft aangewezen:

  * per modaliteit de dichtstbijzijnde knoop in het bijbehorende net, mét afstand
  * spoor en weg apart, want ze delen één knoopruimte in landnet.bin
  * het rapport zet de afstanden op een rij zodat een verkeerd aangewezen punt
    zichzelf verraadt (het Mountain-Pass-patroon uit de wegcorridors)

De coördinaat is de bron van waarheid, niet de knoop-id: knoop-ids verschuiven
bij elke rebake, coördinaten niet. De lader in `keten.js` snapt opnieuw en
rapporteert opnieuw.

Draaien:  python v2/tools/maak_knooppunten.py [--schrijf]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HIER = Path(__file__).resolve().parent
DATA = HIER.parent / "data"

# Windows-console staat standaard op cp1252 en struikelt over "Gdańsk".
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# --------------------------------------------------------------------------
# de gebakken bestanden lezen (alleen blok 1: de knopen)
# --------------------------------------------------------------------------

class Lezer:
    """Zigzag-varint, exact het formaat dat bake_marnet.py schrijft."""

    def __init__(self, buf: bytes):
        self.b = buf
        self.p = 0

    def volgende(self) -> int:
        res = 0
        factor = 1
        while True:
            byte = self.b[self.p]
            self.p += 1
            res += (byte & 0x7F) * factor
            if not (byte & 0x80):
                break
            factor *= 128
        half = res // 2
        return half if res % 2 == 0 else -half - 1


def lees_knopen(json_pad: Path, bin_pad: Path):
    meta = json.loads(json_pad.read_text(encoding="utf-8"))
    lezer = Lezer(bin_pad.read_bytes())
    schaal = meta["schaal"]
    n = meta["knopen"]
    lon = np.empty(n, dtype=np.float64)
    lat = np.empty(n, dtype=np.float64)
    x = y = 0
    for i in range(n):
        x += lezer.volgende()
        y += lezer.volgende()
        lon[i] = x / schaal
        lat[i] = y / schaal
    return meta, lon, lat


def eenheidsvectoren(lon: np.ndarray, lat: np.ndarray) -> np.ndarray:
    la = np.radians(lat)
    lo = np.radians(lon)
    return np.stack([np.cos(la) * np.cos(lo), np.sin(la), np.cos(la) * np.sin(lo)], axis=1)


R_AARDE = 6371.0


def dichtstbij(vec: np.ndarray, idx: np.ndarray, lon: float, lat: float):
    """(knoop-id, km) van het dichtstbijzijnde punt uit een deelverzameling."""
    if idx.size == 0:
        return -1, float("inf")
    la, lo = math.radians(lat), math.radians(lon)
    v = np.array([math.cos(la) * math.cos(lo), math.sin(la), math.cos(la) * math.sin(lo)])
    dots = vec[idx] @ v
    k = int(np.argmax(dots))
    d = float(np.clip(dots[k], -1.0, 1.0))
    return int(idx[k]), R_AARDE * math.acos(d)


# --------------------------------------------------------------------------
# HET REGISTER — dit is de redactionele lijst
# --------------------------------------------------------------------------
# Per punt: welke modaliteiten hier samenkomen en welke paren mogen wisselen.
# `haven` = LOCODE in ports.json (de coördinaat komt daarvandaan); `bij` =
# expliciete [lon, lat] voor een punt dat géén haven is (Kasumbalesa is een
# grensovergang, en dat hoeft geen haven te zijn — §3a van het ontwerp).
#
# ⚠️ Een punt ZONDER "zee" biedt nooit een zee-aanhechting aan, hoe dicht MARNET
# ook ligt. Dat is de Duisburg-fix, en hij is redactioneel: Duisburg is de
# grootste binnenhaven ter wereld en wordt door geen zeeschip aangelopen.

REGISTER = [
    # --- Noordwest-Europa: de Rijn-delta -----------------------------------
    dict(id="rotterdam", naam="Rotterdam", haven="NLRTM", modi=["zee", "binnen", "spoor"]),
    dict(id="antwerpen", naam="Antwerpen", haven="BEANR", modi=["zee", "binnen", "spoor"]),
    dict(id="hamburg", naam="Hamburg", haven="DEHAM", modi=["zee", "binnen", "spoor"]),
    dict(id="duisburg", naam="Duisburg", haven="DEDUI", modi=["binnen", "spoor"]),
    dict(id="le-havre", naam="Le Havre", haven="FRLEH", modi=["zee", "binnen", "spoor"]),
    dict(id="gdansk", naam="Gdańsk", haven="PLGDN", modi=["zee", "binnen", "spoor"]),

    # --- Donau / Zwarte Zee -------------------------------------------------
    dict(id="constanta", naam="Constanța", haven="ROCND", modi=["zee", "binnen", "spoor"]),
    dict(id="wenen", naam="Wenen", haven="ATVIE", modi=["binnen", "spoor"]),
    dict(id="boedapest", naam="Boedapest", haven="HUBUD", modi=["binnen", "spoor"]),
    dict(id="novorossiysk", naam="Novorossiysk", haven="RUNVS", modi=["zee", "spoor"]),

    # --- Mississippi-net ----------------------------------------------------
    dict(id="new-orleans", naam="New Orleans", haven="USMSY", modi=["zee", "binnen", "spoor"]),
    dict(id="baton-rouge", naam="Baton Rouge", haven="USBTR", modi=["binnen", "spoor"]),
    dict(id="memphis", naam="Memphis", haven="USMEM", modi=["binnen", "spoor"]),
    dict(id="st-louis", naam="East Saint Louis", haven="USESL", modi=["binnen", "spoor"]),
    dict(id="cincinnati", naam="Cincinnati", haven="USCVG", modi=["binnen", "spoor"]),
    dict(id="chicago", naam="Chicago", haven="USCHI", modi=["zee", "binnen", "spoor"]),
    dict(id="duluth", naam="Duluth-Superior", haven="USDLH", modi=["zee", "binnen", "spoor"]),
    dict(id="houston", naam="Houston", haven="USHOU", modi=["zee", "binnen", "spoor"]),
    dict(id="corpus-christi", naam="Corpus Christi", haven="USCRP", modi=["zee", "spoor"]),
    dict(id="montreal", naam="Montréal", haven="CAMTR", modi=["zee", "binnen", "spoor"]),
    dict(id="vancouver", naam="Vancouver BC", haven="CAVAN", modi=["zee", "spoor"]),

    # --- Zuid-Amerika -------------------------------------------------------
    # Macapá i.p.v. Manaus als zee↔binnen-punt: Manaus is een échte oceaanhaven,
    # maar zijn dichtstbijzijnde MARNET-knoop ligt 1.084 km weg — de zee komt
    # daar via de rivier, niet dwars door het regenwoud. Het riviernet draagt
    # Macapá→Manaus (1.261,9 km), dus de overslag hoort bij de monding.
    dict(id="macapa", naam="Macapá (Amazonemond)", haven="BRMCP", modi=["zee", "binnen"]),
    dict(id="santos", naam="Santos", haven="BRSSZ", modi=["zee", "spoor"]),
    dict(id="rosario", naam="Rosario", haven="ARROS", modi=["zee", "binnen", "spoor"]),
    dict(id="buenos-aires", naam="Buenos Aires", haven="ARBUE", modi=["zee", "binnen", "spoor"]),
    dict(id="callao", naam="Callao", haven="PECLL", modi=["zee", "spoor"]),
    # Géén "weg" bij Matarani/Antofagasta: de wegcorridors eindigen daar niet.
    # Las Bambas→Pillones stopt bij Pillones (148 km van Matarani) en
    # li-atacama-lanegra is een van de drie corridors zonder pad — het dichtste
    # wegpunt bij Antofagasta ligt 857 km verderop. Aanwijzen wat er niet ligt
    # geeft een teleport, niet een overslag.
    dict(id="matarani", naam="Matarani", haven="PEMRI", modi=["zee", "spoor"]),
    dict(id="antofagasta", naam="Antofagasta", haven="CLANF", modi=["zee", "spoor"]),

    # --- Afrika: de Copperbelt-uitgangen -----------------------------------
    dict(id="durban", naam="Durban", haven="ZADUR", modi=["zee", "spoor", "weg"]),
    dict(id="richards-bay", naam="Richards Bay", haven="ZARCB", modi=["zee", "spoor"]),
    dict(id="saldanha", naam="Saldanha Bay", haven="ZASDB", modi=["zee", "spoor"]),
    dict(id="dar-es-salaam", naam="Dar es Salaam", haven="TZDAR", modi=["zee", "spoor", "weg"]),
    dict(id="beira", naam="Beira", haven="MZBEW", modi=["zee", "spoor", "weg"]),
    dict(id="walvis-bay", naam="Walvis Bay", haven="NAWVB", modi=["zee", "spoor", "weg"]),
    dict(id="lobito", naam="Lobito", haven="AOLOB", modi=["zee", "spoor"]),
    # Grensovergang, géén haven — het punt waar de Copperbelt-truckcorridor op
    # het Zambiaanse spoor komt. Precies het geval waarvoor het register een
    # eigen entiteit moest worden i.p.v. een afgeleide van ports.json.
    dict(id="kasumbalesa", naam="Kasumbalesa (grens DRC/Zambia)",
         bij=[27.7940, -12.2530], modi=["spoor", "weg"]),

    # --- Azië ---------------------------------------------------------------
    dict(id="shanghai", naam="Shanghai", haven="CNSHA", modi=["zee", "binnen", "spoor"]),
    dict(id="nanjing", naam="Nanjing", haven="CNNKG", modi=["zee", "binnen", "spoor"]),
    dict(id="wuhan", naam="Wuhan", haven="CNWUH", modi=["binnen", "spoor"]),
    dict(id="chongqing", naam="Chongqing", haven="CNCKG", modi=["binnen", "spoor"]),
    dict(id="tianjin", naam="Tianjin", haven="CNTSN", modi=["zee", "spoor"]),
    dict(id="qingdao", naam="Qingdao", haven="CNTAO", modi=["zee", "spoor"]),
    dict(id="singapore", naam="Singapore", haven="SGSIN", modi=["zee", "spoor"]),
    dict(id="nhava-sheva", naam="Nhava Sheva", haven="INNSA", modi=["zee", "spoor"]),
    dict(id="karachi", naam="Karachi", haven="PKKHI", modi=["zee", "spoor"]),
    dict(id="yokohama", naam="Yokohama", haven="JPYOK", modi=["zee", "spoor"]),

    # --- Oceanië ------------------------------------------------------------
    dict(id="port-hedland", naam="Port Hedland", haven="AUPHE", modi=["zee", "spoor"]),
    dict(id="bunbury", naam="Bunbury", haven="AUBUY", modi=["zee", "spoor", "weg"]),
    dict(id="townsville", naam="Townsville", haven="AUTSV", modi=["zee", "spoor"]),
]

# Welke paren mogen wisselen? Alle paren van de aanwezige modaliteiten, tenzij
# het punt zelf iets anders zegt. Dat is eerlijk: als spoor én zee hier fysiek
# samenkomen (kade + emplacement), dan is overslag daar precies wat er gebeurt.


def paren(modi):
    uit = []
    for i, a in enumerate(modi):
        for b in modi[i + 1:]:
            uit.append([a, b])
    return uit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true", help="knooppunten.json wegschrijven")
    args = ap.parse_args()

    ports = json.loads((DATA / "ports.json").read_text(encoding="utf-8"))
    zee_knopen = ports["zeeKnopen"]
    op_locode = {}
    for i in range(ports["aantal"]):
        op_locode.setdefault(ports["locodes"][i], i)

    print("marnet lezen…", flush=True)
    m_meta, m_lon, m_lat = lees_knopen(DATA / "marnet.json", DATA / "marnet.bin")
    m_vec = eenheidsvectoren(m_lon, m_lat)
    idx_zee = np.arange(0, zee_knopen)
    idx_binnen = np.arange(zee_knopen, len(m_lon))

    print("landnet lezen…", flush=True)
    l_meta, l_lon, l_lat = lees_knopen(DATA / "landnet.json", DATA / "landnet.bin")
    l_vec = eenheidsvectoren(l_lon, l_lat)

    # Modus per landnet-KNOOP afleiden uit de label-ranges (die staan per EDGE).
    # Daarvoor moeten we blok 2 lezen; goedkoper: de bake schrijft labels op
    # oplopende edge-ranges en edges liggen gegroepeerd per label, dus we lezen
    # blok 2 apart uit.
    lezer = Lezer((DATA / "landnet.bin").read_bytes())
    for _ in range(l_meta["knopen"]):
        lezer.volgende(); lezer.volgende()
    n_edges = l_meta["edges"]
    e_a = np.empty(n_edges, dtype=np.int64)
    e_b = np.empty(n_edges, dtype=np.int64)
    a = b = 0
    for i in range(n_edges):
        a += lezer.volgende()
        b += lezer.volgende()
        e_a[i] = a
        e_b[i] = b
        lezer.volgende()          # km
        lezer.volgende()          # soort
        lezer.volgende()          # aantal punten
        if lezer.volgende() == 1:
            for _ in range(4):
                lezer.volgende()

    knoop_modus = np.zeros(l_meta["knopen"], dtype=np.uint8)   # 1=spoor, 2=weg
    for lab in l_meta["labels"]:
        code = 1 if lab["modus"] == "spoor" else 2
        v, t = lab["edgeVan"], min(lab["edgeTot"], n_edges)
        knoop_modus[e_a[v:t]] = code
        knoop_modus[e_b[v:t]] = code
    idx_spoor = np.flatnonzero(knoop_modus == 1)
    idx_weg = np.flatnonzero(knoop_modus == 2)
    print(f"  landnet: {idx_spoor.size:,} spoorknopen · {idx_weg.size:,} wegknopen")

    punten = []
    print()
    print(f"{'punt':28s} {'zee':>10s} {'binnen':>10s} {'spoor':>10s} {'weg':>10s}")
    print("-" * 74)
    fouten = []
    for entry in REGISTER:
        if "bij" in entry:
            lon, lat = entry["bij"]
            bron = f"aangewezen coördinaat"
        else:
            i = op_locode.get(entry["haven"])
            if i is None:
                fouten.append(f"{entry['id']}: LOCODE {entry['haven']} niet in ports.json")
                continue
            lon, lat = ports["ll"][2 * i], ports["ll"][2 * i + 1]
            bron = f"ports.json {entry['haven']}"

        meting = {}
        meting["zee"] = dichtstbij(m_vec, idx_zee, lon, lat)
        meting["binnen"] = dichtstbij(m_vec, idx_binnen, lon, lat)
        meting["spoor"] = dichtstbij(l_vec, idx_spoor, lon, lat)
        meting["weg"] = dichtstbij(l_vec, idx_weg, lon, lat)

        def cel(m):
            k, d = meting[m]
            merk = "*" if m in entry["modi"] else " "
            return f"{merk}{d:9.1f}"

        print(f"{entry['naam'][:28]:28s} " + " ".join(cel(m) for m in ("zee", "binnen", "spoor", "weg")))

        aanhechting = {}
        for m in entry["modi"]:
            k, d = meting[m]
            if k < 0:
                fouten.append(f"{entry['id']}: geen knoop voor modaliteit {m}")
                continue
            # De COÖRDINAAT gaat het register in, niet de knoop-id: ids
            # verschuiven bij elke rebake, coördinaten niet. Voor zee/binnen/
            # spoor/weg nemen we de knoopcoördinaat zelf — dat is de plek waar
            # de overslag fysiek plaatsvindt, en de lader hersnapt hem toch.
            if m in ("zee", "binnen"):
                aanhechting[m] = [round(float(m_lon[k]), 5), round(float(m_lat[k]), 5)]
            else:
                aanhechting[m] = [round(float(l_lon[k]), 5), round(float(l_lat[k]), 5)]

        punten.append({
            "id": entry["id"],
            "naam": entry["naam"],
            **({"locode": entry["haven"]} if "haven" in entry else {}),
            "bij": [round(lon, 5), round(lat, 5)],
            "aanhechting": aanhechting,
            "overslag": paren(entry["modi"]),
            "bron": f"aangewezen 2026-07-23 ({bron})",
        })

    print("-" * 74)
    print("* = aangewezen modaliteit · getal = km tot de dichtstbijzijnde knoop in dat net")
    if fouten:
        print("\n⚠️ FOUTEN:")
        for f in fouten:
            print("  " + f)
        return 1

    uit = {
        "versie": 1,
        "toelichting": (
            "Aangewezen overslagpunten. Een eigen entiteit met eigen ids — géén "
            "afgeleide van ports.json (LOCODE is geen sleutel: 38 duplicaten, "
            "waaronder USPWM = Portland Oregon én Portland Maine). Een punt "
            "zonder 'zee' biedt nooit een zee-aanhechting aan, hoe dicht MARNET "
            "ook ligt."
        ),
        "punten": punten,
    }
    print(f"\n{len(punten)} punten · "
          f"{sum(len(p['overslag']) for p in punten)} toegestane overstappen")
    if args.schrijf:
        pad = DATA / "knooppunten.json"
        pad.write_text(json.dumps(uit, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"geschreven: {pad} ({pad.stat().st_size / 1024:.1f} KB)")
    else:
        print("(niets geschreven — geef --schrijf mee)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
