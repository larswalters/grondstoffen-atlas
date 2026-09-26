#!/usr/bin/env python3
"""voeg_sites_toe.py — de wereldwijde sites uit v2/design/<grondstof>-sitelaag.json
aan de gloedlaag v2/data/gloednodes-<grondstof>.json toevoegen (M29.1 / LAR-556;
sinds 2026-09-26 per grondstof parametriseerbaar voor de zes-grondstoffen-uitrol).

WAAROM. De gloedlaag had 36 sites, allemaal in China, met natte-vinger-gewichten
(LAR-490, visuele pilot). De ontwerpbrief noemt "koper volledig" = 15–30 echte
sites met capaciteit. Onder de lichte werkwijze (routebrief-licht.md) komt die
lijst uit één bronronde: v2/design/<grondstof>-sitelaag.md (leesbaar, met
bronnen) + <grondstof>-sitelaag.json (dezelfde lijst, machineleesbaar). Dit script
vertaalt die lijst naar gloedknopen. De redactie zit in de sitelaag-bestanden,
niet hier.

GEWICHT = CAPACITEIT in de eenheid van de grondstof (tabel EENHEID hieronder, of
--eenheid). Dat is de schaal die de brief bedoelt (besluit 2: capaciteit is het
gewicht in de optelling). De Chinese koper-registersites houden hun schatgewicht
(8–120) tenzij de sitelaag een echte capaciteit voor ze levert
("china_capaciteiten", OPTIONEEL, gematcht op een deelstring van de Chinese naam)
— dan wordt dat getal het gewicht en de bron de gewicht_bron.

ROL is een vrije, niet-lege string (mijn · smelter · raffinaderij ·
smelter+raffinaderij · converter/raffinaderij · HPAL · anodefabriek ·
magneetfabriek · exportterminal · centrale · cokerij · scheiding · …):
gloednodes.js leest het veld niet, het is redactionele context.

IDEMPOTENT: een site met hetzelfde id wordt vervangen, niet gedupliceerd; de
Chinese knopen en de complexknopen blijven staan. Ontbreekt het doelbestand, dan
wordt een nieuw leeg document (versie 2) aangemaakt.

Draaien (vanuit de repo-root):
    python v2/tools/voeg_sites_toe.py                             # koper, rapporteert alleen
    python v2/tools/voeg_sites_toe.py --schrijf                   # schrijft gloednodes-koper.json
    python v2/tools/voeg_sites_toe.py --grondstof lithium --schrijf
    python v2/tools/voeg_sites_toe.py --grondstof ree --eenheid "kt REO/j" --schrijf
"""
import argparse, json, sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
V2 = HIER.parent

# Capaciteitseenheid per grondstof (sleutel = id-prefix van de stromen). Staat
# letterlijk in gewicht_bron en in de waarschuwingstekst. Onbekende sleutel →
# "kt/j", of geef --eenheid mee.
EENHEID = {
    "koper": "kt Cu/j", "lithium": "kt LCE/j", "nikkel": "kt Ni/j",
    "kobalt": "kt Co/j", "grafiet": "kt/j", "ree": "kt REO/j", "kolen": "Mt/j",
}

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def nieuw_doc(gs, eenheid):
    return {
        "versie": 2,
        "toelichting": (f"Gloedlaag {gs} voor het LOD-systeem (LAR-490). LOSSE laag: raakt "
                        "stroomroute-*.json niet en wordt niet gebakken. Bevat uitsluitend "
                        "UITGEZOCHTE sites uit de sitelaag — nadrukkelijk geen generieke "
                        "havenlijst. Alleen knopen met level 'site' worden getekend."),
        "gewicht_waarschuwing": f"Alle sites dragen capaciteit in {eenheid} "
                                "(bron per site in gewicht_bron).",
        "knopen": [],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    ap.add_argument("--grondstof", default="koper",
                    help="sleutel = id-prefix van de stromen (koper, lithium, grafiet, "
                         "kobalt, nikkel, ree, kolen); bepaalt sitelaag- en doelbestand")
    ap.add_argument("--eenheid", default=None,
                    help='capaciteitseenheid voor de teksten, bv. "kt LCE/j" (default per grondstof)')
    a = ap.parse_args()
    gs = a.grondstof
    eenheid = a.eenheid or EENHEID.get(gs) or "kt/j"
    sitelaag_pad = V2 / "design" / f"{gs}-sitelaag.json"
    gloed = V2 / "data" / f"gloednodes-{gs}.json"
    # Context naar stderr, zodat de rapport-uitvoer (stdout) voor koper letterlijk
    # dezelfde blijft als vóór de parametrisering.
    print(f"grondstof {gs} · eenheid {eenheid} · {sitelaag_pad.name} → {gloed.name}", file=sys.stderr)
    if not sitelaag_pad.exists():
        sys.exit(f"sitelaag ontbreekt: {sitelaag_pad}")

    laag = json.loads(sitelaag_pad.read_text(encoding="utf-8"))
    sites = laag["sites"] if isinstance(laag, dict) else laag
    china = (laag.get("china_capaciteiten") or []) if isinstance(laag, dict) else []
    if gloed.exists():
        doc = json.loads(gloed.read_text(encoding="utf-8"))
    else:
        doc = nieuw_doc(gs, eenheid)
        print(f"doelbestand {gloed.name} bestaat nog niet → nieuw document (versie 2)")
    knopen = doc["knopen"]
    bestaand = {k["id"]: i for i, k in enumerate(knopen)}

    fouten, nieuw, vervangen = [], 0, 0
    for s in sites:
        for veld in ("id", "naam", "rol", "lat", "lon", "capaciteit_kt"):
            if s.get(veld) in (None, ""):
                fouten.append(f"{s.get('id','?')}: veld '{veld}' ontbreekt")
        if fouten and fouten[-1].startswith(str(s.get("id"))):
            continue
        rol = str(s["rol"]).strip()
        if not rol:
            fouten.append(f"{s['id']}: rol is leeg"); continue
        if not (-90 <= float(s["lat"]) <= 90 and -180 <= float(s["lon"]) <= 180):
            fouten.append(f"{s['id']}: coördinaat buiten bereik"); continue
        sid = s["id"] if s["id"].startswith("w-") else "w-" + s["id"]
        knoop = {
            "id": sid, "naam": s["naam"], "lon": round(float(s["lon"]), 5),
            "lat": round(float(s["lat"]), 5), "level": "site", "parent": None,
            "rol": rol, "grondstof": [gs], "land": s.get("land"),
            "gewicht": float(s["capaciteit_kt"]),
            "gewicht_bron": f"capaciteit {eenheid} — {s.get('capaciteit_bron','?')}",
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
        k["gewicht_bron"] = f"capaciteit {eenheid} — {c.get('bron','?')}"
        cn_gezet.append(f"{k['naam']} → {k['gewicht']:g}")

    basis = doc.get("toelichting", "").split(" || ")[0]
    if gs == "koper":
        # Letterlijk de M29.1-tekst: de koper-run moet byte-identiek blijven.
        doc["toelichting"] = (basis +
            " || Sinds 2026-09-24 (M29.1, LAR-556) aangevuld met de wereldwijde sitelaag uit "
            "v2/design/koper-sitelaag.json via v2/tools/voeg_sites_toe.py: ids 'w-*', gewicht = "
            "capaciteit in kt Cu/j (bron per site in gewicht_bron); coördinaten op site-niveau "
            "volgens de lichte werkwijze (routebrief-licht.md). De Chinese registersites houden "
            "hun schatgewicht tenzij een capaciteit bekend is.")
        doc["gewicht_waarschuwing"] = ("Chinese registersites zonder capaciteit dragen nog een "
            "ruw schatgewicht (8–120); de 'w-*'-sites en de Chinese sites mét bron dragen "
            "capaciteit in kt Cu/j. Vergelijk alleen sites met een bron in gewicht_bron.")
    else:
        doc["toelichting"] = (basis +
            f" || Gevuld uit v2/design/{gs}-sitelaag.json via v2/tools/voeg_sites_toe.py "
            f"--grondstof {gs}: ids 'w-*', gewicht = capaciteit in {eenheid} (bron per site in "
            "gewicht_bron); coördinaten op site-niveau volgens de lichte werkwijze "
            "(routebrief-licht.md).")
        doc["gewicht_waarschuwing"] = (f"Alle sites dragen capaciteit in {eenheid} (bron per site "
            "in gewicht_bron); vergelijk alleen sites met een bron in gewicht_bron.")

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
        gloed.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"geschreven: {gloed} · {gloed.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main()
