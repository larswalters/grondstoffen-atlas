"""Centrale nameting van nieuwe stroomroute-*.json (golf 7): contract, naden, markers, stippel-aandeel.

Gebruik (vanuit de repo-root):  python centraal_check.py [--alle | id id ...]
Zonder argumenten: alle stroomroute-*.json die NIET in het register of in 'uitgesloten' staan.
"""
import io, json, math, sys, glob, os

REPO = "C:/automation/Projects/General/grondstoffen-atlas"
MODS = {"zee", "binnenvaart", "truck", "spoor", "leiding", "lucht"}


def gc(a, b):
    c = math.sin(math.radians(a[1])) * math.sin(math.radians(b[1])) + math.cos(math.radians(a[1])) * math.cos(math.radians(b[1])) * math.cos(math.radians(a[0] - b[0]))
    return 6371.0088 * math.acos(max(-1, min(1, c)))


def dist_tot_lijn(m, benen):
    # afstand tot het dichtstbijzijnde lijnpunt (punten zijn verdicht, dus voldoende)
    best = 1e9
    for b in benen:
        for p in b["punten"]:
            d = gc(m, p)
            if d < best:
                best = d
    return best


def check(pad):
    d = json.load(io.open(pad, encoding="utf-8"))
    sid = d.get("stroom") or os.path.basename(pad)[len("stroomroute-"):-5]
    B = d["benen"]
    fouten = []
    if d.get("versie") != 2:
        fouten.append(f"versie {d.get('versie')}")
    if d.get("punt_formaat") != "lonlat":
        fouten.append(f"punt_formaat {d.get('punt_formaat')}")
    rijen, naden = [], []
    totaal = stip = 0.0
    for i, b in enumerate(B):
        if b["modaliteit"] not in MODS:
            fouten.append(f"been {i+1} modaliteit {b['modaliteit']}")
        if len(b["punten"]) < 2:
            fouten.append(f"been {i+1} < 2 punten")
        v = b.get("vertakt_van")
        p0 = b["punten"][0]
        if i == 0:
            naad = 0.0
        elif v:
            naad = min(gc(p, p0) for p in B[v - 1]["punten"])
        else:
            naad = gc(B[i - 1]["punten"][-1], p0)
        naden.append(naad)
        km = b["km"]
        totaal += km
        if b.get("stippel"):
            stip += km
        rijen.append(f"   {i+1:2} {b['modaliteit']:<11}{km:>9.1f} km  naad {naad:6.2f}  {'stippel' if b.get('stippel') else '       '} {b['naam'][:78]}")
    ver = []
    for m in d.get("markers", []):
        pt = [m.get("lon"), m.get("lat")] if "lon" in m else m.get("punt") or m.get("coord")
        if not pt or pt[0] is None:
            continue
        dd = dist_tot_lijn(pt, B)
        if dd > 0.5:
            ver.append(f"{m.get('naam', '?')[:40]} {dd:.2f} km")
    kb = os.path.getsize(pad) / 1024
    return {
        "id": sid, "pad": pad, "benen": len(B), "km": round(totaal, 1), "stippel_pct": round(100 * stip / totaal, 1) if totaal else 0,
        "naad_max": round(max(naden), 2), "markers": len(d.get("markers", [])), "kb": round(kb), "fouten": fouten, "markers_ver": ver, "rijen": rijen,
        "titel": d.get("titel"),
    }


def main():
    reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))
    bekend = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg["uitgesloten"]}
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if args:
        paden = [f"{REPO}/v2/data/stroomroute-{a}.json" for a in args]
    elif "--alle" in sys.argv:
        paden = sorted(glob.glob(REPO + "/v2/data/stroomroute-*.json"))
    else:
        paden = [p for p in sorted(glob.glob(REPO + "/v2/data/stroomroute-*.json")) if os.path.basename(p) not in bekend]
    uit = []
    for p in paden:
        try:
            r = check(p)
        except Exception as e:  # noqa: BLE001
            print("FOUT", p, e)
            continue
        uit.append(r)
        vlag = []
        if r["naad_max"] > 5:
            vlag.append("NAAD>5")
        if r["stippel_pct"] > 60:
            vlag.append("STIPPEL>60%")
        if r["kb"] > 300:
            vlag.append("KB>300")
        if r["fouten"]:
            vlag.append("CONTRACT")
        if r["markers_ver"]:
            vlag.append("MARKER>0,5km")
        print(f"{r['id']}: {r['benen']} benen · {r['km']} km · stippel {r['stippel_pct']}% · naad max {r['naad_max']} km · {r['markers']} markers · {r['kb']} KB {' '.join('⚑' + v for v in vlag)}")
        if "-v" in sys.argv or vlag:
            for x in r["rijen"]:
                print(x)
            if r["fouten"]:
                print("   contract:", r["fouten"])
            if r["markers_ver"]:
                print("   markers ver van lijn:", r["markers_ver"])
    print(f"== {len(uit)} stromen gecontroleerd; vlaggen: {sum(1 for r in uit if r['naad_max']>5 or r['stippel_pct']>60 or r['kb']>300 or r['fouten'])}")


main()
