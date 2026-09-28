# Routebrief (licht) · kobalt — Ambatovy (Moramanga) → Toamasina (Madagaskar)

**stroom-id:** `kobalt-ambatovy-toamasina` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** lateriet-slurry van de Ambatovy-mijn bij Moramanga per **ondergrondse zwaartekracht-pijpleiding** (220 km, ~1.000 m hoogteverschil) naar het proces-/raffinaderijterrein bij Toamasina, waar nikkel én kobalt tot metaal worden geraffineerd — de kade ligt al aan het net, maar geen bron noemt een naam-en-adres-afnemer, dus de brief stopt op het terrein.
**Welke as van het verhaal:** *Madagaskars enige leiding-modaliteit in de kobaltketen* én een keten middenin een eigendomswissel: Sumitomo's 54%-belang is in **mei 2026 al verkocht** aan het AMRI-consortium (Essenwood Partners/Jason Kluk, ex-hoofd nikkelhandel Glencore, + het Zuid-Afrikaanse Zungu Investments), naast KOMIR (45,82%) [9][10]. Cycloon **Gezani** (11-02-2026) trof Toamasina en legde de raffinage ruim vier maanden stil; herstart 23-05-2026 (eerste zuurfabriek), volledig operationeel eind juni [4][6]. Jaarvolume 2024-2025 structureel onder de 60 kt Ni/j-nameplate: Ni 28-31 kt/j, **Co 2,5-4,0 kt/j** (t/j 2.500-4.000) [3].

## 1 · Ketenkaart
```
Ambatovy-mijn/ertsvoorbereiding, Moramanga `co-ambatovy-moramanga` ──(b1 leiding · slurry, schematisch — geen OSM-way · 220 km)──►
Ambatovy proces- en raffinaderijterrein, Toamasina `co-ambatovy-plant` ⏹ stoppunt (fase D vervalt — één terrein, geen tweede fabriek gebrond)
  ⋯ (been B niet getekend) ⋯ Ambatovy-raffinaderijkade, Port of Toamasina `co-toamasina-kade` (marker, 3,8 km van een MARNET-zeeknoop; geen naam-en-adres-afnemer)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `co-ambatovy-moramanga` → `co-ambatovy-plant` | Ambatovy slurry-pijpleiding, ondergronds, zwaartekracht-gedreven (~1.000 m hoogteverschil), ~60 cm diameter — **bevestigd niet als doorlopende OSM-way gekarteerd** (35 `man_made=pipeline`-ways in de madagaskar-extract, alle bij Vohipeno/elders, niet op deze corridor) [1][2][11] | 220 (Ausenco/EIB — vaste bron) [1] | stippel "leiding (schematisch — geen OSM-way)" | **ja**, conform de eigen valkuil in het ontwerp; bevestigd door de directe pyosmium-scan van `madagaskar-latest.osm.pbf`, geen keuze meer |
| — | B | zee | `co-ambatovy-plant` → `co-toamasina-kade` → (geen afnemer) | markt: Europese/Japanse roestvrijstaal-/batterijsector, geen naam-en-adres | n.v.t. | niet getekend | n.v.t. — stoppunt; Toamasina-kade ligt al 3,8 km van een MARNET-zeeknoop, geen haven-aanloop nodig zodra er ooit een afnemer gebrond wordt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-ambatovy-moramanga` | mijn / ertsvoorbereiding (kop) | Ambatovy Mine, Moramanga (open lateriet-dagbouw + ertsvoorbereiding) | -18.8446, 48.3077 | Wikipedia-geohack 18°50′42″S 48°18′25″E [2] + OSM/Nominatim "Ambatovy Mine Société anonyme" [11] + satelliet | **bron-gelegd** (z15 gezien: uitgestrekte lateriet-dagbouwputten met karakteristieke oranje/beige afgravingsterrassen aan weerszijden van een centrale bedrijfsweg, met een gebouwencluster/procesterrein pal op het kruispunt) |
| `co-ambatovy-plant` | proces- en raffinaderijterrein (staart van b1, stoppunt fase D) | Ambatovy Plant Site, Toamasina (HPAL-raffinaderij, ~320 ha) | -18.2002, 49.3604 | OSM/Nominatim "Ambatovy Plant Site" (node 1529311150) [11] + satelliet | **bron-gelegd** (z15 gezien, deels bewolkt: donker verkleurde procesgebouwen en tankinstallaties op een industrieterrein tussen de spoorlijn en de kustweg, ~10 km zuid van de haven — komt overeen met de gepubliceerde "11 km zuid van Port of Toamasina" [1][5]) |
| `co-toamasina-kade` | overslag land → zee (marker, stoppunt been B) | Ambatovy Bulk Jetty Terminal / Port of Toamasina | -18.1556, 49.4278 | Ausenco (finger pier, 2 ligplaatsen, pijpband-conveyor naar railcar-loadout) [5] + portcode.net (18°09′20″S 49°25′40″E) [12] + OSM "Toamasina Port" [11] + satelliet | **bron-gelegd** (z15 gezien: finger pier met kranen/hijswerk, containers en bulklading op de kade, duidelijk aangelegde havenwerken direct aan de kustlijn) |

## 4 · Via-punten
Geen — been A is een schematische stippellijn zonder OSM-geometrie (geen corridorkeuze te tekenen); been B wordt niet getekend.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ambatovy Plant Site, Toamasina | AMRI (54,18%, sinds mei 2026) + KOMIR (45,82%) | lateriet-slurry → nikkel-/kobaltmetaal (HPAL + raffinage, incl. precursor-/zuurfabrieken) | nameplate 60 kt Ni/j; gemeten 2024-2025: Ni 28-31 kt/j, Co 2,5-4,0 kt/j; na cycloon Gezani ~2.500 t Ni + ~250 t Co in juni 2026 | [1][3][6][9] |

## 6 · Stoppunt
De brief stopt op het Ambatovy-terrein bij Toamasina: mijn en raffinaderij zijn via de slurry-pijpleiding rechtstreeks verbonden (geen tussenknoop), en geen bron noemt een specifieke afnemer voor het geraffineerde nikkel/kobalt — alleen de markt (Europese en Japanse roestvrijstaal- en batterijsector). Fase B (zee) blijft daarom ongetekend; de kade-marker staat er wel, voor als er ooit een naam-en-adres-afnemer gebrond wordt.

## 7 · Open punten
- **Geen naam-en-adres-afnemer voor het metaal na Toamasina** — alleen marktregio's gedocumenteerd, geen specifieke smelter/klant; been B blijft daarom een stoppunt zonder lijn.
- **Pipeline-lengte: 220 km (Ausenco/EIB, in het ontwerp als vaste bron) tegen 200 km bij Wikipedia** — beide bronnen genoemd in §8; de brief volgt de Ausenco/EIB-bron zoals voorgeschreven, het verschil (~9%) is niet verder te herleiden zonder een derde bron.
- **`co-ambatovy-plant` is site-niveau, niet perceel-niveau** — het OSM-punt "Ambatovy Plant Site" ligt in een gedeeltelijk bewolkt satellietbeeld; de exacte grens tussen raffinaderij, tankfarm en eventuele precursorlijn is op dit beeld niet te onderscheiden.
- **Eigendomswissel loopt door tijdens dit ontwerp** — AMRI nam Sumitomo's belang in mei 2026 over; toekomstige afzetkanalen (en dus een eventuele fase B/C) kunnen daardoor nog veranderen.
- **Cobalt-cijfer is een t/j-bandbreedte uit één vakpersbron (Skillings)**, niet een officieel jaarverslagcijfer — geen tweede bron gevonden ter bevestiging.

## 8 · Bronnen
[1] Ausenco, "Ambatovy Nickel Project: World's first commercial nickel laterite slurry pipeline" — 220 km ondergrondse slurrypijpleiding, ~1.000 m hoogteverschil, zwaartekracht-gedreven. https://ausenco.com/projects/worlds-first-commercial-nickel-laterite-slurry-pipeline/
[2] Wikipedia, "Ambatovy mine" — mijncoördinaat 18°50′42″S 48°18′25″E; pijpleiding "200 km" (afwijkende bronvermelding, zie §7); productie ~40 kt Ni / ~4 kt Co (2022). https://en.wikipedia.org/wiki/Ambatovy_mine
[3] Skillings, "Nickel market outlook 2026: Ambatovy resumes operations after cyclone" — Ni 28-31 kt/j, Co 2.500-4.000 t/j (2024-2025), nameplate 60 kt Ni/j. https://www.skillings.net/nickel-market-outlook-2026-ambatovy-resumes-operations-after-cyclone/
[4] CNBC Africa, "Madagascan miner Ambatovy resumes nickel production after cyclone" — cycloon Gezani (11-02-2026, Toamasina); herstart eerste zuurfabriek 23-05-2026, tweede eind juni; ~2.500 t Ni + ~250 t Co in juni 2026; KOMIR + Sumitomo (verkocht mei 2026) financierden het herstel. https://www.cnbcafrica.com/2026/madagascan-miner-ambatovy-resumes-nickel-production-after-cyclone
[5] Ausenco, "Ambatovy Nickel Project: Toamasina Port" — finger pier met 2 ligplaatsen, 4 ontvangsttrechters, pijpband-conveyor naar railcar-loadout, capaciteit 2,8 Mt/j bulkimport; plant "enkele kilometers" van de haven. https://ausenco.com/projects/ambatovy-nickel-project-toamasina-port/
[6] Mining.com / Reuters, "Madagascan miner Ambatovy resumes nickel production after cyclone" — productiehervatting-tijdlijn, vier maanden stilstand. https://www.mining.com/web/madagascan-miner-ambatovy-resumes-nickel-production-after-cyclone
[7] Mining Weekly, "Sumitomo finances Ambatovy stake sale to exit project, sources say" — ontwerp-bron, Sumitomo's exit-traject. https://www.miningweekly.com/article/sumitomo-finances-ambatovy-stake-sale-to-exit-project-sources-say-2026-06-08
[8] Mining.com, "Ex-Glencore trader part of Ambatovy nickel takeover, documents show" — AMRI/Essenwood Partners, Jason Kluk (ex-hoofd nikkelhandel Glencore) + Zungu Investments; verkoop al afgerond. https://www.mining.com/web/ex-glencore-trader-part-of-ambatovy-nickel-takeover-documents-show/
[9] Billionaires.africa, "South African billionaire Sandile Zungu, ex-Glencore trader Jason Kluk to take over Sumitomo's failed Madagascar nickel mine" (2026-05-02) — AMRI (Jersey), 54%-overname afgerond mei 2026, KOMIR 45,82% blijft. https://www.billionaires.africa/2026/05/02/south-african-billionaire-sandile-zungu-ex-glencore-trader-jason-kluk-to-take-over-sumitomos-failed-madagascar-nickel-mine/
[10] Finance News Network, "Glencore Veteran Leads Sumitomo's Ambatovy Nickel Divestment" — $445 mln verlies voor Sumitomo op de verkoop, cumulatief verlies ~400 mrd yen (~$2,6 mld); Essenwood Partners + Zungu Investments. https://www.finnewsnetwork.com.au/archives/finance_news_network4693009.html
[11] OpenStreetMap via Nominatim (ODbL), bevraagd 2026-09-28 — "Ambatovy Mine Société anonyme" (way 179216028, -18,84458/48,30770), "Ambatovy Plant Site" (node 1529311150, -18,20022/49,36043), "Toamasina Port" (way 183964495, -18,15865/49,42721); directe pyosmium-scan van `madagaskar-latest.osm.pbf` op `man_made=pipeline` gaf 35 ways, geen op de Moramanga→Toamasina-corridor. https://www.openstreetmap.org
[12] portcode.net, "Tamatave (Toamasina) Ambatovy Bulk Jetty Terminal" — havencode + coördinaat 18°09′20″S 49°25′40″E. https://portcode.net/madagascar/tamatave-toamasina/tamatave-toamasina-ambatovy-bulk-jetty-terminal/
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-kobalt-ambatovy-toamasina-mijn-moramanga.png`, `sat-kobalt-ambatovy-toamasina-plant-toamasina.png`, `sat-kobalt-ambatovy-toamasina-kade-toamasina.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `kobalt-ambatovy-toamasina`** → `v2/data/stroomroute-kobalt-ambatovy-toamasina.json` — 1 been, **132,1 km**, 2 punten, 3 markers (leiding, stippel).
Recept: `bak_stromen.sh` (functie `bak_kobalt_ambatovy_toamasina`).

**b1 (leiding, stippel, enige been):** `--stippel "leiding|Ambatovy slurry-pijpleiding Moramanga → Toamasina (schematisch — geen OSM-way)|-18.8446,48.3077|-18.2002,49.3604"` — rechte lijn tussen de twee ankers, **132,1 km** (hemelsbreed). Geen geometrie-tool: bevestigd door de haalbaarheidstoets uit de opdracht (pyosmium-scan van `madagaskar-latest.osm.pbf` op `man_made=pipeline` gaf 35 ways, geen op deze corridor — de enige benoemde ligt bij Vohipeno).

⚠️ **Lengtetoets buiten de norm, bevinding niet dichtgetrokken:** 132,1 km tegen de gepubliceerde 220 km (Ausenco/EIB) = **−40,0%**, ruim buiten ±15%. De pijpleiding is een ondergrondse zwaartekracht-leiding met ~1.000 m hoogteverschil die het reliëf van Madagaskar's oostelijke escarpement volgt (Moramanga op het hoogland, Toamasina aan de kust); een rechte stippellijn tussen kop en staart is per constructie de hemelsbrede afstand en kan het bochtige, hoogteverschil-volgende trace niet weergeven. Dit is dus geen meetfout maar een eigenschap van de stippel-conventie op een corridor met een groot hoogteverschil (analoog aan het bochtige spoor- of wegtracé elders, maar hier zonder een gekarteerde geometrie om tegen te toetsen). Buiten de norm = bevinding, geen via-punt of omweg-correctie toegepast — er is geen corridorkeuze om te tekenen (brief §4: geen via-punten).

**Markers:** `co-ambatovy-moramanga` (kop, 0 m van de lijn) · `co-ambatovy-plant` (staart, 0 m van de lijn) · `co-toamasina-kade` (losse marker, geen been/stippel-regel ernaartoe — fase B is bewust niet getekend, brief §6).

**Toets:** `toets_knikken.py` — 0 knikken ≥60°, 0 omkeringen. `toets_rechte_benen.py --min-km 5` — 1 been gevonden (🟠 GROOT, stippel, omwegfactor 1,000): correct geclassificeerd als stippel-met-reden, geen bevinding op zichzelf. json geldig: versie 2, punt_formaat lonlat, modaliteit `leiding` (in de toegestane set), 1 been met 2 punten, bestandsgrootte 0,85 KB (ruim < 300 KB). Geen naad te meten — één been, geen opeenvolgende segmenten.

**Gereedschapslessen:**
- Een stippel-been dat een gepubliceerde lengte draagt (geen schatting) blijft normaal toetsbaar tegen ±15% — maar op een corridor met een groot hoogteverschil en een bochtig trace geeft de rechte-lijn-conventie van een stippel structureel een te lage hemelsbrede afstand. De ±15%-norm veronderstelt impliciet een corridor die redelijk recht loopt; bij een sterk kronkelend of hoogteverschil-volgend traject (hier ~1.000 m over de korte hemelsbrede afstand) is de afwijking een eigenschap van de conventie, niet van de meting. Buiten de norm blijft een bevinding, geen reden om alsnog een geometrie te verzinnen.
- Een marker voor een stoppunt zonder getekend been (hier de kade, fase B niet getekend) hoeft geen `--been`/`--stippel`-regel te krijgen — `--marker` alleen volstaat om het punt in de sitelaag/gloed te laten oplichten zonder een lijn te claimen die de brief expliciet niet trekt.
