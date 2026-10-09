"""Golf 8: bouwt golf8-script.mjs uit golf7-script.mjs (zelfde prompts) met nieuwe invoer en drie verbeteringen:
  1. agentR(): één agent-aanroep met tot 3 pogingen en een korte pauze (netwerkuitval, ongeldige JSON);
  2. slots met literale paden (de veiligheidscheck weigert rm -rf met een variabel pad);
  3. wegbenen via v2/tools/wegscan_puur.py (pyosmium is geblokkeerd, Overpass valt uit).

Invoer: golf7-grondstoffen.json (de 14 grondstof-objecten van golf 7), golf8-reserves.json (reserve-assen met toets),
het register en de afwijzingen uit de runbestanden van golf 7. Uitvoer: golf8-script.mjs (LF, zonder U+FE0F).
"""
import io, json, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
REPO = "C:/automation/Projects/General/grondstoffen-atlas"

src = io.open(OUT + "/golf7-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
slots_bron = io.open(OUT + "/golf7c-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
G = json.load(io.open(OUT + "/golf7-grondstoffen.json", encoding="utf-8"))
rs = json.load(io.open(OUT + "/golf8-reserves.json", encoding="utf-8"))
reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))

bestaand, sleutels = {}, {}
for s in reg["stromen"]:
    bestaand.setdefault(s["grondstof"], []).append(s["bestand"].replace("stroomroute-", "").replace(".json", ""))
    sleutels.setdefault(s["grondstof"], []).append(s["sleutel"])
bestaand["grafiet"] = ["grafiet-balama-vidalia (bestand stroomroute-pilot.json, tot Casa Grande)" if x == "pilot" else x for x in bestaand["grafiet"]]

RES = [{"id": r["id"], "g": r["g"], "as": r["as"], "toets": r["toets"]} for r in rs["reserves"]]
res_per_g, onget_per_g = {}, {}
for r in RES:
    res_per_g.setdefault(r["g"], []).append(r["id"])
for o in rs["ongetoetst"]:
    onget_per_g.setdefault(o["g"], []).append(o["id"])

AFGEWEZEN_G7 = {
    "grafiet": ["grafiet-qingdao-kendal", "grafiet-mahenge-sejong", "grafiet-seadrift-calais"],
    "nikkel": ["nikkel-eagle-sudbury"], "lithium": ["lithium-albemarlesalar-antofagasta"],
    "zilver": ["zilver-glogow-londen", "zilver-londen-mumbai"], "kobalt": ["kobalt-ramu-basamuk"],
    "goud": ["goud-muruntau-navoi"], "ree": ["ree-kuantan-sanmarcos", "ree-larochelle-ellesmereport"],
}

MAXP = 3
G8 = []
for g in G:
    g = dict(g)
    k = g["sleutel"]
    g["max"] = MAXP
    g["bestaand"] = bestaand[k]
    g["sleutels"] = sleutels[k]
    # oude hint schoonmaken: de golf-7-staartzin en de verouderde STAND-NA-GOLF-6-voorzin eraf
    hint = g["hint"]
    hint = re.sub(r"STAND NA GOLF 6:.*?(?=Gaten t\.o\.v\. v1:|Goud reist|De scherpste|$)", "", hint, flags=re.S)
    hint = re.sub(r" GOLF 7: er staan al.*$", "", hint, flags=re.S)
    hint = hint.strip()
    nieuw = (f" GOLF 8: er staan al {len(bestaand[k])} ketens op de bol ({', '.join(x.split(k + '-', 1)[-1] for x in bestaand[k])}). "
             "De voor de hand liggende assen zijn gebouwd; zoek wat NOG ONTBREEKT: andere regio's, andere rollen (mijn, verwerker, afnemer, kluis, "
             "recycling), andere corridors en modaliteiten, en afnemers die nog niet op de bol staan. Wat een bestaande keten dekt komt niet terug. "
             f"Kies {MAXP} over verschillende landen en rollen.")
    if onget_per_g.get(k):
        nieuw += (" EERDER ONTWORPEN, MAAR NOOIT GETOETST (golf 7: de toets viel uit): " + ", ".join(onget_per_g[k]) +
                  ". Je mag ze overnemen of verbeteren; de toets beoordeelt ze nu alsnog.")
    g["hint"] = hint + nieuw
    afw = [x.strip() for x in re.split(r"\s·\s", g["afgewezen"]) if x.strip() and "APART GEBAKKEN" not in x]
    tekst = " · ".join(afw)
    extra = ", ".join(AFGEWEZEN_G7.get(k, []))
    if extra:
        tekst += (" · " if tekst else "") + "golf 7 afgewezen: " + extra
    if res_per_g.get(k):
        tekst += (" · " if tekst else "") + "AL ONTWORPEN EN GETOETST, WORDEN IN DEZE GOLF APART GEBAKKEN (NIET opnieuw voorstellen): " + ", ".join(res_per_g[k])
    g["afgewezen"] = tekst or "geen"
    G8.append(g)
GBY = {g["sleutel"]: g for g in G8}

body = src
# 1. meta
i = body.index("const GRONDSTOFFEN_DATA")
meta = """export const meta = {
  name: 'atlas-m31-golf8-grote-ronde',
  description: 'Grondstoffen Atlas M31 golf 8: 12 reserve-assen uit golf 7 (brief, bake, keuring) plus een nieuwe ontwerpronde over veertien grondstoffen (~42 ketens) — ontwerp, toets, brief, bake, keuring; met retries, literale slots en een pure-Python wegscan',
  phases: [
    { title: 'Ontwerp', detail: 'één agent per grondstof: nieuwe handelsassen naast de bestaande' },
    { title: 'Toets', detail: 'skeptische haalbaarheids- en juistheidstoets per grondstof' },
    { title: 'Brieven', detail: 'één agent per keten: lichte routebrief met satellietblik' },
    { title: 'Bakken', detail: 'één agent per keten: geometrie, toets, bak-noot' },
    { title: 'Keuring', detail: 'onafhankelijke natoets per keten, alleen mechanisch herstel' },
  ],
}
"""
body = meta + "\n" + body[i:]

# 2. data
lines = body.split("\n")
for n, l in enumerate(lines):
    if l.startswith("const GRONDSTOFFEN_ALLE = "):
        lines[n] = "const GRONDSTOFFEN_ALLE = " + json.dumps(G8, ensure_ascii=True)
    elif l.startswith("const GRONDSTOFFEN_DATA = "):
        lines[n] = "const GRONDSTOFFEN_DATA = " + json.dumps(G8, ensure_ascii=True)
    elif l.startswith("const RESERVES_DATA = "):
        lines[n] = "const RESERVES_DATA = " + json.dumps(RES, ensure_ascii=True)
body = "\n".join(lines)

# 3. golf 7 -> golf 8 in teksten
body = body.replace("voor golf 7 van M31", "voor golf 8 van M31")
body = body.replace("Na golf 6 staan er 182 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 7 is een grote ronde die alle veertien grondstoffen (nu 11–15 ketens elk) verder aanvult.",
                    "Na golf 7 staan er 221 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 8 is een grote ronde die alle veertien grondstoffen (nu 13–17 ketens elk) verder aanvult.")
body = body.replace("M31 · golf 7 (", "M31 · golf 8 (").replace("(M31 golf 7)", "(M31 golf 8)").replace("M31 golf 7", "M31 golf 8")
assert "golf 7 is een grote" not in body

# 4. REGELS: webbudget zonder firecrawl, CRLF, FeatureCollection
oud = "en via WebFetch of firecrawl_scrape op concrete url's"
assert oud in body
body = body.replace(oud, "en via WebFetch op concrete url's (firecrawl_scrape heeft GEEN credits meer en faalt: gebruik het niet)")
oud = "- REGISTER EN BUNDEL ZIJN CENTRAAL:"
assert oud in body
body = body.replace(oud, "- BESTANDSFORMAAT: v2/tools/bak_stromen.sh is een LF-bestand. Schrijf je functie met LF-regeleinden (geen CRLF; controleer na je edit met een korte python-regel die b'\\r\\n' in het bestand telt: moet 0 zijn). Een --been-geojson (leiding, lucht, vooraf gestikt) moet een FeatureCollection zijn, geen kale Feature. Houd de tekstvelden in je eindrapport kort (onder ~400 tekens per veld) en vermijd backslashes in vrije tekst: een ongeldige JSON laat je rapport falen.\n- REGISTER EN BUNDEL ZIJN CENTRAAL:", 1)

# 5. slots met literale paden (uit het 7c-script)
j = body.index("const SLOTS = `")
k = body.index("`", j + len("const SLOTS = `")) + 1
js = slots_bron.index("const SLOTS = `")
ks = slots_bron.index("`", js + len("const SLOTS = `")) + 1
slots_nieuw = slots_bron[js:ks].replace("wegscan: een weg-slot (plus een reus-slot bij een reus-extract), dan het scancommando, dan vrijgeven.",
                                          "wegscan: een weg-slot (plus een reus-slot bij een reus-extract), dan python v2/tools/wegscan_puur.py --profiel <sleutel>, dan vrijgeven.")
body = body[:j] + slots_nieuw + body[k:]

# 6. wegtool in de bake-prompt
oud = "scan via het weg-slot (en het reus-slot bij een reus-extract)."
assert oud in body
body = body.replace(oud, "scan met python v2/tools/wegscan_puur.py --profiel <sleutel> (single-threaded; neem vooraf een weg-slot en bij een reus-extract ook een reus-slot). pyosmium is op deze machine geblokkeerd en Overpass valt uit: gebruik NIET maak_stroombeen_weg.py rechtstreeks, ook niet met --bron geofabrik of overpass. wegscan_puur.py leest het pbf-bestand zelf en roept dezelfde logica aan; een tweede run met hetzelfde profiel is meteen klaar (cache). Bij een grote extract: Bash-timeout 600000 ms, of op de achtergrond met een logbestand in v2/build-cache/ais/graaf/ en wachten met een until-lus.")
oud = "Draai alle commando's vanuit de repo-root"
assert oud in body

# 7. agentR
agentr = r"""
const pauze = (ms) => (typeof setTimeout === 'function' ? new Promise((r) => setTimeout(r, ms)) : Promise.resolve())
async function agentR(prompt, opts) {
  let fout = null
  for (let poging = 0; poging < 3; poging++) {
    try {
      const p = poging === 0 ? prompt : prompt + `\n\nLET OP (poging ${poging + 1}): de vorige poging viel uit (netwerk of ongeldige uitvoer). Houd elk tekstveld in je eindrapport onder ~400 tekens, gebruik geen backslashes in vrije tekst en lever geldige JSON. Een eerder begonnen werk op schijf mag je hergebruiken (kijk eerst wat er al staat).`
      const r = await agent(p, opts)
      if (r) return r
      log(`${opts.label}: leeg resultaat bij poging ${poging + 1}`)
    } catch (e) {
      fout = e
      log(`${opts.label}: fout bij poging ${poging + 1}: ${String((e && e.message) || e).slice(0, 160)}`)
    }
    if (poging < 2) await pauze(60000)
  }
  if (fout) throw fout
  return null
}
"""
anker = "function ketenPipeline(items) {"
assert anker in body
# EERST de aanroepen omzetten, DAN agentR zelf invoegen (agentR roept de echte agent() aan)
n_voor = body.count("await agent(") + body.count("=> agent(")
body = body.replace("await agent(", "await agentR(").replace("=> agent(", "=> agentR(")
body = body.replace(anker, agentr + "\n" + anker, 1)
assert "const r = await agent(p, opts)" in body, "agentR roept zichzelf aan"
print("agent-aanroepen omgezet naar agentR:", n_voor)

# 8. de achteraf-stroom van 7b zit niet in golf7-script; reserve-stroom en ontwerpstroom blijven
body = body.replace(chr(0xFE0F), "")
io.open(OUT + "/golf8-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf8-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G8, ensure_ascii=False, indent=1))
print("golf8-script.mjs:", len(body), "tekens;", len(G8), "grondstoffen; max totaal", MAXP * len(G8), "; reserves", len(RES))
for g in G8:
    print(f"  {g['sleutel']:9} bestaand {len(g['bestaand']):2}  reserves {res_per_g.get(g['sleutel'], [])}  ongetoetst {onget_per_g.get(g['sleutel'], [])}")
