#!/usr/bin/env python3
"""voeg_been_toe.py — benen AANHECHTEN aan een al gebakken stroom, zonder de
bestaande benen aan te raken en zonder de stroom opnieuw te bakken.

WAAROM DIT BESTAAT. Een stroom groeit in fasen: eerst A-C, later D/E. De
bestaande weg om dat te doen is `hecht_marnet route` opnieuw draaien met álle
benen — maar dat herbakt ook de benen die al goedgekeurd zijn, en dat is precies
wat je niet wilt:

  * een herbake verandert benen die niemand ter discussie stelde (de
    generator↔uitvoer-drift is in dit project al drie keer opgedoken, en
    `snoei_keerlussen` veranderde met terugwerkende kracht een grafietbeen van
    502,7 naar 497,9 km);
  * de ene bake maakt de andere ongeldig — met vijf stromen die elk hun eigen
    netstadium dragen, is "alles opnieuw" een vorm van werk die zichzelf
    aanvult zonder dat de kaart beter wordt (besluit Lars, 2026-08-06);
  * en `collahuasi-tongling` HEEFT geen bak-recept, dus voor die stroom is
    "opnieuw bakken" niet eens gedefinieerd.

`vervang_spoorbeen.py` loste de spiegelvorm hiervan al op (één been VERVANGEN);
dit is dezelfde gedachte voor TOEVOEGEN. Zelfde discipline: één commando dat in
de geschiedenis terug te vinden is, niet met de hand in het json knippen — een
gegenereerd bestand dat met de hand is bijgewerkt loopt stil uit de pas met zijn
generator (de cu-guixi-spoor-les, 741 m).

⚠️ HET GAT NAAR HET VORIGE BEEN WORDT GEMETEN EN GERAPPORTEERD, NIET
DICHTGETROKKEN. Een naad tussen twee benen is in dit project inhoudelijke
informatie: 0 m betekent dat de netten elkaar raken, en een gat van honderden
meters is een PROCESGAT dat het ontbrekende anker aanwijst (Guixi 584 m,
De Soto 443 m). Boven --max-gat-km weigert het script, want dan is het geen
procesgat meer maar een fout uiteinde.

Draaien:
    python v2/tools/voeg_been_toe.py \\
        --stroom v2/data/stroomroute-koper-collahuasi-tongling.json \\
        --been "weg|kathode → foliefabriek|v2/build-cache/.../stroombeen-x.geojson" \\
        --stippel "weg|last mile|30.98656,117.77180|30.98700,117.77300" \\
        --marker "铜冠铜箔 — foliefabriek|30.9xxxx,117.7xxxx" \\
        --max-gat-km 1.0
"""
import argparse
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import bake_marnet as bm   # noqa: E402 — gc_km


class _KetenActie(argparse.Action):
    """Houdt de volgorde vast over --been en --stippel heen; de reisvolgorde is
    de volgorde waarin de vlaggen op de opdrachtregel staan (zelfde patroon als
    hecht_marnet.py, zodat de twee tools zich hetzelfde gedragen)."""

    def __call__(self, parser, ns, waarde, optie=None):
        if getattr(ns, "keten", None) is None:
            ns.keten = []
        soort = {"--been": "geojson", "--stippel": "stippel"}[optie]
        ns.keten.append((soort, waarde))


def lees_lijn(pad):
    d = json.load(open(pad, encoding="utf-8"))
    g = d["features"][0]["geometry"] if d.get("type") == "FeatureCollection" else d
    if g["type"] == "LineString":
        return [tuple(p) for p in g["coordinates"]]
    if g["type"] == "MultiLineString":
        uit = []
        for deel in g["coordinates"]:
            uit.extend(tuple(p) for p in deel)
        return uit
    raise SystemExit(f"geen (Multi)LineString in {pad}")


def _punt(spec, wat):
    deel = spec.split(",")
    if len(deel) != 2:
        sys.exit(f"{wat}: verwacht LAT,LON — kreeg {spec!r}")
    return float(deel[0]), float(deel[1])


def _lengte_km(punten):
    return sum(bm.gc_km(punten[j - 1], punten[j]) for j in range(1, len(punten)))


def main():
    ap = argparse.ArgumentParser(
        description="benen aanhechten aan een gebakken stroomroute-*.json")
    ap.add_argument("--stroom", required=True)
    ap.add_argument("--been", dest="keten", action=_KetenActie, default=None,
                    metavar="MOD|NAAM|PAD",
                    help="herhaalbaar: been uit een GeoJSON-lijn ([lon,lat]), "
                         "doorgetrokken opgenomen")
    ap.add_argument("--stippel", dest="keten", action=_KetenActie,
                    metavar="MOD|NAAM|VAN_LAT,VAN_LON|NAAR_LAT,NAAR_LON",
                    help="herhaalbaar: rechte lijn van twee punten, "
                         "'stippel': true — eigen verbinding of net reikt niet")
    ap.add_argument("--marker", action="append", default=[],
                    metavar="NAAM|LAT,LON", help="herhaalbaar")
    ap.add_argument("--max-gat-km", type=float, default=1.0,
                    help="grens op de naad tussen het laatste bestaande been "
                         "en het eerste nieuwe (default 1,0 km). Erboven is het "
                         "geen procesgat maar een fout uiteinde")
    ap.add_argument("--droog", action="store_true", help="alleen rapporteren")
    args = ap.parse_args()

    if not args.keten:
        sys.exit("geen --been of --stippel opgegeven — niets te doen")

    d = json.load(open(args.stroom, encoding="utf-8"))
    if d.get("punt_formaat") != "lonlat":
        sys.exit(f"onverwacht punt_formaat {d.get('punt_formaat')!r}")
    oude_benen = len(d["benen"])
    oude_km = sum(b.get("km", 0.0) for b in d["benen"])

    nieuw = []
    for soort, spec in args.keten:
        deel = spec.split("|")
        if soort == "geojson":
            if len(deel) != 3:
                sys.exit(f"--been: verwacht MOD|NAAM|PAD — kreeg {spec!r}")
            mod, naam, pad = deel
            if not os.path.exists(pad):
                sys.exit(f"--been: bestand niet gevonden: {pad}")
            punten = lees_lijn(pad)
            if len(punten) < 2:
                sys.exit(f"--been: minder dan 2 punten in {pad}")
            nieuw.append({"modaliteit": mod, "naam": naam,
                          "km": round(_lengte_km(punten), 1),
                          "punten": [[round(lo, 5), round(la, 5)]
                                     for lo, la in punten],
                          "_bron": os.path.basename(pad)})
        else:
            if len(deel) != 4:
                sys.exit(f"--stippel: verwacht MOD|NAAM|VAN|NAAR — kreeg {spec!r}")
            mod, naam, van, naar = deel
            la_a, lo_a = _punt(van, "--stippel van")
            la_b, lo_b = _punt(naar, "--stippel naar")
            punten = [(lo_a, la_a), (lo_b, la_b)]
            nieuw.append({"modaliteit": mod, "naam": naam, "stippel": True,
                          "km": round(_lengte_km(punten), 3),
                          "punten": [[round(lo, 5), round(la, 5)]
                                     for lo, la in punten],
                          "_bron": "rechte lijn"})

    # ── de naad naar het bestaande laatste been ────────────────────────────
    staart = d["benen"][-1]["punten"][-1]
    kop = nieuw[0]["punten"][0]
    gat = bm.gc_km(tuple(staart), tuple(kop))
    print(f"stroom: {d['stroom']} — {oude_benen} benen · {oude_km:,.1f} km")
    print(f"naad naar het bestaande laatste been "
          f"[{d['benen'][-1]['modaliteit']}] {d['benen'][-1]['naam']}:")
    print(f"  {gat*1000:,.0f} m")
    if gat > args.max_gat_km:
        sys.exit(
            f"GEWEIGERD: de naad is groter dan {args.max_gat_km:g} km. Een gat van "
            f"deze orde is geen bewust procesgat maar een fout uiteinde — het "
            f"eerste nieuwe been begint ergens anders dan de bestaande keten "
            f"ophoudt. Controleer de ankers, of verhoog --max-gat-km met een "
            f"reden in de routebrief.")

    print("\ntoe te voegen benen:")
    for b in nieuw:
        print(f"  [{b['modaliteit']}] {b['naam']} · {b['km']:,.3f} km · "
              f"{len(b['punten'])} pt · stippel={b.get('stippel', False)} "
              f"· uit {b['_bron']}")

    # naden tussen de nieuwe benen onderling
    for a, b in zip(nieuw, nieuw[1:]):
        g = bm.gc_km(tuple(a["punten"][-1]), tuple(b["punten"][0]))
        print(f"  naad {a['naam']} -> {b['naam']}: {g*1000:,.0f} m")

    markers = []
    for spec in args.marker:
        deel = spec.split("|")
        if len(deel) != 2:
            sys.exit(f"--marker: verwacht NAAM|LAT,LON — kreeg {spec!r}")
        la, lo = _punt(deel[1], "--marker")
        markers.append({"naam": deel[0], "lon": round(lo, 5), "lat": round(la, 5)})
    for m in markers:
        print(f"  marker: {m['naam']} ({m['lat']}, {m['lon']})")

    nieuwe_km = oude_km + sum(b["km"] for b in nieuw)
    print(f"\nna toevoegen: {oude_benen + len(nieuw)} benen · {nieuwe_km:,.1f} km")

    if args.droog:
        print("(droog — niets weggeschreven)")
        return

    for b in nieuw:
        b.pop("_bron", None)
    d["benen"].extend(nieuw)
    d.setdefault("markers", []).extend(markers)
    with open(args.stroom, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
    print(f"weggeschreven: {args.stroom}")


if __name__ == "__main__":
    main()
