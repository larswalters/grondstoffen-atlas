#!/usr/bin/env python3
"""
maak_rivierbeen_wesel.py — het Wesel-vak van de Rijn als ECHTE riviergeometrie,
uit de lokale Geofabrik-extract `de-nrw-latest.osm.pbf`.

── WAAROM DIT BESTAAT ─────────────────────────────────────────────────────
Been 6 van `stroomroute-koper-lobito-duisburg.json` was een KAARSRECHTE stippel
van 47,3 km met twee punten, tussen de laatste AIS-ping stroomafwaarts
(51,7540 / 6,3660) en de eerstvolgende stroomopwaarts (51,4000 / 6,7450). Die
stippel bestaat om een gemeten reden: over dat vak liggen **0 van 35.237**
collector-tracks (lon 6,45–6,60, structureel gemeten over 12,5 uur —
`memory/bugs-and-risks.md`).

⚠️ MAAR "GEEN AIS" ZEGT NIETS OVER OF DE GEOMETRIE BESTAAT. Dat is de
Escondida-denkfout, nu op water: daar stond een leiding recht omdat OSM hem niet
als doorlopende pijp kende, terwijl het tracé wél te volgen was. Hier is het nog
scherper — de Rijn ligt in dit vak **volledig in OSM**: tien ways
`waterway=river` + `name=Rhein`, aaneengesloten via gedeelde node-ids, samen
103,5 km binnen het venster. De rechte lijn lag er tot **8,19 km** vanaf
(bij 51,3504 / 6,6576). Een rechte lijn was hier dus geen vereenvoudiging maar
een fout, precies zoals bij Escondida.

⚠️ WAT DIT BEEN WEL EN NIET VERANDERT. De stippel is een AIS-uitspraak, dit been
is een GEOMETRIE-uitspraak. Ze spreken elkaar niet tegen: we weten nu waar het
water ligt, we hebben nog steeds geen waarneming van een schip dat er vaart.
Dat is dezelfde rolverdeling als bij het Escondida-leidingbeen — doorgetrokken
betekent in dit project "we weten waar de lijn ligt", niet "we hebben hem zien
rijden". Het meten van de dekking blijft dus staan; alleen de reden om hier een
rechte lijn te tekenen is vervallen.

WAAROM NIET `maak_rivierbeen.py` (dat tool bestaat hiervoor). Gemeten, niet
aangenomen: op de MARNET-bulklaag draaien geeft wél een pad (68,93 km / 384
punten), maar met twee bezwaren die hier beslissend zijn:
  1. de bulklaag draagt **geen namen** — alle 15.721 EU-edges zitten in één
     systeem `bulk-eu`, dus er is geen manier om te toetsen dat het gevonden pad
     de Rijn is en niet een havenkanaal of een oude arm. Bij Duisburg (de
     grootste binnenhaven ter wereld) is dat geen theoretisch bezwaar;
  2. het pad begint en eindigt op een BULK-KNOOP, en die liggen ~10 km uit
     elkaar: de uiteinden kwamen 1,38 km resp. 1,29 km van de gevraagde punten
     te liggen. De keten eist ≤ 300 m.
De bulklaag blijft wel de onafhankelijke tweede meting: dit tool rapporteert
zijn eigen lengte, en 68,93 km uit een andere pijplijn is de kruiscontrole.

WAT DIT TOOL DOET, in vier stappen die elk hun eigen maat afdrukken:
  1. lees `waterway=river` + `name=Rhein` uit de lokale NRW-extract (pyosmium,
     dezelfde leesroutine als `fetch_waterways.py`);
  2. stik de ways aan elkaar op GEDEELDE NODE-IDS — niet op afstand. OSM's
     topologie is exact (verbonden ⟺ gedeelde node), dezelfde regel die op
     2026-07-29 de spoorgraaf 1-op-1 maakte. Blijft er meer dan één keten over,
     dan stopt het tool i.p.v. een gat te overbruggen;
  3. knip de keten op de LOODRECHTE PROJECTIES van de twee been-uiteinden
     (`knip_osm_been.projecteer/knip` — hetzelfde gereedschap dat op 05-08 de
     overschiet-en-terug-fout bij Guixi oploste, hier op een rivier);
  4. vereenvoudig met Douglas-Peucker en rapporteer wat dat kost. ⚠️ De
     OSM-middellijn is hier al grover dan de doelkorrel van 200 m (313 m per
     punt gemeten), dus deze stap DUNT niet — de tolerantie is een
     vorm-tolerantie: 10 m is de maximale afwijking van de OSM-lijn, dezelfde
     waarde en dezelfde redenering als de landnet-simplify van 2026-07-29
     ("de tolerantie ÍS de maximale afwijking").

⚠️ DE BRON IS EEN LOKAAL EXTRACT EN DUS ONGETRACKT (v2/.gitignore dekt
   build-cache/). Op een verse clone draait dit script niet zonder eerst
   `fetch_waterways.py geofabrik --download` voor de-nrw. Dat geldt voor élk
   --been-geojson in bak_stromen.sh behalve het Escondida-leidingbeen, dat zijn
   puntenlijst in de broncode draagt.

Draaien vanuit de repo-root:
    python v2/tools/maak_rivierbeen_wesel.py
Daarna komt het been de stroom in als:
    --been-geojson "binnenvaart|…|v2/build-cache/ais/graaf/rivierbeen-wesel.geojson"
"""
import argparse
import json
import math
import os
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))

from knip_osm_been import km, knip, projecteer   # noqa: E402 — hergebruik

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

WORTEL = HIER.parent                                     # …/v2
PBF = WORTEL / "build-cache" / "geofabrik" / "de-nrw-latest.osm.pbf"
UIT = WORTEL / "build-cache" / "ais" / "graaf" / "rivierbeen-wesel.geojson"

# De twee been-uiteinden = de laatste/eerstvolgende AIS-ping rond het gat.
# Ze staan hier als default omdat ze de REDEN van dit bestand zijn; met
# --van/--naar is het tool ook op een ander vak te draaien.
VAN = (51.7540, 6.3660)      # lat, lon — laatste ping stroomafwaarts (bij Rees)
NAAR = (51.4000, 6.7450)     # lat, lon — eerstvolgende ping (Duisburg)

# Het venster waarin de Rijn-ways worden gezocht. Ruim om de twee uiteinden
# heen, maar niet ruimer: hoe kleiner het venster, hoe kleiner de kans dat een
# ver weg liggende gelijknamige way de keten vertakt.
VENSTER = (6.10, 6.95, 51.25, 51.90)                     # lon0 lon1 lat0 lat1


# ── 1 · lezen ──────────────────────────────────────────────────────────────
def lees_ways(pbf, naam, venster):
    """Alle `waterway=river`-ways met deze naam die het venster raken, mét hun
    node-ids (die zijn de topologie, niet de coördinaten)."""
    import osmium                                        # alleen dit pad

    lo0, lo1, la0, la1 = venster
    fp = (osmium.FileProcessor(str(pbf))
          .with_locations()
          .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
          .with_filter(osmium.filter.KeyFilter("waterway")))
    uit = []
    for obj in fp:
        t = obj.tags
        if t.get("waterway") != "river":
            continue
        if (t.get("name") or t.get("name:de") or "") != naam:
            continue
        pts, refs = [], []
        for n in obj.nodes:
            if n.location.valid():
                pts.append((n.location.lon, n.location.lat))
                refs.append(n.ref)
        if len(pts) < 2:
            continue
        if not any(lo0 <= lo <= lo1 and la0 <= la <= la1 for lo, la in pts):
            continue
        uit.append({"id": obj.id, "pts": pts, "refs": refs,
                    "tags": {k: v for k, v in t}})
    return uit


# ── 2 · stikken op gedeelde node-ids ───────────────────────────────────────
def stik(ways):
    """Ketens bouwen door ways aan elkaar te leggen waar ze een node-id delen.
    Geen afstandsdrempel: OSM zegt zélf of twee ways verbonden zijn."""
    los = {w["id"]: w for w in ways}
    ketens = []
    while los:
        w = los.pop(next(iter(los)))
        pts, refs, gebruikt = list(w["pts"]), list(w["refs"]), [w["id"]]
        gegroeid = True
        while gegroeid:
            gegroeid = False
            for wid, x in list(los.items()):
                if x["refs"][0] == refs[-1]:
                    pts += x["pts"][1:]; refs += x["refs"][1:]
                elif x["refs"][-1] == refs[-1]:
                    pts += x["pts"][::-1][1:]; refs += x["refs"][::-1][1:]
                elif x["refs"][-1] == refs[0]:
                    pts = x["pts"][:-1] + pts; refs = x["refs"][:-1] + refs
                elif x["refs"][0] == refs[0]:
                    pts = x["pts"][::-1][:-1] + pts
                    refs = x["refs"][::-1][:-1] + refs
                else:
                    continue
                del los[wid]; gebruikt.append(wid); gegroeid = True
        ketens.append({"pts": pts, "refs": refs, "ways": gebruikt})
    ketens.sort(key=lambda k: -lengte(k["pts"]))
    return ketens


def lengte(pts):
    return sum(km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


# ── 4 · vereenvoudigen ─────────────────────────────────────────────────────
def dp(pts, tol_km):
    """Douglas-Peucker, uiteinden vast. Verwijdert alleen punten die minder dan
    `tol_km` van de rechte lijn tussen hun buren-op-afstand liggen; de maximale
    afwijking van de oorspronkelijke lijn ís dus de tolerantie (de les van de
    landnet-simplify van 2026-07-29)."""
    if len(pts) < 3:
        return list(pts)
    houd = [False] * len(pts)
    houd[0] = houd[-1] = True
    stapel = [(0, len(pts) - 1)]
    while stapel:
        i, j = stapel.pop()
        if j <= i + 1:
            continue
        beste, bi = -1.0, None
        for k in range(i + 1, j):
            d, _, _, _ = projecteer(pts[k], [pts[i], pts[j]])
            if d > beste:
                beste, bi = d, k
        if beste > tol_km:
            houd[bi] = True
            stapel += [(i, bi), (bi, j)]
    return [p for p, h in zip(pts, houd) if h]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pbf", default=str(PBF))
    ap.add_argument("--naam", default="Rhein",
                    help="OSM-naam van de rivier (exacte match op name/name:de)")
    ap.add_argument("--van", default=f"{VAN[0]},{VAN[1]}", help="lat,lon")
    ap.add_argument("--naar", default=f"{NAAR[0]},{NAAR[1]}", help="lat,lon")
    ap.add_argument("--korrel-m", type=float, default=200.0,
                    help="doelkorrel na vereenvoudiging (meter per punt)")
    ap.add_argument("--simplify-m", type=float, default=10.0,
                    help="Douglas-Peucker-tolerantie in meter = de maximale "
                         "afwijking van de OSM-lijn")
    ap.add_argument("--max-aanloop-m", type=float, default=300.0,
                    help="hard maximum voor uiteinde → rivier; erboven stopt "
                         "het tool, want dan hangt het been aan niets")
    ap.add_argument("--uit", default=str(UIT))
    a = ap.parse_args()

    def punt(s):
        la, lo = (float(x) for x in s.split(","))
        return (lo, la)                                  # intern (lon, lat)

    van, naar = punt(a.van), punt(a.naar)
    if not Path(a.pbf).exists():
        sys.exit(f"extract niet gevonden: {a.pbf}\n"
                 f"  haal hem op met: python v2/tools/fetch_waterways.py "
                 f"geofabrik --download")

    ways = lees_ways(Path(a.pbf), a.naam, VENSTER)
    if not ways:
        sys.exit(f"geen waterway=river met naam {a.naam!r} in het venster")
    print(f"BRON  {Path(a.pbf).name} · waterway=river · name={a.naam!r}")
    print(f"  {len(ways)} ways · {lengte([p for w in ways for p in w['pts']]):.0f} km ruw "
          f"(losse ways, som van de eigen lengtes: "
          f"{sum(lengte(w['pts']) for w in ways):.2f} km)")

    ketens = stik(ways)
    print(f"\nSTIKKEN (op gedeelde node-ids, geen afstandsdrempel)")
    for i, k in enumerate(ketens):
        print(f"  keten {i}: {len(k['ways'])} ways · {lengte(k['pts']):.2f} km · "
              f"{len(k['pts'])} punten · "
              f"({k['pts'][0][1]:.4f}, {k['pts'][0][0]:.4f}) → "
              f"({k['pts'][-1][1]:.4f}, {k['pts'][-1][0]:.4f})")
    if len(ketens) > 1:
        rest = sum(lengte(k["pts"]) for k in ketens[1:])
        print(f"  ⚠️ {len(ketens)} ketens — {rest:.2f} km ligt LOS van de "
              f"hoofdketen. Niet overbrugd: een gat dichttrekken met geleende "
              f"geometrie is precies wat dit project niet doet.")
    keten = ketens[0]["pts"]

    # ── controleren dat beide uiteinden op DEZE keten liggen ───────────────
    dv, _, _, pv = projecteer(van, keten)
    dn, _, _, pn = projecteer(naar, keten)
    print(f"\nAANHECHTING (loodrechte projectie op de keten)")
    print(f"  van  ({van[1]:.4f}, {van[0]:.4f}) → {dv*1000:6.0f} m  "
          f"op ({pv[1]:.5f}, {pv[0]:.5f})")
    print(f"  naar ({naar[1]:.4f}, {naar[0]:.4f}) → {dn*1000:6.0f} m  "
          f"op ({pn[1]:.5f}, {pn[0]:.5f})")
    for naam_, d in (("van", dv), ("naar", dn)):
        if d * 1000 > a.max_aanloop_m:
            sys.exit(f"STOP: uiteinde '{naam_}' ligt {d*1000:.0f} m van de "
                     f"{a.naam} (max {a.max_aanloop_m:.0f} m).")

    stuk, _, _, vooruit = knip(keten, van, naar)
    ruw_km, ruw_n = lengte(stuk), len(stuk)
    richting = ("volgorde van de keten" if vooruit else
                "omgekeerd — de keten is stroomopwaarts getekend, het been "
                "vaart stroomafwaarts → stroomopwaarts")
    print("\nKNIPPEN")
    print(f"  richting: {richting}")
    print(f"  ruw been: {ruw_km:.2f} km · {ruw_n} punten "
          f"({ruw_km*1000/max(1, ruw_n-1):.0f} m per punt)")

    lijn = dp(stuk, a.simplify_m / 1000.0)
    kmTot = lengte(lijn)
    print(f"\nVEREENVOUDIGEN (Douglas-Peucker, tolerantie {a.simplify_m:.0f} m)")
    korrel = kmTot * 1000 / max(1, len(lijn) - 1)
    print(f"  {ruw_n} → {len(lijn)} punten · {kmTot:.2f} km "
          f"({kmTot-ruw_km:+.3f} km) · "
          f"{korrel:.0f} m per punt (doelkorrel {a.korrel_m:.0f} m)")
    if korrel > a.korrel_m:
        print(f"  ⚠️ grover dan de doelkorrel — de OSM-middellijn is hier zelf "
              f"al {ruw_km*1000/max(1, ruw_n-1):.0f} m per punt. Deze stap "
              f"DUNT dus niet, hij begrenst alleen de vormfout op "
              f"{a.simplify_m:.0f} m. Verdichten zou punten VERZINNEN.")

    # ── de eigen maten, want een been dat zijn maten niet afdrukt is niet
    #    toetsbaar (de toets_corridor.py-les) ────────────────────────────────
    recht = km(lijn[0], lijn[-1])
    verh = kmTot / recht if recht else float("inf")
    # grootste afstand van de RECHTE lijn tot de werkelijke loop = wat de oude
    # stippel fout stond
    afw = max(projecteer(p, [lijn[0], lijn[-1]])[0] for p in lijn)
    afw_p = max(lijn, key=lambda p: projecteer(p, [lijn[0], lijn[-1]])[0])
    # terugloop: hoeveel van de lijn loopt tégen de reisrichting in
    terug = 0.0
    for i in range(len(lijn) - 1):
        vooruit_km = km(lijn[i], lijn[-1]) - km(lijn[i + 1], lijn[-1])
        if vooruit_km < 0:
            terug += -vooruit_km
    print(f"\nMATEN")
    print(f"  lengte           : {kmTot:.2f} km · {len(lijn)} punten")
    print(f"  hemelsbreed      : {recht:.2f} km  (de oude rechte stippel)")
    print(f"  pad ÷ hemelsbreed: {verh:.3f}")
    print(f"  kop → gevraagd   : {km(lijn[0], van)*1000:.0f} m   "
          f"(eis ≤ {a.max_aanloop_m:.0f} m)")
    print(f"  staart → gevraagd: {km(lijn[-1], naar)*1000:.0f} m   "
          f"(eis ≤ {a.max_aanloop_m:.0f} m)")
    print(f"  max afwijking van de rechte lijn: {afw:.2f} km "
          f"bij ({afw_p[1]:.4f}, {afw_p[0]:.4f})")
    print(f"  netto terugloop (som van de stappen die van het einde AF gaan): "
          f"{terug*1000:.0f} m")

    props = {
        "id": "cu-lobito-b6-wesel",
        "naam": f"{a.naam} — Wesel-vak (Rees → Duisburg), echte riviergeometrie",
        "modaliteit": "binnenvaart",
        "km": round(kmTot, 3),
        "punten": len(lijn),
        "hemelsbreedKm": round(recht, 3),
        "omwegfactor": round(verh, 3),
        "maxAfwijkingRechteLijnKm": round(afw, 3),
        "kopTotGevraagdM": round(km(lijn[0], van) * 1000, 1),
        "staartTotGevraagdM": round(km(lijn[-1], naar) * 1000, 1),
        "bron": (f"OSM (ODbL) via {Path(a.pbf).name}: {len(ketens[0]['ways'])} "
                 f"ways waterway=river name={a.naam}, gestikt op gedeelde "
                 f"node-ids, geknipt op de loodrechte projecties van de twee "
                 f"AIS-uiteinden, Douglas-Peucker {a.simplify_m:.0f} m"),
        "osmWays": ketens[0]["ways"],
        "voorbehoud": ("GEOMETRIE, GEEN WAARNEMING: over dit vak liggen 0 van "
                       "35.237 collector-tracks (lon 6,45-6,60, 12,5 uur). Dit "
                       "been zegt waar het water ligt, niet dat wij hier een "
                       "schip gezien hebben."),
        "gereedschap": "maak_rivierbeen_wesel.py",
    }
    doc = {"type": "FeatureCollection", "features": [
        {"type": "Feature", "properties": props,
         "geometry": {"type": "LineString",
                      "coordinates": [[round(lo, 5), round(la, 5)]
                                      for lo, la in lijn]}}]}
    pad = Path(a.uit)
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    print(f"\n  geschreven: {pad} · {os.path.getsize(pad)/1024:.1f} KB")


if __name__ == "__main__":
    main()
