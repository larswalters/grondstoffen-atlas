"""Golf 10: bouwt golf10-script.mjs uit golf9-script.mjs — ALLEEN de reserve-route (brief, bake, keuring), geen ontwerpronde.
Invoer: golf9-script.mjs (uit deze map), golf10-reserves.json (de 15 reserve-assen met toets uit het golf 9-journal; twee lithium-
assen zonder toets krijgen in het script eerst een toets), het register (bestaande ketens + bezette sleutels per grondstof).
Uitvoer: golf10-script.mjs (LF, zonder U+FE0F) en golf10-grondstoffen.json in de uitvoermap.
Gebruik: python maak_golf10.py <map met golf10-reserves.json> [<scratchpad van de sessie die de workflow start>]
"""
import glob, io, json, os, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
SCRATCH = sys.argv[2] if len(sys.argv) > 2 else OUT
HIER = os.path.dirname(os.path.abspath(__file__))
REPO = "C:/automation/Projects/General/grondstoffen-atlas"

src = io.open(HIER + "/golf9-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
rs = json.load(io.open(OUT + "/golf10-reserves.json", encoding="utf-8"))
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

RES = [{"id": r["id"], "g": r["g"], "as": r["as"], "toets": r["toets"]} for r in rs["reserves"]]
for r in RES:
    assert r["as"], "reserve zonder ontwerp-as: " + r["id"]
    assert r["id"] not in bekend and not os.path.exists(REPO + "/v2/data/stroomroute-" + r["id"] + ".json"), "bestaat al: " + r["id"]

G10 = []
for g in G9:
    g = dict(g)
    k = g["sleutel"]
    g["bestaand"] = list(dict.fromkeys(bestaand[k] + [x for x in op_schijf if x.startswith(k + "-")]))
    g["sleutels"] = sleutels[k]
    g["hint"] = re.sub(r" GOLF 9: er staan al.*$", "", g["hint"], flags=re.S).strip()
    G10.append(g)

meta = """export const meta = {
  name: 'atlas-m31-golf10-reserves',
  description: 'Grondstoffen Atlas M31 golf 10: de 15 getoetste reserve-assen uit golf 9 bakken (brief, bake, keuring); geen ontwerpronde',
  phases: [
    { title: 'Toets', detail: 'alleen voor reserve-assen die in golf 9 geen per-keten-oordeel kregen' },
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
        lines[n] = "const GRONDSTOFFEN_DATA = " + json.dumps(G10, ensure_ascii=True)
    elif l.startswith("const RESERVES_DATA = "):
        lines[n] = "const RESERVES_DATA = " + json.dumps(RES, ensure_ascii=True)
    elif l.startswith("const SCRATCH = "):
        lines[n] = "const SCRATCH = " + json.dumps(SCRATCH)
body = "\n".join(lines)

# De orkestratie: alleen de reserve-route; ontwerp/toets-functies blijven staan (toetsPrompt wordt gebruikt voor ongetoetste reserves).
oud_start = body.index("const ontwerpStroom = () => pipeline(GRONDSTOFFEN,")
nieuw_slot = """const reserveItems = RESERVES.map((r) => ({ id: r.id, as: r.as, toets: r.toets, g: GBY[r.g], afgewezen: false }))
const reserveRes = await ketenPipeline(reserveItems)
const reserveKetens = (reserveRes || []).filter(Boolean)
const resultaten = []

const alle = reserveKetens
const ok = alle.filter((k) => k.bake && k.bake.gebakken)
log(`klaar: ${ok.length}/${alle.length} gebakken, ${ok.filter((k) => !k.keuring || k.keuring.oordeel !== 'niet-registreren').length} registreerbaar van ${RESERVES.length} reserve-assen (${reserveItems.filter((it) => it.afgewezen).length} in de toets afgewezen)`)
"""
oud_eind = body.index("return {\n  overzicht:")
body = body[:oud_start] + nieuw_slot + body[oud_eind:]
body = body.replace("  afgewezen: Object.fromEntries(resultaten.map((r) => [r.grondstof, r.afgewezen])),\n  resultaten,\n}",
                    "  afgewezen_in_toets: reserveItems.filter((it) => it.afgewezen).map((it) => ({ id: it.id, toets: it.toets })),\n}")

oud_stap = """    async (it) => {
      const g = it.g
      const brief = await agentR(briefPrompt(it)"""
nieuw_stap = """    async (it) => {
      const g = it.g
      if (!it.toets) {
        const t = await agentR(toetsPrompt(g, { grondstof: g.naam, assen: [it.as] }), { label: `toets:${it.id}`, phase: 'Toets', effort: 'high', schema: TOETS_SCHEMA, ...OPTS })
        const k = t && (t.ketens || []).find((x) => x.keten_id === it.id)
        it.toets = k || { opmerking: 'geen per-keten-oordeel gevonden', algemeen: t && t.algemeen }
        if (k && k.haalbaar === false) {
          log(`${it.id}: toets wijst af — ${(k.problemen || []).join(' | ').slice(0, 200)}`)
          it.afgewezen = true
          return { id: it.id, grondstof: g.sleutel, toets: it.toets, brief: null, afgewezen_in_toets: true }
        }
      }
      const brief = await agentR(briefPrompt(it)"""
assert oud_stap in body
body = body.replace(oud_stap, nieuw_stap)

for a, b in [("M31 golf 9", "M31 golf 10"), ("golf 9 van M31", "golf 10 van M31"), ("M31 · golf 9 (", "M31 · golf 10 ("), ("(M31 golf 9)", "(M31 golf 10)")]:
    body = body.replace(a, b)
body = body.replace(chr(0xFE0F), "")
assert "ontwerpStroom" not in body and "parallel([" not in body
io.open(OUT + "/golf10-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf10-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G10, ensure_ascii=False, indent=1))
print("golf10-script.mjs:", len(body), "tekens;", len(RES), "reserves (", sum(1 for r in RES if not r["toets"]), "zonder toets );", len(G10), "grondstoffen; op schijf niet geregistreerd:", len(op_schijf))
