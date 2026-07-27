# haal_ais_data.py — de verzamelde AIS-dagbestanden van de VPS naar deze PC.
#
# De collector (LAR-529) draait op de VPS, maar de verwerking naar tracks en
# graaf (LAR-530) draait hier. Dit script haalt de AFGESLOTEN dagen op — die
# zijn gegzipt en veranderen niet meer, dus overhalen is een keer kopieren en
# daarna klaar. De dag van vandaag wordt bewust overgeslagen: die groeit nog.
#
# Trekken in plaats van duwen, omdat deze PC niet altijd aan staat en geen
# inkomende toegang heeft. De SSH-sleutel die er al ligt doet het werk; er komen
# geen nieuwe credentials bij.
#
# Draaien:
#   python v2/tools/haal_ais_data.py              # alles wat hier nog niet is
#   python v2/tools/haal_ais_data.py --ook-vandaag
#   python v2/tools/haal_ais_data.py --opruimen   # na kopie van de VPS wissen
#
# De --opruimen-stand is er omdat de VPS maar ~22 GB vrij had: zodra een dag
# hier veilig staat (grootte gecontroleerd) mag hij daar weg.

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VPS = "root@187.124.169.172"
OP_VPS = "/var/lib/ais-collector/ais"
HIER = Path(__file__).resolve().parent
# ⚠️ Stond op .../ais/tracks — dat is de UITVOERmap van bouw_tracks.py
# (vs-landelijk.jsonl.gz, wereld-collector.jsonl.gz). Ruwe collector-dagen daarin
# zetten maakt `bouw_tracks.py --bron` zelfverwijzend (bron en uitvoer in dezelfde
# map) en liet de slottelling 669 MB aan tracks meetellen als "opgehaald".
# De drie dagen die er al stonden waren met de hand naar .../ais/vps gekopieerd;
# dát is de bron-map die bouw_tracks.py met --bron krijgt. Pad gelijkgetrokken.
LOKAAL = HIER.parent / "build-cache" / "ais" / "vps"


def ssh(*args: str) -> str:
    r = subprocess.run(["ssh", "-o", "BatchMode=yes", VPS, *args],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ssh mislukt: {r.stderr.strip()}")
    return r.stdout


def op_vps() -> dict:
    """{bestandsnaam: bytes} van alles wat er op de VPS staat."""
    uit = {}
    for regel in ssh(f"ls -l --time-style=+ {OP_VPS} 2>/dev/null").splitlines():
        stukken = regel.split()
        if len(stukken) >= 5 and stukken[-1].startswith("2"):
            uit[stukken[-1]] = int(stukken[4])
    return uit


def main() -> None:
    p = argparse.ArgumentParser(description="AIS-dagbestanden ophalen (M28)")
    p.add_argument("--ook-vandaag", action="store_true",
                   help="ook het nog groeiende bestand van vandaag meenemen")
    p.add_argument("--opruimen", action="store_true",
                   help="na een geslaagde kopie het bestand op de VPS wissen")
    args = p.parse_args()

    LOKAAL.mkdir(parents=True, exist_ok=True)
    vandaag = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    op_afstand = op_vps()
    if not op_afstand:
        sys.exit("Geen dagbestanden gevonden op de VPS")

    te_halen = []
    for naam, bytes_ in sorted(op_afstand.items()):
        if not args.ook_vandaag and naam.startswith(vandaag):
            print(f"  overslaan {naam} — vandaag, groeit nog")
            continue
        lokaal = LOKAAL / naam
        if lokaal.exists() and lokaal.stat().st_size == bytes_:
            print(f"  al hier    {naam} ({bytes_ / 1e6:.1f} MB)")
            continue
        te_halen.append((naam, bytes_))

    if not te_halen:
        print("niets te doen — alles staat al lokaal")
        return

    totaal = sum(b for _, b in te_halen)
    print(f"ophalen: {len(te_halen)} bestand(en), {totaal / 1e6:.0f} MB")
    for naam, bytes_ in te_halen:
        print(f"  {naam} ({bytes_ / 1e6:.1f} MB) ...", end="", flush=True)
        r = subprocess.run(["scp", "-q", f"{VPS}:{OP_VPS}/{naam}",
                            str(LOKAAL / naam)])
        if r.returncode != 0:
            print(" MISLUKT")
            continue
        gekopieerd = (LOKAAL / naam).stat().st_size
        if gekopieerd != bytes_:
            # Nooit opruimen op een half gelukte kopie — dat is precies hoe je
            # data kwijtraakt die je niet opnieuw kunt verzamelen.
            print(f" ONVOLLEDIG ({gekopieerd} van {bytes_} byte) — niet opgeruimd")
            continue
        print(" ok", end="")
        if args.opruimen and not naam.startswith(vandaag):
            ssh(f"rm -f {OP_VPS}/{naam}")
            print(" · van de VPS verwijderd", end="")
        print()

    hier = sum(f.stat().st_size for f in LOKAAL.glob("*.jsonl*"))
    print(f"\nlokaal nu: {len(list(LOKAAL.glob('*.jsonl*')))} bestand(en), "
          f"{hier / 1e6:.0f} MB in {LOKAAL}")


if __name__ == "__main__":
    main()
