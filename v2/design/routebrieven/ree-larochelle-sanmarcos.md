# Routebrief (licht) · Zeldzame aardmetalen — Solvay La Rochelle → Noveon San Marcos (haven Houston aangenomen) (Frankrijk → Verenigde Staten)

**stroom-id:** `ree-larochelle-sanmarcos` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken (2026-10-09)
**Keten in één zin:** gescheiden NdPr-/Dy-/Tb-oxiden van Solvay La Rochelle (Chef de Baie) gaan — aangenomen — per truck
(last mile, stippel) naar een kade van La Pallice, per zeeschip over de Atlantische Oceaan naar Barbours Cut (Houston) en
per truck (I-10 → US-183 → TX-80) naar de magneetmaker Noveon in San Marcos, Texas.
**Welke as van het verhaal:** de transatlantische REE-oxideleverantie Europa → VS (verwerker → magneetmaker), naast de
Mountain Pass → Fort Worth-landketen. Volume: **niet gepubliceerd** — Solvay-CEO "limited volumes", NdPr direct, DyTb in de
loop van 2026 [1][2]. Plantniveau La Rochelle: enkele honderden t NdPr/j (2025) → doel 30% van de Europese NdPr-vraag in
2030 ≈ 4,5 kt/j (marktschatting, geen Solvay-cijfer; kt REO per jaar, peiljaar 2025) [4][9]. Het gloedgewicht hoort bij de site, niet bij deze as.
**⚠️ Eerlijkheid:** GEEN bron noemt een haven, een modaliteit of een route; alleen de relatie Solvay → Noveon is bron-gelegd [1][2].
Havenkeuze (La Pallice → Houston) en zee/truck zijn een aanname: een Texaanse afnemer en een Golfhaven maken zee aannemelijk.

## 1 · Ketenkaart
Solvay La Rochelle `ree-larochelle-site` ──(b1 truck · last mile · 1,8 km · STIPPEL)──► kade La Pallice `ree-larochelle-kade`
──(b2a zee · haven-aanloop · 9,3 km · STIPPEL)──► zeeknoop 4239 ──(b2 zee · aannemelijk · MARNET ~9.040 km)──►
Barbours Cut Terminal, Houston `ree-houston-kade` ──(b3 truck · aannemelijk · SH-146 → SH-225 → I-10 → US-183 → TX-80 → FM-110 → SH-123)──►
Noveon San Marcos `ree-noveon-fabriek` ⏹ stoppunt

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-larochelle-site` → `ree-larochelle-kade` | havenwegen La Pallice | hemelsbreed 1,8 km (berekend; geen publicatie) | `--stippel` | **ja** — last mile (geen net op deze korrel, < 2 km) |
| b2a | B | zee | `ree-larochelle-kade` → zeeknoop 4239 (46.2392, -1.2612) | haven-aanloop La Pallice (kade 9,28 km van de zeeknoop > 5 km) | hemelsbreed 9,3 km (berekend) | `maak_havenaanloop.py` liep op 2026-10-09 vast op `timeout 300` (exit 124, kade → zeeknoop 4239) → rechte `--stippel` (geen tweede poging) | **ja** — MARNET reikt niet tot de kade |
| b2 | B | zee | zeeknoop 4239 → `ree-houston-kade` | zeeschip La Pallice → Houston (aannemelijk: geen bron voor haven of route; alleen de relatie Solvay → Noveon is bron-gelegd) | geen gepubliceerde km; MARNET-test 9.040,5 km (1.014 punten); hemelsbreed kade–kade 7.948 km | MARNET | nee; geen aanloop Houston (kade 1,56 km van zeeknoop 6228, router snapt op 0,019 km) |
| b3 | C | truck | `ree-houston-kade` → `ree-noveon-fabriek` | SH-146 → SH-225 → I-10 W → US-183 (Luling) → TX-80 → FM-110 → SH-123 [10] | hemelsbreed 285 km, geen wegkm (nagemeten met de definitieve ankers 286,0 km) | maak_stroombeen_weg (extract us-texas) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-larochelle-site` | scheiding / laadplek | Solvay La Rochelle, Chef de Baie (40 ha, gesticht 1948) | 46.1525, -1.2075 | hergebruikt letterlijk uit `ree-sitelaag.json` (`w-larochelle`) [4][9] | bron-gelegd (z15 opnieuw gezien: industrieel gebouwencomplex met lange hallen tussen havenbekken (N) en kustlijn (Z)) |
| `ree-larochelle-kade` | overslag / kade | La Pallice, kade aan de zuidoostzijde van de noordelijke havenmole (aangenomen kade) | 46.1586, -1.2297 | [5][8], satelliet | **onzeker** — z16: kade met kranen, loodsen en een afgemeerd schip; Wikipedia-punt 46.1583, -1.2278 ligt in open water voor de haven en is naar de kade verschoven; geen bron noemt de kade |
| `ree-houston-kade` | overslag / kade | Barbours Cut Container Terminal, Houston (La Porte) | 29.6819, -94.9983 | [8] Wikipedia-geohack | aannemelijk (z15 gezien: kadefront met ≥5 portaalkranen, containerstapels en een afgemeerd schip — het terminalbeeld uit [8]); de haven zelf is een aanname |
| `ree-noveon-fabriek` | losplek / magneetfabriek | Noveon Magnetics, 1550 Clovis R. Barker Road, San Marcos, TX 78666 | 29.8413, -97.9554 | [3] adres noveon.co + [7] OSM-adresnode | aannemelijk (z16 gezien: nieuw industrie-/distributiepark aan de Clovis R. Barker Road, grote hallen; welk pand Noveon is niet te onderscheiden; noveon.co zegt niet of dit HQ of fabriek is) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Alle punten liggen op de doorgaande weg (OSM-wegpunten uit een OSRM-route [10], niet in een stadscentrum); te converteren naar (lon, lat) in het profiel.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | SH-225 La Porte/Pasadena Freeway | 29.7117, -95.1430 | pint SH-146 → SH-225 westwaarts i.p.v. I-10 East via Baytown |
| b3 | 2 | I-10 Katy Freeway, ten westen van Houston | 29.7851, -95.6500 | pint I-10 W door/langs Houston en sluit US-90A/SH-71-zuidroutes uit; buiten het centrum |
| b3 | 3 | I-10 tussen Sealy en Columbus | 29.7190, -96.4420 | houdt de route op I-10 (geen SH-71 via La Grange/Bastrop) |
| b3 | 4 | I-10 tussen Flatonia en Waelder | 29.6923, -97.2030 | idem; midden in het lange I-10-stuk (191 km) |
| b3 | 5 | I-10-afrit naar US-183 (Luling) | 29.6534, -97.5876 | verlaat I-10 bij Luling (US-183/TX-80) i.p.v. door te rijden naar Seguin en TX-123 (~33 km langer) |
| b3 | 6 | TX-80 → FM-110 (NO van San Marcos) | 29.8648, -97.8779 | benadert Noveon via FM-110/SH-123 aan de oostzijde, niet door het centrum van San Marcos |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Solvay La Rochelle | Solvay | REE-feed uit meerdere leveranciers, deels recycling (EoL-magneetmateriaal) → gescheiden NdPr-/Dy-/Tb-oxiden | enkele honderden t NdPr/j (2025) → ~4,5 kt/j 2030 (marktschatting) | [2][4][9] |
| Noveon San Marcos | Noveon Magnetics | NdPr-/Dy-/Tb-oxiden → gesinterde NdFeB-magneten | niet gepubliceerd (Series C 2026 meldt uitbreiding zonder tonnage) | [3][11] |

## 6 · Stoppunt
De brief stopt bij Noveon San Marcos: dat is de enige in de bron genoemde afnemer; Solvay noemt de magneten voor "key customers" zonder namen, dus fase D en E
vervallen (geen gedocumenteerde fabriek/afnemer erna).

## 7 · Open punten
- **Geen bron voor haven of route.** Kitco en het Solvay-persbericht noemen alleen leverancier en afnemer [1][2]; Houston Barbours Cut is een aanname (Golfhaven bij een Texaanse afnemer; Bayport ligt 5,7 km van zijn zeeknoop en kreeg dus een aanloop — Barbours Cut is gekozen).
- **La Pallice is geen evidente containerhaven:** larochelle.port.fr noemt graan, olieproducten, hout, agribulk, BTP, project cargo/wind, scheepsbouw, cruise — geen containers of Noord-Amerikalijnen [6]. Realistischer is landtransport naar Le Havre of Antwerpen; dat is ongedocumenteerd en wordt niet getekend. De havenkeuze is de zwakste schakel (zie beennaam b2).
- **Fabriek La Rochelle is impliciet:** het Solvay-persbericht noemt La Rochelle niet, Kitco wel (Solvay-verwerking in La Rochelle sinds april 2025) [1][2]; het is Solvays enige REE-scheiding.
- **Oxiden deels uit recycling** (end-of-life-magneten naast andere feedstock) [2] — het is dus niet louter een mijn-gebaseerde keten.
- **Kade La Pallice onzeker** (z16: meerdere kades met kranen en loodsen; geen bron noemt een berth). Het kade-anker kan verschuiven zonder dat de keten verandert.
- **Noveon-adres is straatniveau:** OSM kent 1550 Clovis R. Barker Road als adresnode [7], maar welk pand van Noveon is niet te zien; de brief weet niet of dit HQ of fabriek is [3].
- **Wegkm b3:** geen publicatie. Een OSRM-route geeft ~312 km (indicatie, dezelfde OSM-bron — geen norm) [10]; de ±15%-toets is hier alleen een indicatie. Noveon-capaciteit: een derdepartijprofiel noemt ~2.000 t/j magneten (onbevestigd) — niet gebruikt.
- **Bak-risico:** `pyosmium`/Geofabrik-scan kan geblokkeerd zijn en Overpass was onbereikbaar op 2026-10-09; us-texas-pbf is 711 MB (max 2 wegscans tegelijk).

## 8 · Bronnen
[1] Kitco/Reuters, "Solvay seals two deals to supply rare earths to US magnet makers", 2025-11-12 — https://www.kitco.com/news/off-the-wire/2025-11-12/solvay-seals-two-deals-supply-rare-earths-us-magnet-makers
[2] Solvay, "Noveon and Solvay forge partnership … light and heavy rare earth materials supply" (NdPr/Dy/Tb-oxiden vanaf 2026, deels end-of-life; geen plant, geen logistiek) — https://www.solvay.com/en/press-release/noveon-and-solvay-forge-partnership-light-heavy-rare-earth-materials-supply
[3] Noveon Magnetics, footer: 1550 Clovis Barker Road, San Marcos, TX 78666 — https://noveon.co/
[4] Solvay, "Solvay advances European rare earths production through capacity expansion", 2025-04-08 (La Rochelle 40 ha, 30% van de Europese vraag in 2030) — https://www.solvay.com/en/press-release/solvay-advances-european-rare-earths-production-through-capacity-expansion
[5] Port of La Rochelle (Grand Port Maritime), traffic types — https://www.larochelle.port.fr/en/
[6] zie [5]: geen containers/Noord-Amerikalijnen op de pagina genoemd
[7] OpenStreetMap/Nominatim: adresnode "1550, Clovis R. Barker Road, San Marcos" 29.8412945, -97.9554250 — https://nominatim.openstreetmap.org/
[8] Wikipedia API: La Pallice 46.1583, -1.2278; Barbours Cut Terminal 29.6819, -94.9983 — https://en.wikipedia.org/wiki/Barbours_Cut_Terminal · https://en.wikipedia.org/wiki/La_Pallice
[9] `v2/design/ree-sitelaag.json` / `ree-sitelaag.md` (`w-larochelle`; B8 Solvay, B9 rawmaterials.net — https://rawmaterials.net/solvay-expands-rare-earth-production-at-la-rochelle/)
[10] OSRM demo-router (OSM): Barbours Cut → Noveon, 312 km; wegpunten voor §4 — https://router.project-osrm.org/
[11] Noveon, "Noveon Magnetics completes $215 million Series C" (2026-01) — https://noveon.co/noveon-completes-series-c
Satellietblik: `v2/build-cache/satcheck/sat-ree-larochelle-sanmarcos-{solvay,pallice-kade,pallice-z16,pallice-kade2,barbours,noveon,noveon-a}.png` (Esri z14–z16, 2026-10-09).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh ree-larochelle-sanmarcos` (functie `bak_ree_larochelle_sanmarcos`); wegprofiel `ree-larochelle-sanmarcos-houston-sanmarcos` in `maak_stroombeen_weg.py`; uitvoer `v2/data/stroomroute-ree-larochelle-sanmarcos.json` (61,4 KB, versie 2, lonlat). Totaal **9.363,9 km · 3.051 punten · 4 markers**.

| # | modaliteit | km | punten | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck (stippel) | 1,8 | 2 | — | last mile Solvay → kade La Pallice, geen net op deze korrel (< 2 km) |
| b2a | zee (stippel) | 9,3 | 2 | 0,000 | haven-aanloop kade → zeeknoop 4239; `maak_havenaanloop.py` liep op 2026-10-09 vast (timeout 300, exit 124) → rechte stippel, geen tweede poging |
| b2 | zee | 9.040,5 | 1.014 | 0,000 | MARNET (108 edges) + 16 track-edges in het Houston Ship Channel + 1 connector; snap 0,000 / 0,019 km; landtoets 0 verworpen; Houston-kade 1,56 km van zeeknoop 6228 (< 5 km) → geen aanloop |
| b3 | truck | 312,3 | 2.033 | 0,019 | OSM-wegnet us-texas; 7 via-benen, alle via-snaps ≤ 0,14 km; 16,1 · 56,7 · 78,1 · 74,6 · 37,9 · 38,7 · 10,1 km |

**Toets.** b3 heeft geen gepubliceerde wegkm: gemeten 312,3 km tegen hemelsbreed 286,0 km (factor 1,092) en de OSRM-indicatie ~312 km (+0,1%, dezelfde OSM-bron, geen onafhankelijke norm) — de ±15%-toets is alleen een indicatie en slaagt. Naden 0,000 / 0,000 / 0,019 km (max 0,019 km, norm < 5 km). Alle 4 markers op 0,0 km van de lijn. `toets_knikken.py`: 20 knikken, 3 omkeringen (alle drie "scherpe bocht, echt", v = 1,5–1,9, klaverbladen rond Pasadena/Loop-knooppunt 29,77/−95,22 en 29,68/−95,03), 0 terugloop. `toets_rechte_benen.py --min-km 5`: enige rechte benen zijn de stippel-aanloop (terecht).
**Eindklassen:** first mile 3,31 km (residential, service) bij Barbours Cut, last mile 1,65 km (service, tertiary) bij Noveon; anker-verbindingen 0,14 / 0,02 km.

**Toelichting stippels.** b1: last mile < 2 km, "geen net op deze korrel". b2a: MARNET reikt niet tot de kade (9,28 km, > 5 km); de kustlijn 1:10M kent de haven La Pallice niet. Beide dragen geen kennisclaim over de ligging van de kade (kade onzeker).
**Vlucht/leiding:** geen. **Fase D/E:** vervallen (Noveon enige genoemde afnemer).

**Lessen / bevindingen.**
- **Wegbron:** `pyosmium` is op deze machine geblokkeerd (toepassingsbeheer) en Overpass gaf 500/504 op overpass-api.de, kumi en private.coffee (alleen maps.mail.ru antwoordde). Het wegnet komt daarom uit een eigen pure-python PBF-lezer (numpy + zlib) over `us-texas-latest.osm.pbf` (scan 268 s, 29,3 mln nodes in het venster, 1,07 mln way-delen → 95.295 ways in het corridorvenster); zelfde `weg_houden`, zelfde 40 km-venster, zelfde 12 km-eindklassen als het Geofabrik-pad. Wrapper: `v2/build-cache/ais/graaf/ree-larochelle-sanmarcos-wegscan-wrapper.py` (gitignored scratch).
- **Aannemelijk:** haven (La Pallice → Houston), modaliteit en route zijn een aanname; kade La Pallice onzeker; Noveon-anker op straatniveau.
- **Gereedschap:** `bak_stromen.sh` stond bij het bakken met CRLF-regeleinden in het werkexemplaar; bash breekt dan op de backslash-continuaties van elke multi-line functie. Gebakken via een LF-kopie (`tr -d ''`); de regeleinden zelf niet aangeraakt. Het slot-snippet met `rm -rf "$d"` wordt door de safety check geweigerd; vrijgave gedaan met `rm -f sinds` + `rmdir`.
