import io, json, os, sys, glob, re

WF = "C:/Users/lars/.claude/projects/C--automation/e7a9cdcd-806f-4b24-bff9-62ca9d25a4a9/workflows"
SP = "C:/Users/lars/AppData/Local/Temp/claude/C--automation/95c32275-2b02-4437-b2e5-170dcaf9b1c1/scratchpad"
OUT = SP + "/golf7"
REPO = "C:/automation/Projects/General/grondstoffen-atlas"


def laad(p):
    return json.load(io.open(p, encoding="utf-8"))


def lijst(x):
    return json.loads(x) if isinstance(x, str) else x


# ---- bronnen --------------------------------------------------------------------
run6 = laad(WF + "/wf_0c1f784d-7dc.json")
run3 = laad(WF + "/wf_e34d33df-202.json")
run2 = laad(WF + "/wf_7bbf0e2a-fef.json")
g6 = {g["sleutel"]: g for g in lijst(run6["args"]["grondstoffen"])}
g3 = {g["sleutel"]: g for g in lijst(run3["args"]["grondstoffen"])}
g2 = {g["sleutel"]: g for g in lijst(run2["args"]["grondstoffen"])}
bron = {}
for k in ("koper",):
    bron[k] = g2[k]
for k in ("goud", "diamant"):
    bron[k] = g3[k]
for k, g in g6.items():
    bron[k] = g

register = laad(REPO + "/v2/data/stromen-register.json")
bestaand, sleutels = {}, {}
for s in register["stromen"]:
    gs = s["grondstof"]
    bestaand.setdefault(gs, []).append(s["bestand"].replace("stroomroute-", "").replace(".json", ""))
    sleutels.setdefault(gs, []).append(s["sleutel"])
# de pilot heet stroomroute-pilot.json maar is grafiet-balama-vidalia; niet als id gebruiken
bestaand["grafiet"] = ["grafiet-balama-vidalia (bestand stroomroute-pilot.json, tot Casa Grande)" if x == "pilot" else x for x in bestaand["grafiet"]]

# alle eerdere afwijzingen/reserves uit de vorige golven
afg = {}
for f in sorted(glob.glob(WF + "/wf_*.json")):
    d = laad(f)
    res = d["result"]
    if isinstance(res, str):
        try:
            res = json.loads(res)
        except Exception:
            continue
    a = res.get("afgewezen") if isinstance(res, dict) else None
    if isinstance(a, dict):
        for gs, l in a.items():
            for x in l:
                afg.setdefault(gs, [])
                if x not in afg[gs]:
                    afg[gs].append(x)

# de 11 reserve-assen uit golf 6 (haalbaar volgens de toets, niet gebakken)
nietgekozen = laad(OUT + "/golf6-niet-gekozen.json")
reserves = [x for x in nietgekozen if x["haalbaar"] is True]
res_per_g = {}
for r in reserves:
    res_per_g.setdefault(r["g"], []).append(r["id"])

# ---- per grondstof het ontwerp-invoerobject ------------------------------------
VOLGORDE = ["grafiet", "nikkel", "ree", "pgm", "lithium", "zilver", "kolen", "kobalt",
            "uranium", "gas", "olie", "diamant", "goud", "koper"]
MAX = {k: 2 for k in VOLGORDE}
MAX["grafiet"] = 3

EXTRA = {
    "koper": "STAND NA GOLF 6: 15 ketens, vooral Chili/Peru-concentraat naar China, de Copperbelt, Grasberg, Oyu Tolgoi, Aurubis, Olympic Dam, Aktogay, Antamina, Bingham. Nog niet gedekt: Peru zuid (Cerro Verde → Matarani, Toquepala/Cuajone → Ilo), Zambia Kansanshi/Lumwana → Dar es Salaam of Walvis Bay, Mexico (Buenavista/Cananea → Guaymas/Manzanillo), Brazilie (Salobo/Sossego → Itaqui of Vila do Conde), Polen KGHM Glogow, Chili Los Pelambres → Punta Chungo (slurryleiding), Indonesie Batu Hijau, Australie Mount Isa → Townsville, Japan Saganoseki/Zuid-Korea Onsan als smelter-eindpunt, Congo Kamoa-Kakula. Cobre Panama ligt stil sinds eind 2023: niet kiezen.",
    "goud": "STAND NA GOLF 6: 15 ketens (Zuid-Afrika, West-Afrika, Peru, Rusland, Australie, Nevada, Canada, de Zwitserse raffinaderijen, Dubai, India, Istanbul). Nog niet gedekt: Indonesie (Grasberg/Batu Hijau), Papoea-Nieuw-Guinea (Lihir/Porgera → Brisbane of Perth Mint), Ghana Obuasi, Tanzania Geita, Burkina Faso Essakane, Oezbekistan Muruntau/Navoi, Kirgizie Kumtor, China Shandong/Zijin → SGE-kluizen, Brazilie Paracatu, Argentinie Veladero, Suriname, Turkije Copler, Hongkong als kluis, Londen LBMA-kluizen, New York COMEX-kluizen. Minstens de helft met een vlucht; begin bij een mijn waar het kan.",
    "diamant": "STAND NA GOLF 6: 13 ketens (Botswana, Zuid-Afrika, Canada, Namibie, Angola, Zimbabwe, DRC, Lesotho, Rusland naar Mumbai, Surat naar Hongkong, Mumbai naar New York, Gahcho Kue). Nog niet gedekt: Diavik (Rio Tinto) → Antwerpen, Sierra Leone Koidu → Antwerpen, Tanzania Williamson, Zuid-Afrika Cullinan/Finsch, Orapa (Debswana), Antwerpen → Surat of Dubai (herexport rough, post-sanctie), Surat → Tokio/Dubai/Shanghai (gepolijst), Dubai → Mumbai (rough-handel), Israel Ramat Gan (extract ontbreekt: stippel of overslaan), Mirny → Dubai (reserve uit golf 3 werd al afgewezen of ingehaald: controleer).",
}

G = []
for k in VOLGORDE:
    b = dict(bron[k])
    g = {
        "naam": b["naam"], "sleutel": k, "titel": b.get("titel") or k.capitalize(),
        "prefix": b["prefix"], "anker": b["anker"], "kort": b["kort"],
        "v1": b["v1"], "v1brief": b.get("v1brief"), "max": MAX[k],
        "eenheidHint": b["eenheidHint"],
        "bestaand": bestaand[k], "sleutels": sleutels[k],
    }
    afwijs = list(dict.fromkeys(afg.get(k, [])))
    afwijs_txt = []
    for x in afwijs:
        ident = x.split(" ")[0]
        if ident in bestaand[k] or ident in res_per_g.get(k, []):
            continue
        afwijs_txt.append(x.replace("(reserve)", "(eerder als reserve ontworpen, niet gebakken)"))
    pieces = []
    if b.get("afgewezen"):
        pieces.append(str(b["afgewezen"]))
    if afwijs_txt:
        pieces.append("uit eerdere golven: " + ", ".join(afwijs_txt))
    if res_per_g.get(k):
        pieces.append("AL ONTWORPEN EN GETOETST, WORDEN IN DEZE GOLF APART GEBAKKEN (NIET opnieuw voorstellen): " + ", ".join(res_per_g[k]))
    g["afgewezen"] = " · ".join(pieces) if pieces else "geen"
    hint = re.sub(r"Kies (de )?(drie|vier|twee|[0-9]+)[^.]*\.", "", b["hint"])
    if k in EXTRA:
        hint = EXTRA[k] + " " + hint
    hint += f" GOLF 7: er staan al {len(bestaand[k])} ketens op de bol ({', '.join(x.split(k + '-', 1)[-1] for x in bestaand[k])}). Zoek de assen die NOG ONTBREKEN: andere regio's, andere rollen (mijn, verwerker, afnemer, kluis, recycling), andere corridors en modaliteiten. Wat een bestaande keten al dekt komt niet terug. Kies {MAX[k]} over verschillende landen en rollen."
    g["hint"] = hint
    G.append(g)

GBY = {g["sleutel"]: g for g in G}
RES = [{"id": r["id"], "g": r["g"], "as": r["as"], "toets": r["toets"]} for r in reserves]
assert len(RES) == 11, len(RES)

# ---- het script --------------------------------------------------------------------
body = io.open(OUT + "/golf6-script.js", encoding="utf-8").read()

# 1. meta
meta_nieuw = """export const meta = {
  name: 'atlas-m31-golf7-grote-ronde',
  description: 'Grondstoffen Atlas M31 golf 7: 11 reserve-assen uit golf 6 (brief, bake, keuring) plus een nieuwe ontwerpronde over veertien grondstoffen (~29 ketens) — ontwerp, toets, brief, bake, keuring',
  phases: [
    { title: 'Ontwerp', detail: 'één agent per grondstof: nieuwe handelsassen naast de bestaande' },
    { title: 'Toets', detail: 'skeptische haalbaarheids- en juistheidstoets per grondstof' },
    { title: 'Brieven', detail: 'één agent per keten: lichte routebrief met satellietblik' },
    { title: 'Bakken', detail: 'één agent per keten: geometrie, toets, bak-noot' },
    { title: 'Keuring', detail: 'onafhankelijke natoets per keten, alleen mechanisch herstel' },
  ],
}
"""
i = body.index("const REPO")
body = meta_nieuw + "\n" + body[i:]

# 2. scratch + data
body = body.replace("C:/Users/lars/AppData/Local/Temp/claude/C--automation/e7a9cdcd-806f-4b24-bff9-62ca9d25a4a9/scratchpad",
                    SP)
body = body.replace("const GRONDSTOFFEN = typeof args.grondstoffen === 'string' ? JSON.parse(args.grondstoffen) : args.grondstoffen",
                    "const GRONDSTOFFEN = GRONDSTOFFEN_DATA\nconst GBY = Object.fromEntries(GRONDSTOFFEN.map((g) => [g.sleutel, g]))\nconst RESERVES = RESERVES_DATA")

# 3. golf 6 -> golf 7 in teksten
body = body.replace("voor golf 6 van M31 (\"meer stromen op de bol\"). Na golf 5 staan er 158 gemeten ketens over 14 grondstoffen op de bol (v1 had 578 stromen); golf 6 is een grote ronde die elf grondstoffen (nu 9–12 ketens elk) aanvult tot ~13.",
                    "voor golf 7 van M31 (\"meer stromen op de bol\"). Na golf 6 staan er 182 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 7 is een grote ronde die alle veertien grondstoffen (nu 11–15 ketens elk) verder aanvult.")
body = body.replace("(M31 golf 6)", "(M31 golf 7)").replace("M31 golf 6", "M31 golf 7")
for m in re.finditer("golf 6", body):
    print("CTX:", body[max(0, m.start() - 60):m.start() + 60].replace(chr(10), " "))

# 4. regels: register/bundel blijven centraal, id = werkelijk eindpunt
body = body.replace("- JE RAAKT ALLEEN JE EIGEN BESTANDEN:",
                    "- REGISTER EN BUNDEL ZIJN CENTRAAL: wijzig v2/data/stromen-register.json en de bundelbestanden (v2/data/stromen.json, stromen-basis.bin, stromen-fijn-*.bin) NIET en draai NIET 'bash v2/tools/bak_stromen.sh bundel' of bundel-check; jouw stroom staat pas op de bol nadat ik hem centraal registreer.\n- HET STROOM-ID NOEMT HET WERKELIJKE EINDPUNT van de lijn (eerdere golven hadden ids die niet bij het eindpunt pasten, zoals nikkel-cerromatoso-cartagena dat in Ningbo eindigt). Valt het eindpunt tijdens het onderzoek anders uit dan het id belooft, zet dan het echte eindpunt in de titel en in afwijkingen_van_ontwerp; het id zelf blijft staan.\n- JE RAAKT ALLEEN JE EIGEN BESTANDEN:")

# 5. registerregel in de bake-prompt
oud = "Lever het eindrapport (schema), met registerregel exact: { sleutel: \"${it.g.kort}-<xy>\", bestand: \"stroomroute-${it.id}.json\", grondstof: \"${it.g.sleutel}\", aan: true } — xy = de eerste letter van het <van>- en het <naar>-deel van het stroom-id."
assert oud in body
nieuw = "Lever het eindrapport (schema), met registerregel exact: { sleutel: \"${it.g.kort}-<xy>\", bestand: \"stroomroute-${it.id}.json\", grondstof: \"${it.g.sleutel}\", label: \"<Van> → <Naar>\", aan: true, noot: \"M31 · golf 7 (${DATUM}): <één zin over de keten>\" } — xy = de eerste letter van het <van>- en het <naar>-deel van het stroom-id. BEZETTE SLEUTELS van deze grondstof (kies een vrije; botst xy, neem dan een derde letter): ${it.g.sleutels.join(', ')}."
body = body.replace(oud, nieuw)

# 6. onderste deel: reserves + ontwerpstroom naast elkaar
j = body.index("const resultaten = await pipeline(GRONDSTOFFEN,")
bodem = """function ketenPipeline(items) {
  return pipeline(items,
    async (it) => {
      const g = it.g
      const brief = await agent(briefPrompt(it), { label: `brief:${it.id}`, phase: 'Brieven', effort: 'high', schema: BRIEF_SCHEMA, ...OPTS })
      if (!brief || brief.afgebroken) log(`${it.id}: brief ${brief ? 'AFGEBROKEN — ' + (brief.reden_afgebroken || '') : 'ontbreekt'}`)
      return { id: it.id, grondstof: g.sleutel, toets: it.toets, brief }
    },
    async (r, it) => {
      if (!r || !r.brief || r.brief.afgebroken) return r
      const bake = await agent(bakePrompt(it, r.brief), { label: `bake:${it.id}`, phase: 'Bakken', effort: 'high', schema: BAKE_SCHEMA, ...OPTS })
      log(`${it.id}: ${bake && bake.gebakken ? 'gebakken ' + (bake.totaal_km || '?') + ' km' : 'NIET gebakken'}`)
      return { ...r, bake }
    },
    async (r, it) => {
      if (!r || !r.bake || !r.bake.gebakken) return r
      const keuring = await agent(keuringPrompt(it, r.bake), { label: `keuring:${it.id}`, phase: 'Keuring', effort: 'medium', schema: KEURING_SCHEMA, ...OPTS })
      log(`${it.id}: keuring ${keuring ? keuring.oordeel + (keuring.herbakken ? ' (hersteld)' : '') : 'ontbreekt'}`)
      return { ...r, keuring }
    },
  )
}

const ontwerpStroom = () => pipeline(GRONDSTOFFEN,
  (g) => agent(ontwerpPrompt(g), { label: `ontwerp:${g.sleutel}`, phase: 'Ontwerp', effort: 'high', schema: ONTWERP_SCHEMA, ...OPTS }),
  async (ontwerp, g) => {
    if (!ontwerp) { log(`ontwerp ${g.sleutel} mislukt — grondstof overgeslagen`); return null }
    const toets = await agent(toetsPrompt(g, ontwerp), { label: `toets:${g.sleutel}`, phase: 'Toets', effort: 'high', schema: TOETS_SCHEMA, ...OPTS })
    return { ontwerp, toets }
  },
  async (ot, g) => {
    if (!ot) return null
    const { ontwerp, toets } = ot
    const oordeel = new Map(((toets && toets.ketens) || []).map((k) => [k.keten_id, k]))
    const assen = [...(ontwerp.assen || [])].sort((a, b) => (a.prioriteit || 99) - (b.prioriteit || 99))
    const bestaand = new Set(g.bestaand)
    const gereserveerd = new Set(RESERVES.map((r) => r.id))
    const gekozen = assen.filter((a) => { const t = oordeel.get(a.keten_id); return !bestaand.has(a.keten_id) && !gereserveerd.has(a.keten_id) && (!t || t.haalbaar !== false) }).slice(0, g.max)
    const afgewezen = assen.filter((a) => !gekozen.includes(a)).map((a) => `${a.keten_id}${oordeel.get(a.keten_id) && oordeel.get(a.keten_id).haalbaar === false ? ' (afgewezen)' : ' (reserve)'}`)
    log(`${g.sleutel}: ${gekozen.length}/${g.max} ketens door — ${gekozen.map((a) => a.keten_id).join(', ')}${afgewezen.length ? ' · niet: ' + afgewezen.join(', ') : ''}${toets ? '' : ' · LET OP: toets ontbreekt'}`)
    const items = gekozen.map((a) => ({ id: a.keten_id, as: a, toets: oordeel.get(a.keten_id) || { opmerking: 'geen per-keten-oordeel gevonden', algemeen: toets && toets.algemeen }, g }))
    const ketens = await ketenPipeline(items)
    return { grondstof: g.sleutel, ontwerp, toets, afgewezen, ketens: ketens.filter(Boolean) }
  },
)

const reserveStroom = () => ketenPipeline(RESERVES.map((r) => ({ id: r.id, as: r.as, toets: r.toets, g: GBY[r.g] })))

const [ontwerpRes, reserveRes] = await parallel([ontwerpStroom, reserveStroom])
const resultaten = (ontwerpRes || []).filter(Boolean)
const reserveKetens = (reserveRes || []).filter(Boolean)

const alle = [...resultaten.flatMap((r) => r.ketens), ...reserveKetens]
const ok = alle.filter((k) => k.bake && k.bake.gebakken)
log(`klaar: ${ok.length}/${alle.length} gebakken, ${ok.filter((k) => !k.keuring || k.keuring.oordeel !== 'niet-registreren').length} registreerbaar (waarvan ${reserveKetens.filter((k) => k.bake && k.bake.gebakken).length} reserve-assen), over ${resultaten.length}/${GRONDSTOFFEN.length} grondstoffen`)
return {
  overzicht: alle.map((k) => ({
    id: k.id, grondstof: k.grondstof, reserve: reserveKetens.includes(k),
    afgebroken: !!(k.brief && k.brief.afgebroken), reden: k.brief && k.brief.afgebroken ? k.brief.reden_afgebroken : null,
    gebakken: !!(k.bake && k.bake.gebakken),
    titel: k.bake && k.bake.titel,
    registerregel: k.bake && k.bake.registerregel,
    totaal_km: k.keuring && k.keuring.totaal_km_na ? k.keuring.totaal_km_na : k.bake && k.bake.totaal_km,
    naden_max_km: k.keuring && k.keuring.naden_max_km_na != null ? k.keuring.naden_max_km_na : k.bake && k.bake.naden_max_km,
    bestand_kb: k.keuring && k.keuring.bestand_kb ? k.keuring.bestand_kb : k.bake && k.bake.bestand_kb,
    keuring: k.keuring && k.keuring.oordeel, keuring_reden: k.keuring && k.keuring.reden,
    omweg: k.keuring && k.keuring.omweg_verdenkingen, stippel_pct: k.keuring && k.keuring.stippel_aandeel_pct,
    hersteld: k.keuring && k.keuring.hersteld, problemen: k.bake && k.bake.problemen,
  })),
  afgewezen: Object.fromEntries(resultaten.map((r) => [r.grondstof, r.afgewezen])),
  resultaten,
}
"""
body = body[:j] + bodem

# 7. data bovenaan inbedden
data = "const GRONDSTOFFEN_DATA = " + json.dumps(G, ensure_ascii=False) + "\nconst RESERVES_DATA = " + json.dumps(RES, ensure_ascii=False) + "\n"
k = body.index("const REPO")
body = body[:k] + data + "\n" + body[k:]

body = body.replace(chr(0xFE0F), "")
io.open(OUT + "/golf7-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf7-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G, ensure_ascii=False, indent=1))
print("script", len(body), "tekens;", len(G), "grondstoffen;", len(RES), "reserves; max totaal", sum(MAX.values()))
for g in G:
    print(g["sleutel"], "max", g["max"], "bestaand", len(g["bestaand"]), "| afgewezen:", g["afgewezen"][:160])
