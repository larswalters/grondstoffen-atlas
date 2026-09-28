# Routebrief (licht) · nikkel — Cerro Matoso (Montelíbano) → Cartagena → Ningbo (Beilun, aannemelijk)

**stroom-id:** `nikkel-cerromatoso-cartagena` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** Colombiaans ferronikkel (CoreX Holding, ex-South32) van de Cerro Matoso-mijn+smelter
(Montelíbano, Córdoba) per truck over de Troncal de Occidente naar de exportkade van Sociedad Portuaria de
Cartagena (SPRC, Manga), per zeeschip (MARNET, aannemelijk via het Panamakanaal) naar de Ningbo–Beilun-losberth
(hergebruikt anker) — China is één van drie genoemde afzetmarkten, geen specifieke afnemer gebrond.
**Welke as van het verhaal:** de derde Colombiaanse nikkelas naar Azië — ferronikkel-granulaat, uitsluitend
voor roestvrijstaal. ≈40,2 kt Ni in ferronikkel, 2024 werkelijk (nameplate 50 kt Ni/j) [1][3]; ⚠️ productie
sindsdien onder druk door een gasleveringscrisis (§7).

## 1 · Ketenkaart
```
Cerro Matoso mijn+smelter `ni-cerromatoso-mina` (Montelíbano, Córdoba)
  ──(b1 truck · Troncal de Occidente via Planeta Rica–Sincelejo–Turbaco ·
      hemelsbreed ~278 km, geen wegkm)──►
SPRC-exportkade `ni-cartagena-sprc` (Manga, Cartagena de Indias)
  ──(b2 zee · MARNET, aannemelijk via Panamakanaal · China = één van drie markten)──►
Ningbo–Beilun-losberth `ni-beilun-losberth` (hergebruikt anker) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-cerromatoso-mina` → `ni-cartagena-sprc` | Troncal de Occidente (Ruta 25): Montelíbano–Planeta Rica–Sincelejo–Turbaco–Cartagena | hemelsbreed 278 km, geen wegkm gepubliceerd [berekend + 5][webcheck] | maak_stroombeen_weg | nee |
| b2 | B | zee | `ni-cartagena-sprc` → `ni-beilun-losberth` | MARNET, aannemelijk via Panamakanaal (China = één van drie genoemde markten, geen specifieke afnemer) [risico-ontwerp] | MARNET-uitkomst, niet vooraf berekend [webcheck grootcirkel ≈15.157] | MARNET | nee (beide kandidaat-kades <5 km van hun MARNET-zeeknoop, 1,9–3,7 km [haalbaarheidstoets]) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-cerromatoso-mina` | mijn + smelter (laadplek) | Cerro Matoso open-pit mijn + ferronikkelsmelter (CoreX Holding, ex-South32), Montelíbano, Córdoba | 7.9049, -75.5516 | [1][2][osm] | bron-gelegd (z15 gezien: actieve open-pit mijn met karakteristieke laterietbanden en het smeltercomplex incl. hoge schoorsteen ~600 m ten noorden ervan; marker in het midden van de put — mijn en smelter vormen samen één site-anker) |
| `ni-cartagena-sprc` | overslag (exportkade, zee) | Sociedad Portuaria de Cartagena (SPRC), Manga | 10.4062, -75.5342 | [haalbaarheidstoets][osm] | bron-gelegd (z15 gezien: bulk-/general-cargo kade met loodsen, kranen en afgemeerde schepen aan de Manga-oever; ligt duidelijk apart van de containerterminal CONTECAR 3,2 km verderop NW — bevestigt de haalbaarheidstoets dat CONTECAR de verkeerde kade was) |
| `ni-beilun-losberth` | losplek zee (hergebruikt anker, koper-/nikkelketens) | Ningbo–Zhoushan, Beilun-losberth | 29.9364, 121.883 | [koper-sitelaag] | hergebruikt — niet opnieuw satelliet-gelegd (werkwijze §1); al gelegd in vier andere nikkelketens, o.a. `nikkel-morowali-quzhou.md` en `nikkel-obi-ningbo.md`; kanttekening uit die brieven blijft staan: containerterminal/big-bag-lading, mogelijk niet de juiste bulkkade voor ferronikkel-granulaat |

## 4 · Via-punten (alleen b1 — corridorkeuze op de Troncal de Occidente)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Planeta Rica | 8.4077, -75.5840 | eerste corridorknoop N van de mijn; pint de route op de Troncal de Occidente (Ruta 25) i.p.v. een oostelijke omweg via San Marcos/Magangué |
| b1 | 2 | Sincelejo | 9.2973, -75.3927 | regionale hoofdknoop op de doorgaande N-25; sluit een westelijkere kustroute via Lorica/Coveñas uit |
| b1 | 3 | Turbaco | 10.3306, -75.4127 | laatste knoop vóór Cartagena; pint de aansluiting op de SPRC-kade in Manga i.p.v. een noordelijkere invalsweg naar de industriezone Mamonal |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cerro Matoso (Montelíbano) | CoreX Holding (ex-South32) | lateriet-erts (eigen mijn, niet getekend) → ferronikkel-granulaat | nameplate 50 kt Ni/j; 2024 werkelijk ≈40,2 kt Ni (88,6 mln lb) | [1][3] |

## 6 · Stoppunt
De brief stopt bij `ni-beilun-losberth`: geen bron noemt een specifieke Chinese roestvrijstaalfabriek als
afnemer van dit ferronikkel — het ontwerp zelf noemt "China" slechts als één van drie afzetmarkten (naast VS en
Europa), zonder specifieke afnemer. Fase C (Chinese verwerker) en fase D/E vervallen. Ningbo/Beilun volgt hetzelfde
patroon als `nikkel-morowali-quzhou` en `nikkel-obi-ningbo`: een aannemelijke, niet-gebronde vervolgbestemming op
basis van een al gelegd anker, geen specifieke lading-koppeling.

## 7 · Open punten
- **Geen gepubliceerde wegkilometer**: bronnen noemen alleen "per truck naar Cartagena, ~440 t/dag" zonder route
  of km — onafhankelijk bevestigd via mining-technology.com/newint.org: "13 trucks/day, equivalent to more than
  440 tonnes per day... shipped by sea from Cartagena" [haalbaarheidstoets-webcheck][5]. §1/§2 gebruiken daarom de
  hemelsbrede afstand (278 km) — de ±15%-toets geldt hier als indicatie, niet als norm.
- **BINDEND VERWERKT (haalbaarheidstoets):** CONTECAR (het ontwerp-voorstel) is bevestigd een containerterminal —
  vervangen door SPRC (Manga), het historische general-cargo/bulkterrein, beter passend bij ferronikkel-granulaat.
  Beide kandidaten liggen <5 km van hun MARNET-zeeknoop (1,9–3,7 km), dus geen haven-aanloop nodig.
- **China blijft één van drie genoemde markten** (China/VS/Europa) — geen specifieke Chinese afnemer gebrond;
  Ningbo/Beilun is een aanname op basis van het bestaande `nikkel-morowali-quzhou`/`nikkel-obi-ningbo`-patroon.
- **⚠️ Actueel operationeel risico, gevonden bij broncheck (niet in het ontwerp):** Canacol Energy diende
  28-04-2026 bij een rechtbank in Alberta een verzoek in om de gasleveringscontracten met Cerro Matoso te
  beëindigen — de mijn haalt ~80% van zijn gas bij Canacol en de hoogovens draaien 24/7 zonder energiealternatief;
  bij stopzetting dreigt structurele ovenschade (COP 500–730 mrd/oven, >10 maanden herstel) [8]. Mysteel meldt
  daarnaast een 40,43% YoY-daling van de ferronikkelproductie in Q4 2025 [9]. De uitkomst van de rechtszaak/
  leveringssituatie na 28-04-2026 is binnen het webbudget van deze ronde niet gevonden — het 40,2 kt-jaarvolume
  (2024) kan dus een overschatting zijn van de huidige (2026) output.
- **Eigenaarswissel:** South32 verkocht Cerro Matoso per 01-12-2025 aan een dochter van CoreX Holding (Robert
  Yüksel Yildirim); >US$100 mln, deels contingent op productie/nikkelprijs/vergunningen [6][7].
- **Via-punten b1 zijn indicatief** (bekende steden op de Troncal de Occidente/Ruta 25, niet zelf OSM-wegvertex-
  geverifieerd binnen het webbudget) — de bak-agent routeert over het echte OSM-wegnet.

## 8 · Bronnen
[1] Wikipedia, "Cerro Matoso mine" — locatie, geschiedenis, eigenaarschap. https://en.wikipedia.org/wiki/Cerro_Matoso_mine
[2] Mining Technology, "Cerro Matoso Nickel Mine, Colombia" — smeltercapaciteit 50.000 t/j, geïntegreerd mijn+smelter. https://www.mining-technology.com/projects/cerro-matoso/
[3] South32/CoreX Fact Sheet Nickel, november 2025 (PDF) — 2024-productie ≈40,2 kt Ni (88,6 mln lb). https://saportalanm.blob.core.windows.net/public-files/2025-12/Fact%20Sheet%20Nickel%2011%202025.pdf
[4] Geomechanics.io, "South32 completes Cerro Matoso ferronickel sale" — verkoop aan CoreX Holding, effectief 01-12-2025. https://www.geomechanics.io/news/article/south32-completes-cerro-matoso-ferronickel-sale-portfolio-shift-lens-for-mine-planners
[5] New Internationalist, 2016 — "We are slowly being killed by this mine": trucks vervoeren ferronikkel over smalle wegen naar Cartagena. https://newint.org/features/2016/11/01/we-are-slowly-being-killed-by-this-mine
[6] International Mining, 2025-07 — "South32 to sell Cerro Matoso ferronickel operation to CoreX Holding": dealstructuur, CoreX-achtergrond (opgericht 2024, Robert Yüksel Yildirim). https://im-mining.com/2025/07/07/south32-to-sell-cerro-matoso-ferronickel-operation-to-corex-holding/
[7] South32, "Sale of Cerro Matoso complete" — persbericht verkoop afgerond. https://www.south32.net/news-media/latest-news/sale-of-cerro-matoso-complete
[8] Rio Times Online, 2026-04 — "Colombia's Top Nickel Mine Faces Closure as Gas Supplier Pulls Out": Canacol-rechtszaak Alberta, ~80% gasafhankelijkheid, ovenschade-risico. https://www.riotimesonline.com/colombias-top-nickel-mine-faces-closure-as-gas-supplier-pulls-out/
[9] Mysteel, 2026 — "FLASH: South32 reports 40.43% year-on-year drop in ferronickel production for Q4 2025". https://www.mysteel.net/news/5112321-flash-south32-reports-4043-year-on-year-drop-in-ferronickel-production-for-q4-2025
[risico-ontwerp] Ketenontwerp voor `nikkel-cerromatoso-cartagena` (deze workflow-ronde) — risicoveld: "China één van drie genoemde markten (China/VS/Europa)".
[haalbaarheidstoets] Haalbaarheidstoets voor `nikkel-cerromatoso-cartagena` (deze workflow-ronde, bindend) — CONTECAR-weerlegging, SPRC-aanpassing, zeeknoop-afstanden 1,9–3,7 km.
[osm] OpenStreetMap (ODbL) via Nominatim — CONTECAR harbour 10,3779/-75,5072 · "Sociedad Portuaria de Cartagena" industrial landuse 10,40615/-75,53421 · Montelíbano 7,9801/-75,4167 · Planeta Rica 8,4077/-75,5840 · Sincelejo 9,2973/-75,3927 · Turbaco 10,3306/-75,4127. https://www.openstreetmap.org
[koper-sitelaag] `v2/design/koper-sitelaag.json` + eerdere nikkelbrieven (`nikkel-morowali-quzhou.md`, `nikkel-obi-ningbo.md`) — hergebruikt anker Ningbo–Beilun-losberth, 29,9364/121,883.
Satellietblik: `v2/build-cache/satcheck/sat-nikkel-cerromatoso-cartagena-mina.png`,
`sat-nikkel-cerromatoso-cartagena-sprc.png` (Esri z15, 2026-09-28).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**2 benen · 17.120,6 km · 7.424 punten · 3 markers · 144,6 KB.**

| # | fase | modaliteit | km | stippel? | naad met vorige been |
|---|---|---|---|---|---|
| b1 | A | truck | 380,5 km | nee (doorgetrokken) | 0,00 km (start) |
| b2 | B | zee | 16.740,1 km | nee (doorgetrokken) | 3,70 km (SPRC-kade → MARNET-zeeknoop) |

**Recept:** `bash v2/tools/bak_stromen.sh nikkel-cerromatoso-cartagena` (functie
`bak_nikkel_cerromatoso_cartagena` in `v2/tools/bak_stromen.sh`), profiel
`nikkel-cerromatoso-cartagena-mina-sprc` in `v2/tools/maak_stroombeen_weg.py`
(`--bron geofabrik`, extract `colombia`).

**b1 (truck, weg — nieuwe wegscan):** getekende lijn **380,5 km** tegen de
hemelsbrede 278 km uit §1/§2 (**+36,9%**). §7 zegt al dat bronnen alleen "per
truck naar Cartagena, ~440 t/dag" noemen zonder route of gepubliceerde km —
de ±15%-toets geldt hier daarom als **indicatie, geen norm**. Deze 380,5 km is
daarmee zelf de eerste "echte" (gescande, over het OSM-wegnet) wegkilometer
voor deze corridor en is het waard om in een volgende bronronde als
referentiewaarde terug te melden. Via-punten Planeta Rica / Sincelejo /
Turbaco waren indicatief (§7) en zijn door de scan bevestigd als corridor-
knopen op de Troncal de Occidente/Ruta 25 — geen omweg gemeten (10 keerlussen
gesnoeid, netto 0,0 km verschil). ⚠️ Anker-verbinding mijn → eerste
wegvertex = 0,99 km (> 0,5 km, bevinding — geen last-mile-stippel: onder de
~2 km-drempel van de lichte werkwijze); weg → kade = 0,04 km.
`toets_knikken.py`: 1 echte scherpe bocht (156,7°, R 9 m, bij 9.36698,-75.43567,
op de doorgaande weg — geen kopmaak/terugloop) + 9 spikes (alle <25 m radius,
OSM-zigzag op straatniveau); 0 terugloop.

**b2 (zee, MARNET-router):** **16.740,1 km** via het Panamakanaal (MARNET kiest
dit zelf, zoals de brief-aanwijzing vroeg — niet vooraf geforceerd). Snap
SPRC-kade → MARNET-zeeknoop **3,705 km** (binnen de brief-haalbaarheidstoets
1,9-3,7 km) en Beilun-losberth → zeeknoop **1,269 km** — beide **<5 km**, dus
geen haven-aanloop nodig aan beide kanten, exact zoals de bak-aanwijzing
voorschreef. `toets_knikken.py`: 7 krappe bochten op de MARNET-graaf (grootste
140,1° bij de Yangtze-mond, R 4.465 m — normale havenaanloop-geometrie), 0
omkeringen, 0 terugloop.

**Naad b1 → b2:** 3,70 km (SPRC-kade-uiteinde van het wegbeen tot de
MARNET-zeeknoop) — binnen de ≤5 km-norm van §5 van de bakhandleiding, geen
haven-aanloop nodig.

**Toetsen:** `toets_knikken.py` groen (0 terugloop) · `toets_rechte_benen.py
--min-km 5` geeft geen bevinding voor deze stroom · JSON: `versie: 2`,
`punt_formaat: lonlat`, beide modaliteiten in de toegestane set, elk been
≥2 punten, bestand 144,6 KB. Markers: ni-cerromatoso-mina en ni-cartagena-sprc
op 0 m van hun been (anker = routeerpunt); ni-beilun-losberth op 1.269 m
(anker ≠ routeerpunt — hetzelfde hergebruikte anker ligt in vier andere
nikkelketens op dezelfde afstand van zijn zeeknoop, zie `nikkel-morowali-
quzhou.md`/`nikkel-obi-ningbo.md`).

**Lessen / bevindingen:**
- De hemelsbrede 278 km uit §1/§2 was bewust een indicatie zonder norm-status
  (§7) — de gescande 380,5 km (+36,9%) bevestigt dat de indicatie flink kon
  afwijken; dit getal is nu de beste beschikbare wegkm-schatting voor deze
  corridor en verdient een vermelding in een toekomstige bronronde.
- Geen nieuwe satellietpas nodig voor `ni-beilun-losberth` (letterlijk
  hergebruikt anker, §3/§8) — bevestigt dat het lichte-werkwijze-hergebruik
  van bestaande ankers ook op de vierde/vijfde toepassing nog klopt.
- De open punten uit §7 (het operationele gasleverings-risico bij Cerro
  Matoso, de Q4-2025-productiedaling, de niet-gebronde specifieke Chinese
  afnemer) zijn ontwerp-/bronwerk en blijven onveranderd staan — het bakken
  raakt ze niet.
