# Routebrief (licht) · olie — Porto do Açu (Brazilië) → Dongjiakou (Qingdao Port, China)

**stroom-id:** `olie-acu-dongjiakou` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Braziliaanse pre-sal-crude (Santos-/Campos-bekken) via het STS-oliefront T-OIL van Porto do Açu
(São João da Barra, RJ) per **VLCC** langs de Kaap de Goede Hoop, door de Straat van Soenda, de Zuid-Chinese Zee en de
Straat van Taiwan naar de VLCC-terminal van Dongjiakou (Qingdao Port) — stoppunt bij de terminal.
**Welke as van het verhaal:** *Zuid-Amerika → China om de Kaap* (tegenhanger van de Atlantische kant; de Brazilië-Rotterdam-
as is een andere stroom). Açu is ~30% van de Braziliaanse olie-export (2023) [1]; Brazilië exporteerde 2025 ~1.980 kb/d,
China ~40–45% daarvan [3][4]. Dongjiakou is **aannemelijk: één bron** (geen lading op kade-niveau gebrond) — zie §7.

## 1 · Ketenkaart
```
T-OIL STS-berth Porto do Açu `ol-acu-toil` (Prumo, Terminal 1-golfbreker, São João da Barra)
  ──(b1 zee · haven-aanloop Açu → zeeknoop −23.5000,−41.3000 · 199,4 km over water, 44 punten)──►
  MARNET-zeeknoop Rio-kust
  ──(b2 zee · Zuid-Atlantisch → Kaap de Goede Hoop → Indische Oceaan → Straat van Soenda → Zuid-Chinese Zee →
      Straat van Taiwan → Gele Zee · 20.554 km gemeten, +2,8% t.o.v. 20.000-schatting)──►
  MARNET-zeeknoop Dongjiakou 35.5758,119.7029
  ──(b3 zee · haven-aanloop Dongjiakou, LETTERLIJKE KOPIE uit olie-kharg-dongjiakou · 9,4 km)──►
  Dongjiakou-olieterminal `ol-dongjiakou-terminal` ── stoppunt (aannemelijk: één bron)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ol-acu-toil` → zeeknoop −23.5000,−41.3000 | haven-aanloop Açu (open kust, Campos-bekken) | 199,4 over water (hemelsbreed 191,4; rechte lijn zou 18 km over land gaan) [eigen run] | maak_havenaanloop.py → `v2/build-cache/ais/graaf/olie-acu-dongjiakou-aanloop-acu.geojson` (al gebakken, kade→zeeknoop) | **ja** — MARNET reikt niet (kade 191 km van de dichtstbijzijnde zeeknoop) |
| b2 | B | zee | zeeknoop −23.5000,−41.3000 → zeeknoop 35.5758,119.7029 | Kaap · Soenda · Straat van Taiwan (gemeten: 4/6/11 km van de punten; Malakka 534 km ernaast) | 20.554 gemeten; ontwerp ~20.000 [hemelsbreed-schatting, geen gepubliceerde route] | MARNET | nee |
| b3 | B | zee | zeeknoop 35.5758,119.7029 → `ol-dongjiakou-terminal` | haven-aanloop Dongjiakou (kopie olie-kharg-dongjiakou, been 2) | 9,4 [bestaande keten] | kopie `--stippel` uit `bak_olie_kharg_dongjiakou` | ja — 1:10M-kust kent de haven niet |
Geen land-/leidingbenen, geen fase D/E (geen bron noemt de raffinaderij achter Dongjiakou voor Braziliaanse lading).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-acu-toil` | laadplek / STS-oliefront | Porto do Açu T-OIL, STS-berth op de golfbreker van Terminal 1 | -21.8046, -40.9791 | [2][5] | bron-gelegd (z17 gezien: twee VLCC-grote tankers (één oranje) naast elkaar afgemeerd langs een lange betonnen golfbreker met afmeerplatform = STS-overslag; lengte-as NNW–ZZO; Ferroport-ertspier met bulkcarrier 600 m westelijker) |
| `ol-dongjiakou-terminal` | losplek / VLCC-diepwaterterminal | Dongjiakou-olieterminal (Qingdao Port) | 35.5900, 119.8050 | [6] | HERGEBRUIK letterlijk uit olie-kharg-dongjiakou §3 (bron-gelegd, z16: lange trestle met aanmeerplatform en tankenpark) |
Verworpen alternatief: **-21.8342,-40.9929** (toets: tanker met laadarmen aan de noordpier van het T2-bekken, z16) — dat is een
andere pier (T2-kant); T-OIL ligt volgens [2] op de golfbreker van T1 met 3 STS-berths, en dáár liggen twee tankers langszij.
Porto-centroïde (-21.8209,-41.0199) is geen anker. Afstand tussen beide kandidaten 3,6 km.

## 4 · Via-punten
Geen — alle benen zijn zee of haven-aanloop; geen corridorkeuze buiten MARNET.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| T-OIL Porto do Açu | Prumo Logística (T-OIL) | shuttletankers uit het Santos-/Campos-bekken → STS naar VLCC | 3 STS-berths, 1,2 Mb/d [2]; Açu ~30% van de Braziliaanse export [1] | [1][2] |
| Dongjiakou-havenzone | Qingdao Port Group | VLCC → tankenpark → Shandong-raffinaderijen | zie olie-kharg-dongjiakou §5 | [6] |

## 6 · Stoppunt
De brief stopt bij de Dongjiakou-olieterminal: geen bron koppelt een Açu-lading aan een met naam genoemde raffinaderij (fase D/E vervallen).

## 7 · Open punten
- **Dongjiakou is aannemelijk, niet bewezen per lading:** Signal Ocean noemt Dongjiakou en Qingdao als belangrijke losplaats van Braziliaanse crude, Noord-China 73% van de aankomsten [4]; Platts' Americas-VLCC-basket bevat Porto do Açu–Qingdao [7]. Een Petrobras/Qingdao-Port-depot (Seatrade, volgens toets) kon ik niet openen (403). Brazilië → Ningbo of Rotterdam is even goed mogelijk.
- **Açu is vaak STS-overslag:** de lading kan op de rede worden overgezet; de lijn toont de structurele route terminal → terminal, geen AIS-track.
- **Haven-aanloop Açu:** zeeknoop −23.5000,−41.3000 ligt 191 km uit; `maak_havenaanloop` slaagde in ~6 min (timeout 590 s gebruikt; 300 s is te krap): 199,4 km, 0 km land midden op de lijn. Liep een herhaling toch op exit 124, gebruik dan het bestaande geojson, NIET een rechte stippel (die gaat 18 km over land).
- **Volume:** Açu totaal ~600 kb/d (30% × ~1.980 kb/d, eigen berekening); China-aandeel ~40% [4] (Petrobras zelf 62% in Q1 2026 [8]) → orde 250–350 kb/d naar China; het Dongjiakou-deel is **niet gebrond**. Peiljaar 2025, eenheid kb/d.
- Km: geen gepubliceerde routelengte; "hemelsbreed-schatting ~20.000 km, geen gepubliceerde km" — ±15%-toets is een indicatie.

## 8 · Bronnen
[1] Wikipedia, "Superporto do Açu" — 21°49′15″S 41°01′11″W, 2023: 30% van de Braziliaanse olie-export. https://en.wikipedia.org/wiki/Superporto_do_A%C3%A7u
[2] Wikipedia (pt), "Porto do Açu" — T-OIL operationeel sinds aug 2016, op de golfbreker van T1, 3 STS-berths, 1,2 Mb/d, VLCC sinds 2017. https://pt.wikipedia.org/wiki/Porto_do_A%C3%A7u
[3] Ontwerp ketenkaart (StoneX/MDIC): Brazilië 2025 ~1.980 kb/d ruwe olie, China 45%.
[4] Signal Ocean via AJOT, "Chart of the week: Brazilian crude oil shipments" — China ~40%, 93,6 mln vaten Q2 2025, Noord-China 73%, Dongjiakou/Qingdao genoemd. https://www.ajot.com/news/signal-ocean-chart-of-the-week-brazilian-crude-oil-shipments
[5] Esri World Imagery via `sat_check.py` (live) — `sat-olie-acu-dongjiakou-acu-{toil-t1,t1kop,t2,t2-z16,overzicht,toil}.png`.
[6] Brief `olie-kharg-dongjiakou.md` (anker + haven-aanloop Dongjiakou); Wikipedia, "Qingdao Port". https://en.wikipedia.org/wiki/Qingdao_Port
[7] S&P Global Platts, amendement Americas-VLCC Brazil/Uruguay–China-basket (3 jun 2024): Porto do Açu–Qingdao. https://www.spglobal.com/energy/en/pricing-benchmarks/our-methodology/subscriber-notes/060324-platts-amends-basket-for-americas-vlcc-braziluruguay-china-dirty-tanker-assessment-june-3
[8] Datamar News, "Asia accounted for 85% of Petrobras oil exports in Q1" — 888 kb/d, China 62%. https://datamarnews.com/noticias/asia-accounted-for-85-of-petrobras-oil-exports-in-the-first-quarter/
[9] Hellenic Shipping News (Signal Ocean) — China-aandeel/Dongjiakou. https://www.hellenicshippingnews.com/?p=1097120

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-olie-acu-dongjiakou.json` (40,5 KB, versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh olie-acu-dongjiakou` (functie `bak_olie_acu_dongjiakou`) · **totaal 20.762,7 km · 2.147 punten · 2 markers**

| # | modaliteit | km | punten | stippel | geometrie |
|---|---|---|---|---|---|
| b1 | zee | 199,4 | 44 | ja | haven-aanloop Açu, het al gebakken geojson `olie-acu-dongjiakou-aanloop-acu.geojson` (kade → zeeknoop −23.5000,−41.3000), niet opnieuw gedraaid |
| b2 | zee | 20.553,9 | 2.101 | nee | MARNET zeeknoop → zeeknoop (snap 0,000 km aan beide kanten; 95 MARNET-edges, 0 track-edges) |
| b3 | zee | 9,4 | 2 | ja | letterlijke kopie van de haven-aanloop Dongjiakou uit `bak_olie_kharg_dongjiakou` (35.57580,119.70290 → 35.5900,119.8050) |

**Toets.** Naden b1→b2→b3 allemaal 0,000 km. Markers 0,0 m van hun lijn (`ol-acu-toil` −21.8046,−40.9791 en `ol-dongjiakou-terminal` 35.5900,119.8050). b2 20.553,9 km tegen de ontwerp-schatting ~20.000 km = +2,8%, binnen ±15% maar alleen indicatief: er is geen gepubliceerde routekilometer, de schatting is hemelsbreed. `toets_knikken`: 0 knikken, 0 omkeringen. `toets_rechte_benen --min-km 5`: alleen de Dongjiakou-stippel (9,4 km, bewust recht, reden in de naam). json.load, versie 2, punt_formaat lonlat, modaliteiten alleen zee, elk been ≥ 2 punten.

**Stippels met reden.** b1: de kade ligt 191 km van de dichtstbijzijnde MARNET-zeeknoop, en een rechte lijn zou 18 km over land gaan. Daarom de over-water-aanloop van `maak_havenaanloop.py` (199,4 km, 0 km land, ~6 min met timeout 590 s). b3: de 1:10M-kust kent de haven niet, de kade ligt 9,37 km van de zeeknoop.

**Aannemelijk, niet bewezen.** Dongjiakou rust op één bron (Signal Ocean, Platts-basket Açu–Qingdao). Het been is doorgetrokken en "aannemelijk: één bron" staat in de beennaam en de markernaam. De lijn is de structurele terminal-naar-terminal-route, geen AIS-track, want Açu-lading wordt vaak STS overgezet.

**Lessen.** (1) Bij een kade > ~100 km van de zeeknoop is de rechte stippel gevaarlijk (hier 18 km over land): hergebruik een gelukt aanloop-geojson. (2) Een bake draait `bak_stromen.sh` incrementeel gelezen door bash; omdat andere agenten tegelijk hetzelfde bestand bewerken verscheen na afloop "line 9954: t: command not found". Het json was dan al compleet geschreven en onschuldig. (3) Geen weg, spoor, leiding of lucht in deze keten, dus geen wegscan en geen slot voor weg/reus nodig.
