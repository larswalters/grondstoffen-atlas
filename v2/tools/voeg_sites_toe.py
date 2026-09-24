#!/usr/bin/env python3
"""voeg_sites_toe.py — de wereldwijde kopersites uit v2/design/koper-sitelaag.json
aan de gloedlaag v2/data/gloednodes-koper.json toevoegen (M29.1 / LAR-556).

WAAROM. De gloedlaag had 36 sites, allemaal in China, met natte-vinger-gewichten
(LAR-490, visuele pilot). De ontwerpbrief noemt "koper volledig" = 15–30 echte
sites met capaciteit. Onder de lichte werkwijze (routebrief-licht.md) komt die
lijst uit één bronronde: v2/design/koper-sitelaag.md (leesbaar, met bronnen) +
koper-sitelaag.json (dezelfde lijst, machineleesbaar). Dit script vertaalt die
lijst naar gloedknopen. De redactie zit in de sitelaag-bestanden, niet hier.

GEWICHT = CAPACITEIT IN kt Cu/j. Dat is de schaal die de brief bedoelt (besluit
2: capaciteit is het gewicht in de optelling). De Chinese registersites houden
hun schatgewicht (8–120) tenzij de sitelaag een echte capaciteit voor ze levert
("china_capaciteiten", gematcht op een deelstring van de Chinese naam) — dan
wordt dat getal het gewicht en de bron de gewicht_bron.

IDEMPOTENT: een site met hetzelfde id wordt vervangen, niet gedupliceerd; de
Chinese knopen en de complexknopen blijven staan.

Draaien (vanuit de repo-root):
    python v2/tools/voeg_sites_toe.py            # rapporteert alleen
    python v2/tools/voeg_sites_toe.py --schrijf  # schrijft gloednodes-koper.json
"""
import argparse, json, sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
V2 = HIER.parent
SITELAAG = V2 / "design" / "koper-sitelaag.json"
GLOED = V2 / "data" / "gloednodes-koper.json"
ROL = {"mijn": "mijn", "smelter": "smelter", "raffinaderij": "raffinaderij",
       "smelter+raffinaderij": "smelter+raffinaderij"}

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    a = ap.parse_args()

    laag = json.loads(SITELAAG.read_text(encoding="utf-8"))
    sites = laag["sites"] if isinstance(laag, dict) else laag
    china = (laag.get("china_capaciteiten") or []) if isinstance(laag, dict) else []
    doc = json.loads(GLOED.read_text(encoding="utf-8"))
    knopen = doc["knopen"]
    bestaand = {k["id"]: i for i, k in enumerate(knopen)}

    fouten, nieuw, vervangen = [], 0, 0
    for s in sites:
        for veld in ("id", "naam", "rol", "lat", "lon", "capaciteit_kt"):
            if s.get(veld) in (None, ""):
                fouten.append(f"{s.get('id','?')}: veld '{veld}' ontbreekt")
        if fouten and fouten[-1].startswith(str(s.get("id"))):
            continue
        if s["rol"] not in ROL:
            fouten.append(f"{s['id']}: onbekende rol '{s['rol']}'"); continue
        if not (-90 <= float(s["lat"]) <= 90 and -180 <= float(s["lon"]) <= 180):
            fouten.append(f"{s['id']}: coördinaat buiten bereik"); continue
        sid = s["id"] if s["id"].startswith("w-") else "w-" + s["id"]
        knoop = {
            "id": sid, "naam": s["naam"], "lon": round(float(s["lon"]), 5),
            "lat": round(float(s["lat"]), 5), "level": "site", "parent": None,
            "rol": ROL[s["rol"]], "grondstof": ["koper"], "land": s.get("land"),
            "gewicht": float(s["capaciteit_kt"]),
            "gewicht_bron": f"capaciteit kt Cu/j — {s.get('capaciteit_bron','?')}",
            "bron": s.get("coord_bron", "?"),
            "korrel": f"site-niveau, lichte werkwijze (M29.1); status {s.get('status','?')}",
            "notitie": s.get("notitie", ""),
        }
        if sid in bestaand:
            knopen[bestaand[sid]] = knoop; vervangen += 1
        else:
            knopen.append(knoop); bestaand[sid] = len(knopen) - 1; nieuw += 1

    cn_gezet = []
    for c in china:
        zoek = c.get("naam_zoekstring", "")
        treffers = [k for k in knopen if k.get("level") == "site"
                    and not k["id"].startswith("w-") and zoek and zoek in k["naam"]]
        if len(treffers) != 1:
            fouten.append(f"china '{zoek}': {len(treffers)} treffers (verwacht 1)"); continue
        k = treffers[0]
        k["gewicht"] = float(c["capaciteit_kt"])
        k["gewicht_bron"] = f"capaciteit kt Cu/j — {c.get('bron','?')}"
        cn_gezet.append(f"{k['naam']} → {k['gewicht']:g}")

    doc["toelichting"] = (doc["toelichting"].split(" || ")[0] +
        " || Sinds 2026-09-24 (M29.1, LAR-556) aangevuld met de wereldwijde sitelaag uit "
        "v2/design/koper-sitelaag.json via v2/tools/voeg_sites_toe.py: ids 'w-*', gewicht = "
        "capaciteit in kt Cu/j (bron per site in gewicht_bron); coördinaten op site-niveau "
        "volgens de lichte werkwijze (routebrief-licht.md). De Chinese registersites houden "
        "hun schatgewicht tenzij een capaciteit bekend is.")
    doc["gewicht_waarschuwing"] = ("Chinese registersites zonder capaciteit dragen nog een "
        "ruw schatgewicht (8–120); de 'w-*'-sites en de Chinese sites mét bron dragen "
        "capaciteit in kt Cu/j. Vergelijk alleen sites met een bron in gewicht_bron.")

    alle = [k for k in knopen if k.get("level") == "site"]
    print(f"sites in sitelaag: {len(sites)} · nieuw: {nieuw} · vervangen: {vervangen} · "
          f"china-capaciteiten gezet: {len(cn_gezet)} · sites totaal nu: {len(alle)}")
    for r in cn_gezet: print("  cn:", r)
    zw = sorted(alle, key=lambda k: -k["gewicht"])[:8]
    print("  zwaarste:", " · ".join(f"{k['naam'][:28]} {k['gewicht']:g}" for k in zw))
    for f in fouten: print("  ⚠️", f)
    if fouten and a.schrijf:
        sys.exit("niet geschreven: los eerst de fouten op")
    if a.schrijf:
        GLOED.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"geschreven: {GLOED} · {GLOED.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main()
