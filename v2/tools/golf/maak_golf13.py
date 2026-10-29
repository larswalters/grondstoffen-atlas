"""Golf 13: bouwt golf13-script.mjs uit golf11-script.mjs (de laatste volledige ontwerpronde) — opnieuw een ONTWERPRONDE zonder
reserve-assen (de 11 reserves van golf 11 zijn in golf 12 gebakken): per grondstof ontwerp (2 nieuwe ketens + 2 reserves voor golf 14),
toets, en per gekozen keten brief -> bake -> keuring.
Invoer: golf11-script.mjs en golf11-resultaat.json (uit deze map; de in de toets afgewezen assen van golf 11 met hun eerste reden),
het register (bestaande ketens + bezette sleutels per grondstof). De kobalt-hint is herschreven (golf 11: vier van vier afgewezen).
Uitvoer: golf13-script.mjs (LF, zonder U+FE0F) en golf13-grondstoffen.json in de uitvoermap.
Gebruik: python maak_golf13.py [<uitvoermap>] [<scratchpad van de sessie die de workflow start>]
"""
import glob, io, json, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else HIER
SCRATCH = sys.argv[2] if len(sys.argv) > 2 else OUT
REPO = "C:/automation/Projects/General/grondstoffen-atlas"
MAXP = 2
GOLF, VORIG = 13, 11

src = io.open(HIER + "/golf11-script.mjs", encoding="utf-8", newline="").read().replace("\r\n", "\n")
res11 = json.load(io.open(HIER + "/golf11-resultaat.json", encoding="utf-8"))
reg = json.load(io.open(REPO + "/v2/data/stromen-register.json", encoding="utf-8"))

G11 = None
for l in src.split("\n"):
    if l.startswith("const GRONDSTOFFEN_DATA = "):
        G11 = json.loads(l[len("const GRONDSTOFFEN_DATA = "):])
assert G11, "GRONDSTOFFEN_DATA niet gevonden in golf11-script.mjs"

bestaand, sleutels = {}, {}
for s in reg["stromen"]:
    bestaand.setdefault(s["grondstof"], []).append(s["bestand"].replace("stroomroute-", "").replace(".json", ""))
    sleutels.setdefault(s["grondstof"], []).append(s["sleutel"])
bestaand["grafiet"] = ["grafiet-balama-vidalia (bestand stroomroute-pilot.json, tot Casa Grande)" if x == "pilot" else x for x in bestaand["grafiet"]]
bekend = {s["bestand"] for s in reg["stromen"]} | {u["bestand"] for u in reg["uitgesloten"]}
op_schijf = sorted(os.path.basename(p)[len("stroomroute-"):-5] for p in glob.glob(REPO + "/v2/data/stroomroute-*.json") if os.path.basename(p) not in bekend)

# Golf 11: alles wat de toets afwees (haalbaar false) met de eerste reden. De reserves (haalbaar, niet gekozen) zijn in golf 12 gebakken
# en staan in het register; alles wat gekozen was is in golf 11 gebakken.
afg11 = {}
nog_niet = []
for r in res11["resultaten"]:
    g = r["grondstof"]
    for k in (r.get("toets") or {}).get("ketens", []):
        kid = k.get("keten_id")
        if not kid:
            continue
        if k.get("haalbaar") is False:
            reden = re.sub(r"\s+", " ", (k.get("problemen") or [""])[0]).strip()[:90]
            afg11.setdefault(g, []).append(f"{kid} (golf 11: {reden})" if reden else kid)
        elif f"stroomroute-{kid}.json" not in bekend and kid not in op_schijf:
            nog_niet.append(kid)
assert not nog_niet, "golf 11-assen die haalbaar waren maar niet geregistreerd zijn: " + ", ".join(nog_niet)

KOBALT_HINT = (
    "ANDERE INVALSHOEK DAN GOLF 11. In golf 11 vielen alle vier kobalt-assen in de toets af, steeds om dezelfde reden: de bestemming "
    "(een cathode-/celfabriek of een Europese zusterfabriek) had geen bilaterale bron en meestal geen site-anker; Kokkola -> Olen was bovendien "
    "inhoudelijk achterhaald (de kobaltraffinage is van Olen naar Kokkola verhuisd). Herhaal die klasse NIET: geen verlenging van Niihama, "
    "Kokkola, Nikkelverk of een HPAL naar een batterij- of cathodefabriek 'omdat die klant is', geen opstarters zonder draaiende plant (Pomalaa), "
    "geen as waarvan de bestemming alleen 'aannemelijk' is. Kies assen waarvan BEIDE uiteinden een gedocumenteerde, lokaliseerbare industriele site "
    "zijn (kobalt-sitelaag, OSM-object, registerpunt of een anker in een bestaande routebrief) EN waarvoor een bron de leverrelatie of de exportroute noemt. "
    "Kansrijke klassen: (a) een DRC-/Zambia-producent die nog niet op de bol staat (Deziwa/CNMC, Sicomines, Ruashi/Jinchuan, Chemaf Mutoshi, "
    "Boss Mining/ERG, Chambishi in Zambia) naar een exporthaven via een corridor die kobalt nog niet gebruikt: Beira (bestaat al als koper-anker), "
    "Durban (Noord-Zuid-corridor, bestaat al voor koper), TAZARA/Dar es Salaam (bestaat al voor Kisanfu) -- de keten mag bij de haven stoppen als een "
    "douane-, bedrijfs- of havenbron de export van die producent over die haven noemt; (b) de IMPORT-kant in China: hydroxide van een benoemde "
    "DRC-plant via Tianjin, Qingdao of Shanghai naar een raffinaderij buiten Quzhou/Tongxiang/Ganzhou (Jinchuan Lanzhou, GEM Jingmen, Huayou Tianjin, "
    "Hanrui Jiangsu, Brunp Foshan), alleen met een bron die die raffinaderij als afnemer van die plant of die producent noemt; (c) Indonesisch MHP van een "
    "DRAAIENDE HPAL (Huayue/QMB op IMIP, Huafei op IWIP) naar een benoemde afnemer buiten Quzhou/Tongxiang (GEM Jingmen, Ecopro of Posco in Korea) met bron; "
    "(d) Terrafame Sotkamo kobaltsulfaat naar een benoemde afnemer, maar NIET Harjavalta (dat is de nikkellijn, golf 9 afgewezen) en alleen met bron. "
    "Controleer VOOR je een as opschrijft dat beide site-ankers bestaan (ls v2/build-cache/satcheck/, de sitelaag, de routebrieven) en noem per anker de bron. "
    "Liever twee korte, goed gebronde assen dan vier mooie verhalen die de toets afwijst. Let op het exportverbod van DR Congo (2025) en de quota daarna: "
    "noem de actuele status met bron."
)

totaal = len(reg["stromen"])
G13 = []
for g in G11:
    g = dict(g)
    k = g["sleutel"]
    g["max"] = MAXP
    g["bestaand"] = list(dict.fromkeys(bestaand[k] + [x for x in op_schijf if x.startswith(k + "-")]))
    g["sleutels"] = sleutels[k]
    hint = re.sub(r" GOLF 11: er staan al.*$", "", g["hint"], flags=re.S).strip()
    if k == "kobalt":
        hint = KOBALT_HINT
    g["hint"] = (hint + f" GOLF 13: er staan al {len(g['bestaand'])} ketens op de bol ({', '.join(x.split(k + '-', 1)[-1] for x in g['bestaand'])}). "
                 f"Dit is de derde ontwerpronde op rij (golf 11 en 12 brachten samen 37 ketens): kies de {MAXP} ketens die het meeste nieuw verhaal "
                 "toevoegen (andere regio, rol of corridor dan wat er al ligt; ook de tweede en derde speler in een land; ook de import- of verwerkingskant "
                 f"als de exportkant al ligt) en die je met bronnen kunt onderbouwen, plus 2 reserve-assen voor golf 14. Kies {MAXP}.")
    afw = [x.strip() for x in re.split(r"\s·\s", g["afgewezen"]) if x.strip() and "APART GEBAKKEN" not in x and x.strip() != "geen"]
    tekst = " · ".join(afw)
    if afg11.get(k):
        tekst += (" · " if tekst else "") + "golf 11 afgewezen: " + ", ".join(afg11[k])
    g["afgewezen"] = tekst or "geen"
    G13.append(g)

meta = """export const meta = {
  name: 'atlas-m31-golf13-ontwerpronde',
  description: 'Grondstoffen Atlas M31 golf 13: nieuwe ontwerpronde, twee nieuwe ketens per grondstof (ontwerp, toets, brief, bake, keuring); kobalt met herschreven hint; geen reserve-assen',
  phases: [
    { title: 'Ontwerp', detail: 'een agent per grondstof: de twee meest waardevolle nieuwe assen plus twee reserves voor golf 14' },
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
        lines[n] = "const GRONDSTOFFEN_DATA = " + json.dumps(G13, ensure_ascii=True)
    elif l.startswith("const RESERVES_DATA = "):
        lines[n] = "const RESERVES_DATA = []"
    elif l.startswith("const SCRATCH = "):
        lines[n] = "const SCRATCH = " + json.dumps(SCRATCH)
body = "\n".join(lines)

oud = ("Na golf 10 staan er 315 gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 11 is een nieuwe "
       "ontwerpronde: 2 nieuwe ketens per grondstof, plus reserve-assen voor een latere golf.")
assert oud in body, "openingszin van het ontwerp niet gevonden"
body = body.replace(oud, f"Na golf 12 staan er {totaal} gemeten ketens over 14 grondstoffen (v1 had 578 stromen); golf 13 is opnieuw een "
                         f"ontwerpronde: {MAXP} nieuwe ketens per grondstof, plus reserve-assen voor golf 14.")
assert "const ontwerpRes = await ontwerpStroom()\nconst reserveRes = []" in body, "golf 11-orkestratie (alleen ontwerpStroom) niet gevonden"
for a, b in [("M31 golf 11", "M31 golf 13"), ("golf 11 van M31", "golf 13 van M31"), ("M31 · golf 11 (", "M31 · golf 13 ("), ("(M31 golf 11)", "(M31 golf 13)")]:
    body = body.replace(a, b)
rest = body.replace(json.dumps(KOBALT_HINT, ensure_ascii=True)[1:-1], "")
rest = rest.replace("golf 11 afgewezen", "").replace("golf 11:", "").replace("GOLF 11", "").replace("golf 11 en 12", "")
assert "golf 11" not in rest, "losse verwijzing naar golf 11 blijft staan"
body = body.replace(chr(0xFE0F), "")
io.open(OUT + "/golf13-script.mjs", "w", encoding="utf-8", newline=chr(10)).write(body)
io.open(OUT + "/golf13-grondstoffen.json", "w", encoding="utf-8").write(json.dumps(G13, ensure_ascii=False, indent=1))
print("golf13-script.mjs:", len(body), "tekens;", len(G13), "grondstoffen; max totaal", MAXP * len(G13), "; register", totaal,
      "; golf 11 afgewezen", sum(len(v) for v in afg11.values()), "; op schijf niet geregistreerd:", len(op_schijf))
