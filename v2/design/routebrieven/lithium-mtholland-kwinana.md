# Routebrief (licht) · Lithium — Mt Holland → Moorine Rock → Kwinana (Australië)

**stroom-id:** `lithium-mtholland-kwinana` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken
**Keten in één zin:** spodumeenconcentraat van de Mt Holland-mijn (Covalent Lithium: Wesfarmers 50% / SQM 50%) gaat per
truck over de Mt Holland-weg (Bounty Access Rd → Marvel Loch–Forrestania Rd → Parker Range Rd) naar Moorine Rock, dan
westwaarts over de Great Eastern Highway en via Roe Highway en Kwinana Freeway naar de eigen Covalent-hydroxideraffinaderij
aan Mason Road in Kwinana (~505 km, eigen OSRM-routering) — **niet** naar Tianqi/IGO's TLK-fabriek (w-li-kwinana, 2,4 km zuidelijker).
**Welke as van het verhaal:** *tweede Australische mijn-naar-eigen-raffinaderij-as, naast Greenbushes/Kemerton* — het
beginpunt van de enige Australische keten waar mijn én raffinaderij van dezelfde joint venture zijn. Volume: raffinaderij
50 kt LiOH/j nameplate ≈ **44 kt LCE/j** (×0,88), peiljaar 2024 [2]; mijn 380 kt spodumeenconcentraat/j nameplate, wordt 760 kt/j
(besluit juli 2026, eerste uitbreidingsproductie 1H 2030) [6]. Werkelijke output raffinaderij onbekend (opstart).

## 1 · Ketenkaart
```
Mt Holland-mijn/concentrator `li-mtholland-laad` ──(b1 truck — aannemelijk: transportmodus niet expliciet gebrond ·
Bounty Access Rd → Marvel Loch–Forrestania Rd → Parker Range Rd → Moorine Rock → Great Eastern Hwy W → Roe Hwy →
Kwinana Fwy → Anketell Rd → Thomas Rd → Rockingham Rd → Mason Rd · ~505 km)──► Covalent-raffinaderij Kwinana
`li-covalent-fabriek` ⏹ stoppunt (hydroxide gaat daarna naar batterijmakers; geen bron per fabriek)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (spodumeenconcentraat — aannemelijk: transportmodus niet expliciet gebrond; wegupgrade GEH↔mijn wijst op wegvracht) | `li-mtholland-laad` → `li-covalent-fabriek` | Mt Holland-weg (Bounty Access Rd, Marvel Loch–Forrestania Rd, Parker Range Rd) → Great Eastern Hwy (94) → Roe Hwy (3) → Kwinana Fwy (2) → Anketell Rd → Thomas Rd → Rockingham Rd → Mason Rd | **geen gepubliceerde wegkm voor het hele been.** Deelstuk GEH↔mijn ≈ **113 km** wegupgrade (Decmil/Macmahon-contract Covalent) [5]; eigen OSRM-routering mijn→Moorine Rock 123,6 km (+9%) en totaal **505,0 km** [11] — indicatie, geen norm; **hemelsbreed 377,0 km, geen wegkm** | maak_stroombeen_weg (extract australie) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-mtholland-laad` | mijn / concentraatterrein | Mt Holland (Covalent Lithium) | -32.0990, 119.7740 | **hergebruik letterlijk** `w-li-mtholland` uit `lithium-sitelaag.json` [8] | **bron-gelegd** (sitelaag, 2026-09-26); op mijn z15-blik: kruis op een lichte pad direct oost van de concentrator (procesgebouwen, tailings-dam rechts, dagbouwput noord) — binnen het mijnterrein, ~0,4 km van het procesblok |
| `li-covalent-fabriek` | raffinaderij (losplek, stoppunt) | Covalent Lithium Refinery, 15 Mason Road, Kwinana Beach | -32.2188, 115.7714 | adres/oppervlak [1][3]; coördinaat **afgeleid** uit satellietchronologie [9], niet uit een bron | **aannemelijk** — z16 live (opname 2025-09-10): kruis midden op een nieuw procescomplex met pijprek, lange witte opslagloods (-32.2170, 115.7703), tanks en schakelstation; Wayback 2021-08-11: kale gebiedsvlakte van ~50 ha op dezelfde plek, 2023-08-10: complex in aanbouw. Past op "40 ha huurgrond, Lot 15 Mason Road, Kwinana SIA"; perceelgrens niet gezien |

## 4 · Via-punten (b1 — corridorkeuzes)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Parker Range Rd, begin (kruising Marvel Loch–Forrestania Rd) | -31.6323, 119.5803 | pint de noordelijke Mt Holland-weg naar Moorine Rock i.p.v. het zuidelijke alternatief via Hyden–Brookton Hwy (OSRM-default, 477 km) |
| b1 | 2 | Moorine Rock, kruising Parker Range Rd/Great Eastern Hwy | -31.3124, 119.1270 | het aansluitpunt op de GEH (naam "Moorine Rock–Mt Holland road" [2]); op de doorgaande weg, geen dorpscentrum |
| b1 | 3 | Great Eastern Hwy, tussen Merredin en Cunderdin | -31.6235, 117.5911 | houdt de lijn op de GEH (94) en niet op de parallelle landbouwwegen |
| b1 | 4 | Great Eastern Hwy, ten oosten van Northam | -31.6336, 116.7943 | idem; vóór de Northam-doorgang, niet in het centrum |
| b1 | 5 | Great Eastern Hwy → Roe Hwy (Midland-noordoost) | -31.8982, 116.0253 | corridorkeuze: Roe Hwy/Kwinana Fwy i.p.v. Tonkin Hwy/Armadale Rd (OSRM-default voor het zuidelijke alternatief) |
| b1 | 6 | Roe Hwy → Kwinana Fwy (Kenwick) | -32.0879, 115.8560 | splitsing Roe/Tonkin; pint de Kwinana Fwy zuidwaarts |
| b1 | 7 | Kwinana Fwy → Anketell Rd (afrit) | -32.2100, 115.8511 | laatste afslag van de snelweg naar het industrieterrein |
| b1 | 8 | Thomas Rd → Rockingham Rd | -32.2261, 115.7876 | corridorkeuze naar Mason Rd i.p.v. Patterson/Kwinana Beach Rd |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mt Holland-concentrator | Covalent Lithium (Wesfarmers/SQM, 50/50) | erts → spodumeenconcentraat | 380 kt/j nameplate (→ 760 kt/j, 1H 2030) | [2][6] |
| Covalent Lithium Refinery, Kwinana | Covalent Lithium (Wesfarmers/SQM) | spodumeenconcentraat → batterijkwaliteit lithiumhydroxide | 50 kt LiOH/j nameplate ≈ 44 kt LCE/j | [1][2] |

## 6 · Stoppunt
De brief stopt bij de raffinaderij: er is geen bron die het hydroxide aan een benoemde fabriek koppelt (fase D vervalt) en
het plan om expansie-volumes als concentraat te verkopen [6] maakt een tweede streng uit Mt Holland onzeker.

## 7 · Open punten
- **Transportmodus niet expliciet gebrond.** Geen geopende bron zegt "truck" voor het stuk mijn → Kwinana; de wegupgrade GEH↔mijn [5], de
  Moorine Rock–Mt Holland-weg [2] en het ontbreken van spoor in Mt Holland maken wegvracht aannemelijk. Rail vanaf Moorine Rock/Southern Cross niet uitgesloten.
- **Geen gepubliceerde wegkilometer voor het hele been**; 505,0 km is een eigen OSRM-routering (OSM-wegnet), Decmil-113 km dekt alleen het mijnstuk.
- **Coördinaat Covalent-raffinaderij is afgeleid**, niet uit een bron: EPA/DWER (WAF 403), Firecrawl (geen credits) en Overpass waren niet bereikbaar.
  Perceelsgrens/Lot 15 niet gezien; **bevestig één keer met de ruimtelijke bijlage van Ministerial Statement 1170 / DWER W6499/2021/1**.
- **Verwarringsgevaar:** sitelaag `w-li-kwinana` (-32.2400, 115.7700) is Tianqi/IGO's TLK-fabriek — 2,4 km zuidelijker. Voorstel centraal: nieuw sitelaag-anker `w-li-covalent` op -32.2188, 115.7714.
- **Eerste hydroxide-output en actuele bezetting** (ontwerp: 15-08-2025; mijn: bouw gereed juli 2025) niet onafhankelijk door mij bevestigd.
- Wegklassen langs de Mt Holland-weg: Bounty Access Rd = unclassified/gravel, Marvel Loch–Forrestania Rd en Parker Range Rd = tertiary/unclassified (deels unpaved) [10] — bij een OSM-gat wordt dat stuk stippel.
- Last mile: geen eigen been; het anker ligt ~0,25 km binnen het terrein, ≤ 2 km van de openbare Mason Rd.

## 8 · Bronnen
[1] WA-regering, "Covalent Lithium to build new facility in Kwinana" (2021-09-01) — 40 ha, Kwinana SIA, lange-termijnhuur, 50 kt LiOH/j. https://www.wa.gov.au/government/media-statements/McGowan%20Labor%20Government/Covalent-Lithium-to-build-new-facility-in-Kwinana-20210901
[2] WA-regering, "New lithium mine set to boost WA's credentials as battery hub" (2024-03-07) — mijn 110 km ZO van Southern Cross, 380 kt/j, Moorine Rock–Mt Holland-weg A$60 mln. https://www.wa.gov.au/government/media-statements/Cook-Labor-Government/New-lithium-mine-set-to-boost-WA's-credentials-as-battery-hub-20240307
[3] EPA WA, "Covalent Lithium Hydroxide Refinery" (Ministerial Statement 1170, 2021-07-15) — "Lot 15 Mason Road, Kwinana", 76 ha envelop, 11,2 ha clearing (via zoekresultaat; pagina zelf 403). https://www.epa.wa.gov.au/proposals/covalent-lithium-hydroxide-refinery
[4] DWER werkvergunning W6499/2021/1 Covalent Lithium (wijziging 2025-04-08; via zoekresultaat). https://www.der.wa.gov.au/component/k2/item/22117-w6499-2021-1
[5] Macmahon/Decmil-contract A$123 mln, ~113 km upgrade GEH↔Mt Holland (via zoekresultaat; onderliggende pagina niet apart geopend). https://im-mining.com/tag/mount-holland
[6] IM Mining, "Covalent Lithium to double spodumene output from Mt Holland" (2026-07-22). https://im-mining.com/2026/07/22/covalent-lithium-to-double-spodumene-output-from-mt-holland/
[7] NS Energy, "Covalent lithium refinery in Kwinana" (2021-09-02) — buren Alcoa, CSBP, Tianqi, Avertas WtE. https://www.nsenergybusiness.com/news/covalent-lithium-refinery-in-kwinana/
[8] `v2/design/lithium-sitelaag.json` — `w-li-mtholland` (bron-gelegd), `w-li-kwinana` (TLK, benaderd).
[9] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-lithium-mtholland-kwinana-covalent-z16.png` (live, opname 2025-09-10), `-hist2021-wb51423.png` (2021-08-11), `-hist2023-wb17632.png` (2023-08-10), `-z16-wb63116.png`, `-z15.png`, `-mtholland-z15.png`.
[10] OpenStreetMap (ODbL) via Nominatim — Moorine Rock (-31.3127/119.1269), Mason Road (way 1503511595, 25005800), wegklassen Parker Range/Marvel Loch–Forrestania/Bounty Access Rd, Kwinana WtE (-32.2105/115.7785).
[11] OSRM-demoroutering (project-osrm.org), mijn → Moorine Rock → anker: 505,0 km (123,6 + 381,6), opgevraagd 2026-10-09; mijn → anker direct (zuidelijk alternatief) 477,3 km. http://router.project-osrm.org
[12] Geofabrik `australie-latest.osm.pbf` — extract voor de bak-agent (`maak_stroombeen_weg.py`).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Resultaat:** `v2/data/stroomroute-lithium-mtholland-kwinana.json` (69,6 KB, contract versie 2, `lonlat`) · **1 been · 508,6 km · 3.235 punten · 2 markers** · geen naden (enkel been) · markers 0,0 km van de lijn.

| # | modaliteit | km (gemeten) | km (brief) | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | truck — spodumeenconcentraat Mt Holland → Covalent Kwinana (aannemelijk: modus niet gebrond) | 508,6 (wegnet 507,9 + 0,61 plant-verbinding + 0,14 kade-verbinding) | 505 (eigen OSRM, géén wegkm) | **+0,7%** — indicatie, geen norm | nee |

**Recept:** profiel `lithium-mtholland-kwinana-mtholland-kwinana` in `maak_stroombeen_weg.py` (10 via-punten, extract `australie`, refs 94/3/2, `corridorKlassen` tertiary+unclassified, `trimStaart`, vensterKm 75) → `lithium-mtholland-kwinana-weg-mtholland-kwinana.geojson`; functie `bak_lithium_mtholland_kwinana()` in `bak_stromen.sh`; tussenuitvoer en logs met prefix `lithium-mtholland-kwinana-` in `v2/build-cache/ais/graaf/`.
**Toetsen:** `toets_knikken` 10 knikken ≥ 60° (alle spikes van 6–129 m op ankers/junctiepunten), **0 omkeringen, 0 terugloop** · `toets_rechte_benen` omwegfactor 1,349 (geen rechte lijn) · `json.load` ok, versie 2, `lonlat`, modaliteit {truck}, bestand 69,6 KB.

**⚠️ Wegbron (afwijking van het gewone recept).** `--bron geofabrik` faalt: pyosmium is op deze machine geblokkeerd (toepassingsbeheer, "DLL load failed") en is niet omzeild. `--bron overpass` faalt ook (overpass-api.de: verbinding verbroken, kumi.systems: 500; ook private.coffee 500, openstreetmap.fr 403, mail.ru 504, osm.jp onbereikbaar). Daarom is het wegnet voor dit been de **unie van bestaande Geofabrik-scancaches** (`build-cache/land/weg-australie-*.json`, eerder met het gewone tool uit `australie-latest.osm.pbf` gescand) via een eigen wrapper (`lithium-mtholland-kwinana-wegscan-wrapper.py`, vervangt alleen `_ways_uit_overpass`; het tool zelf is ongewijzigd) — plus **vier exacte OSM-ways uit Nominatim** (`lookup`, `polygon_geojson`): Bounty Access Rd 332621121 (unclassified, gravel; de mijnontsluiting, ontbrak in alle caches), Marvel Loch–Forrestania Rd 29422982 + 1564278325 (de cache-keten 29422982 is vereenvoudigd en miste de junctievertex, dus vervangen) en Parker Range Rd 612737411. Alle geometrie is dus OSM; filter en routering zijn die van het tool. **Les:** de scancaches zijn gevouwen, vereenvoudigde ketens met het id van de eerste way; combineer ze niet met exacte ways zonder de overlappende keten te vervangen (eerste poging gaf een lus van 1,9 km en een omweg).

**Afwijkingen van de brief (via-punten):**
1. **Toegevoegd** via-punt "Parker Range Rd, midden" = vertex 16 van OSM-way 321759593 (119,2781 / −31,4590). Zonder dat wijkt de router (refs-straf ×3 op ongenummerde wegen) uit naar een noordelijke weg die ~35 km oostelijker op de GEH aansluit (83 km i.p.v. 59 km tussen Parker Range Rd-begin en Moorine Rock). Dit is de corridorkeuze "Parker Range Rd" uit §2/§4 van de brief.
2. **Verplaatst** via 2 "Moorine Rock" van (−31,3124 / 119,1270) naar de echte junctie Parker Range Rd/GEH (−31,3155 / 119,1218; vertex van way 219518794): het oorspronkelijke punt lag 0,6 km oostelijk op de GEH en gaf een heen-en-terug-spike (TERUGLOOP 180°).
3. Overige via-punten uit §4 ongewijzigd; alle snaps ≤ 0,01 km, behalve het plant-anker (0,61 km).

**Bevindingen / open (ongewijzigd uit §7 + nieuw):**
- **Plant-anker → Bounty Access Rd: 0,61 km rechte verbinding** (> 0,5 km-norm, ≤ 2 km: geen last-mile-been, geen stippel). Het concentraatterrein ligt tussen de weg en het anker; zelfde patroon als de brief (§3: anker ~0,4 km van het procesblok).
- **Mijn → Parker Range Rd-begin 67,6 km en GEH-junctie Moorine Rock na 126,4 km** (mijn → Moorine Rock) tegen OSRM 123,6 km (+2%) en de gepubliceerde Decmil-113 km GEH↔mijn: consistent.
- **Eerste 7,2 km Bounty Access Rd is gravel** (OSM `surface=gravel`, `highway=unclassified`, doorgetrokken omdat OSM de weg als unclassified kent); Marvel Loch–Forrestania Rd/Parker Range Rd deels unpaved.
- Transportmodus (truck) en Covalent-coördinaat blijven **aannemelijk** (§7); geen last mile, geen zee/haven-aanloop, geen leiding, geen luchtbeen, geen kopie.
- Voorstel centraal (uit §7): sitelaag-anker `w-li-covalent` op −32,2188 / 115,7714 (nu alleen `w-li-kwinana` = TLK, 2,4 km zuidelijker).
- **Registerregel (centraal):** `{ "sleutel": "li-mk", "bestand": "stroomroute-lithium-mtholland-kwinana.json", "grondstof": "lithium", "label": "Mt Holland → Kwinana (Covalent)", "aan": true, "noot": "M31 · golf 7 (2026-10-09): spodumeenconcentraat per truck (aannemelijk) van Mt Holland via Moorine Rock en de GEH naar Covalents hydroxideraffinaderij in Kwinana" }` (sleutel li-mk = m(tholland) + k(winana); niet bezet in de lijst van lithium-sleutels, centraal op botsingen controleren).

**Lessen voor volgende bakers:** (1) bij pyosmium-blokkade én Overpass-uitval is de unie van bestaande `weg-<extract>-*.json`-caches een werkbare terugval mits het ontbrekende stuk met exacte OSM-ways (Nominatim lookup) wordt aangevuld; (2) de refs-straf ×3 trekt de route naar genummerde wegen, ook als dat een omweg is: zet een via op de echte corridorweg; (3) zet een via op de junctie van een zijweg met de hoofdweg, niet op het dorpspunt, anders ontstaat een terugloop; (4) de slot-hulpfunctie met `rm -rf "$d"` wordt door de veiligheidscheck geweigerd — neem het slot met `mkdir` op letterlijke paden en geef vrij met `rmdir` op het letterlijke pad.
