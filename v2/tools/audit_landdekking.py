#!/usr/bin/env python3
"""
audit_landdekking.py — welke atlas-plekken liggen buiten onze Geofabrik-extracts?

Waarom dit bestaat (M25, [LAR-491]): het landnet wordt gescand uit de extracts
die op schijf staan. Een land dat niet in de registry staat heeft geen bestand,
dus de scan meldt er niets — en elke assert in de bake blijft groen terwijl de
kaart liegt. Dit is het enige mechanisme dat zo'n gat kán vangen: je moet het
meten aan de VRAAGKANT (waar liggen de mijnen, raffinaderijen en havens van de
atlas) en niet aan de aanbodkant (wat vond de scan).

Werkwijze:
  1. lees elke `data/<grondstof>.js` en verzamel de nodes met een ECHTE plaats;
  2. lees de bbox uit de header van elke aanwezige .osm.pbf (geen scan, ~ms);
  3. rapporteer per node of hij binnen minstens één extract-bbox valt.

⚠️ Een bbox is grover dan de regio zelf: een punt kan binnen de bbox van een
buurland vallen zonder dat het extract die geometrie bevat. Deze audit is dus
conservatief in de VERKEERDE richting — hij overschat de dekking. Wat hij
aanwijst als ONGEDEKT is daarom hard; wat hij groen noemt is "waarschijnlijk".
De echte controle blijft de aanhecht-afstand ná de bake (landnet-aanhecht.json).

Draaien:  python v2/tools/audit_landdekking.py
          python v2/tools/audit_landdekking.py --alle   (ook de gedekte nodes)
"""

import argparse
import glob
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
REPO = os.path.dirname(V2)
DATA = os.path.join(REPO, "data")
GEOFABRIK = os.path.join(V2, "build-cache", "geofabrik")

# Nodes met een ECHTE plaats op de kaart. Bewust NIET: market/exchange/hub —
# dat zijn centroïdes van een land of een beurs (cu-mkt-usa staat op
# -84,00/39,00, een akker in Ohio). Die als dekkingseis nemen laat de audit
# extracts eisen voor plaatsen die niet bestaan.
PLAATS_TYPES = {"mine", "refinery", "port", "terminal", "recycler", "reserve",
                "smelter", "plant", "airport"}

# ⚠️ DE BBOX-VAL. Een bbox-treffer bewijst niet dat het extract de geometrie
# bevat: Mongolië ligt volledig binnen de bbox van China, Lesotho binnen die van
# Zuid-Afrika, Zimbabwe binnen die van Mozambique/Zambia. Zonder deze tabel meldt
# de audit die plekken als gedekt terwijl de scan er geen meter spoor vindt —
# precies het stille gat dat dit gereedschap moet vangen.
#
# Per atlas-landnaam: de extract-sleutels die dat land ECHT bevatten. Een node
# telt pas als gedekt als minstens één dekkende bbox ook in deze lijst staat.
# Landen zonder entry (klein of irrelevant voor landtransport) vallen terug op
# de kale bbox-toets; die staan in de uitvoer als "alleen bbox".
LAND_NAAR_EXTRACT = {
    "Algerije": ["algerije"], "Angola": ["angola"], "Argentinië": ["argentina"],
    "Australie": ["australie"], "Australië": ["australie"],
    "Azerbeidzjan": ["azerbeidzjan"], "België": ["belgie"], "Benin": ["benin"],
    "Bolivia": ["bolivia"], "Botswana": ["botswana"], "Brazilië": ["brazilie"],
    "Canada": ["canada"], "Chili": ["chili"], "China": ["china"],
    "Colombia": ["colombia"], "Cuba": ["cuba"], "DR Congo": ["congo-drc"],
    "Duitsland": ["de-"], "Duitsland/NL": ["de-", "nederland"],
    "Estland": ["estland"], "Filipijnen": ["filipijnen"], "Finland": ["finland"],
    "Frankrijk": ["fr-"], "Georgië": ["georgie"], "Ghana": ["ghana"],
    "Griekenland": ["griekenland"], "Groenland": ["groenland"],
    "Hongkong": ["china"], "India": ["india"], "Indonesië": ["indonesie"],
    "Irak": ["irak"], "Iran": ["iran"], "Italië": ["italie"], "Japan": ["japan"],
    "Kazachstan": ["kazachstan"], "Koeweit": ["koeweit", "gcc"],
    "Lesotho": ["lesotho", "south-africa", "zuid-afrika"],
    "Madagaskar": ["madagaskar", "madagascar"], "Malawi": ["malawi"],
    "Maleisie": ["maleisie"], "Maleisië": ["maleisie"], "Mali": ["mali"],
    "Marokko": ["marokko", "morocco"], "Mexico": ["mexico"],
    "Mongolië": ["mongolia", "mongolie"], "Mozambique": ["mozambique"],
    "Myanmar": ["myanmar"], "Namibië": ["namibie", "namibia"],
    "Nederland": ["nederland"], "Nieuw-Caledonië": ["nieuw-caledonie", "new-caledonia"],
    "Niger": ["niger"], "Nigeria": ["nigeria"], "Noorwegen": ["noorwegen"],
    "Oekraine": ["oekraine"], "Oekraïne": ["oekraine"],
    "Oezbekistan": ["oezbekistan", "uzbekistan"], "Panama": ["panama"],
    "Papoea-N.-Guinea": ["papoea"], "Peru": ["peru"], "Polen": ["polen"],
    "Portugal": ["portugal"], "Qatar": ["qatar", "gcc"], "Rusland": ["rusland"],
    "Saoedi-Arabië": ["saoedi", "saudi", "gcc"], "Servië": ["servie"],
    "Singapore": ["maleisie", "singapore"], "Spanje": ["spanje"],
    "Sri Lanka": ["sri-lanka"], "Sudan": ["sudan"], "Tanzania": ["tanzania"],
    "Turkije": ["turkije"], "Turkmenistan": ["turkmenistan"],
    "VAE": ["vae", "uae", "gcc", "emirates"], "VK": ["groot-brittannie"],
    "Verenigd Koninkrijk": ["groot-brittannie"], "VS": ["us-"],
    "VS (Alaska)": ["us-alaska"], "VS (Louisiana)": ["us-louisiana"],
    "VS (Tennessee)": ["us-tennessee"], "VS (Utah)": ["us-utah"],
    "VS (Wyoming)": ["us-wyoming"], "Venezuela": ["venezuela"],
    "Vietnam": ["vietnam"], "Zambia": ["zambia"], "Zimbabwe": ["zimbabwe"],
    "Zuid-Afrika": ["zuid-afrika", "south-africa"], "Zuid-Korea": ["zuid-korea"],
    "Zweden": ["zweden"], "Zwitserland": ["zwitserland"],
}


def lees_nodes(pad):
    """Trekt de node-objecten uit een data/<grondstof>.js. Balans-scan op de
    `nodes: [`-array; alleen blokken met lat én lon tellen mee."""
    tekst = open(pad, encoding="utf-8").read()
    m = re.search(r"\bnodes\s*:\s*\[", tekst)
    if not m:
        return []
    i = m.end()
    diep, start, blokken = 0, None, []
    while i < len(tekst):
        c = tekst[i]
        if c == "]" and diep == 0:
            break
        if c == "{":
            if diep == 0:
                start = i
            diep += 1
        elif c == "}":
            diep -= 1
            if diep == 0 and start is not None:
                blokken.append(tekst[start:i + 1])
                start = None
        i += 1

    uit = []
    for b in blokken:
        lat = re.search(r"\blat\s*:\s*(-?[\d.]+)", b)
        lon = re.search(r"\blon\s*:\s*(-?[\d.]+)", b)
        if not (lat and lon):
            continue
        veld = lambda k: (re.search(rf'\b{k}\s*:\s*"([^"]*)"', b) or [None, ""])[1]
        uit.append({
            "id": veld("id"), "type": veld("type"), "naam": veld("name"),
            "land": veld("country"),
            "lat": float(lat.group(1)), "lon": float(lon.group(1)),
        })
    return uit


def extract_bboxen():
    """(sleutel, lon0, lat0, lon1, lat1) per aanwezige .osm.pbf — uit de HEADER,
    dus zonder de 65 GB te lezen."""
    import osmium
    uit = []
    for pad in sorted(glob.glob(os.path.join(GEOFABRIK, "*.osm.pbf"))):
        sleutel = os.path.basename(pad).replace("-latest.osm.pbf", "")
        try:
            rd = osmium.io.Reader(pad, osmium.osm.osm_entity_bits.NOTHING)
            b = rd.header().box()
            rd.close()
        except Exception as e:                      # noqa: BLE001
            print(f"  ⚠️ header onleesbaar: {sleutel} ({e})")
            continue
        if not b.valid():
            print(f"  ⚠️ geen bbox in de header: {sleutel}")
            continue
        uit.append((sleutel, b.bottom_left.lon, b.bottom_left.lat,
                    b.top_right.lon, b.top_right.lat))
    return uit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alle", action="store_true", help="ook de gedekte nodes tonen")
    a = ap.parse_args()

    bestanden = sorted(glob.glob(os.path.join(DATA, "*.js")))
    bestanden = [b for b in bestanden if not os.path.basename(b).startswith("_")]
    nodes = []
    for pad in bestanden:
        grondstof = os.path.basename(pad)[:-3]
        for n in lees_nodes(pad):
            n["grondstof"] = grondstof
            nodes.append(n)
    plaatsen = [n for n in nodes if n["type"] in PLAATS_TYPES]
    print(f"atlas: {len(nodes):,} nodes in {len(bestanden)} grondstoffen · "
          f"{len(plaatsen):,} met een echte plaats "
          f"({len(nodes) - len(plaatsen):,} markt/beurs/hub overgeslagen)")

    bboxen = extract_bboxen()
    gb = sum(os.path.getsize(os.path.join(GEOFABRIK, f"{s}-latest.osm.pbf"))
             for s, *_ in bboxen) / 1e9
    print(f"extracts: {len(bboxen)} aanwezig · {gb:,.1f} GB\n")

    ongedekt, per_land = [], defaultdict(list)
    zonder_tabel = set()
    for n in plaatsen:
        raak = [s for s, lo0, la0, lo1, la1 in bboxen
                if lo0 <= n["lon"] <= lo1 and la0 <= n["lat"] <= la1]
        n["extracts"] = raak
        sleutels = LAND_NAAR_EXTRACT.get(n["land"])
        if sleutels is None:
            zonder_tabel.add(n["land"])
            echt = raak                       # geen tabel-entry: kale bbox-toets
            n["reden"] = "alleen bbox"
        else:
            echt = [s for s in raak if any(s.startswith(k) or k in s for k in sleutels)]
            n["reden"] = "geen extract van dit land" if raak and not echt else "buiten élke bbox"
        n["echt"] = echt
        if not echt:
            ongedekt.append(n)
            per_land[n["land"] or "(land onbekend)"].append(n)
        elif a.alle:
            print(f"  ok  {n['naam']:<34} {n['land']:<22} → {', '.join(echt[:3])}")

    schijn = [n for n in ongedekt if n["reden"] == "geen extract van dit land"]
    print(f"{'=' * 78}\nONGEDEKT: {len(ongedekt)} van {len(plaatsen)} plaatsen "
          f"({100 * len(ongedekt) / max(1, len(plaatsen)):.0f}%)\n"
          f"  waarvan {len(ongedekt) - len(schijn)} buiten élke bbox en "
          f"{len(schijn)} SCHIJNBAAR gedekt (bbox van een buurland, geen eigen "
          f"extract)\n{'=' * 78}")
    for land, ns in sorted(per_land.items(), key=lambda kv: -len(kv[1])):
        soorten = defaultdict(int)
        for n in ns:
            soorten[n["type"]] += 1
        detail = " · ".join(f"{k} {v}" for k, v in sorted(soorten.items()))
        redenen = {n["reden"] for n in ns}
        buren = sorted({e for n in ns for e in n["extracts"]})[:3]
        staart = f" — bbox-treffer op {', '.join(buren)}" if buren else ""
        print(f"\n{land}  ({len(ns)} plaatsen: {detail}) [{'/'.join(sorted(redenen))}]{staart}")
        for n in sorted(ns, key=lambda x: x["naam"])[:12]:
            print(f"    {n['naam']:<34} {n['type']:<10} "
                  f"{n['lat']:8.3f},{n['lon']:9.3f}  [{n['grondstof']}]")
        if len(ns) > 12:
            print(f"    … en {len(ns) - 12} meer")

    if zonder_tabel:
        print(f"\n⚠️ geen entry in LAND_NAAR_EXTRACT (kale bbox-toets gebruikt): "
              f"{', '.join(sorted(zonder_tabel))}")
    print(f"\n{'=' * 78}")
    print("Een bbox-treffer bewijst niets over de INHOUD van een extract — Mongolië")
    print("ligt volledig in de bbox van China. Daarom telt alleen een extract dat")
    print("het land zelf dekt. De eindtoets blijft de aanhecht-afstand ná de bake.")


if __name__ == "__main__":
    main()
