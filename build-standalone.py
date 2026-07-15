#!/usr/bin/env python3
"""build-standalone.py — genereert de single-file build uit de modulaire bron.

Principe: modulair = bron van waarheid; de single-file is een GEGENEREERDE build.
Dit script leest index.html als waarheid (dezelfde script-laadvolgorde), lijnt
style.css en elk LOKAAL script inline, en laat externe CDN-scripts (three.js) staan.

Uitvoer: atlas-standalone.html — handig om via drag-and-drop op Netlify te zetten
of op mobiel te bekijken. De modulaire bestanden blijven leidend; draai dit script
opnieuw na elke wijziging.

Gebruik:  python build-standalone.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"
OUT = ROOT / "atlas-standalone.html"


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def inline_css(html: str) -> str:
    def repl(m):
        href = m.group(1)
        path = ROOT / href
        if not path.exists():
            return m.group(0)  # extern of ontbrekend: laat staan
        return "<style>\n" + read(path) + "\n</style>"
    return re.sub(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"[^>]*/?>', repl, html)


def inline_scripts(html: str) -> str:
    def repl(m):
        src = m.group(1)
        if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
            return m.group(0)  # CDN (three.js): extern laten
        path = ROOT / src
        if not path.exists():
            print(f"  ! script niet gevonden, overgeslagen: {src}", file=sys.stderr)
            return m.group(0)
        code = read(path)
        # geen </script> in de payload verwachten, maar voor de zekerheid ontsnappen
        code = code.replace("</script>", "<\\/script>")
        return f"<script>\n{code}\n</script>"
    return re.sub(r'<script[^>]*\ssrc="([^"]+)"[^>]*>\s*</script>', repl, html)


def main():
    if not INDEX.exists():
        sys.exit("index.html niet gevonden")
    html = read(INDEX)
    html = inline_css(html)
    html = inline_scripts(html)

    OUT.write_text(html, encoding="utf-8")
    size_kb = OUT.stat().st_size / 1024

    # kleine sanity-checks
    remaining_local = re.findall(r'<script[^>]*\ssrc="(?!https?://|//)([^"]+)"', html)
    checks = {
        "goud geregistreerd": 'id: "goud"' in html,
        "bevat data/goud (Valcambi)": "Valcambi" in html,
        "koper geregistreerd": 'id: "copper"' in html,
        "bevat data/copper (Escondida)": "Escondida" in html,
        "zeldzame aardmetalen geregistreerd": 'id: "rare-earths"' in html,
        "bevat data/rare-earths (Ganzhou/Kachin)": "Ganzhou" in html and "Kachin" in html,
        "REE-grenscorridor (grens-ruili)": "grens-ruili" in html,
        "nikkel geregistreerd": 'id: "nickel"' in html,
        "nikkel uitgewerkt": 'id: "nickel"' in html and "IMIP Morowali" in html and "Weda Bay" in html,
        "nikkel class-1/2 + LME-nuance": "class-1" in html and "LME-nikkel" in html,
        "olie geregistreerd": 'id: "oil"' in html,
        "olie uitgewerkt": 'id: "oil"' in html and "Ghawar" in html and "Fujairah" in html,
        "olie Hormuz-bypass + Rusland-omleiding": "Habshan" in html and "Kozmino" in html,
        "olie-vaarpunten (Golf van Mexico)": "wp-golf-mexico" in html,
        "olie SPR-voorraden-laag (data)": 'type: "reserve"' in html and "US SPR" in html,
        "olie SPR-toggle bedraad (engine)": "showReserves" in html and "hasReserves" in html,
        "geen lokale <script src> meer": not remaining_local,
        "three.js CDN behouden": "three.min.js" in html,
    }
    print(f"[build] {OUT.name} geschreven — {size_kb:.0f} KB")
    for k, v in checks.items():
        print(f"  {'OK ' if v else 'FOUT'} {k}")
    if remaining_local:
        print(f"  ! nog lokale scripts niet ingelijnd: {remaining_local}", file=sys.stderr)
    if not all(checks.values()):
        sys.exit(2)


if __name__ == "__main__":
    main()
