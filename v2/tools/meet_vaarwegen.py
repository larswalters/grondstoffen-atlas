"""Meet hoeveel bevaarbaar water er in de Geofabrik-extracts zit (M24 · scope-verbreding).

Waarom dit bestaat: Lars koos "alles wat bevaarbaar is" als scope-ondergrens in
plaats van CEMT >= IV, met het argument dat M25 (spoor/weg) straks uitkomt op
plekken waar anders geen water ligt. Voordat die keuze in Linear vastgelegd wordt
moet vaststaan wat hij KOST — in kilometers, in knopen en in `marnet.bin`-bytes.
Dit script beantwoordt dat zonder dat er iets gebakken hoeft te worden.

De tegenhanger van `meet_spoor.py` (M25 · LAR-491), zelfde opzet en zelfde
uitgangspunt: ALLEEN LEZEN, raakt geen data en geen cache aan.

VIER LAGEN, want de ondergrens is precies de open vraag:

    A  soort         waterway in {river, canal, fairway}          = het plafond
    B  + naam        idem, mét een naam                           = wat stitchbaar is
    C  bevaarbaar    een expliciet bevaarbaarheidssignaal         <- Lars' keuze
    D  CEMT >= IV    het huidige strenge criterium                = wat we nu doen

Laag C matcht op CEMT-tag, boat/motorboat/ship=yes, draft/maxdraft, of
usage=transportation. Bewust ONGEACHT het soort-veld: bij de sluis van Poses
draagt de doorgaande Seine-vaargeul `waterway=stream` mét naam en CEMT (de derde
foutcategorie — het TYPE kan fout gemapt zijn). Die gevallen worden apart geteld
zodat zichtbaar is hoe groot dat effect is.

⚠️ De vertex-telling is RUWE OSM-dichtheid en dus geen databegroting. De atlas
bakt na `strak_trekken()` op ~3,6 punten/km (gemeten: Yangon 83 punten over
23,2 km). Het rapport rekent dat allebei door.

Gebruik:
    python v2/tools/meet_vaarwegen.py v2/build-cache/geofabrik/*.osm.pbf
    python v2/tools/meet_vaarwegen.py --alles          # alle extracts in build-cache

Extracts komen uit het Geofabrik-pad van fetch_waterways.py:
    python v2/tools/fetch_waterways.py geofabrik --download
"""
import sys
import os
import glob
import math
import time
from collections import Counter

import osmium

R_AARDE = 6371.0

# Het plafond: wat überhaupt een vaargeul kan zijn. `stream`/`ditch`/`drain`
# horen hier NIET in — die komen alleen binnen via het bevaarbaarheidssignaal.
SOORTEN = {"river", "canal", "fairway"}

# CEMT-klassen op volgorde. `0` bestaat in OSM en betekent "buiten klasse"
# (vaak een klein kanaal) -> rang 0, valt dus nooit onder de >= IV-drempel.
CEMT_RANG = {
    "0": 0, "I": 1, "II": 2, "III": 3, "IV": 4,
    "Va": 5, "Vb": 6, "VIa": 7, "VIb": 8, "VIc": 9, "VII": 10,
}
CEMT_DREMPEL = 4  # >= IV

JA = {"yes", "designated", "permissive", "official"}


def km(a, b):
    """Haversine tussen (lon,lat)-paren — zelfde formule als fetch_waterways."""
    (lo1, la1), (lo2, la2) = a, b
    p1, p2 = math.radians(la1), math.radians(la2)
    dp, dl = p2 - p1, math.radians(lo2 - lo1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_AARDE * math.asin(min(1.0, math.sqrt(h)))


def lengte(pts):
    return sum(km(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def cemt_rang(t):
    """Rang van de CEMT-tag, of None als hij ontbreekt/onleesbaar is."""
    v = t.get("CEMT")
    if v is None:
        return None
    return CEMT_RANG.get(v.strip())


def bevaarbaar_signaal(t):
    """Een expliciete aanwijzing dat hier vracht of gemotoriseerd verkeer vaart.

    Bewust ruim: dit IS de verbrede ondergrens. Een `boat=yes` op een kanaal van
    klasse II telt mee, want daar kan straks een spoorterminal op uitkomen.
    """
    if t.get("CEMT") is not None:
        return "CEMT"
    for k in ("ship", "motorboat", "boat"):
        if (t.get(k) or "").strip() in JA:
            return k
    for k in ("draft", "maxdraft", "maxdraught"):
        if t.get(k):
            return "draft"
    if (t.get("usage") or "").strip() == "transportation":
        return "usage"
    return None


def leeg():
    return dict(km=0.0, ways=0, vertices=0)


def tel(bak, L, n):
    bak["km"] += L
    bak["ways"] += 1
    bak["vertices"] += n


def meet(pad):
    lagen = {k: leeg() for k in ("A", "B", "C", "D")}
    # De Poses-categorie: bevaarbaarheidssignaal op een soort die er niet in hoort.
    fout_getypeerd = leeg()
    soort_val = Counter()
    signaal_val = Counter()
    cemt_val = Counter()

    fp = (osmium.FileProcessor(pad)
          .with_locations()
          .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
          .with_filter(osmium.filter.KeyFilter("waterway")))

    for obj in fp:
        t = obj.tags
        soort = t.get("waterway")
        sig = bevaarbaar_signaal(t)

        # Alleen geometrie berekenen voor wat kan meetellen — scheelt de helft
        # van de tijd, want `stream`/`ditch` domineren elk extract in aantal.
        if soort not in SOORTEN and sig is None:
            continue

        pts = [(n.location.lon, n.location.lat) for n in obj.nodes
               if n.location.valid()]
        if len(pts) < 2:
            continue
        L, n = lengte(pts), len(pts)

        soort_val[soort] += 1
        if sig:
            signaal_val[sig] += 1
        rang = cemt_rang(t)
        if t.get("CEMT") is not None:
            cemt_val[t.get("CEMT")] += 1

        if soort in SOORTEN:
            tel(lagen["A"], L, n)
            if t.get("name"):
                tel(lagen["B"], L, n)
        else:
            # soort valt buiten SOORTEN maar draagt wél een signaal
            tel(fout_getypeerd, L, n)

        if sig:
            tel(lagen["C"], L, n)
        if rang is not None and rang >= CEMT_DREMPEL:
            tel(lagen["D"], L, n)

    return dict(lagen=lagen, fout_getypeerd=fout_getypeerd, soort_val=soort_val,
                signaal_val=signaal_val, cemt_val=cemt_val)


LABELS = {
    "A": "A  soort river/canal/fairway",
    "B": "B  + heeft een naam",
    "C": "C  bevaarbaarheidssignaal  <- gekozen ondergrens",
    "D": "D  CEMT >= IV              (huidig criterium)",
}


def toon_lagen(lagen, fout):
    print(f"{'laag':<44} {'km':>11} {'ways':>9} {'vertices':>11}")
    for k in ("A", "B", "C", "D"):
        b = lagen[k]
        print(f"{LABELS[k]:<44} {b['km']:>11,.0f} {b['ways']:>9,} {b['vertices']:>11,}")
    if fout["ways"]:
        print(f"{'   waarvan fout getypeerd (Poses-categorie)':<44}"
              f" {fout['km']:>11,.0f} {fout['ways']:>9,} {fout['vertices']:>11,}")


def budget(km_c):
    """Wat laag C kost: knopen in de routeergraaf, punten in marnet.bin."""
    print(f"\nbudget bij de gekozen ondergrens (laag C = {km_c:,.0f} km):")
    print(f"  routeergraaf   {km_c / 15.0:>10,.0f} knopen bij 15 km bemonstering"
          f"   (huidige vuistregel)")
    # 3,6 punten/km is de gemeten dichtheid NA strak_trekken (Yangon: 83 punten
    # over 23,2 km). ~4 byte/punt is de varint-delta-codering van marnet.bin.
    punten = km_c * 3.6
    print(f"  tekengeometrie {punten:>10,.0f} punten na strak_trekken (3,6/km)"
          f"  = {punten * 4 / 1e6:,.1f} MB in marnet.bin")


def rapport(naam, r):
    print(f"\n{'=' * 78}\n{naam}\n{'=' * 78}")
    toon_lagen(r["lagen"], r["fout_getypeerd"])
    print("\nsoort=*    :", ", ".join(f"{k}={v}" for k, v in r["soort_val"].most_common(6)))
    print("signaal    :", ", ".join(f"{k}={v}" for k, v in r["signaal_val"].most_common(6)) or "(geen)")
    print("CEMT=*     :", ", ".join(f"{k}={v}" for k, v in r["cemt_val"].most_common(8)) or "(geen)")


def optellen(alle):
    tot_lagen = {k: leeg() for k in ("A", "B", "C", "D")}
    tot_fout = leeg()
    for r in alle:
        for k in tot_lagen:
            for veld in ("km", "ways", "vertices"):
                tot_lagen[k][veld] += r["lagen"][k][veld]
        for veld in ("km", "ways", "vertices"):
            tot_fout[veld] += r["fout_getypeerd"][veld]
    return tot_lagen, tot_fout


def meet_pad(pad):
    """Worker voor de pool — moet module-level staan om picklebaar te zijn."""
    return os.path.basename(pad), meet(pad)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--serieel"]
    serieel = "--serieel" in sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)

    if args[0] == "--alles":
        hier = os.path.dirname(os.path.abspath(__file__))
        wortel = os.path.join(hier, "..", "build-cache", "geofabrik")
        paden = sorted(glob.glob(os.path.join(wortel, "*.osm.pbf")))
    else:
        paden = args

    paden = [p for p in paden if os.path.exists(p) or print(f"ontbreekt: {p}")]
    gb = sum(os.path.getsize(p) for p in paden) / 1e9

    # Elk extract is een eigen bestand zonder gedeelde staat, dus de scan is
    # embarrassingly parallel. Twee cores vrijlaten zodat de machine bruikbaar
    # blijft; boven ~14 workers wordt de schijf toch de rem en niet de CPU.
    workers = 1 if serieel else max(1, min(14, (os.cpu_count() or 2) - 2))
    print(f"{len(paden)} extracts, {gb:,.1f} GB, {workers} workers\n", flush=True)

    alle, t0 = [], time.time()
    if workers == 1:
        resultaten = (meet_pad(p) for p in paden)
    else:
        import multiprocessing as mp
        pool = mp.Pool(workers)
        # imap houdt de volgorde aan, zodat het rapport reproduceerbaar blijft
        resultaten = pool.imap(meet_pad, paden)

    for i, (naam, r) in enumerate(resultaten, 1):
        alle.append(r)
        rapport(naam, r)
        print(f"  [{i}/{len(paden)}] ({time.time() - t0:,.0f} s verstreken)",
              flush=True)

    if workers > 1:
        pool.close()
        pool.join()

    if len(alle) > 1:
        tot_lagen, tot_fout = optellen(alle)
        print(f"\n\n{'#' * 78}\nTOTAAL over {len(alle)} extracts ({gb:,.1f} GB)\n{'#' * 78}")
        toon_lagen(tot_lagen, tot_fout)
        budget(tot_lagen["C"]["km"])
        print(f"\nscantijd: {time.time() - t0:,.0f} s op {workers} workers")
