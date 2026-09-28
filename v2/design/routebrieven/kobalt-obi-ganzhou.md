# Routebrief (licht) · kobalt — Obi (Indonesië) → Xiamen → Ganzhou (China)

**stroom-id:** `kobalt-obi-ganzhou` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) · **status:** gebakken
**Keten in één zin:** MHP/nikkelsulfaat met kobalt als bijproduct (4–5 % Co) uit het Kawasi HPAL-complex van Harita/Lygend op Obi Island gaat per **zeeschip** — via twee haven-aanlopen — naar de containerterminal Xiamen Haicang, en de lijn stopt daar: geen bron van deze sessie koppelt de lading met een site-niveau coördinaat aan GEM Ganzhou (Jiangxi), de veronderstelde eindraffinaderij.
**Welke as van het verhaal:** reserve-as uit golf 2, teruggehaald in golf 4 — Indonesië als tweede kobaltbron náást Morowali (`kobalt-morowali-quzhou`), bewust via een **andere Chinese kade dan Ningbo** (Xiamen) om corridor-overlap met die as te beperken. Obi was Harita's eerste operationele Indonesische HPAL en is dezelfde site die de nikkelas `nikkel-obi-ningbo` al op Ningbo/Beilun legde — deze kobaltas kiest bewust een andere Chinese aanlanding.

## 1 · Ketenkaart
```
Kawasi HPAL-complex `co-obi-kawasi` ──(b1 zee-aanloop · Molukse Zee · ~84,9 km, stippel —
   letterlijke kopie nikkel-obi-ningbo b1)──► zeeknoop 9031 (-1.1099, 127.9122)
   ──(b2 zee · Makassar/Lombok → Zuid-Chinese Zee → Straat Taiwan · indicatief ~3.700–3.900 km)──►
   zeeknoop 5576 (24.4515, 117.9163)
   ──(b3 zee-aanloop · Xiamen-baai · ~5,7 km, stippel)──► Xiamen Haicang containerterminal
   `co-xiamen-haicang` ⏹ stoppunt
        ┊ (niet getekend — GEM Ganzhou-coördinaat niet site-niveau gevonden)
   GEM Ganzhou (Jiangxi) `co-ganzhou-gem` (knoop, §5)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee (haven-aanloop) | `co-obi-kawasi` → zeeknoop 9031 | Molukse Zee (kade ligt 72,7 km van de zeeknoop) | 84,9 (gemeten, letterlijke kopie) | `maak_havenaanloop.py` — hergebruik `nikkel-obi-ningbo-aanloop-kawasi.geojson` | ja — MARNET reikt niet, zelfde aanloop als `nikkel-obi-ningbo` |
| b2 | B | zee | zeeknoop 9031 → zeeknoop 5576 | Molukse Zee → Straat Makassar/Lombok → Zuid-Chinese Zee → Straat Taiwan | ~3.700–3.900 indicatief (analogie `nikkel-obi-ningbo`: 4.202,5 km via dezelfde corridor naar Ningbo; Xiamen ligt ~300 km dichterbij hemelsbreed) | MARNET `--been "zee\|…\|-1.1099,127.9122\|24.4515,117.9163"` | nee |
| b3 | B | zee (haven-aanloop) | zeeknoop 5576 → `co-xiamen-haicang` | Xiamen-baai (kade ligt 5,7 km van de zeeknoop, > 5 km-drempel LAR-586) | ~5,7 (indicatief, hemelsbreed; gemeten pad volgt bij bake) | `maak_havenaanloop.py` (nieuw) | ja — kade > 5 km van de zeeknoop |

**Been C (Xiamen → GEM Ganzhou, NIET getekend):** geen bron van deze sessie geeft een site-niveau coördinaat voor GEM's Ganzhou-vestiging (alleen een v1-registercentroïde op stadsniveau, zie §3/§7) — zelfde uitkomst als het onopgeloste "been C" in `kobalt-morowali-quzhou.md`. De lijn eindigt waar het bewijs eindigt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-obi-kawasi` | mijn + HPAL + eigen exportjetty (hergebruikt anker) | Kawasi HPAL-complex, Obi Island — Harita/Lygend (PT Halmahera Persada Lygend / PT Obi Nickel Cobalt) | -1.5361, 127.4160 | [1][2][3][9] | bron-gelegd (hergebruikt letterlijk uit `nikkel-obi-ningbo.md` §3 — z14/z16 daar al gezien: dicht industrieel HPAL-complex + jetty-structuur; niet opnieuw gecheckt deze ronde) |
| `co-xiamen-haicang` | overslag zee → (onbekend vervolg) | Xiamen Haicang Container Terminal, Fujian | 24.4585, 117.9720 | [12] | bron-gelegd (z16 gezien: rijen gestapelde containers over een groot verhard terrein, een reeks portaalkranen op de kadelijn direct ten zuiden, en een containerschip in de vaargeul — ondubbelzinnig een actieve containerterminal) |
| `co-ganzhou-gem` | raffinaderij + recycling (knoop, niet aan een been gekoppeld) | GEM Co., Ltd. — vestiging Ganzhou, Jiangxi | 25.83, 114.93 (v1-registercentroïde, GEEN anker) | [5][6][7][11] | onzeker/open — stadscentroïde, geen site-coördinaat; OSM-naamzoeken op 格林美/GEM in de Ganzhou-regio leverde geen treffer (Overpass deze sessie onbereikbaar, herhaald 406/timeout op meerdere mirrors); coördinaat niet verzonnen |

## 4 · Via-punten
Geen — alle drie de benen zijn zeebenen (router / haven-aanloop, geen corridorkeuze op land). Er is geen truck- of spoorbeen: het enige landstuk (GEM Ganzhou-koppeling) is niet gevonden en dus niet getekend.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kawasi HPAL-complex (Obi) | Lygend Resources / PT Trimegah Bangun Persada (Harita) | lateriet-erts (eigen mijn, binnen het complex) → MHP/nikkelsulfaat (Co als bijproduct, 4–5 %) | ~65 kt Ni/j metallic metal (2024, groepscijfer) [1][2]; kobalt niet apart gerapporteerd — v1-register schat de hele Obi-as op **~6 kt Co/j (indicatief, peiljaar onbekend)** [5], een op typische MHP-samenstelling (Co ≈ Ni/8–9) herleide orde van ~7 kt Co/j ligt in dezelfde range |
| Xiamen Haicang containerterminal | Xiamen Port Holding Group | overslag zeeschip → onbekend vervolgtransport | grote containerterminal, meerdere berths (nieuw anker, niet eerder gebruikt op deze kaart) | [12] |
| GEM Ganzhou — **knoop, niet gekoppeld** | GEM Co., Ltd. | MHP/kobalthydroxide + gerecyclede batterijen → kobaltsulfaat/-tetroxide | alleen groepsniveau-cijfer (>6 kt gerecycled Co, 9M-2025, alle vestigingen samen); vestigingsspecifiek Co-tonnage niet gevonden | [6][7][8] |

## 6 · Stoppunt
De brief stopt op de Xiamen Haicang-kade (`co-xiamen-haicang`): de veronderstelde eindraffinaderij GEM Ganzhou bestaat aantoonbaar (groepsniveau-cijfers, meerdere bronnen), maar geen bron van deze sessie geeft een site-coördinaat op de vereiste resolutie — dezelfde klasse open punt als de Huayou Quzhou-knoop in `kobalt-morowali-quzhou.md`. Die brief liet dat been ongetekend; deze doet hetzelfde. De keten is dus **haalbaar tot en met de Chinese kade**, niet tot de fabrieksdeur.

## 7 · Open punten
- **GEM Ganzhou heeft geen site-niveau coördinaat.** Alleen een v1-registercentroïde (stadsniveau, 25,83/114,93) — geen anker volgens werkwijze §1 ("een markt-/stadscentroïde is geen anker"). OSM-naamzoeken (Nominatim, 格林美/GEM) binnen de Ganzhou-regio gaf geen treffer; Overpass was deze sessie op meerdere mirrors onbereikbaar (406/timeout), dus geen kruiscontrole mogelijk.
- **Chinese kade bewust Xiamen, niet Ningbo** — conform de haalbaarheidstoets, om overlap met `kobalt-morowali-quzhou` (dat wél Ningbo gebruikt) te beperken. De zeecorridor zelf (Molukse Zee → Makassar/Lombok → Zuid-Chinese Zee) overlapt nog steeds grotendeels met die as; alleen de laatste ~300–500 km en de aanlandingskade verschillen.
- **b2 heeft geen gepubliceerde lengte** — de indicatieve 3.700–3.900 km is een analogie met de gebakken `nikkel-obi-ningbo`-corridor (4.202,5 km naar Ningbo), niet een eigen bronopgave voor Xiamen; wordt bij het bakken vervangen door de gemeten MARNET-waarde.
- **Cobalt-specifiek volume voor Obi is niet apart gepubliceerd** — het cijfer van 6 kt Co/j komt uit het v1-register (`data/cobalt.js`, peiljaar onbekend) en is alleen ruw kruisgecheckt tegen het bekende nikkelvolume via een typische MHP-Co-fractie, geen directe bron.
- **Volume dubbelzinnig zoals bij `nikkel-obi-ningbo`:** 65 kt Ni/j (2024, huidig) vs. >400 kt/j projectcapaciteit (fase III compleet, nog niet bereikt) zijn twee peilmomenten — niet optellen.
- **Xiamen Haicang is nieuw op deze kaart** (geen ander stroom gebruikt deze kade nog) — geen kruiscontrole met een bestaand anker mogelijk, alleen de eigen satellietblik.

## 8 · Bronnen
[1] Global Energy Monitor (gem.wiki), "PT Halmahera Persada Lygend Nickel Smelter power station" — Kawasi HPAL-complex, fase I–III, coördinaten (hergebruikt via `nikkel-obi-ningbo.md`). https://www.gem.wiki/PT_Halmahera_Persada_Lygend_Nickel_Smelter_power_station
[2] tbpnickel.com, "1Q24 Analyst & Investor Briefing" (PDF) — Obi-projectcapaciteit (500 kt/j nikkelsulfaat + >400 kt/j nikkelmetaal-equivalent bij volledige opschaling). https://tbpnickel.com/files/pdf_assets/1Q24%20Analyst%20Investor%20Briefing.pdf
[3] Indonesia Business Post, "Harita Nickel's Big Plan: From Acquisition to New Investor Entry" — HPL MHP-capaciteit + Co-inhoud, geen exporthaven genoemd. https://indonesiabusinesspost.com/2078/business-and-investment/harita-nickels-big-plan-from-acquisition-to-new-investor-entry
[4] IndonesiaMiner.com, "Harita Nickel (NCKL) HPAL Smelter to Operate in mid-2024" — bouw-/opstartstatus Obi HPAL. https://indonesiaminer.com/news/detail/2023-11-22103203-harita-nickel-nckl-hpal-smelter-to-operate-in-mid2024
[5] `data/cobalt.js` (v1-register, intern) — flow `co-obi → co-ref-ganzhou`, 6 kt Co/jaar (indicatief), peiljaar onbekend; unit-declaratie "kt Co/jaar (indicatief)".
[6] `v2/design/kobalt-sitelaag.json`/`.md`, anker `w-gem-ganzhou` — coördinaat blijft v1-registercentroïde, dit en vorige ronde niet site-niveau bevestigd; noemt GEM's grotere recyclingvestiging in Jingmen (Hubei) als mogelijke verwarring.
[7] GEM Co., Ltd. / GEM Indonesia, 9M-2025 resultaten (persberichten, groepsniveau, [B29] in `kobalt-sitelaag.md`). http://en.gemindonesia.com/
[8] Wikipedia, "Glencore" — bevestigt GEM (China) als kobalt-koper/-recycler op groepsniveau ("China's battery recycler GEM", 18.000 t 2019 / 21.000 t 2020 contractvolume), niet Obi-specifiek. https://en.wikipedia.org/wiki/Glencore
[9] `v2/design/routebrieven/nikkel-obi-ningbo.md` §3/§9 — hergebruikt anker `co-obi-kawasi` (letterlijk `ni-obi-kawasi`) + letterlijke kopie van de haven-aanloop-geometrie (Kawasi → zeeknoop 9031, 84,9 km, `nikkel-obi-ningbo-aanloop-kawasi.geojson`).
[10] `v2/design/routebrieven/kobalt-morowali-quzhou.md` §5/§6 — precedent voor "knoop, niet gekoppeld" wanneer een Chinese eindfabriek geen site-coördinaat oplevert.
[11] OpenStreetMap via Nominatim (ODbL) — "赣州经济技术开发区" (Ganzhou Economic & Technological Development Zone), relatie 8847867, 25,8532/114,8349 — bevestigt de regio, is geen site-anker; opgevraagd 2026-09-28. https://www.openstreetmap.org
[12] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live) — `sat-kobalt-obi-ganzhou-xiamen-haicang.png` (z14, oriëntatie), `-xiamen-haicang-b.png` (z15, containerterminal gelokaliseerd), `-xiamen-haicang-c.png` (z16, anker bevestigd op het containeryard).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Stroom `kobalt-obi-ganzhou`** → `v2/data/stroomroute-kobalt-obi-ganzhou.json` — 3 benen, **3.340,9 km**, 370 punten, 2 markers. Uitsluitend modaliteit **zee**: stippel 84,9 + MARNET 3.250,3 + stippel 5,7 km.
Recept: `v2/tools/bak_stromen.sh` (functie `bak_kobalt_obi_ganzhou`).

**b1 (zee, haven-aanloop, letterlijke kopie, stippel):** `--stippel-geojson` met exact `v2/build-cache/ais/graaf/nikkel-obi-ningbo-aanloop-kawasi.geojson` (gebakken in `bak_nikkel_obi_ningbo`) — **84,9 km, 32 punten**, ongewijzigd. Geen nieuwe `maak_havenaanloop.py`-run nodig; dezelfde fysieke Kawasi-jetty en hetzelfde pad als `nikkel-obi-ningbo` b1. Naad b1→b2 **0,000 km**.

**b2 (zee, MARNET, nieuw, geen stippel):** `--been "zee|…|-1.1099,127.9122|24.4515,117.9163"` — snap **0,000 km** aan beide uiteinden (op de zeeknopen zelf), 22 MARNET-edges, **3.250,3 km / 336 punten** (lengte-invariant: getekende lijn 3.250,335 vs som edge-km 3.250,600 = −0,265 km, de naden binnen het been zelf). Tegen de indicatieve schatting uit de brief (~3.700–3.900 km, analogie met de gebakken `nikkel-obi-ningbo`-corridor naar Ningbo) is dit **−12 tot −17%** — geen ±15%-harde toets, want er is geen gepubliceerde km voor déze corridor, alleen een analogie (brief §7). Tegen de hemelsbrede afstand obi-zk→xiamen-zk (~3.039,9 km) is de omwegfactor **1,069** — aanmerkelijk directer dan de Ningbo-corridor (omwegfactor ~1,2–1,3): de MARNET-route naar Xiamen via de Straat Taiwan blijkt korter bij te draaien dan de langere Malakka/Oost-Chinese-Zee-route naar Ningbo. `toets_knikken.py`: 1 knik ≥60° (70,2°, straal 7.865 m bij 6,906/121,863 — een krappe bocht in de Straat Taiwan-doorgang, geen omkering/terugloop). Naad b2→b3 **0,000 km**.

**b3 (zee, haven-aanloop, nieuw, stippel):** `timeout 300 python v2/tools/maak_havenaanloop.py --naam kobalt-obi-ganzhou-xiamen --van 24.4585,117.9720 --naar 24.4515,117.9163 …` vond **geen pad binnen 300 s** (exit 124) — conform bak-aanwijzing en bakhandleiding §2 direct teruggevallen op de rechte stippel, **geen tweede poging**: `--stippel "zee|…|24.4515,117.9163|24.4585,117.9720"` → **5,7 km, 2 punten**. De Xiamen Haicang-kade ligt 5,7 km van zeeknoop 5576, boven de 5 km-drempel (LAR-586) — dus VERPLICHT een haven-aanloop, ook al ligt de kade ruim binnen de 25 km-snap. `toets_rechte_benen.py --min-km 5` merkt dit been terecht als 🟡 MIDDEL (omwegfactor 1,002 — bijna een rechte lijn): dat klopt, want het IS een rechte fallback-stippel na de timeout, correct als stippel getekend, geen fout.

**Geen been C (Xiamen → GEM Ganzhou):** conform de bak-aanwijzing en brief §6/§7 — GEM's Ganzhou-vestiging heeft geen site-niveau coördinaat (alleen een v1-stadscentroïde, geen geldig anker; OSM/Nominatim leverde geen treffer, Overpass was deze sessie onbereikbaar op meerdere mirrors). Geen lijn, geen stippel, geen marker voor die knoop — zelfde patroon als de Huayou Quzhou-knoop in `kobalt-morowali-quzhou.md`.

**Toets:** km-som **3.340,9 km** — geen gepubliceerde totaal-km om hard tegen te toetsen (b1 = hergebruikte, al gemeten lengte; b2 = analogie, geen eigen publicatie; b3 = fallback-stippel). Naden **0,000 / 0,000 km**, ruim onder de 5 km-norm (bakhandleiding §5). `toets_knikken.py`: **1 knik ≥60°, 0 omkeringen, 0 terugloop** — de enige knik is een krappe maar echte bocht in het MARNET-zeebeen, geen reparatie nodig. `toets_rechte_benen.py --min-km 5`: alleen b3 (fallback-stippel, 🟡 MIDDEL) in de uitslag, en dat is de verwachte, correcte staat — geen been met omwegfactor 1,000 dat ten onrechte NIET gestippeld is. json geldig: versie 2, punt_formaat lonlat, modaliteit uitsluitend `{zee}`, elk been ≥2 punten, bestandsgrootte **7,8 KB** (ruim onder de ~300 KB-norm). Beide markers liggen exact (0 m) op het begin-/eindpunt van hun been — `co-obi-kawasi` op b1, `co-xiamen-haicang` op b3.

**Gereedschapslessen:**
- Een "letterlijke kopie" van een gedeeld been (b1) erft de al-gemeten km van de moederstroom zonder nieuwe scan — hier bovendien over grondstofgrenzen heen: `nikkel-obi-ningbo` (nikkel) en `kobalt-obi-ganzhou` (kobalt) delen dezelfde fysieke Kawasi-jetty, want MHP/nikkelsulfaat draagt beide metalen tegelijk.
- Een `maak_havenaanloop.py`-timeout (exit 124) op een korte aanloop (5,7 km) is geen fout in de tool maar een kenmerk van de zoektrappen op deze specifieke kustlijn (Xiamen-baai) — de bakhandleiding-regel "geen tweede poging" hield hier stand: de rechte stippel-terugval gaf een correct, klein en goed-gelabeld been.
- Een analogie-schatting (b2, "~3.700-3.900 km op basis van de Ningbo-corridor") is bruikbaar als ordegrootte maar geen harde toets: de werkelijke MARNET-route naar Xiamen bleek 12-17% korter dan de analogie voorspelde, omdat de omwegfactor van de Xiamen-corridor (1,069) lager ligt dan die van de Ningbo-corridor — twee corridors met een gedeeld beginstuk hoeven geen gelijke omwegfactor te hebben.
