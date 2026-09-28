# Routebrief (licht) · uranium — Arlit (Niger) → Cotonou (Benin)

**stroom-id:** `uranium-arlit-cotonou` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** yellowcake-concentraat van de SOMAIR-mijn bij Arlit (Agadez-regio, Niger) per **truck** over de
RN1 (Niger) en de RNIE2 (Benin) naar Parakou, vandaar per **spoor** (OCBN-noordlijn) naar de haven van Cotonou —
de historische exportroute van Nigerees uranium, **gestaakt sinds de grenssluiting Niger–Benin van 26-07-2023**.
**Welke as van het verhaal:** *landlocked en stilgevallen* — Niger produceerde historisch ≈2.000 tU/jaar (≈4% van
de wereldwinning, WNA) via SOMAIR; sinds juni 2025 volledig genationaliseerd (Orano verloor de operationele
controle al in dec. 2024), en Niger kondigde eind nov. 2025 aan zelf uranium te gaan verkopen via een nieuwe
staatsmaatschappij (TSUMCO, mei 2026) — de as ligt bevroren vóór juli 2023, niet gegarandeerd naar Orano/Frankrijk.

## 1 · Ketenkaart
```
Arlit/SOMAIR-mijn `u-arlit-mijn` ──(b1 truck · RN1 Niger, aannemelijk: één bron · ~1.270 km)──►
   grens Gaya/Malanville `u-grens-gaya-malanville`
   ──(b2 truck · RNIE2 Benin (Malanville–Kandi–Parakou) · ~330 km)──► Parakou-emplacement `u-parakou-emplacement`
   ──(b3 spoor · OCBN-noordlijn Parakou–Cotonou · ~400 km)──► Cotonou-haven `u-cotonou-haven`
   ── stoppunt (keten GESTAAKT sinds 26-07-2023; vervolg naar Frankrijk niet getekend, zie §6)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `u-arlit-mijn` → `u-grens-gaya-malanville` | RN1 Niger (Arlit–Agadez–Tahoua–Niamey–Dosso–Gaya), aannemelijk: één bron | ~1.270 [1][8] (afgeleid: 1.600 totaal Arlit→Parakou − ~330 Benin-been) | maak_stroombeen_weg (extract niger) | nee |
| b2 | A | truck | `u-grens-gaya-malanville` → `u-parakou-emplacement` | RNIE2 Benin (Malanville–Kandi–Bembèrèkè–Parakou) | ~330 [2][9] (RNIE2 Cotonou–grens 729 km − spoor 400 km ≈ 329; onafhankelijk Malanville→Parakou ≈322 km) | maak_stroombeen_weg (extract benin) | nee |
| b3 | A | spoor | `u-parakou-emplacement` → `u-cotonou-haven` | OCBN-noordlijn (Beninese spoorlijn, aangelegd 1936) | 400 [1][3] (lijnlengte 437 km incl. aftakkingen) | toets_spoorroute (extract benin) | nee |

Alle drie de benen zijn **doorgetrokken, niet gestippeld**: het net bestaat en is gemeten via gepubliceerde
lengtes — "gestaakt sinds 2023" is een statusfeit (zie §6), geen netafwezigheid (werkwijze §1).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-arlit-mijn` | mijn (kop van b1) | SOMAIR-mijn/verwerkingscomplex, Arlit | 18.7731, 7.3443 | [4][5][10] | bron-gelegd (z15 gezien: open dagbouwputten met blauwgroene restwater­plassen, verwerkingsgebouwen, tailings-bekkens direct rond het punt) |
| `u-grens-gaya-malanville` | grensovergang (b1→b2) | brug Gaya (Niger)–Malanville (Benin) over de Niger-rivier | 11.8807, 3.3961 | [10][11] | bron-gelegd (z15 gezien: de brug over de rivier tussen Gaya en Malanville, precies op de weg die beide oevers verbindt) |
| `u-parakou-emplacement` | overslag truck→spoor (b2→b3) | spoorstation "Gare", Parakou | 9.3487, 2.6099 | [10][11] | aannemelijk (z15 gezien: bebouwing in stedelijk weefsel bij het OSM-punt "Gare"; het spoortracé zelf en een eventueel apart vrachtemplacement zijn op deze korrel niet te onderscheiden van de rest van de stad) |
| `u-cotonou-haven` | loskade (einde b3) | Port Autonome de Cotonou | 6.3444, 2.4187 | [10][11] | bron-gelegd (z14 gezien: kademuur met kranen en aangemeerde schepen, havenbekken met golfbreker; géén apart mineralen-/uraniumterminal te onderscheiden — algemeen ladingsfront) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Agadez | 16.9726, 7.9907 | enige grote knoop tussen Arlit en Niamey; RN1 buigt hier van de mijnroute naar de zuidwaartse hoofdas |
| b1 | 2 | Tahoua | 14.8899, 5.2621 | RN1-tussenstad; sluit een alternatieve oostelijke omweg via Zinder uit |
| b1 | 3 | Niamey | 13.5248, 2.1098 | hoofdstad-knoop waar de RN1 de rivier de Niger volgt richting de zuidgrens |
| b1 | 4 | Dosso | 13.0496, 3.1945 | laatste grote plaats vóór de grens; pint de route op de doorgaande as naar Gaya i.p.v. een zijroute |
| b2 | 1 | Kandi | 11.1311, 2.9322 | RNIE2-knoop waar de route van de grens naar het zuiden afbuigt (alternatief oostwaarts naar Segbana uitgesloten) |
| b2 | 2 | Bembèrèkè | 10.2540, 2.7507 | tussenpunt op de RNIE2 tussen Kandi en Parakou, houdt de lijn op de doorgaande weg |

## 5 · Verwerkingsknopen
Geen — dit is een zuivere transport-/overslagketen (mijn → grens → spoorkop → zeehaven) zonder verwerking op
Nigerees of Benins grondgebied. Elke verwerking (conversie bij Orano/Comurhex Malvési) valt buiten deze keten (§6).

## 6 · Stoppunt
De brief stopt bij de Cotonou-haven: het ontwerp noemt als vervolg "Frankrijk (Orano/Comurhex Malvési)", maar de
haalbaarheidstoets stelt vast dat dat vervolg niet meer aannemelijk is — SOMAIR is sinds juni 2025 volledig
genationaliseerd, Orano verloor de operationele controle al in december 2024, en Niger kondigde eind november 2025
aan zelf uranium op de wereldmarkt te zetten via een nieuwe staatsmaatschappij (TSUMCO, mei 2026), ondanks een
ICSID-uitspraak van september 2025 in Orano's voordeel. Een eventuele hervatting zou dus via een ander
(staats-)kanaal en mogelijk andere afnemers lopen dan Orano/Frankrijk — fase D (Malvési) wordt hier niet getekend.

## 7 · Open punten
- **Exacte kade/berth voor uranium­concentraat in Cotonou is niet gevonden** — de haven heeft geen gedocumenteerd
  apart mineralenterminal; het anker ligt op het algemene ladingsfront (satellietbeeld toont kranen/kademuur, geen
  specifiek uraniumperron).
- **Het Parakou-emplacement (truck→spoor-overslag) is niet scherp gelokaliseerd** — het OSM-punt "Gare" is een
  gebouw in de stad; een apart vrachtstation/laadspoor voor concentraatvaten is op z15 niet te onderscheiden.
- **RN1-tracé in Niger is "aannemelijk: één bron"** (geen operator-gepubliceerde routebeschrijving gevonden, alleen
  de algemene WNA-vermelding van "trucked to Parakou"); de via-punten zijn plausibele knopen op de enige
  verharde as, niet zelf gebrond per punt.
- **Km-verdeling is afgeleid, niet direct gepubliceerd**: WNA noemt alleen het totaal (1.600 km Arlit→Parakou) en
  het spoorstuk (400 km); de knip bij de grens (~1.270 / ~330 km) is berekend uit de RNIE2-totaallengte
  (729 km Cotonou–grens) minus de spoorlijnlengte, niet uit een bron die specifiek het Niger- vs. Benin-deel meet.
- **Status van de 1.050 t gestrande voorraad (2023/2024, ≈€300 mln) is onbekend** — geen bron zegt of die nog in
  Niger, onderweg, of bij Cotonou ligt; niet als anker of volume in deze keten opgenomen.
- **Toekomstig afzetkanaal na eventuele hervatting is niet gebrond** (TSUMCO is pas mei 2026 opgericht) — geen
  fase D/E getekend, zoals besloten in §6.

## 8 · Bronnen
[1] World Nuclear Association, "Uranium in Niger" — historische route: 1.600 km truck Arlit→Parakou, 400 km spoor Parakou→Cotonou, export vnl. naar Comurhex/Frankrijk. https://world-nuclear.org/information-library/country-profiles/countries-g-n/niger
[2] Wikipedia, "Route nationale inter-états 2" — RNIE2 Cotonou–grens Niger, 729 km, via Parakou/Kandi/Malanville. https://fr.wikipedia.org/wiki/Route_nationale_inter-%C3%A9tats_2
[3] Wikipedia/Britannica, "Rail transport in Benin" / "Benin–Niger Railway" — OCBN-noordlijn Cotonou–Parakou, 437 km, aangelegd t/m 1936. https://en.wikipedia.org/wiki/Rail_transport_in_Benin
[4] Wikipedia, "SOMAIR" — Arlit-mijn, 63,4% Orano/36,6% Sopamin tot de nationalisatie; overname door de Nigerese staat 4-12-2024. https://en.wikipedia.org/wiki/SOMAIR
[5] Wikipedia, "Arlit mine" — coördinaten 18°46'23"N 7°20'39"E, 250 km noord van Agadez. https://en.wikipedia.org/wiki/Arlit_mine
[6] World Nuclear News, okt. 2024 — Orano staakt uranium­productie Arlit vanaf eind okt. 2024; 1.050 t concentraat op voorraad, waarde €300 mln. https://www.world-nuclear-news.org/articles/orano-suspends-operations-at-arlit
[7] NucNet, 10-5-2024 — Frankrijk/Orano staakt uraniumproductie uit Niger. https://www.nucnet.org/news/france-s-orano-to-halt-uranium-production-from-end-of-october-10-5-2024
[8] AfriqueXXI, "A Disappointing Future for Arlit" — achtergrond mijnstad en exportroute. https://afriquexxi.info/A-Disappointing-Future-for-Arlit
[9] Rome2Rio, "Malanville → Parakou" — reisafstand ≈322 km (200 mijl) over de RNIE2. https://www.rome2rio.com/fr/s/Malanville/Parakou
[10] OpenStreetMap (ODbL) via Nominatim — "Ancien Pont Gaya-Malanville" 11,8807/3,3961 · "Gare" Parakou 9,3487/2,6099 · "Port Autonome de Cotonou (PAC)" landuse-centroïde 6,3444/2,4187 · plaatsen Agadez/Tahoua/Niamey/Dosso/Kandi/Bembèrèkè. https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15) — `v2/build-cache/satcheck/sat-uranium-arlit-cotonou-mijn.png`, `sat-uranium-arlit-cotonou-grens.png`, `sat-uranium-arlit-cotonou-parakou.png`, `sat-uranium-arlit-cotonou-haven.png`.
[12] Al Jazeera, 20-6-2025 — Niger nationaliseert SOMAIR. https://www.aljazeera.com/news/2025/6/20/niger-nationalises-uranium-mine-as-spat-with-french-nuclear-giant-worsens
[13] World Nuclear News / Orano.group, 2025 — Orano verzet zich tegen nationalisatie-plannen SOMAIR (juni 2025), ICSID-uitspraak (sept. 2025) in Orano's voordeel, Niger kondigt eigen verkoop aan (nov. 2025)/TSUMCO (mei 2026). https://www.orano.group/en/news/news-group/2025/june/orano-opposes-nationalization-plans-of-somair-in-niger

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `uranium-arlit-cotonou`** → `v2/data/stroomroute-uranium-arlit-cotonou.json` — 3 benen, **2.118,9 km**, 12.525 punten, 4 markers. truck 1.353,7 + 323,2 = 1.676,9 km · spoor 442,0 km. Alle drie DOORGETROKKEN (geen stippel).
Recept: `bak_stromen.sh` (functie `bak_uranium_arlit_cotonou`).

**b1 (truck, extract niger, profiel `uranium-arlit-cotonou-arlit-grens`):** SOMAIR-mijn Arlit → Agadez → Tahoua → Niamey → Dosso → grens Gaya/Malanville (RN1 Niger). Eerste poging (WEG_HOUD kaal: motorway–secondary) faalde met "geen wegpad tussen punt 2 en 3" (Tahoua→Niamey); `corridorKlassen: [tertiary, unclassified]` toegevoegd — de RN1 draagt daar kennelijk geen primary/secondary-tag. Resultaat **1.353,7 km over 8.437 punten tegen ~1.270 km (afgeleid) = +6,6%**, ruim binnen ±15%. Snaps: plant 0,15 km · grens 0,20 km (alle ankerverbindingen ≤0,5 km).

**b2 (truck, extract benin, profiel `uranium-arlit-cotonou-grens-parakou`):** grens Gaya/Malanville → Kandi → Bembèrèkè → Parakou-emplacement (RNIE2 Benin). Eerste poging gaf een via-snap van **6,71 km** bij Bembèrèkè (>5 km, werkwijze §5) — vóór het bijschuiven eerst de wegklasse gecontroleerd: een osmium-query op de brief-coördinaat toonde geen primary/secondary binnen 8 km, alleen unclassified (0,39 km) en tertiary (1,13 km). Met `corridorKlassen: [tertiary, unclassified]` snapt Bembèrèkè op **0,39 km**. Resultaat **323,2 km over 3.303 punten tegen ~330 km = -2,1%**, binnen ±15%.

**b3 (spoor, extract benin, `BAKE_SUFFIX=-raw toets_spoorroute.mjs --van=9.3487,2.6099 --naar=6.3444,2.4187`):** Parakou-emplacement → Cotonou-haven (OCBN-noordlijn). Console bevestigt "3260717 spoor-edges" (1-op-1-net). Beide uiteinden vallen TERUG op de dichtste spoorknoop van een **geïsoleerd component van 455 km** (dichtstbijzijnde hoofdnet 198-232 km weg, > `--max-snap` 60) — de terugval is hier de juiste uitkomst: Benin's spoornet hangt aan geen ander land (brief §1/§3). Resultaat **442,0 km over 73 edges tegen 400 km (WNA) = +10,5%** / tegen de lijnlengte 437 km = +1,1% — beide binnen ±15%. Eén OMKERING gemeten (161°, boogstraal ~133 m, bij 6,35600/2,42750, nabij Cotonou) — een echte kopmaak-plek (`toets_knikken.py`: v=2,0, geen terugloop), geen fout.

**Toets:** naden tussen de drie benen **0,0 m** (b1→b2) en **21,9 m** (b2→b3, rondingsverschil tussen de wegroute-eindsnap en de spoorroute-startsnap) — ruim binnen de norm van ≤5 km. `toets_knikken.py`: 69 knikken ≥60° over de hele stroom, waarvan **4 omkeringen ≥150°, 0 daarvan TERUGLOOP** — alle vier zijn echte scherpe bochten (RN1-haarspeldbochten in Niger + de spoorkop bij Cotonou), geen te repareren defect. `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de lijst (geen ongewenste rechte lijn ≥5 km). json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, spoor}, elk been ≥2 punten, bestandsgrootte **227,9 KB** (< 300 KB). Markers: Arlit-mijn 0,1 m · grens Gaya/Malanville 0,1 m · Parakou-emplacement 0,0 m · **Cotonou-haven 166,8 m** (anker ≠ routeerpunt — het spoorbeen eindigt op de dichtstbijzijnde spoorknoop van het havenemplacement, niet op het exacte kademuur-anker; conform brief §3/§7, geen apart mineralenterminal gedocumenteerd).

**Gereedschapslessen:**
- Een via-snap > 5 km is een signaal om eerst de wegklasse te controleren, niet het via-punt te verschuiven: bij Bembèrèkè bevestigde een directe osmium-query op de brief-coördinaat dat de corridor daar geen primary/secondary-tag draagt (werkwijze §5) — `corridorKlassen` bracht de snap van 6,71 naar 0,39 km zonder één coördinaat aan te raken.
- Een geïsoleerd spoorcomponent (hier 455 km, ver onder `--hoofd-km` 1.000) hoeft niet met een lagere `--hoofd-km` "gefixt" te worden: de terugval-melding is hier zelf de juiste uitkomst, want er is geen groter net om op te snappen binnen `--max-snap` 60 km — Benin's OCBN-net is écht geïsoleerd (brief §1).
- "Gestaakt sinds 2023" is een statusfeit in de brief, geen stippel-reden: alle drie de benen zijn doorgetrokken omdat het net bestaat en gemeten is (werkwijze §7) — de operationele status hoort in de tekst, niet in de lijnstijl.
