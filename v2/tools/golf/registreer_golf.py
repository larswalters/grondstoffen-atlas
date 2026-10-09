"""Registreer de gebakken en gekeurde golf-7-ketens in v2/data/stromen-register.json.

    python registreer_golf7.py resultaat1.json [resultaat2.json ...] [--uitsluit id,id] [--achteraf-afgekeurd id,id] [--schrijf]

Een keten komt erin als: gebakken, keuring != niet-registreren, niet in --uitsluit. Sleutels worden op botsingen gecontroleerd
(tegen het register en onderling); bij een botsing een derde letter. Zonder --schrijf alleen een voorstel.
"""
import io, json, re, sys, os, string

REPO = "C:/automation/Projects/General/grondstoffen-atlas"
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

args = sys.argv[1:]
schrijf = "--schrijf" in args
uitsluit = set()
for i, a in enumerate(args):
    if a in ("--uitsluit", "--achteraf-afgekeurd") and i + 1 < len(args):
        uitsluit |= set(args[i + 1].split(","))
bestanden = [a for a in args if a.endswith(".json") and not a.startswith("-")]

NOTEN = json.load(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "noten.json"), encoding="utf-8"))
REG_PAD = REPO + "/v2/data/stromen-register.json"
reg = json.load(io.open(REG_PAD, encoding="utf-8"))
bezet = {s["sleutel"] for s in reg["stromen"]}
bekend_bestand = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg["uitgesloten"]}


def veld(tekst, naam):
    m = re.search(r'["\']?' + naam + r'["\']?\s*:\s*"((?:[^"\\]|\\.)*)"', tekst or "")
    return m.group(1).replace('\\"', '"') if m else None


kandidaten = []
for f in bestanden:
    res = json.load(io.open(f, encoding="utf-8"))
    for o in res["overzicht"]:
        kandidaten.append(o)

nieuw, overgeslagen = [], []
for o in kandidaten:
    i = o["id"]
    if not o.get("gebakken"):
        overgeslagen.append((i, "niet gebakken"))
        continue
    if o.get("keuring") == "niet-registreren":
        overgeslagen.append((i, "keuring: niet-registreren"))
        continue
    if i in uitsluit:
        overgeslagen.append((i, "uitgesloten"))
        continue
    bestand = f"stroomroute-{i}.json"
    if bestand in bekend_bestand:
        overgeslagen.append((i, "staat al in het register"))
        continue
    if not os.path.exists(f"{REPO}/v2/data/{bestand}"):
        overgeslagen.append((i, "bestand ontbreekt"))
        continue
    rr = o.get("registerregel") or ""
    gs = i.split("-")[0]
    sleutel = veld(rr, "sleutel")
    label = veld(rr, "label")
    noot = veld(rr, "noot") or f"M31 · golf 7 (2026-10-09)"
    delen = i.split("-")
    if not sleutel:
        sleutel = f"{gs}-{delen[1][0]}{delen[2][0]}"
    if not label:
        label = (o.get("titel") or i).split("·", 1)[-1].strip()[:60]
    # botsingen
    basis = sleutel
    extra = iter(delen[2] + delen[1] + string.ascii_lowercase)
    while sleutel in bezet:
        sleutel = basis + next(extra)
    bezet.add(sleutel)
    if i in NOTEN:
        noot = noot.rstrip(" .") + ". " + NOTEN[i]
    nieuw.append({"sleutel": sleutel, "bestand": bestand, "grondstof": gs, "label": label, "aan": True, "noot": noot})
    if sleutel != basis:
        print(f"  sleutel {basis} bezet -> {sleutel} ({i})")

print(f"{len(nieuw)} te registreren, {len(overgeslagen)} overgeslagen")
for n in nieuw:
    print(f"  + {n['sleutel']:10} {n['grondstof']:9} {n['label'][:44]:44} {n['bestand']}")
for i, r in overgeslagen:
    print(f"  - {i}: {r}")
if schrijf:
    reg["stromen"].extend(nieuw)
    tekst = json.dumps(reg, ensure_ascii=False, indent=1)
    io.open(REG_PAD, "w", encoding="utf-8", newline="\r\n").write(tekst)  # zoals het bestaande register: CRLF, geen slot-newline
    print("register geschreven:", len(reg["stromen"]), "stromen")
