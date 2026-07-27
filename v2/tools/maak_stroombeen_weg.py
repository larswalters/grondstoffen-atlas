#!/usr/bin/env python3
"""
maak_stroombeen_weg.py — het TRUCKBEEN Balama-plant → Nacala-kade als échte
weggeometrie (N380/N1/N12) voor de stroomlaag.

WAT. Routebrief grafiet-balama-vidalia, been 1: de keten begint niet op zee
maar bij de mijn — "het begint niet echt bij de mijn — dat is wel belangrijk"
(Lars, 2026-07-28). Dit tool bakt dat been één keer als GeoJSON-LineString
([lon, lat]) zodat `hecht_marnet.py route --been-geojson` hem als
DOORGETROKKEN been in het stroomcontract opneemt (geen routering daar, geen
stippel — de geometrie komt letterlijk uit dit bestand).

HOE. Exact dezelfde machinerie als de M25-wegcorridors, geïmporteerd uit
fetch_landnet (niets gedupliceerd):
  * het wegfilter `weg_houden()`/WEG_HOUD via `land_scan(modus="weg")` —
    motorway t/m secondary, bewust ruim: de scope komt van het VENSTER,
    niet van de tag (highway=motorway is 0 km in half Afrika);
  * het corridorvenster om anker → via-punten → anker (⚠️ het venster ligt
    om de VIA-PUNTEN, niet om de grootcirkel — de corridor_punten()-les van
    Kolwezi→Durban); hier straal 40 km;
  * `corridor_keten()`: Dijkstra per been langs de via-punten uit de
    routebrief (in reisvolgorde), refs als záchte voorkeur (factor 3),
    anker-snap ≤ 25 km per punt.

⚠️ DIT IS TEKENGEOMETRIE VOOR DE STROOMLAAG, GEEN LANDNET. De lijn gaat naar
v2/build-cache/ais/graaf/ en wordt door hecht_marnet als been meegebakken;
hij komt NIET in landnet.bin en NIET in de CORRIDORS-lijst op schijf — de
runtime-vervanging hieronder raakt geen enkele bestaande bake of cache
(de cachevingerafdruk hasht de corridorlijst mee, dus deze run krijgt zijn
éigen weg-mozambique-cachebestand naast de M25-caches).

⚠️ LENGTETOETS = RAPPORTEREN, NIET GLADSTRIJKEN. De brief zegt ~485 km
(ESIA-som; gepubliceerd 490-515). Binnen ±10% is goed; erbuiten is een
bevinding die blijft staan — geen via-punt bijschuiven om het getal te halen.

⚠️ HET EERSTE VIA-PUNT IS DE PLANT, NIET HET DORP. Balama-dorp ligt ~9 km
WZW van de plant (briefpunt 2, "referentie — niet aan lijn"); de route start
op de site (-13.310, 38.660).

⚠️ ANKER-VERBINDINGSSTUKKEN AAN BEIDE UITEINDEN, EN WAAROM DAT EERLIJK IS.
De stroomlaag eist dat dit been op de plant begint en op de kade eindigt
(continuïteit met de marker resp. de haven-aanloop-stippel ≤ 0,2 km). Gemeten
in de bron (2026-07-28): dat kan met GEEN ENKEL wegfilter — de dichtstbijzijnde
OSM-weg van wélke klasse ook ligt 0,39 km van de plant (de toegangsweg is
`unclassified`) en 0,38 km van de kade (haventerrein = `service`); de
WEG_HOUD-klassen eindigen op 3,8 km (N14/N380 bij Balama) en 2,6 km (N12 bij
Nacala). Daarom krijgt de lijn twee expliciete rechte verbindingsstukken van
het laatste wegpunt naar het anker — apart gerapporteerd (`kmAanloopVan`/
`kmAanloopNaar`) en NIET meegeteld in de lengtetoets, die uitsluitend over de
weggeometrie gaat. Zelfde patroon als de slurryleiding waarvan de kartering
736 m vóór het terminalvlak ophoudt: het restje is een getekende verbinding,
geen gemeten weg.

Bijvangst uit de meting: de N380 draagt in OSM tussen Balama en Montepuez de
ref `N14` (hernummering); die zit daarom in de zachte ref-voorkeur.

Draaien:
  python v2/tools/maak_stroombeen_weg.py
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fetch_landnet as fl  # noqa: E402 — weg_houden/venster/corridor_keten
import fetch_waterways as fw  # noqa: E402 — km()

# Routebrief been 1, in reisvolgorde; coördinaten (lon, lat) zoals overal in
# fetch_landnet.CORRIDORS. Namen alleen voor de rapportage.
VIA_PUNTEN = [
    ("Balama-plant",        (38.660,  -13.310)),
    ("Montepuez",           (39.0017, -13.1253)),
    ("Metoro (N380×N1)",    (39.873,  -13.104)),
    ("Ocua / Lúrio-brug",   (39.793,  -13.6451)),
    ("Namialo (N1×N12)",    (39.9882, -14.9231)),
    ("Monapo",              (40.2972, -14.9155)),
    ("Nacala-kade",         (40.652,  -14.531)),
]

CORRIDOR = {
    "id": "gr-balama-nacala",
    "naam": "Balama-plant → Porto de Nacala (N380/N1/N12)",
    "van": VIA_PUNTEN[0][1],
    "naar": VIA_PUNTEN[-1][1],
    "via": [p for _, p in VIA_PUNTEN[1:-1]],
    "extracts": ["mozambique"],
    # Zachte voorkeur (factor 3), géén filter: de brief noemt N380 (ex-EN242),
    # N1 en EN8/N12; OSM-Mozambique wisselt tussen N- en EN-schrijfwijzen en
    # draagt op Balama–Montepuez de hernummerde ref N14 (gemeten in de scan).
    "refs": ["N380", "N14", "EN242", "N1", "EN1", "N12", "EN8", "N8"],
    "gepubliceerdKm": 485,          # ESIA-som; gepubliceerd 490-515
    "vensterKm": 40,
}

TOLERANTIE = 0.10                   # de brief-toets: ±10% om 485
UIT = os.path.join(fl.CACHE, "ais", "graaf", "stroombeen-balama-nacala.geojson")


def main():
    # ⚠️ RUNTIME-ONLY: CORRIDORS wordt vervangen door alléén dit been, zodat
    # het scanvenster (en dus de graaf) niet ook de Beira-/Zimbabwe-corridors
    # door Mozambique meeneemt. Omdat we precies één extract scannen draait
    # land_scan in-proces (geen mp-spawn) — dat is een vereiste, want een
    # spawn-worker herimporteert fetch_landnet en zou deze vervanging niet zien.
    fl.CORRIDORS[:] = [CORRIDOR]

    pad_extract = fl.extract_pad("mozambique")
    if not os.path.exists(pad_extract):
        raise SystemExit(f"extract ontbreekt: {pad_extract} — "
                         "haal hem met fetch_landnet.py --download")

    fl.land_scan(["mozambique"], "weg", workers=1)
    ways = fl.land_laad(["mozambique"], "weg")
    keten, rap = fl.corridor_keten(ways, CORRIDOR)
    if keten is None:
        raise SystemExit(f"⚠️ corridor niet gerouteerd: {rap.get('fout')}")

    # ── rapport per been: km + snap van beide via-punten naar de weg ──────
    print(f"\n  {CORRIDOR['naam']}")
    print(f"  {'been':<42} {'km':>8}  snap van → naar (km)")
    for i, been_km in enumerate(rap["benen"]):
        na, nb = VIA_PUNTEN[i][0], VIA_PUNTEN[i + 1][0]
        print(f"    {na + ' → ' + nb:<40} {been_km:>8,.1f}  "
              f"{rap['snapsKm'][i]:.2f} → {rap['snapsKm'][i + 1]:.2f}")

    # ── lengtetoets: rapporteren, niet gladstrijken — ALLEEN de weggeometrie
    afw = rap["km"] / CORRIDOR["gepubliceerdKm"] - 1.0
    vlag = "OK" if abs(afw) <= TOLERANTIE else "⚠️ BUITEN ±10% — bevinding"
    print(f"\n  lengtetoets (weggeometrie): {rap['km']:,.1f} km tegen "
          f"~{CORRIDOR['gepubliceerdKm']} (ESIA-som; gepubliceerd 490-515) "
          f"= {100 * afw:+.1f}%  [{vlag}]")

    # ── anker-verbindingsstukken (zie kop): plant → eerste wegpunt en laatste
    # wegpunt → kade, zodat het been exact op de briefankers begint en eindigt.
    pts = list(keten["pts"])
    plant, kade = CORRIDOR["van"], CORRIDOR["naar"]
    aanloop_van = fw.km(plant, pts[0])
    aanloop_naar = fw.km(pts[-1], kade)
    pts = ([(round(plant[0], 6), round(plant[1], 6))] + pts +
           [(round(kade[0], 6), round(kade[1], 6))])
    km_getekend = rap["km"] + aanloop_van + aanloop_naar
    print(f"  anker-verbindingen: plant → weg {aanloop_van:.2f} km · "
          f"weg → kade {aanloop_naar:.2f} km (rechte stukken, apart "
          f"gerapporteerd, buiten de lengtetoets)")
    print(f"  getekende lijn totaal: {km_getekend:,.1f} km · begint op de "
          f"plant en eindigt op de kade (continuïteit met de haven-aanloop "
          f"= 0,000 km)")

    # ── wegschrijven: [lon, lat], zelfde 6-decimalenkorrel als corridor_keten
    benen_props = []
    for i, been_km in enumerate(rap["benen"]):
        benen_props.append({
            "van": VIA_PUNTEN[i][0], "naar": VIA_PUNTEN[i + 1][0],
            "km": been_km,
            "snapVanKm": rap["snapsKm"][i],
            "snapNaarKm": rap["snapsKm"][i + 1],
        })
    doc = {
        "type": "FeatureCollection",
        "bron": "OpenStreetMap contributors (ODbL) via Geofabrik "
                "mozambique-latest; routebrief grafiet-balama-vidalia been 1",
        "laag": "stroombeen (tekengeometrie voor de stroomlaag — geen landnet)",
        "features": [{
            "type": "Feature",
            "properties": {
                "id": CORRIDOR["id"],
                "naam": CORRIDOR["naam"],
                "modaliteit": "truck",
                # km = de getekende lijn (incl. anker-verbindingen) — dit is
                # wat hecht_marnet uit de geometrie zal meten; kmWeg = de
                # lengtetoets-grootheid (alleen weggeometrie).
                "km": round(km_getekend, 3),
                "kmWeg": round(rap["km"], 3),
                "kmAanloopVan": round(aanloop_van, 3),
                "kmAanloopNaar": round(aanloop_naar, 3),
                "gepubliceerdKm": CORRIDOR["gepubliceerdKm"],
                "afwijkingPct": round(100 * afw, 1),
                "binnenTolerantie": bool(abs(afw) <= TOLERANTIE),
                "vensterKm": CORRIDOR["vensterKm"],
                "benen": benen_props,
            },
            "geometry": {"type": "LineString",
                         "coordinates": [[lo, la] for lo, la in pts]},
        }],
    }
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False)
    print(f"\n  geschreven: {UIT} · {os.path.getsize(UIT) / 1024:.1f} KB · "
          f"{len(pts):,} punten")


if __name__ == "__main__":
    main()
