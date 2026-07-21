#!/usr/bin/env python3
"""
fetch_wpi.py — haalt de NGA World Port Index (Pub 150) op naar de build-cache.

Bron: officiële REST-API van Maritime Safety Information,
  https://msi.nga.mil/api/publications/world-port-index?output=json
(geverifieerd 2026-07-21 via de Browser-pane: ~2.950 havens, ~110 velden per
haven, waaronder `unloCode`, `railway` (S/M/L), `harborSize`, `harborType`,
`harborUse` en de vracht-faciliteitsvelden `loWharves`/`loContainer`/
`loSolidBulk`/`loLiquidBulk`/`loOilTerm`/`loRoro`/`loBreakBulk`.)

Licentie: Pub 150 is een publicatie van de National Geospatial-Intelligence
Agency — een werk van de Amerikaanse federale overheid en daarmee publiek
domein (17 U.S.C. §105), zelfde categorie als USACE/NTAD. Attributie in de
HUD-credits: "World Port Index © NGA (public domain)".

⚠️ De API weigert kale curl (403 op de default user-agent) — een browserachtige
User-Agent volstaat; er is géén login of WAF-omzeiling nodig.

Draaien:  python v2/tools/fetch_wpi.py          (schrijft build-cache/wpi.json)
          python v2/tools/fetch_wpi.py --vers   (negeert de cache)
"""

import json
import os
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(os.path.dirname(HERE), "build-cache")
UIT = os.path.join(CACHE, "wpi.json")
URL = "https://msi.nga.mil/api/publications/world-port-index?output=json"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) grondstoffen-atlas/M24 "
      "(github.com/larswalters/grondstoffen-atlas)")
MIN_HAVENS = 2500      # sanity: minder dan dit = kapot antwoord, cache niet


def haal():
    req = urllib.request.Request(URL, headers={"User-Agent": UA,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    havens = data.get("ports", data)
    if not isinstance(havens, list) or len(havens) < MIN_HAVENS:
        raise SystemExit(f"onverwacht antwoord: {type(havens)} / "
                         f"{len(havens) if isinstance(havens, list) else '?'} havens "
                         f"(minimaal {MIN_HAVENS}) — niets weggeschreven")
    os.makedirs(CACHE, exist_ok=True)
    tijdelijk = UIT + ".deel"
    with open(tijdelijk, "w", encoding="utf-8") as f:
        json.dump({"bron": URL,
                   "licentie": "NGA Pub 150 — US-overheidswerk, publiek domein (17 U.S.C. §105)",
                   "havens": havens}, f, ensure_ascii=False)
    os.replace(tijdelijk, UIT)
    return havens


def main():
    if os.path.exists(UIT) and "--vers" not in sys.argv:
        havens = json.load(open(UIT, encoding="utf-8"))["havens"]
        print(f"wpi.json uit cache: {len(havens):,} havens (--vers voor opnieuw)")
    else:
        havens = haal()
        print(f"opgehaald: {len(havens):,} havens → {UIT} "
              f"({os.path.getsize(UIT) / 1048576:.1f} MB)")
    met_locode = sum(1 for h in havens if (h.get("unloCode") or "").strip())
    met_spoor = sum(1 for h in havens if (h.get("railway") or "").strip() not in ("", "U"))
    groot = sum(1 for h in havens if h.get("harborSize") in ("L", "M"))
    print(f"  LOCODE: {met_locode:,} · spoor (S/M/L): {met_spoor:,} · "
          f"harborSize L/M: {groot:,}")


if __name__ == "__main__":
    main()
