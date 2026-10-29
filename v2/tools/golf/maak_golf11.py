"""Golf 11: bouwt golf11-script.mjs uit golf9-script.mjs (het laatste script met een volledige ontwerpronde).
Een NIEUWE ONTWERPRONDE zonder reserve-assen: per grondstof een ontwerp (2 nieuwe ketens + 2 reserves voor een latere golf),
een toets, en per gekozen keten brief -> bake -> keuring. Invoer: golf9-script.mjs (uit deze map), golf9-assen.json (alle 42 assen
van golf 9 met hun toetsoordeel, uit het golf 9-journal), het register (bestaande ketens + bezette sleutels per grondstof).
Uitvoer: golf11-script.mjs (LF, zonder U+FE0F) en golf11-grondstoffen.json in de uitvoermap.
Gebruik: python maak_golf11.py <uitvoermap met golf9-assen.json> [<scratchpad van de sessie die de workflow start>]
"""
import glob, io, json, os, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
SCRATCH = sys.argv[2] if len(sys.argv) > 2 else OUT
HIER = os.path.dirname(os.path.abspath(__file__))
REPO = "C:/automation/Projects/General/grondstoffen-atlas"
MAXP = 2

src = io.open(HIER + "/golf9-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
assen9 = json.load(io.open(OUT + "/golf9-assen.json", encoding="utf-8"))
reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))

G9 = None
for l in src.split("\n"):
    if l.startswith("const GRONDSTOFFEN_DATA = "):
        G9 = json.loads(l[len("const GRONDSTOFFEN_DATA = "):])
assert G9, "GRONDSTOFFEN_DATA niet gevonden in golf9-script.mjs"

bestaand, sleutels = {}, {}
for s in reg["stromen"]:
    bestaand.setdefault(s["grondstof"], []).append(s["bestand"].replace("stroomroute-", "").replace(".json", ""))
    sleutels.setdefault(s["grondstof"], []).append(s["sleutel"])
bestaand["grafiet"] = ["grafiet-balama-vidalia (bestand stroomroute-pilot.json, tot Casa Grande)" if x == "pilot" else x for x in bestaand["grafiet"]]
bekend = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg["uitgesloten"]}
op_schijf = sorted(os.path.basename(p)[len("stroomroute-"):-5] for p in glob.glob(REPO + "/v2/data/stroomroute-*.json") if os.path.basename(p) not in bekend)

# Golf 9: alles wat de toets afwees (haalbaar false) met de eerste reden; wat haalbaar was is in golf 9 of 10 gebakken en staat in het register.
afg9 = {}
for kid, v in assen9.items():
    if v.get("haalbaar") is False:
        reden = (v.get("problemen") or [""])[0]
        reden = re.sub(r"\s+", " ", reden).strip()[:90]
        afg9.setdefault(v["g"], []).append(f"{kid} (golf 9: {reden})" if reden else kid)
nog_niet = [kid for kid, v in assen9.items() if v.get("haalbaar") is not False and f"stroomroute-{kid}.json" not in bekend and kid not in op_schijf]
assert not nog_niet, "golf 9-assen die haalbaar waren maar niet geregistreerd zijn: " + ", ".join(nog_niet)

totaal = len(reg["stromen"])
G11 = []
for g in G9:
    g = dict(g)
    k = g["sleutel"]
    g["max"] = MAXP
    g["bestaand"] = list(dict.fromkeys(bestaand[k] + [x for x in op_schijf if x.startswith(k + "-")]))
    g["sleutels"] = sleutels[k]
    hint = re.sub(r" GOLF 9: er staan al.*$", "", g["hint"], flags=re.S).strip()
    g["hint"] = (hint + f" GOLF 11: er staan al {len(g['bestaand'])} ketens op de bol ({', '.join(x.split(k + '-', 1)[-1] for x in g['bestaand'])}). "
                 f"Dit is een nieuwe ontwerpronde na twee golven zonder ontwerp: kies de {MAXP} ketens die het meeste nieuw verhaal toevoegen "
                 "(andere regio, rol of corridor dan wat er al ligt; ook de tweede en derde speler in een land, niet alleen de grootste) "
                 f"en die je met bronnen kunt onderbouwen, plus 2 reserve-assen. Kies {MAXP}.")
    afw = [x.strip() for x in re.split(r"\s·\s", g["afgewezen"]) if x.strip() and "APART GEBAKKEN" not in x]
    tekst = " · ".join(afw)
    if afg9.get(k):
        tekst += (" · " if tekst else "") + "golf 9 afgewezen: " + ", ".join(afg9[k])
    g["afgewezen"] = tekst or "geen"
    G11.append(g)

meta = """export const meta = {
  name: 'atlas-m31-golf11-ontwerpronde',
  description: 'Grondstoffen Atlas M31 golf 11: nieuwe ontwerpronde, twee nieuwe ketens per grondstof (ontwerp, toets, brief, bake, keuring); geen reserve-assen',
  phases: [
    { title: 'Ontwerp', detail: 'een agent per grondstof: de twee meest waardevolle nieuwe assen plus twee reserves' },
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
        lines[n] = "const GRONDSTOFFEN_DATA = " + json.dumps(G11, ensure_ascii=True)
    elif l.startswith("const RESERVES_DATA = "):
        lines[n] = "const RESERVES_DATA = []"
    elif l.startswith("const SCRATCH = "):
        lines[n] = "const SCRATCH = " + json.dumps(SCRATCH)
body = "\n".join(lines)

oud = ("Na golf 8 staan er 272 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 9 is de laatste ronde van deze reeks: "
       "reserve-assen plus één nieuwe keten per grondstof.")
assert oud in body
body = body.replace(oud, f"Na golf 10 staan er {totaal} gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 11 is een nieuwe "
                         f"ontwerpronde: {MAXP} nieuwe ketens per grondstof, plus reserve-assen voor een latere golf.")
# Geen reserve-stroom: alleen de ontwerpstroom draait.
oud_par = "const [ontwerpRes, reserveRes] = await parallel([ontwerpStroom, reserveStroom])"
assert oud_par in body
body = body.replace(oud_par, "const ontwerpRes = await ontwerpStroom()\nconst reserveRes = []")
for a, b in [("M31 golf 9", "M31 golf 11"), ("golf 9 van M31", "golf 11 van M31"), ("M31 · golf 9 (", "M31 · golf 11 ("), ("(M31 golf 9)", "(M31 golf 11)")]:
    body = body.replace(a, b)
assert "golf 9" not in body.replace("golf 9 afgewezen", "").replace("golf 9:", ""), "losse verwijzing naar golf 9 blijft staan"
body = body.replace(chr(0xFE0F), "")
io.open(OUT + "/golf11-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf11-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G11, ensure_ascii=False, indent=1))
print("golf11-script.mjs:", len(body), "tekens;", len(G11), "grondstoffen; max totaal", MAXP * len(G11), "; register", totaal,
      "; golf 9 afgewezen", sum(len(v) for v in afg9.values()), "; op schijf niet geregistreerd:", len(op_schijf))
