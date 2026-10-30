"""Golf 14: bouwt golf14-script.mjs uit golf13-script.mjs (de laatste ontwerpronde) -- opnieuw een ONTWERPRONDE zonder reserve-assen,
nu over 13 grondstoffen: KOBALT SLAAT DEZE RONDE OVER (golf 11 en 13: acht van acht assen afgewezen; bakhandleiding par. 13: kobalt alleen
weer meenemen met een vooraf gevonden producent-haven-bron). Per grondstof ontwerp (2 nieuwe ketens + 2 reserves voor golf 15), toets, en per
gekozen keten brief -> bake -> keuring.
Invoer: golf13-script.mjs en golf13-resultaat.json (de in de toets afgewezen assen van golf 13 met hun eerste reden), golf14-reserves.json
(de 8 reserves van golf 13 die al klaar liggen: niet opnieuw ontwerpen), het register (bestaande ketens + bezette sleutels per grondstof).
Uitvoer: golf14-script.mjs (LF, zonder U+FE0F) en golf14-grondstoffen.json in de uitvoermap.
Gebruik: python maak_golf14.py [<uitvoermap>] [<scratchpad van de sessie die de workflow start>]
"""
import glob, io, json, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else HIER
SCRATCH = sys.argv[2] if len(sys.argv) > 2 else OUT
REPO = "C:/automation/Projects/General/grondstoffen-atlas"
MAXP = 2
GOLF, VORIG = 14, 13
OVERSLAAN = {"kobalt"}

src = io.open(HIER + "/golf13-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
res13 = json.load(io.open(HIER + "/golf13-resultaat.json", encoding="utf-8"))
reserves14 = json.load(io.open(HIER + "/golf14-reserves.json", encoding="utf-8"))["reserves"]
reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))

G13 = None
for l in src.split("\n"):
    if l.startswith("const GRONDSTOFFEN_DATA = "):
        G13 = json.loads(l[len("const GRONDSTOFFEN_DATA = "):])
assert G13, "GRONDSTOFFEN_DATA niet gevonden in golf13-script.mjs"

bestaand, sleutels = {}, {}
for s in reg["stromen"]:
    bestaand.setdefault(s["grondstof"], []).append(s["bestand"].replace("stroomroute-", "").replace(".json", ""))
    sleutels.setdefault(s["grondstof"], []).append(s["sleutel"])
bestaand["grafiet"] = ["grafiet-balama-vidalia (bestand stroomroute-pilot.json, tot Casa Grande)" if x == "pilot" else x for x in bestaand["grafiet"]]
bekend = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg["uitgesloten"]}
op_schijf = sorted(os.path.basename(p)[len("stroomroute-"):-5] for p in glob.glob(REPO + "/v2/data/stroomroute-*.json") if os.path.basename(p) not in bekend)

# Golf 13: alles wat de toets afwees (haalbaar false) met de eerste reden. De reserves (haalbaar, niet gekozen) liggen in golf14-reserves.json
# en komen in de hint als "niet opnieuw ontwerpen"; alles wat gekozen was is in golf 13 gebakken en staat in het register.
reserve_ids = {r["id"] for r in reserves14}
reserve_per_g = {}
for r in reserves14:
    reserve_per_g.setdefault(r["g"], []).append(r["id"])
afg13 = {}
nog_niet = []
for r in res13["resultaten"]:
    g = r["grondstof"]
    for k in (r.get("toets") or {}).get("ketens", []):
        kid = k.get("keten_id")
        if not kid:
            continue
        if k.get("haalbaar") is False:
            reden = re.sub(r"\s+", " ", (k.get("problemen") or [""])[0]).strip()[:90]
            afg13.setdefault(g, []).append(f"{kid} (golf 13: {reden})" if reden else kid)
        elif f"stroomroute-{kid}.json" not in bekend and kid not in op_schijf and kid not in reserve_ids:
            nog_niet.append(kid)
assert not nog_niet, "golf 13-assen die haalbaar waren maar niet geregistreerd of gereserveerd zijn: " + ", ".join(nog_niet)

totaal = len(reg["stromen"])
G14 = []
for g in G13:
    g = dict(g)
    k = g["sleutel"]
    if k in OVERSLAAN:
        continue
    g["max"] = MAXP
    g["bestaand"] = list(dict.fromkeys(bestaand[k] + [x for x in op_schijf if x.startswith(k + "-")]))
    g["sleutels"] = sleutels[k]
    hint = re.sub(r" GOLF 13: er staan al.*$", "", g["hint"], flags=re.S).strip()
    res_tekst = ""
    if reserve_per_g.get(k):
        res_tekst = (f" Al als reserve klaar voor een latere golf (NIET opnieuw ontwerpen, ook geen variant ervan): "
                     f"{', '.join(reserve_per_g[k])}.")
    g["hint"] = (hint + f" GOLF 14: er staan al {len(g['bestaand'])} ketens op de bol ({', '.join(x.split(k + '-', 1)[-1] for x in g['bestaand'])}). "
                 f"Dit is de vierde ontwerpronde op rij (golf 11, 12 en 13 brachten samen 61 ketens): de voor de hand liggende assen liggen er; "
                 f"kies de {MAXP} ketens die het meeste nieuw verhaal toevoegen (andere regio, rol of corridor dan wat er al ligt; de tweede en "
                 "derde speler in een land; de import- of verwerkingskant als de exportkant al ligt; een modaliteit die deze grondstof nog mist) "
                 f"en die je met bronnen kunt onderbouwen, plus 2 reserve-assen voor golf 15.{res_tekst} Kies {MAXP}.")
    afw = [x.strip() for x in re.split(r"\s·\s", g["afgewezen"]) if x.strip() and "APART GEBAKKEN" not in x and x.strip() != "geen"]
    tekst = " · ".join(afw)
    if afg13.get(k):
        tekst += (" · " if tekst else "") + "golf 13 afgewezen: " + ", ".join(afg13[k])
    g["afgewezen"] = tekst or "geen"
    G14.append(g)

meta = """export const meta = {
  name: 'atlas-m31-golf14-ontwerpronde',
  description: 'Grondstoffen Atlas M31 golf 14: nieuwe ontwerpronde over 13 grondstoffen (kobalt overgeslagen), twee nieuwe ketens per grondstof (ontwerp, toets, brief, bake, keuring); geen reserve-assen',
  phases: [
    { title: 'Ontwerp', detail: 'een agent per grondstof: de twee meest waardevolle nieuwe assen plus twee reserves voor golf 15' },
    { title: 'Toets', detail: 'skeptische haalbaarheids- en juistheidstoets per grondstof' },
    { title: 'Brieven', detail: 'een agent per keten: lichte routebrief met satellietblik' },
    { title: 'Bakken', detail: 'een agent per keten: geometrie, toets, bak-noot' },
    { title: 'Keuring', detail: 'onafhankelijke natoets per keten, alleen mechanisch herstel' },
  ],
}
"""
j = src.index("const GRONDSTOFFEN_DATA")
body = meta + "\n" + src[j:]
lines = body.split("\n")
for n, l in enumerate(lines):
    if l.startswith("const GRONDSTOFFEN_DATA = "):
        lines[n] = "const GRONDSTOFFEN_DATA = " + json.dumps(G14, ensure_ascii=True)
    elif l.startswith("const RESERVES_DATA = "):
        lines[n] = "const RESERVES_DATA = []"
    elif l.startswith("const SCRATCH = "):
        lines[n] = "const SCRATCH = " + json.dumps(SCRATCH)
body = "\n".join(lines)

oud = ("Na golf 12 staan er 352 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 13 is opnieuw een "
       "ontwerpronde: 2 nieuwe ketens per grondstof, plus reserve-assen voor golf 14.")
assert oud in body, "openingszin van het ontwerp niet gevonden"
body = body.replace(oud, f"Na golf 13 staan er {totaal} gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 14 is opnieuw een "
                         f"ontwerpronde over {len(G14)} grondstoffen (kobalt slaat deze ronde over): {MAXP} nieuwe ketens per grondstof, "
                         "plus reserve-assen voor golf 15.")
assert "const ontwerpRes = await ontwerpStroom()\nconst reserveRes = []" in body, "golf 13-orkestratie (alleen ontwerpStroom) niet gevonden"
for a, b in [("M31 golf 13", "M31 golf 14"), ("golf 13 van M31", "golf 14 van M31"), ("M31 · golf 13 (", "M31 · golf 14 ("), ("(M31 golf 13)", "(M31 golf 14)")]:
    body = body.replace(a, b)
rest = body.replace("golf 13 afgewezen", "").replace("golf 13:", "").replace("golf 11, 12 en 13", "").replace("Na golf 13", "")
assert "golf 13" not in rest, "losse verwijzing naar golf 13 blijft staan"
body = body.replace(chr(0xFE0F), "")
io.open(OUT + "/golf14-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf14-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G14, ensure_ascii=False, indent=1))
print("golf14-script.mjs:", len(body), "tekens;", len(G14), "grondstoffen; max totaal", MAXP * len(G14), "; register", totaal,
      "; golf 13 afgewezen", sum(len(v) for v in afg13.values()), "; reserves klaar", len(reserve_ids), "; op schijf niet geregistreerd:", len(op_schijf))
