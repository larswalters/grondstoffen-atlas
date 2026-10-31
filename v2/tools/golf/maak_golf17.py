"""Golf 17: bouwt golf17-script.mjs uit golf16-script.mjs (de laatste ontwerpronde) -- opnieuw een GROTE ONTWERPRONDE, 3 nieuwe ketens per
grondstof over 13 grondstoffen: KOBALT SLAAT OOK DEZE RONDE OVER (bakhandleiding par. 13). Per grondstof ontwerp (3 nieuwe ketens + 2 reserves
voor golf 18), toets, en per gekozen keten brief -> bake -> keuring. De 7 reserves uit golf 16 (golf17-reserves.json) gaan als "niet opnieuw
ontwerpen" in de hint en blijven liggen voor een reserve-golf. Nieuw in de prompts: een stroom-id bevat uitsluitend [a-z0-9-] (golf 16-les).
Invoer: golf16-script.mjs en golf16-resultaat.json (de in de toets afgewezen assen van golf 16 met hun eerste reden), golf17-reserves.json,
het register (bestaande ketens + bezette sleutels per grondstof).
Uitvoer: golf17-script.mjs (LF, zonder U+FE0F) en golf17-grondstoffen.json in de uitvoermap.
Gebruik: python maak_golf17.py [<uitvoermap>] [<scratchpad van de sessie die de workflow start>]
"""
import glob, io, json, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else HIER
SCRATCH = sys.argv[2] if len(sys.argv) > 2 else OUT
REPO = "C:/automation/Projects/General/grondstoffen-atlas"
MAXP = 3
GOLF, VORIG = 17, 16
OVERSLAAN = {"kobalt"}

src = io.open(HIER + "/golf16-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
res13 = json.load(io.open(HIER + "/golf16-resultaat.json", encoding="utf-8"))
res15 = {"afgewezen_in_toets": []}
reserves14 = json.load(io.open(HIER + "/golf17-reserves.json", encoding="utf-8"))["reserves"]
reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))

G13 = None
for l in src.split("\n"):
    if l.startswith("const GRONDSTOFFEN_DATA = "):
        G13 = json.loads(l[len("const GRONDSTOFFEN_DATA = "):])
assert G13, "GRONDSTOFFEN_DATA niet gevonden in golf16-script.mjs"

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
            afg13.setdefault(g, []).append(f"{kid} (golf 16: {reden})" if reden else kid)
        elif f"stroomroute-{kid}.json" not in bekend and kid not in op_schijf and kid not in reserve_ids:
            nog_niet.append(kid)
# ketens die de briefagent heeft afgebroken (haalbaar in de toets, maar de lading ligt stil) tellen als afgewezen, met de reden
afgebroken = {o["id"]: (o.get("reden") or "") for o in res13["overzicht"] if o.get("afgebroken")}
nog_niet = [k for k in nog_niet if k not in afgebroken]
for kid, reden in afgebroken.items():
    afg13.setdefault(kid.split("-")[0], []).append(f"{kid} (golf 16, brief afgebroken: {re.sub(r'\s+', ' ', reden).strip()[:90]})")
assert not nog_niet, "golf 16-assen die haalbaar waren maar niet geregistreerd of gereserveerd zijn: " + ", ".join(nog_niet)
for x in res15.get("afgewezen_in_toets", []):
    reden15 = re.sub(r"\s+", " ", ((x.get("toets") or {}).get("problemen") or [""])[0]).strip()[:90]
    afg13.setdefault(x["id"].split("-")[0], []).append(f"{x['id']} (golf 15: {reden15})" if reden15 else x["id"])

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
    hint = re.sub(r" GOLF 16: er staan al.*$", "", g["hint"], flags=re.S).strip()
    res_tekst = ""
    if reserve_per_g.get(k):
        res_tekst = (f" Al als reserve klaar voor een latere golf (NIET opnieuw ontwerpen, ook geen variant ervan): "
                     f"{', '.join(reserve_per_g[k])}.")
    g["hint"] = (hint + f" GOLF 17: er staan al {len(g['bestaand'])} ketens op de bol ({', '.join(x.split(k + '-', 1)[-1] for x in g['bestaand'])}). "
                 f"Dit is de zesde ontwerpronde op rij (golf 11 t/m 16 brachten samen 134 ketens): de voor de hand liggende assen liggen er; "
                 f"kies de {MAXP} ketens die het meeste nieuw verhaal toevoegen (andere regio, rol of corridor dan wat er al ligt; de tweede en "
                 "derde speler in een land; de import- of verwerkingskant als de exportkant al ligt; een modaliteit die deze grondstof nog mist; "
                 f"landen of corridors die bij deze grondstof nog helemaal ontbreken) en die je met bronnen kunt onderbouwen, plus 2 reserve-assen voor golf 18.{res_tekst} "
                 f"Drie ketens is meer dan vorige rondes: liever {MAXP} goed gebronde korte ketens dan drie mooie verhalen die de toets afwijst. Kies {MAXP}.")
    afw = [x.strip() for x in re.split(r"\s·\s", g["afgewezen"]) if x.strip() and "APART GEBAKKEN" not in x and x.strip() != "geen"]
    tekst = " · ".join(afw)
    if afg13.get(k):
        tekst += (" · " if tekst else "") + "golf 16 afgewezen: " + ", ".join(afg13[k])
    g["afgewezen"] = tekst or "geen"
    G14.append(g)

meta = """export const meta = {
  name: 'atlas-m31-golf17-ontwerpronde',
  description: 'Grondstoffen Atlas M31 golf 17: tweede grote ontwerpronde over 13 grondstoffen (kobalt overgeslagen), drie nieuwe ketens per grondstof (ontwerp, toets, brief, bake, keuring); geen reserve-assen',
  phases: [
    { title: 'Ontwerp', detail: 'een agent per grondstof: de drie meest waardevolle nieuwe assen plus twee reserves voor golf 18' },
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

oud = ("Na golf 15 staan er 418 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 16 is een grote "
       "ontwerpronde over 13 grondstoffen (kobalt slaat deze ronde over): 3 nieuwe ketens per grondstof, plus reserve-assen voor golf 17.")
assert oud in body, "openingszin van het ontwerp niet gevonden"
body = body.replace(oud, f"Na golf 16 staan er {totaal} gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 17 is opnieuw een grote "
                         f"ontwerpronde over {len(G14)} grondstoffen (kobalt slaat deze ronde over): {MAXP} nieuwe ketens per grondstof, "
                         "plus reserve-assen voor golf 18.")
# id-regel (golf 16-les: een bake-agent maakte een id met een spatie)
oud_id = "- HET STROOM-ID NOEMT HET WERKELIJKE EINDPUNT van de lijn"
assert body.count(oud_id) == 1, "id-regel niet gevonden"
body = body.replace(oud_id, "- EEN STROOM-ID BEVAT UITSLUITEND [a-z0-9-]: kleine letters, cijfers en koppeltekens, geen spaties, hoofdletters of diakrieten (golf 16: 'dares salaam' met spatie moest centraal hernoemd worden; schrijf daressalaam). Dat geldt ook voor de bestandsnaam, de bak-functie en --stroom.\n" + oud_id)
assert "const ontwerpRes = await ontwerpStroom()\nconst reserveRes = []" in body, "golf 16-orkestratie (alleen ontwerpStroom) niet gevonden"
for a, b in [("M31 golf 16", "M31 golf 17"), ("golf 16 van M31", "golf 17 van M31"), ("M31 · golf 16 (", "M31 · golf 17 ("), ("(M31 golf 16)", "(M31 golf 17)")]:
    body = body.replace(a, b)
rest = body.replace("golf 16 afgewezen", "").replace("golf 16:", "").replace("golf 14/15 afgewezen", "").replace("golf 14:", "").replace("golf 15:", "").replace("golf 11 t/m 16", "").replace("golf 16-les", "").replace("(golf 16: ", "")
rest = rest.replace("golf 16, brief afgebroken", "").replace("RESERVE golf 16", "").replace("Reserve golf 16", "").replace("reserve golf 16", "")
for m in re.finditer("golf 16", rest):
    print("LET OP losse verwijzing naar golf 16:", rest[max(0, m.start() - 60):m.end() + 40].replace(chr(10), " "))
body = body.replace(chr(0xFE0F), "")
io.open(OUT + "/golf17-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf17-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G14, ensure_ascii=False, indent=1))
print("golf17-script.mjs:", len(body), "tekens;", len(G14), "grondstoffen; max totaal", MAXP * len(G14), "; register", totaal,
      "; golf 16 afgewezen", sum(len(v) for v in afg13.values()), "; reserves klaar", len(reserve_ids), "; op schijf niet geregistreerd:", len(op_schijf))
