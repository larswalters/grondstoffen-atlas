"""Golf 9: bouwt golf9-script.mjs uit golf8-script.mjs (dat al agentR, literale slots en wegscan_puur heeft).
Invoer: golf8-grondstoffen.json, golf9-reserves.json (de reserve-assen met toets uit golf 8), het register plus de nog niet
geregistreerde stroomroute-bestanden op schijf, en de afwijzingen van golf 8. Uitvoer: golf9-script.mjs (LF, zonder U+FE0F).
Gebruik: python maak_golf9.py <map met de invoer en golf8-script.mjs>
"""
import glob, io, json, os, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
REPO = "C:/automation/Projects/General/grondstoffen-atlas"

src = io.open(OUT + "/golf8-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
G = json.load(io.open(OUT + "/golf8-grondstoffen.json", encoding="utf-8"))
rs = json.load(io.open(OUT + "/golf9-reserves.json", encoding="utf-8"))
reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))

bestaand, sleutels = {}, {}
for s in reg["stromen"]:
    bestaand.setdefault(s["grondstof"], []).append(s["bestand"].replace("stroomroute-", "").replace(".json", ""))
    sleutels.setdefault(s["grondstof"], []).append(s["sleutel"])
bestaand["grafiet"] = ["grafiet-balama-vidalia (bestand stroomroute-pilot.json, tot Casa Grande)" if x == "pilot" else x for x in bestaand["grafiet"]]
bekend = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg["uitgesloten"]}
op_schijf = sorted(os.path.basename(p)[len("stroomroute-"):-5] for p in glob.glob(REPO + "/v2/data/stroomroute-*.json") if os.path.basename(p) not in bekend)

RES = [{"id": r["id"], "g": r["g"], "as": r["as"], "toets": r["toets"]} for r in rs["reserves"]]
res_per_g = {}
for r in RES:
    res_per_g.setdefault(r["g"], []).append(r["id"])
afg_per_g = {}
for i in rs["afgewezen"]:
    afg_per_g.setdefault(i.split("-")[0], []).append(i)

MAXP = 1
G9 = []
for g in G:
    g = dict(g)
    k = g["sleutel"]
    g["max"] = MAXP
    g["bestaand"] = list(dict.fromkeys(bestaand[k] + [x for x in op_schijf if x.startswith(k + "-")]))
    g["sleutels"] = sleutels[k]
    hint = re.sub(r" GOLF 8: er staan al.*$", "", g["hint"], flags=re.S).strip()
    g["hint"] = (hint + f" GOLF 9: er staan al {len(g['bestaand'])} ketens op de bol ({', '.join(x.split(k + '-', 1)[-1] for x in g['bestaand'])}). "
                 "Dit is de laatste ontwerpronde van deze reeks: kies de ENE keten die het meeste nieuw verhaal toevoegt (andere regio, rol of corridor) "
                 f"en die je met bronnen kunt onderbouwen. Kies {MAXP}.")
    afw = [x.strip() for x in re.split(r"\s·\s", g["afgewezen"]) if x.strip() and "APART GEBAKKEN" not in x]
    tekst = " · ".join(afw)
    if afg_per_g.get(k):
        tekst += (" · " if tekst else "") + "golf 8 afgewezen: " + ", ".join(afg_per_g[k])
    if res_per_g.get(k):
        tekst += (" · " if tekst else "") + "AL ONTWORPEN EN GETOETST, WORDEN IN DEZE GOLF APART GEBAKKEN (NIET opnieuw voorstellen): " + ", ".join(res_per_g[k])
    g["afgewezen"] = tekst or "geen"
    G9.append(g)

body = src
i = body.index("const GRONDSTOFFEN_DATA")
meta = """export const meta = {
  name: 'atlas-m31-golf9-reserves-en-laatste-ontwerp',
  description: 'Grondstoffen Atlas M31 golf 9: 14 reserve-assen uit golf 8 (brief, bake, keuring) plus één nieuwe keten per grondstof na een ontwerp en toets',
  phases: [
    { title: 'Ontwerp', detail: 'één agent per grondstof: de ene meest waardevolle nieuwe as' },
    { title: 'Toets', detail: 'skeptische haalbaarheids- en juistheidstoets per grondstof' },
    { title: 'Brieven', detail: 'één agent per keten: lichte routebrief met satellietblik' },
    { title: 'Bakken', detail: 'één agent per keten: geometrie, toets, bak-noot' },
    { title: 'Keuring', detail: 'onafhankelijke natoets per keten, alleen mechanisch herstel' },
  ],
}
"""
# agentR en de helperfuncties staan ná de data-constanten; alles vanaf GRONDSTOFFEN_ALLE blijft staan
j = body.index("const GRONDSTOFFEN_DATA")
body = meta + "\n" + body[j:]
lines = body.split("\n")
for n, l in enumerate(lines):
    if l.startswith("const GRONDSTOFFEN_ALLE = "):
        lines[n] = "const GRONDSTOFFEN_ALLE = " + json.dumps(G9, ensure_ascii=True)
    elif l.startswith("const GRONDSTOFFEN_DATA = "):
        lines[n] = "const GRONDSTOFFEN_DATA = " + json.dumps(G9, ensure_ascii=True)
    elif l.startswith("const RESERVES_DATA = "):
        lines[n] = "const RESERVES_DATA = " + json.dumps(RES, ensure_ascii=True)
body = "\n".join(lines)

body = body.replace("voor golf 8 van M31", "voor golf 9 van M31")
oud = "Na golf 7 staan er 221 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 8 is een grote ronde die alle veertien grondstoffen (nu 13–17 ketens elk) verder aanvult."
assert oud in body
body = body.replace(oud, "Na golf 8 staan er 272 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 9 is de laatste ronde van deze reeks: reserve-assen plus één nieuwe keten per grondstof.")
body = body.replace("M31 · golf 8 (", "M31 · golf 9 (").replace("(M31 golf 8)", "(M31 golf 9)").replace("M31 golf 8", "M31 golf 9")
body = body.replace(chr(0xFE0F), "")
io.open(OUT + "/golf9-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf9-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G9, ensure_ascii=False, indent=1))
print("golf9-script.mjs:", len(body), "tekens;", len(G9), "grondstoffen; max totaal", MAXP * len(G9), "; reserves", len(RES), "; op schijf niet geregistreerd:", len(op_schijf))
