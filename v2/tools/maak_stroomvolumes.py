"""maak_stroomvolumes.py — het jaarvolume per stroom als LOS metadatabestand (LAR-642, 2026-10-29).

Waarom los: het register en de gebakken stroomroute-*.json blijven onaangeraakt (besluit 2026-08-06: extra velden voor de
visuals gaan in een los metadatabestand, geen herbak). De bundelbaker (bak_stroombundel.py) leest dit bestand mee en zet per
stroom een compact `volume`-blok in stromen.json; de bol maakt er lijndikte, het aantal kometen en een HUD-regel van.

BRON VAN DE CIJFERS: per grondstof een bronlijst `v2/design/volumes/<grondstof>.json`, geschreven door een leesagent die
alle routebrieven van die grondstof las (2026-10-29, Sonnet): per stroom het jaarvolume van de lading over DEZE route —
tekst (citaat uit de brief), waarde, eenheid, per (jaar/dag), productvorm, peiljaar, bron, status, toelichting.
  status bron      = de brief geeft het stroomvolume met bron
  status indicatie = benadering (mijn-/fabriekstotaal, capaciteit, natte vinger, v1-checklist) — de toelichting zegt wat het is
  status onbekend  = niets bruikbaars; de bol tekent de dunste lijn, de HUD zegt "volume onbekend"
Een regex over de brieven is bewust GEEN bron: hij pakte fabriekscapaciteiten (Kibali "7,2 Mt/j" = de ertsfabriek).
Handmatige correcties: `v2/data/stroomvolumes-handmatig.json` (zelfde velden, per stroom-id) winnen van de bronlijst.
Een stroom die in geen bronlijst staat (nieuwe golf) is "onbekend" tot een leesagent hem toevoegt — het verslag noemt ze.

NORMALISATIE (alleen voor de relatieve dikte, nooit voor de tekst): per grondstof één basis-eenheid (BASIS); de eenheid
uit de brief wordt omgerekend waar dat eenduidig kan (Mt → kt, koz/Moz → t, kb/d → Mt/j bij 7,3 vaten/t, Mtpa LNG → bcm
bij 1,36, Mlb U3O8 → tU bij 384,6). Product ≠ metaal (erts, concentraat, matte, MHP) wordt NIET omgerekend — dat is de
"±" van Lars' wens: de dikte is relatief en indicatief, de tekst is de waarheid. `rel` = positie op een log-schaal tussen
het 15e en 90e percentiel van de grondstof (robuust tegen uitschieters), 0..1.

Gebruik: python v2/tools/maak_stroomvolumes.py [--schrijf]   (zonder --schrijf alleen het verslag)
Uitvoer: v2/data/stroomvolumes.json
"""
import glob, io, json, math, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(REPO, "v2", "data")
BRONMAP = os.path.join(REPO, "v2", "design", "volumes")
UIT = os.path.join(DATA, "stroomvolumes.json")
HANDMATIG = os.path.join(DATA, "stroomvolumes-handmatig.json")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASIS = {
    "koper": "kt", "nikkel": "kt", "kobalt": "kt", "lithium": "kt", "grafiet": "kt", "zilver": "t", "goud": "t",
    "pgm": "t", "ree": "kt", "uranium": "t", "kolen": "Mt", "olie": "Mt", "gas": "bcm", "diamant": "Mct",
}
# eerste token van de eenheid (kleine letters) → lijst van (factor, basis-eenheid)
OMREKEN = {
    "kt": [(1.0, "kt"), (1000.0, "t"), (0.001, "Mt")], "kton": [(1.0, "kt"), (1000.0, "t")],
    "mt": [(1000.0, "kt"), (1.0, "Mt"), (1e6, "t")], "mwmt": [(1000.0, "kt"), (1.0, "Mt")], "mmt": [(1000.0, "kt"), (1.0, "Mt")],
    "t": [(0.001, "kt"), (1.0, "t"), (1e-6, "Mt")], "ton": [(0.001, "kt"), (1.0, "t")], "tu": [(1.0, "t")], "thm": [(1.0, "t")],
    "kg": [(0.001, "t")],
    "koz": [(0.0311035, "t")], "moz": [(31.1035, "t")], "oz": [(0.0000311035, "t")],
    "mlb": [(384.6, "t")],                         # Mlb U3O8 → tU
    "kb/d": [(365.0 / 7.3 / 1000.0, "Mt")], "mb/d": [(365.0 / 7.3, "Mt")], "kbpd": [(365.0 / 7.3 / 1000.0, "Mt")],
    "mln": None,                                    # 'mln vaten' / 'mln ton' / 'mln t': zie hieronder
    "bcm": [(1.0, "bcm")], "mcm": [(0.001, "bcm")], "bcm/j": [(1.0, "bcm")],
    "mtpa": [(1.36, "bcm"), (1.0, "Mt")], "twh": [(0.0959, "bcm")],
    "mct": [(1.0, "Mct")], "kct": [(0.001, "Mct")], "ct": [(1e-6, "Mct")],
    "pj": [(1.0 / 38.0, "bcm")],                   # ~38 PJ per bcm aardgas
    "kdmt": [(1.0, "kt"), (1000.0, "t")],          # kilo dry metric tonnes
}


def basis_waarde(gs, waarde, eenheid, per):
    """(basis, basisEenheid) of (None, basisEenheid) als de eenheid niet eenduidig omgerekend kan worden."""
    doel = BASIS.get(gs)
    if waarde is None or not eenheid:
        return None, doel
    e = eenheid.strip().lower().replace(" ", " ")
    tok = e.split()
    key = tok[0] if tok else ""
    w = float(waarde)
    if per == "dag" and key not in ("kb/d", "mb/d", "kbpd"):
        w *= 365.0
    if key == "mln" and len(tok) > 1:
        if tok[1].startswith("vat") or tok[1].startswith("bbl") or tok[1].startswith("barrel"):
            key, w = "mt", w / 7.3
        elif tok[1] in ("t", "ton", "tonnes", "tons"):
            key = "mt"
        elif tok[1].startswith("m3") or tok[1].startswith("m³"):
            key = "mcm"                             # mln m3 (per dag al ×365 hierboven)
    if key in ("mt",) and len(tok) > 1 and "lng" in e and doel == "bcm":
        key = "mtpa"
    if key == "mtpa" and doel in ("Mt", "kt"):
        key = "mt"
    for f, b in OMREKEN.get(key) or []:
        if b == doel:
            return round(w * f, 4), doel
    return None, doel


def kort_tekst(waarde, eenheid, per):
    if waarde is None or not eenheid:
        return None
    w = float(waarde)
    if w >= 100:
        s = f"{w:,.0f}".replace(",", ".")
    elif w >= 10:
        s = f"{w:.1f}".rstrip("0").rstrip(".").replace(".", ",")
    else:
        s = f"{w:.2f}".rstrip("0").rstrip(".").replace(".", ",")
    e = eenheid.strip()
    suffix = "/d" if per == "dag" else "/j"
    if re.search(r"/(d|j|jaar)$", e):
        suffix = ""
    return f"≈ {s} {e}{suffix}"


def main():
    schrijf = "--schrijf" in sys.argv
    reg = json.load(io.open(os.path.join(DATA, "stromen-register.json"), encoding="utf-8"))
    handmatig = json.load(io.open(HANDMATIG, encoding="utf-8")) if os.path.exists(HANDMATIG) else {}
    bron = {}
    for p in sorted(glob.glob(os.path.join(BRONMAP, "*.json"))):
        for r in json.load(io.open(p, encoding="utf-8")):
            if r.get("id"):
                bron[r["id"]] = r
    uit, tel, ontbreekt = {}, {"bron": 0, "indicatie": 0, "onbekend": 0, "handmatig": 0, "zonder_basis": 0}, []
    for s in reg["stromen"]:
        doc = json.load(io.open(os.path.join(DATA, s["bestand"]), encoding="utf-8"))
        sid = doc.get("stroom")
        gs = s["grondstof"]
        rec = {"sleutel": s["sleutel"], "grondstof": gs, "tekst": None, "kort": None, "waarde": None, "eenheid": None, "per": "jaar",
               "productvorm": None, "peiljaar": None, "bron": None, "status": "onbekend", "toelichting": None,
               "basis": None, "basisEenheid": BASIS.get(gs), "rel": None}
        r = bron.get(sid)
        if sid in handmatig:
            r = dict(r or {}, **handmatig[sid]); tel["handmatig"] += 1
        if r is None:
            ontbreekt.append(sid)
        else:
            for k in ("tekst", "waarde", "eenheid", "per", "productvorm", "peiljaar", "bron", "status", "toelichting"):
                if r.get(k) is not None:
                    rec[k] = r[k]
            if rec["status"] not in ("bron", "indicatie", "onbekend"):
                rec["status"] = "indicatie"
            if rec["status"] != "onbekend" and (rec["waarde"] is None or not rec["eenheid"]):
                # een status zonder getal is geen dikte, wel een tekst
                rec["status"] = "onbekend" if not rec["tekst"] else rec["status"]
            if rec["status"] != "onbekend":
                rec["basis"], _ = basis_waarde(gs, rec["waarde"], rec["eenheid"], rec["per"])
                rec["kort"] = kort_tekst(rec["waarde"], rec["eenheid"], rec["per"])
        uit[sid] = rec
        tel[rec["status"]] += 1
        if rec["status"] != "onbekend" and rec["basis"] is None:
            tel["zonder_basis"] += 1

    # rel per grondstof op log-schaal tussen p15 en p90 (robuust)
    per_gs = {}
    for r in uit.values():
        if r["basis"] and r["basis"] > 0:
            per_gs.setdefault(r["grondstof"], []).append(math.log10(r["basis"]))
    grenzen = {}
    for gs, xs in per_gs.items():
        xs = sorted(xs)
        if len(xs) >= 4:
            lo = xs[int(0.15 * (len(xs) - 1))]
            hi = xs[int(round(0.90 * (len(xs) - 1)))]
        else:
            lo, hi = xs[0], xs[-1]
        if hi - lo < 0.3:   # alles vrijwel gelijk: geen zinvolle spreiding
            lo, hi = xs[0] - 0.15, xs[-1] + 0.15
        grenzen[gs] = (lo, hi)
    for r in uit.values():
        if r["basis"] and r["basis"] > 0 and r["grondstof"] in grenzen:
            lo, hi = grenzen[r["grondstof"]]
            r["rel"] = round(max(0.0, min(1.0, (math.log10(r["basis"]) - lo) / (hi - lo))), 3)

    print(f"{len(uit)} stromen: {tel}; niet in een bronlijst: {len(ontbreekt)}")
    for gs in sorted(BASIS):
        rs = [r for r in uit.values() if r["grondstof"] == gs]
        n_ok = sum(1 for r in rs if r["rel"] is not None)
        lo, hi = grenzen.get(gs, (None, None))
        schaal = f"{10 ** lo:.4g} – {10 ** hi:.4g} {BASIS[gs]}" if lo is not None else "-"
        print(f"  {gs:8} {n_ok:2}/{len(rs):2} met dikte · schaal {schaal}")
    print("\nZONDER DIKTE (onbekend, of eenheid niet om te rekenen):")
    for sid, r in sorted(uit.items()):
        if r["rel"] is None:
            print(f"  {sid:42} {r['status']:9} {r['eenheid'] or '':14} {(r['tekst'] or '')[:70]}")
    if ontbreekt:
        print("\nNIET IN EEN BRONLIJST (leesagent nodig):", ", ".join(ontbreekt))
    if schrijf:
        io.open(UIT, "w", encoding="utf-8", newline="\n").write(json.dumps(
            {"toelichting": "GEGENEREERD door v2/tools/maak_stroomvolumes.py uit v2/design/volumes/*.json (leesagenten over de "
                            "routebrieven) + stroomvolumes-handmatig.json; jaarvolume per stroom als tekst + getal + basis per "
                            "grondstof; rel = log-positie tussen p15 en p90 van de grondstof (0..1). Niet met de hand bewerken.",
             "basisEenheid": BASIS, "stromen": uit}, ensure_ascii=False, indent=1))
        print("geschreven:", UIT)


if __name__ == "__main__":
    main()
