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
runtime-vervanging hieronder raakt geen enkele bestaande bake of cache.
⚠️ CACHEVINGERAFDRUK: fetch_landnet hasht WEG_HOUD en de corridorlijst
(id + punten + vensterKm) mee, maar NIET een runtime-gepatchte weg_houden.
Daarom draagt het corridor-id dat de scan ziet een eigen
eindklassen-marker (zie main): de M25-caches blijven onaangeraakt én een
oudere cache van dit tool (ander filter of andere kade) kan nooit
stilzwijgend hergebruikt worden.

⚠️ LENGTETOETS = RAPPORTEREN, NIET GLADSTRIJKEN. De brief zegt ~485 km
(ESIA-som; gepubliceerd 490-515). Binnen ±10% is goed; erbuiten is een
bevinding die blijft staan — geen via-punt bijschuiven om het getal te halen.

⚠️ HET EERSTE VIA-PUNT IS DE PLANT, NIET HET DORP. Balama-dorp ligt ~9 km
WZW van de plant (briefpunt 2, "referentie — niet aan lijn"); de route start
op de site (-13.310, 38.660).

⚠️ HET LAATSTE VIA-PUNT IS DE CONTAINERTERMINAL OP DE OOSTOEVER (correctie
Lars, satelliet-check ?v=093). Het onderzoekspunt (-14.531, 40.652) bleek op
open water bij de kolen-jetty op de WESTOEVER te liggen — nota bene het
terminal dat in de routebrief als "hoort NIET bij deze stroom" staat. Het
nieuwe anker (-14.5383, 40.6673) is satelliet-gelegd op de containerkade
(Esri z16, 0,01-graden-grid — de Tongling-werkwijze).

⚠️ KLEINE WEGKLASSEN DOEN MEE, MAAR ALLEEN BIJ DE UITEINDEN. Gemeten in de
bron (2026-07-28): met alléén WEG_HOUD (motorway t/m secondary) eindigt de
weg 3,8 km van de plant (N14/N380 bij Balama) en blijft het laatste stuk een
rechte lijn dwars over het mijnterrein — "dat laatste stukje gaat niet over
de weg" (Lars). De echte toegangsweg bestaat wél in OSM maar draagt een
kleinere klasse: `unclassified` op 0,39 km van de plant, en bij Nacala liggen
de havenstraten als `service`/`residential`. Daarom accepteert deze run óók
EIND_KLASSEN (tertiary/unclassified/residential/service) — maar uitsluitend
binnen EIND_STRAAL_KM van de plant resp. de kade, NIET corridor-breed: anders
trekt elk dorpsspoor het venster in en kan een bush-track (zachte
ref-voorkeur is maar factor 3) de N1 aftroeven. De hoofdroute blijft zo op de
N-wegen; alleen de first/last mile pakt de echte toegangsweg. De resterende
anker-verbindingsstukjes (anker → dichtstbijzijnde wegvertex) horen daarmee
≤ ~0,5 km per kant te zijn; ze blijven apart gerapporteerd (`kmAanloopVan`/
`kmAanloopNaar`) en tellen NIET mee in de lengtetoets, die uitsluitend over
de weggeometrie gaat. Zelfde patroon als de slurryleiding waarvan de
kartering 736 m vóór het terminalvlak ophoudt: het restje is een getekende
verbinding, geen gemeten weg.

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
    # ⚠️ Satelliet-gelegd op de containerterminal-OOSToever (Esri z16,
    # 0,01°-grid) — correctie Lars: het onderzoekspunt (40.652, -14.531) bleek
    # in het water bij de kolen-jetty op de westoever te liggen (het terminal
    # dat per routebrief NIET bij deze stroom hoort). Hier komen de trucks aan.
    ("Nacala-kade",         (40.6673, -14.5383)),
]

# ⚠️ Kleine wegklassen: ALLEEN binnen EIND_STRAAL_KM van plant/kade (zie kop).
# weg_houden() krijgt alleen tags, dus de straal-beperking gebeurt geometrisch
# ná land_laad; de tag-verruiming zelf is een runtime-patch op fetch_landnet.
EIND_KLASSEN = ("residential", "service", "tertiary", "unclassified")
EIND_STRAAL_KM = 12.0

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
    # ⚠️ RUNTIME-ONLY (1/3): CORRIDORS wordt vervangen door alléén dit been,
    # zodat het scanvenster (en dus de graaf) niet ook de Beira-/Zimbabwe-
    # corridors door Mozambique meeneemt. Omdat we precies één extract scannen
    # draait land_scan in-proces (geen mp-spawn) — dat is een vereiste, want
    # een spawn-worker herimporteert fetch_landnet en zou geen van deze
    # patches zien. Het corridor-id dat de SCAN ziet draagt de eindklassen-
    # configuratie: _venster_sleutel hasht (id, punten, vensterKm), dus zo
    # krijgt deze filtervariant een eigen cachevingerafdruk — de M25-caches
    # blijven staan en de oude v093-cache (WEG_HOUD-only, oude kade) kan niet
    # stilletjes hergebruikt worden. corridor_keten krijgt gewoon CORRIDOR
    # (zelfde punten/venster), alleen de cache-sleutel verschilt.
    scan_corridor = dict(CORRIDOR)
    scan_corridor["id"] = (CORRIDOR["id"] + "+eind-" + ",".join(EIND_KLASSEN)
                           + f"@{EIND_STRAAL_KM:g}km")
    fl.CORRIDORS[:] = [scan_corridor]

    # ⚠️ RUNTIME-ONLY (2/3): weg_houden accepteert óók de kleine eindklassen
    # (zelfde access-uitsluiting). De 12-km-straal kan hier niet — weg_houden
    # krijgt alleen tags, geen geometrie — en volgt ná land_laad (zie onder).
    _weg_houden_orig = fl.weg_houden

    def _weg_houden_eind(tags):
        houd, reden = _weg_houden_orig(tags)
        if houd:
            return True, ""
        soort = (tags.get("highway") or "").strip()
        if (soort in EIND_KLASSEN
                and (tags.get("access") or "").strip() not in fl.WEG_ACCESS_WEG):
            return True, ""
        return houd, reden

    fl.weg_houden = _weg_houden_eind

    # ⚠️ RUNTIME-ONLY (3/3): snelle bbox-afwijzing vóór de segmentlus van
    # _raakt_venster. Met de kleine klassen erbij zou anders élke
    # residential-way van Maputo door zes segment-afstandsberekeningen per
    # vertex gaan. Gedrag identiek — de bbox is een ruime superset van het
    # corridorvenster (marge ruim boven vensterKm) — alleen sneller.
    lons = [p[0] for _, p in VIA_PUNTEN]
    lats = [p[1] for _, p in VIA_PUNTEN]
    marge = CORRIDOR["vensterKm"] / 100.0 + 0.25   # ° — ruim > 40 km op lat -14
    bb = (min(lons) - marge, max(lons) + marge,
          min(lats) - marge, max(lats) + marge)
    _raakt_orig = fl._raakt_venster

    def _raakt_venster_bbox(pts, vensters):
        for lo, la in pts:
            if bb[0] <= lo <= bb[1] and bb[2] <= la <= bb[3]:
                return _raakt_orig(pts, vensters)
        return False

    fl._raakt_venster = _raakt_venster_bbox

    pad_extract = fl.extract_pad("mozambique")
    if not os.path.exists(pad_extract):
        raise SystemExit(f"extract ontbreekt: {pad_extract} — "
                         "haal hem met fetch_landnet.py --download")

    fl.land_scan(["mozambique"], "weg", workers=1)
    ways = fl.land_laad(["mozambique"], "weg")

    # ── de 12-km-beperking: kleine klassen ALLEEN bij plant en kade ────────
    # Corridor-breed zou elk dorpsspoor het venster in trekken; hier vallen
    # alle kleine-klasse-ways af die geen enkele vertex binnen EIND_STRAAL_KM
    # van een van de twee ankers hebben. De hoofdroute blijft op WEG_HOUD.
    plant, kade = CORRIDOR["van"], CORRIDOR["naar"]

    def _bij_eind(w):
        return any(fw.km((lo, la), plant) <= EIND_STRAAL_KM
                   or fw.km((lo, la), kade) <= EIND_STRAAL_KM
                   for lo, la in w["pts"])

    n_klein_tot = sum(1 for w in ways if w["soort"] in EIND_KLASSEN)
    ways = [w for w in ways if w["soort"] not in EIND_KLASSEN or _bij_eind(w)]
    n_klein_mee = sum(1 for w in ways if w["soort"] in EIND_KLASSEN)
    print(f"  eindklassen ({'/'.join(EIND_KLASSEN)}): {n_klein_mee:,} van "
          f"{n_klein_tot:,} kleine-klasse-ways binnen {EIND_STRAAL_KM:g} km "
          f"van plant/kade doen mee; {len(ways):,} ways totaal in de graaf")

    keten, rap = fl.corridor_keten(ways, CORRIDOR)
    if keten is None:
        raise SystemExit(f"⚠️ corridor niet gerouteerd: {rap.get('fout')}")

    # ── wegklasse per vertex (voor de eindrapportage: waarover loopt de
    # first/last mile werkelijk?) — zelfde 6-decimalenkorrel als de graaf ────
    vertex_klassen = {}
    for w in ways:
        for lo, la in w["pts"]:
            vertex_klassen.setdefault((round(lo, 6), round(la, 6)),
                                      set()).add(w["soort"])

    def _klein_stuk(pts_keten, vanaf_start):
        """km + klassen vanaf het keten-uiteinde tot de eerste vertex die aan
        een WEG_HOUD-way ligt — het stuk dat over de kleine klassen loopt."""
        volgorde = pts_keten if vanaf_start else list(reversed(pts_keten))
        km_klein, klassen = 0.0, set()
        for i in range(len(volgorde) - 1):
            kl = vertex_klassen.get((round(volgorde[i][0], 6),
                                     round(volgorde[i][1], 6)), set())
            if kl & fl.WEG_HOUD:
                break
            klassen |= kl
            km_klein += fw.km(volgorde[i], volgorde[i + 1])
        return km_klein, sorted(klassen)

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
    # Met de eindklassen erbij horen deze stukjes ≤ ~0,5 km per kant te zijn —
    # rapporteren, niet gladstrijken: erboven is een bevinding die blijft staan.
    pts = list(keten["pts"])
    aanloop_van = fw.km(plant, pts[0])
    aanloop_naar = fw.km(pts[-1], kade)
    km_klein_van, kl_van = _klein_stuk(pts, True)
    km_klein_naar, kl_naar = _klein_stuk(pts, False)
    pts = ([(round(plant[0], 6), round(plant[1], 6))] + pts +
           [(round(kade[0], 6), round(kade[1], 6))])
    km_getekend = rap["km"] + aanloop_van + aanloop_naar
    v_van = "OK" if aanloop_van <= 0.5 else "⚠️ > 0,5 km — bevinding"
    v_naar = "OK" if aanloop_naar <= 0.5 else "⚠️ > 0,5 km — bevinding"
    print(f"  anker-verbindingen (rechte stukken, apart gerapporteerd, buiten "
          f"de lengtetoets):")
    print(f"    plant → weg {aanloop_van:.2f} km [{v_van}] · "
          f"weg → kade {aanloop_naar:.2f} km [{v_naar}]")
    print(f"  first mile over kleine klassen: {km_klein_van:.2f} km "
          f"({', '.join(kl_van) or 'geen — direct op WEG_HOUD'}) · "
          f"last mile: {km_klein_naar:.2f} km "
          f"({', '.join(kl_naar) or 'geen — direct op WEG_HOUD'})")
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
                # de first/last mile over de kleine eindklassen (zie kop):
                # echte weggeometrie, telt gewoon mee in kmWeg.
                "eindKlassen": list(EIND_KLASSEN),
                "eindStraalKm": EIND_STRAAL_KM,
                "kmKleinVan": round(km_klein_van, 3),
                "kmKleinNaar": round(km_klein_naar, 3),
                "klassenVan": kl_van,
                "klassenNaar": kl_naar,
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
