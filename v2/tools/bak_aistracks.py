# bak_aistracks.py — echte scheepstracks als kijk-laag voor de bol.
#
# Leest EEN OF MEER tracksets (jsonl.gz van bouw_tracks.py, één track per regel)
# en kiest wat de bol nodig heeft. Geen vensters — de pilot-vensters gaven
# precies de "afgekapte rivier" die Lars op de bol zag.
#
# De selectie is DEKKINGSGEDREVEN, niet volume-gedreven: een track gaat mee als
# hij genoeg nog-onbezette 0,01°-cellen (~1 km) dekt. Zo haalt élke zijrivier,
# elk kanaal en elke havenarm de bol (de eerste track daar is per definitie
# nieuw), terwijl de duizenden herhaal-doorvaarten op de hoofdvaarweg niet
# allemaal meegaan. Op- en afvaart tellen als gescheiden celruimtes, zodat beide
# vaarbanen van een geul gedekt blijven.
#
# ⚠️ MEERDERE BRONNEN — TWEE REGELS DIE HET GEDRAG DRAGEN
#
#  1. KORRELKLASSE-CELRUIMTE. De bronnen verschillen een factor ~80 in korrel
#     (gemeten punt-tot-punt: DK 0,25 · NO 0,27 · VS 0,27 · collector 0,45 ·
#     AMSA 20,4 km). Eén gedeelde celruimte laat een GROVE bron een gebied
#     bezetten dat een FIJNE bron veel beter had getekend — een AMSA-koorde van
#     20 km snijdt elke bocht af en kan per definitie geen kade halen. Daarom
#     heeft elke korrelklasse zijn eigen celruimte, ASYMMETRISCH gekoppeld: een
#     geaccepteerde track bezet cellen in zijn eigen klasse én in alle GROVERE
#     klassen. Gevolg: fijn wordt nooit weggedrukt door grof, grof wél door fijn
#     — precies besluit 2/4 uit het fase-1-rapport (AMSA levert het
#     offshore-bereik dat de collector mist, de fijne bronnen het kade-eind).
#     `--celruimte gedeeld` zet dit uit (de naïeve variant, ter vergelijking).
#
#  2. RONDGANG OVER DE BRONNEN. De drempel loopt op naarmate het puntenbudget
#     volloopt. Bronnen ná elkaar afwerken betekent dus: wie het laatst komt,
#     krijgt de strengste drempel — een tweede, verborgen rangorde bovenop de
#     korrelklasse. Daarom wordt er per ronde één track per bron aangeboden;
#     alle bronnen zien dezelfde oplopende drempel. `--volgorde serie` zet dit
#     uit (bron voor bron, fijn → grof).
#
# Daarnaast: een segment dat een TIJDGAT overspant is geen gevaren lijn maar een
# valse las (fase-1-rapport §7.2: tot 634 km rechte lijn in de VS-set). Zulke
# segmenten worden geknipt — de track valt uiteen in stukken, er verdwijnt geen
# gemeten geometrie.
#
#   python tools/bak_aistracks.py \
#       --tracks build-cache/ais/tracks/*.jsonl.gz \
#       --uit data/aistracks-pilot.json
#
# Uitvoer (aisnet-patroon, punten als [lon, lat]):
#   {"bron": ..., "bronnen": [{...per bron...}],
#    "lijnen": [{"bron": "vs", "richting": "op"|"af", "punten": [[lon,lat], ..]}]}

import argparse
import gzip
import json
import math
import time
from pathlib import Path

CEL = 0.01                # ~1 km — de dekkings-korrel van de FIJNE bronnen
CEL_GROF = 0.20           # ~22 km — idem voor de GROVE (AMSA stapt 21 km)
MIN_NIEUW = 6             # cellen die een track nieuw moet dekken om mee te gaan
MAX_PUNTEN = 1_200_000    # puntenbudget van het bol-bestand (na verdunning)
TOL_M = 40.0              # Douglas-Peucker
KORREL_MONSTER = 4000     # tracks per bron waarop de korrel wordt gemeten
KORREL_GRENS = 2.0        # km — mediane stap hierboven = GROVE bron
GAT_MIN = 90.0            # minuten — een segment dat hier overheen springt ...
GAT_KM = 25.0             # ... én langer is dan dit, is een valse las ...
GAT_FACTOR = 3.0          # ... mits het óók 3× de eigen korrel overschrijdt
DECIMALEN = 5             # coördinaat-afronding (5 ≈ 1 m, 4 ≈ 11 m)

# bestandsstam -> (sleutel, attributie). Onbekende stam = sleutel is de stam.
BRONNEN = {
    "vs-landelijk": ("vs", "MarineCadastre (NOAA/USACE, publiek domein)"),
    "dk-landelijk": ("dk", "DMA — Danish Maritime Authority (Denemarken)"),
    "no-corridors": ("no", "Kystdatahuset — Kystverket (NLOD)"),
    "au-landelijk": ("au", "AMSA — Australian Maritime Safety Authority "
                           "(CC BY-NC 3.0 AU)"),
    "wereld-collector": ("wereld", "eigen aisstream-collector"),
}

# leesbare vakken voor de dekkingsrapportage (lon0, lon1, lat0, lat1)
VAKKEN = [
    ("VS-binnenwater + kust", -128.0, -64.0, 22.0, 50.0),
    ("Alaska/NW-Pacific", -180.0, -128.0, 45.0, 72.0),
    ("Grote Meren/Seaway", -93.0, -64.0, 40.0, 52.0),
    ("Noordzee/NW-Europa", -6.0, 9.5, 48.0, 56.0),
    ("Oostzee/Denemarken", 9.5, 31.0, 53.0, 66.0),
    ("Noorwegen (fjorden)", 3.0, 20.0, 57.0, 72.0),
    ("Australië/Tasman", 108.0, 180.0, -48.0, -8.0),
    ("Indische Oceaan", 40.0, 108.0, -48.0, 26.0),
    ("Middellandse Zee/Zwarte Zee", -6.0, 42.0, 30.0, 48.0),
    ("Oost-Azië", 100.0, 150.0, 0.0, 46.0),
]


def haversine(la1, lo1, la2, lo2):
    p = math.pi / 180.0
    a = (0.5 - math.cos((la2 - la1) * p) / 2
         + math.cos(la1 * p) * math.cos(la2 * p) * (1 - math.cos((lo2 - lo1) * p)) / 2)
    return 12742.0 * math.asin(math.sqrt(max(0.0, a)))


def dp(punten, tol_m):
    """Douglas-Peucker op [lat, lon]-punten."""
    if len(punten) < 3:
        return punten
    cosl = math.cos(math.radians(punten[0][0]))
    m_per_graad = 111_320.0

    def afstand(p, a, b):
        ax, ay = a[1] * cosl, a[0]
        bx, by = b[1] * cosl, b[0]
        px, py = p[1] * cosl, p[0]
        dx, dy = bx - ax, by - ay
        l2 = dx * dx + dy * dy
        if l2 == 0:
            return math.hypot(px - ax, py - ay) * m_per_graad
        t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / l2))
        return math.hypot(px - (ax + t * dx), py - (ay + t * dy)) * m_per_graad

    houden = [0, len(punten) - 1]
    stapel = [(0, len(punten) - 1)]
    while stapel:
        i0, i1 = stapel.pop()
        if i1 - i0 < 2:
            continue
        verste, dmax = -1, tol_m
        for i in range(i0 + 1, i1):
            dist = afstand(punten[i], punten[i0], punten[i1])
            if dist > dmax:
                verste, dmax = i, dist
        if verste >= 0:
            houden.append(verste)
            stapel.append((i0, verste))
            stapel.append((verste, i1))
    return [punten[i] for i in sorted(set(houden))]


def knip_valse_lassen(punten, gat_min, gat_km):
    """Knip een track op segmenten die een tijdgat én een lange koorde overspannen.

    Punten zijn [lat, lon, t_min]. Geeft een lijst stukken terug (elk ≥ 2 punten)
    plus het aantal knippen en de weggeknipte koordelengte in km.
    """
    if gat_min <= 0 or len(punten) < 2:
        return [punten], 0, 0.0
    stukken, start, knippen, weg = [], 0, 0, 0.0
    for i in range(1, len(punten)):
        dt = punten[i][2] - punten[i - 1][2]
        if dt <= gat_min:
            continue
        d = haversine(punten[i - 1][0], punten[i - 1][1], punten[i][0], punten[i][1])
        if d <= gat_km:
            continue
        if i - start >= 2:
            stukken.append(punten[start:i])
        start, knippen, weg = i, knippen + 1, weg + d
    if len(punten) - start >= 2:
        stukken.append(punten[start:])
    return stukken, knippen, weg


def meet_korrel(pad, monster):
    """Mediane punt-tot-punt-afstand (km) én mediane tijdstap (min) van een bron.

    Gemeten over de eerste `monster` tracks. Beide medianen sturen de rest: de
    afstand bepaalt de korrelklasse (en dus de celmaat), de tijdstap bepaalt
    vanaf welk gat een segment een valse las is.
    """
    stappen, dts = [], []
    with gzip.open(pad, "rt", encoding="utf-8") as fh:
        for n, regel in enumerate(fh):
            if n >= monster:
                break
            p = json.loads(regel)["punten"]
            for i in range(1, len(p)):
                stappen.append(haversine(p[i - 1][0], p[i - 1][1], p[i][0], p[i][1]))
                dts.append(p[i][2] - p[i - 1][2])
    if not stappen:
        return 0.0, 0.0, 0
    stappen.sort()
    dts.sort()
    return stappen[len(stappen) // 2], dts[len(dts) // 2], len(stappen)


def vak_van(la, lo):
    for naam, lo0, lo1, la0, la1 in VAKKEN:
        if lo0 <= lo <= lo1 and la0 <= la <= la1:
            return naam
    return "overig"


def main():
    p = argparse.ArgumentParser(description="Track-selectie bakken voor de bol")
    p.add_argument("--tracks", type=Path, nargs="+", required=True,
                   help="een of meer jsonl.gz van bouw_tracks.py")
    p.add_argument("--uit", type=Path, required=True)
    p.add_argument("--max-punten", type=int, default=MAX_PUNTEN)
    p.add_argument("--min-nieuw", type=int, default=MIN_NIEUW)
    p.add_argument("--tol-m", type=float, default=TOL_M)
    p.add_argument("--decimalen", type=int, default=DECIMALEN)
    p.add_argument("--korrel-grens", type=float, default=KORREL_GRENS,
                   help="mediane stap (km) waarboven een bron GROF heet")
    p.add_argument("--korrel-monster", type=int, default=KORREL_MONSTER)
    p.add_argument("--gat-min", type=float, default=GAT_MIN,
                   help="vloer in minuten; 0 = geen valse-lassen-knip")
    p.add_argument("--gat-km", type=float, default=GAT_KM, help="vloer in km")
    p.add_argument("--gat-factor", type=float, default=GAT_FACTOR,
                   help="veelvoud van de eigen gemeten korrel dat óók gehaald "
                        "moet worden vóór er geknipt wordt")
    p.add_argument("--cel-grof", type=float, default=CEL_GROF,
                   help="celmaat (graden) voor de grove korrelklasse")
    p.add_argument("--celruimte", choices=["klasse", "gedeeld"], default="klasse",
                   help="klasse = eigen celruimte per korrelklasse (grof blokkeert "
                        "fijn niet); gedeeld = één ruimte voor alle bronnen")
    p.add_argument("--volgorde", choices=["rond", "serie", "bestand"], default="rond",
                   help="rond = rondgang over de bronnen; serie = bron voor bron "
                        "fijn→grof; bestand = bron voor bron in de opgegeven volgorde")
    p.add_argument("--stats-uit", type=Path, default=None)
    args = p.parse_args()

    t0 = time.time()

    # --- 1. korrel meten en de bronnen ordenen -----------------------------
    bronnen = []
    for pad in args.tracks:
        stam = pad.name.split(".")[0]
        sleutel, attributie = BRONNEN.get(stam, (stam, stam))
        korrel, dt, n = meet_korrel(pad, args.korrel_monster)
        bronnen.append({"sleutel": sleutel, "naam": attributie, "pad": pad,
                        "korrelKm": round(korrel, 3), "korrelMin": round(dt, 1),
                        "korrelN": n,
                        "aangeboden": 0, "gekozen": 0, "lijnen": 0, "punten": 0,
                        "km": 0.0, "knippen": 0, "knipKm": 0.0, "cellen": set(),
                        "vakken": {}})
    if args.volgorde != "bestand":
        bronnen.sort(key=lambda b: b["korrelKm"])
    for b in bronnen:
        b["klasse"] = 0 if b["korrelKm"] <= args.korrel_grens else 1
        b["klasseNaam"] = "fijn" if b["klasse"] == 0 else "grof"
        # ⚠️ De valse-lassen-drempels schalen mee met de bron. Een gat van
        # 90 min is voor een bron met 1 ping/min een gapend gat en voor AMSA
        # (1 ping/uur, knip-min 180) doodgewone bemonstering; hetzelfde geldt
        # voor de koorde. Vandaar: de vloer uit de vlaggen, maar minstens
        # `--gat-factor` × de eigen gemeten mediaan.
        b["gatMin"] = max(args.gat_min, args.gat_factor * b["korrelMin"])
        b["gatKm"] = max(args.gat_km, args.gat_factor * b["korrelKm"])
    n_klassen = 1 if args.celruimte == "gedeeld" else (max(b["klasse"] for b in bronnen) + 1)
    # celmaat per klasse: een bron met stappen van 20 km doet geen uitspraak
    # over een cel van 1 km, dus meet zijn nieuwheid op zijn eigen resolutie
    cel_klasse = [CEL if k == 0 else args.cel_grof for k in range(n_klassen)]

    print("bron          korrel(km)  korrel(min)  klasse  cel(°)  valse las >  bestand")
    for b in bronnen:
        k = 0 if args.celruimte == "gedeeld" else b["klasse"]
        print(f"  {b['sleutel']:<10} {b['korrelKm']:>8.3f} {b['korrelMin']:>11.1f}  "
              f"{b['klasseNaam']:<6} {cel_klasse[k]:>6.2f}  "
              f"{b['gatMin']:>5.0f} min/{b['gatKm']:>4.0f} km  {b['pad'].name}")
    print(f"  ({n_klassen} celruimte(s) · volgorde {args.volgorde} · "
          f"budget {args.max_punten:,} punten)")

    bezet = [{"op": set(), "af": set()} for _ in range(n_klassen)]
    lijnen = []
    n_punten = 0

    def bied_aan(b, t):
        """Toets één track tegen de dekking en neem hem over als hij nieuw is."""
        nonlocal n_punten
        b["aangeboden"] += 1
        r = ("op" if (t["dlat"] if abs(t["dlat"]) >= abs(t["dlon"])
                      else t["dlon"]) > 0 else "af")
        k = 0 if args.celruimte == "gedeeld" else b["klasse"]
        cellen = {(round(q[0] / cel_klasse[k]), round(q[1] / cel_klasse[k]))
                  for q in t["punten"]}
        nieuw = cellen - bezet[k][r]
        # naarmate het budget volloopt wordt de laag kieskeuriger: nieuwe
        # gebieden blijven binnenkomen, herhaling steeds minder
        vol = n_punten / args.max_punten
        drempel = args.min_nieuw + int(vol * vol * 60)
        if len(nieuw) < drempel:
            return
        bezet[k][r] |= cellen
        for j in range(k + 1, n_klassen):      # fijn bezet ook de grovere ruimtes
            bezet[j][r] |= {(round(q[0] / cel_klasse[j]), round(q[1] / cel_klasse[j]))
                            for q in t["punten"]}
        stukken, knippen, knipkm = knip_valse_lassen(t["punten"], b["gatMin"],
                                                     b["gatKm"])
        b["knippen"] += knippen
        b["knipKm"] += knipkm
        b["gekozen"] += 1
        for stuk in stukken:
            pts = dp([[q[0], q[1]] for q in stuk], args.tol_m)
            if len(pts) < 2:
                continue
            n_punten += len(pts)
            b["punten"] += len(pts)
            b["lijnen"] += 1
            for i in range(1, len(pts)):
                b["km"] += haversine(pts[i - 1][0], pts[i - 1][1],
                                     pts[i][0], pts[i][1])
            for la, lo in pts:
                b["cellen"].add((round(la), round(lo)))
                v = vak_van(la, lo)
                b["vakken"][v] = b["vakken"].get(v, 0) + 1
            lijnen.append({"bron": b["sleutel"], "richting": r,
                           "punten": [[round(lo, args.decimalen),
                                       round(la, args.decimalen)]
                                      for la, lo in pts]})

    # --- 2. de selectie ----------------------------------------------------
    if args.volgorde == "rond":
        fhs = [(b, gzip.open(b["pad"], "rt", encoding="utf-8")) for b in bronnen]
        try:
            while fhs:
                nog = []
                for b, fh in fhs:
                    regel = fh.readline()
                    if not regel:
                        fh.close()
                        continue
                    bied_aan(b, json.loads(regel))
                    nog.append((b, fh))
                fhs = nog
        finally:
            for b, fh in fhs:
                fh.close()
    else:
        for b in bronnen:
            with gzip.open(b["pad"], "rt", encoding="utf-8") as fh:
                for regel in fh:
                    bied_aan(b, json.loads(regel))

    # --- 3. schrijven ------------------------------------------------------
    doc = {"bron": "dekkingsgedreven selectie uit " +
                   " · ".join(b["naam"] for b in bronnen) +
                   " — via bak_aistracks.py",
           "bronnen": [{"sleutel": b["sleutel"], "naam": b["naam"],
                        "korrelKm": b["korrelKm"], "korrelMin": b["korrelMin"],
                        "klasse": b["klasseNaam"],
                        "aangeboden": b["aangeboden"], "gekozen": b["gekozen"],
                        "lijnen": b["lijnen"], "punten": b["punten"],
                        "km": round(b["km"]), "cellen1g": len(b["cellen"])}
                       for b in bronnen],
           "lijnen": lijnen}
    args.uit.write_text(json.dumps(doc, separators=(",", ":")), encoding="utf-8")
    mb = args.uit.stat().st_size / 1e6

    # --- 4. rapport --------------------------------------------------------
    op = sum(1 for l in lijnen if l["richting"] == "op")
    print(f"\n{'bron':<8} {'aangeboden':>11} {'gekozen':>9} {'%':>6} {'lijnen':>8} "
          f"{'punten':>10} {'km':>10} {'1°-cellen':>10} {'knip':>6}")
    for b in bronnen:
        pct = 100.0 * b["gekozen"] / b["aangeboden"] if b["aangeboden"] else 0.0
        print(f"{b['sleutel']:<8} {b['aangeboden']:>11,} {b['gekozen']:>9,} "
              f"{pct:>5.1f}% {b['lijnen']:>8,} {b['punten']:>10,} "
              f"{b['km']:>10,.0f} {len(b['cellen']):>10,} {b['knippen']:>6,}")
    print(f"{'TOTAAL':<8} {sum(b['aangeboden'] for b in bronnen):>11,} "
          f"{sum(b['gekozen'] for b in bronnen):>9,} {'':>6} {len(lijnen):>8,} "
          f"{n_punten:>10,} {sum(b['km'] for b in bronnen):>10,.0f}")
    print(f"\nop {op:,} · af {len(lijnen)-op:,} · {mb:.1f} MB "
          f"({args.uit.stat().st_size / max(1, n_punten):.1f} byte/punt) "
          f"-> {args.uit}  [{time.time()-t0:.0f} s]")
    for b in bronnen:
        top = sorted(b["vakken"].items(), key=lambda kv: -kv[1])[:4]
        print(f"  {b['sleutel']:<8} " + " · ".join(
            f"{naam} {100.0*n/max(1,b['punten']):.0f}%" for naam, n in top))
    knipkm = sum(b["knipKm"] for b in bronnen)
    if knipkm:
        print(f"  valse lassen geknipt: {sum(b['knippen'] for b in bronnen):,} "
              f"segmenten · {knipkm:,.0f} km niet getekend")

    if args.stats_uit:
        args.stats_uit.write_text(json.dumps(
            {"instelling": {"maxPunten": args.max_punten, "tolM": args.tol_m,
                            "celruimte": args.celruimte, "volgorde": args.volgorde,
                            "gatMin": args.gat_min, "gatKm": args.gat_km,
                            "decimalen": args.decimalen},
             "bytes": args.uit.stat().st_size, "punten": n_punten,
             "lijnen": len(lijnen),
             "bronnen": [{"sleutel": b["sleutel"], "korrelKm": b["korrelKm"],
                          "korrelMin": b["korrelMin"], "gatMin": b["gatMin"],
                          "gatKm": round(b["gatKm"], 1),
                          "klasse": b["klasseNaam"], "aangeboden": b["aangeboden"],
                          "gekozen": b["gekozen"], "lijnen": b["lijnen"],
                          "punten": b["punten"], "km": round(b["km"]),
                          "cellen1g": len(b["cellen"]), "knippen": b["knippen"],
                          "knipKm": round(b["knipKm"]), "vakken": b["vakken"]}
                         for b in bronnen]},
            indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
