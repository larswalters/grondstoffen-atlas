# Grondstoffen Atlas — project spec

*Categorie: General · Linear-project: "Grondstoffen Atlas" (team Lars / LAR) · Laatst bijgewerkt: 2026-07-19 (M24.1 gestart: Rijn Done + aftakken op elk punt Done)*

> **🚢 M24.1 GESTART (2026-07-19, laatste) — DE RIJN STAAT ([LAR-492] Done) EN VAARWEGEN ZIJN NU EEN NET
> ([LAR-504] Done).** Live t/m `b402fc5` (`?v=022`), visuele go van Lars: *"Rotterdam Kehl ziet er goed
> uit."* **→ VOLGENDE: [LAR-505] Maas + Benelux-delta** (nieuw), daarna [LAR-493] Main + [LAR-494] Donau
> = de as Rotterdam→Zwarte Zee compleet, dan [LAR-495].
>
> **De Rijn als twee ketens:** `rijn` Nijmegen→Bingen **355,0 km** (officieel rkm 884,6−528 = 356,6 →
> **−0,4%**) · `rijn-boven` Bingen→Basel **360,6 km** (358,1 → **+0,7%**). Aanleiding: álle
> searoute-Rijnhavens snapten op knoop 9697, het binneneinde van `waal`, van Duisburg 75,8 km tot Kehl
> 389,4 — het Nijmegen/Memphis-patroon over een hele as. **Haventoets** (searoute = andere bron dan OSM),
> snap vóór→na: Duisburg 75,8→**1,5** · Koblenz 207,3→**0,7** · Keulen 130,1→**1,1** · Mainz 266,1→**1,4**
> · Karlsruhe 360,3→**1,9** · Kehl 389,4→5,6 · Straatsburg 388,0→9,4 km (die laatste twee liggen in een
> zijbekken, niet aan de doorgaande geul). Havens >50 km 1.449→**1.430**. Corridor-toets 0 m, beide
> aansluitingen 0,00 km. **Regressie exact:** 6818→9654 **19.610** · 6391→6818 **8.031** · R'dam→Nijmegen
> 172 · A'dam→Shanghai 19.677 · R'dam→Memphis 10.000 · R'dam→Wuhan 20.626. Netwerk 9.863→**9.910**
> knopen, 16.110→**16.157** edges.
>
> **⚠️ HET SPLITSPUNT UIT HET ISSUE KLOPTE NIET.** Voorgesteld was `zeevaart=True`→`False` bij
> Keulen/Duisburg, maar `waal` stroomafwaarts staat al op `zeevaart=False` — dat zou zeggen dat
> zeeschepen Duisburg wél halen en Rotterdam niet. De vlag is bovendien **alleen metadata**
> (`marnet.js` geeft `meta.vaarwegen` door; de browser leest er enkel `bron` uit). De échte waarde van
> splitsen zit in het **passage-label = een eigen `vermijd`-knop**. Besluit van Lars: knip waar een
> **verstoring** zit. Bij **Kaub** legde het laagwater van 2018/2022 de as stil, en dat reproduceert
> exact: met `rijn-boven` in `vermijd` blijven Duisburg 281 km en Keulen 373 km bereikbaar en vallen
> Mainz/Karlsruhe/Kehl weg.
>
> **⚠️ LARS' VERVOLGVRAAG LEGDE EEN ONTWERPFOUT BLOOT** (*"we moeten nog wel meer mappen dan alleen de
> rijn, de maas en stukken biesbosch"*): M24 bakte **lijnen** — een vervolgsysteem hing aan
> `keten_eind[volgt_op]`, dus uitsluitend aan het **uiteinde** — terwijl een riviernet **aftakkingen**
> heeft. Bijt op zes plekken: Main bij Mainz (30 km ín `rijn-boven`), Ohio bij Cairo ([LAR-496] zegt het
> zélf al), Illinois bij Grafton, Nieuwe Merwede, Bergsche Maas, Amsterdam-Rijnkanaal; later Mosel en
> Neckar. **[LAR-504]:** `hecht_aan_keten()` zoekt de dichtstbijzijnde plek op de voorganger en knipt
> die edge door — `(a,b)` → `(a,nieuw)` + `(nieuw,b)`, hetzelfde passage-label en dezelfde soort. **De
> knip valt ALTIJD op een bestaande geometrie-vertex**, dus er verschuift geen enkele coördinaat en de
> corridor-toets van de moederketen blijft per constructie geldig. Bewijs: `marnet.bin`, `marnet.json`
> én `ports.json` komen **byte-identiek** uit de bake. ⚠️ Nog **niet** bewezen: een route dwars *door*
> een aftakking heen — dat is de acceptatie van [LAR-505].
>
> **DRIE LESSEN VOOR DE REST VAN DE UITROL.**
> 1. **De namen-survey is nu gereedschap** — `v2/tools/survey_vaarwegen.py` rangschikt de benoemde
>    vaarwegen in een venster op **lengte** mét hun lon/lat-**strekking**; aan die strekking zie je of de
>    whitelist een *doorlopend* traject dekt. Ving twee stille ketenbreuken: **`Boven-Rijn`** (mét
>    koppelteken, 4,3 km) is de enige schakel tussen `Bijlandsch Kanaal` en `Rhein`, en
>    **`Le Rhin / Rhein`** is de gecombineerde grensnaam op het Frans-Duitse traject — de
>    `Dunaj / Duna`-val, nu vóóraf gevangen in plaats van achteraf.
> 2. **Kijk waar de GEUL ligt, niet welke landen de rivier raakt.** Tussen Basel en Straatsburg loopt de
>    vaargeul in het **Grand Canal d'Alsace**, volledig op Frans grondgebied; zonder de nieuwe extract
>    **`fr-alsace`** knipt de keten met een gat van **72,9 km** — en beide randen van dat gat heten óók
>    `Grand Canal d'Alsace`.
> 3. **Water ≠ vaarweg.** `Vieux Rhin / Altrhein` (54 km) bewust NIET gewhitelist: de Restrhein is wél
>    water maar géén bevaarbare geul en zou een korter, onvaarbaar pad geven. Zelfde principe als de
>    ≥150 m-klaring bij de Amazone.
>
> **Bijvangst:** Geofabrik gebruikt nog de **pre-2016 Franse regio-indeling** — `alsace`,
> `basse-normandie` (136 MB) en `rhone-alpes` (500 MB) bestaan, **`normandie` niet**, en die geeft geen
> 404 maar een bestand van **0 bytes** (de Brazilië-shapefile-val) → controleer de bestandsgrootte, niet
> de HTTP-status. Daarmee is het open punt uit de uitrol-brief beantwoord vóór [LAR-495]. Verder draait
> de hele vaarwegenset nu op het Geofabrik-pad en zijn de acht bestaande systemen **coördinaat voor
> coördinaat identiek** aan de Overpass-set. Gecorrigeerd: `now.md` noemde 9.877/16.124 waar
> `marnet.json` op 9.863/16.110 stond. Zie `memory/decisions.md` +
> [[2026-07-19-grondstoffen-atlas-lar492-rijn-aftakmechanisme]].

> **🛤️ M25-BRONNENPLAN VASTGELEGD (2026-07-19, laatste, plansessie zonder code) — COMPLEET SPOORNET
> GEKOZEN. Startissue [LAR-491] (High, Todo), zelfstandig leesbaar. → VOLGENDE: eerst M24's uitrol
> afmaken (M24.0–M24.5, LAR-492..503); Lars wil wegen en sporen bewust pas daarna.**
> **Context die het gesprek kantelde:** land is de **grootste** groep, niet de kleinste — geteld in
> `data/`: **275 landstromen** (134 spoor + 105 weg + 36 pijpleiding) tegen **223 zeestromen**. M22–M24
> waren drie milestones voor de zeekant; land heeft in `v2/` nog **nul** geometrie.
> **Besluit van Lars: het complete hoofdspoornet, géén corridor-scope** (*"complete spoor is wel beter
> zeker voor de simulator"*) — hetzelfde argument dat in M23 al won: een netwerk beantwoordt vragen die
> je niet vooraf hebt uitgerekend. Blokkeer `grens-kasumbalesa` en met een compleet net **ís** Lobito of
> Dar es Salaam de uitkomst; met corridor-scope kan M21 alleen verstoringen tonen die we vooraf bedachten.
> Dat verwerpt de derde afbakening uit de milestone ("vooraf gebakken corridors — land hoeft niet
> herrouteerbaar te zijn voor de simulator"): die tekst is van vóór de drie **land**knelpunten.
> **Gelaagd zoals water:** compleet spoor = de MARNET-rol · de verhalende corridors (Kasumbalesa, Lobito,
> Gashuunsukhait, Ruili) = de `EXTRA_VAARWEGEN`-rol, apart gebakken en op lengte gecontroleerd, mét
> passage-label = de M21-knop.
> **Bron per modus** (de drie zijn níet gelijk bedeeld): **spoor** = OSM via Geofabrik-pbf, meetlat NARN
> (VS) / RINF-lengtes (EU) / gepubliceerde lijnlengtes elders — de enige landmodus mét zowel goede
> geometrie als een echte scheidsrechter · **pijpleiding** = OSM waar goed (TAPS 0,15 km puntafstand,
> ADCOP 1% van ADNOC's cijfer) + **GEM's openbare GitHub-repo** voor de rest · **weg** = Overture of
> Overpass per corridor en **bewust klein**, want weg heeft als enige **géén** scheidsrechter (GRIP4 valt
> af op vier tegenstrijdige licentieclaims).
> **⚠️ Op land verliest de corridor-toets z'n kracht** — "≤250 m van een middellijn" was sterk bewijs
> omdat water schaars is; op land ligt élke verkeerde route ook dicht bij een weg. De LAR-487-les
> (*lengte beslist, niet puntafstand*) is hier geen verfijning maar **het hele fundament**.
> **Het filter werkt door UITSLUITING, niet door insluiting** — `usage=main` eisen sloopt precies Afrika
> en Zuidoost-Azië: **40% (Myanmar) tot 43% (China)** van de spoor-ways draagt géén `usage`-tag, en in
> Myanmar dragen die 843 km = 13% van het net. Gevalideerd tegen gepubliceerde route-lengtes met de
> nieuwe tool **`v2/tools/meet_spoor.py`** (`55d6c5a`): Cambodja 652 km (~650) · Myanmar 6.643 (6.207,6
> volgens het ministerie, **+7%**). Scan **34 s voor 1,56 GB** → wereldwijd een half uur.
> **⚠️ DE STAP DIE M24 NIET NODIG HAD: parallelle sporen samenvouwen.** China meet **266.146 km tegen
> 109.767 gepubliceerde route-km (+142%)** — geen meetfout: `tracks=2` staat op maar 5.406 ways, dus
> vrijwel al het dubbelspoor is als twéé losse lijnen gemapt. Gevolg (a) de lengtetoets meet er 2,4× te
> veel, (b) de graaf verdubbelt gratis mee met nul routeerwaarde. **Rivieren komen niet in paren.** Bouw
> dit vóór pilot 1; kies als eerste ijkpunt een expliciet enkelsporige lijn (Sishen–Saldanha 861 km).
> **Budget:** wereld gefilterd ≈ 1,9–2,4M km → routeergraaf **190–240k knopen bij 10 km** (past, is het
> niveau dat het fundament-plan al accepteerde), maar ruwe tekengeometrie ~11M punten ≈ **36 MB** (past
> niet). **Vorm ≠ routering** — bij water droeg één `LineSegments` beide taken, bij spoor niet meer;
> M24's `strak_trekken()` is de kandidaat-oplossing.
> **Pijpleidingen zonder formulier.** GEM's downloadformulier vraagt naam/e-mail/organisatie; Lars
> opperde een verzonnen identiteit — niet gedaan, en overbodig: `GlobalEnergyMonitor/GOIT-GGIT-pipeline-
> routes` staat openbaar (5.163 routes / 1,92M km). Centraal-Azië–China **1.838,5 km** tegen CNPC's 1.833
> (**0,3%**) waar OSM er 4,1 km van heeft; Petroline **0 km in OSM** tegen 1.190 bij GEM. ⚠️ De repo
> draagt **geen LICENSE-bestand** — vastzetten vóór live. Droezjba blijft bewust een benadering.
> **Afgevallen mét bewijs (niet opnieuw onderzoeken):** NE spoor (926.446 km nagemeten; Noord-Amerika 56%
> van NARN; Azië dateert van vóór de Chinese uitbouw) · NE wegen (3,89 km puntafstand) · GRIP4 · gROADS ·
> OGIM (92,9% Noord-Amerika, oostelijk halfrond mediaan 76 km) · HIFLD Open (opgeheven 2025) · ENTSOG
> (alleen PDF) · HDX railways (2014). **ERA RINF valt níet af maar heeft géén geometrie** — alleen
> lengtes per baanvak; daarmee de beste EU-meetlat en categorisch onbruikbaar als bron.
> **Open bij de start van M25:** pilotkeuze (voorstel VS/EU/Mongolië óf Copperbelt–Lobito) · GEM-licentie ·
> dedup vóór of tijdens pilot 1 · knoopafstand 5 of 10 km. Zie `memory/decisions.md` +
> [[2026-07-19-grondstoffen-atlas-m25-bronnenplan-landroutes]].

> **🚢 M24-UITROL OPGEZET (2026-07-19, laatste) — TWEE NIEUWE CAPABILITIES + YANGON EN AMAZONE ERBIJ.**
> Live t/m `45a21eb` (`?v=021`). **→ VOLGENDE: de uitrol uitvoeren; die staat klaar als 6 milestones
> M24.0–M24.5 met 12 issues [LAR-492]…[LAR-503]** (per regio een milestone, issues per systeem —
> Lars' indeling). Aanbevolen volgorde: M24.1 Europa (grootste tonnage + officiële meetlat) → M24.2
> Noord-Amerika (Ohio = kolen, nodig bij M26) → de rest.
>
> **1 · `fetch_waterways.py geofabrik` — lokale regio-extracts i.p.v. de Overpass-API.** Overpass was
> de traagste én broosste stap van de pijplijn (~25 min voor 6 systemen tegen ~1 min bakken, met 504's
> op queries die minuten eerder gewoon slaagden). Nu **40 regio's / 17 GB in ~6 min** (44,8 MB/s), en
> daarna offline en herhaalbaar. **Gevalideerd, niet aangenomen:** hetzelfde systeem via beide paden
> gehaald → **coördinaat voor coördinaat identiek, 0,000 m afwijking**. Overpass blijft bestaan als
> kruiscontrole; de filters spiegelen de clauses exact. Shapefile viel af (Geofabrik genereert die
> niet voor Brazilië/Rusland → 0 bytes). **Nieuwe build-dependency: `pyosmium`** (osmium 4.3.1).
>
> **2 · `v2/tools/middellijn_uit_vlakken.py` — middellijn AFLEIDEN uit watervlakken.** Nodig omdat de
> Amazone tussen Manaus en de monding géén benoemde middellijn heeft: >10 km breed, dus als wátervlak
> gemapt. Herbruikbaar voor Rio de la Plata, estuaria en stuwmeren. Aanpak: watervlakken rasteren →
> per watercel de **klaring** (afstand tot de oever; exacte afstandstransformatie, anisotroop) →
> alleen cellen met **≥150 m klaring** gelden als bevaarbaar — *dat encodeert "commercieel bevaarbaar"
> in de geometrie zélf* → Dijkstra met milde voorkeur voor het midden → `strak_trekken()` + simplify.
> Bewust géén medial axis. Een systeem met een `vlakken`-blok gaat door dit pad; de rest van de
> pijplijn (baker, corridor-toets, `volgtOp`) merkt het verschil niet.
>
> **Twee systemen erbij:** `yangon` 23,2 km — de M23-stub uit [LAR-485] is weg (snap 21,8 → **1,3 km**;
> Rotterdam→Yangon 14.989 km) · `amazone` **1.261,9 km** Macapá→Manaus — snap **1.084 → 0,9 km**, het
> grootste gat in het hele netwerk (Rotterdam→Manaus 9.268 km; klaring min 0,44 / mediaan 1,60 / max
> 7,61 km; haventoets Óbidos 3,15 km van de lijn). **Regressie exact:** 6818→9654 **19.610**,
> 6391→6818 **8.031**; Mississippi 1.032 / Yangtze 1.016 onveranderd. Netwerk **9.877** knopen /
> **16.124** edges; havens >50 km 1.471 → **1.449**.
>
> **⚠️ DRIE REGELS VOOR WIE DE UITROL DOET** (alle drie duur geleerd):
> 1. **Namen opzoeken, niet raden.** Met de extract lokaal: 51.191 ways in 4 s → `ရန်ကုန်မြစ်`
>    (Yangon), `လှိုင်မြစ်` (Hlaing). Een blinde query op "Yangon River" geeft nul segmenten.
> 2. **Rangschik kandidaten op LENGTE, niet op vertex-aantal.** Vertex-dichtheid meet detailniveau,
>    niet belang — brede rivieren zijn als vlak gemapt met spaarzame middellijn. Op vertices stond de
>    Rijn 6e en vielen Donau/Wolga/Paraná/Amazone weg. Dat ving vier fouten: de Donau draagt
>    **gecombineerde grensnamen** (`Dunaj / Duna`, `Dunărea - Дунав` — zonder die twee knipt de keten
>    bij elke grens door), de Wolga-Don heet voluit `…им. В. И. Ленина`, `扬子江` bestaat niet, en de
>    Amazone heeft géén benoemde middellijn.
> 3. **Trapjes weg met bewijslast, niet met tolerantie.** De 8-richtingen-Dijkstra kwantiseert op 45°;
>    DP-simplify haalt dat er niet uit want de treden (445 m) zijn **groter** dan de tolerantie
>    (250 m). `strak_trekken()` = het `simplify_water()`-principe. Effect 312 → **83 punten en 4,4%
>    korter** — het was dus ook een lengtefout, geen cosmetica.
>
> **Uitrol-regel (Lars):** *"als er geen commercieel boten kunnen varen dan niet, of als het echt
> nergens heen leidt, maar het moet wel uitgebreid zijn voor de simulator."* Criterium 2 snijdt het
> scherpst — een vaarweg die niet aan het zeenetwerk hangt is een **geïsoleerde component**: Congo
> boven Kinshasa, Paraná boven Itaipú, Mekong boven de Khone-watervallen, Nijl boven Aswan vallen af.
> **Schaal:** ~40–50 systemen (Lars: *"ik dacht dat je meteen veel meer rivier/kanalen zou hebben in
> Brazilië maar het is er maar 1"* — het eerste plan was te grof). Goedkoper dan het klinkt: de meeste
> rivieren staan wél als benoemde lijn in OSM en gaan door het snelle pad.
> Volledige brief: `v2/design/binnenvaart-uitrol.md`. Zie ook `memory/decisions.md` +
> [[2026-07-19-grondstoffen-atlas-geofabrik-vlakken-uitrolplan]].

> **✅ LAR-487 + LAR-488 DONE (2026-07-19, laatste) — DE M24-PILOTREEKS NL→VS→CHINA IS COMPLEET.**
> Lars' visuele go: *"ik heb even gekeken naar die test routes dat ziet er wel goed uit mooi over de rivier"* → beide op Done. Alle drie de controle-situaties bewezen: twee onafhankelijke bronnen (NL) ·
> officiële meetlat (VS) · géén scheidsrechter (China).
> Live t/m `919b046` (`?v=018`). **Beide zones eindigden ergens anders dan hun naam suggereert:** MARNET's
> `mississippi`-tak gaat vanaf New Orleans **niet de rivier op maar het Pontchartrainmeer in** en loopt dood
> (knoop 113) → traject werd New Orleans→Baton Rouge→Memphis; de `yangtze`-zone ("Nanjing–Jiangyin") eindigt bij
> **Zhenjiang** (knoop 9668), 78 km vóór Nanjing. Vooraf snapte Memphis **532,7 km** weg (fictieve route 303 km) en
> Wuhan **528,4 km** (240 km) — het Nijmegen-patroon van M23.
> **Nieuw mechanisme `volgtOp`:** het zeevaart-beleid (zeevaart t/m Baton Rouge resp. Nanjing, daarboven binnenvaart)
> past niet in één keten met één vlag → een vervolgsegment hangt aan het **binneneinde van zijn voorganger** i.p.v.
> aan MARNET, **zónder polygoon-toets** (dat punt ligt al op een corridor-getoetste keten). Eén rivier draagt zo twee
> labels met elk een eigen zeevaart-vlag én een eigen `vermijd`-knop voor M21/M26; beide hechtten op **0,00 km**.
> Ketens: `mississippi` 218,8 km (zeevaart) · `mississippi-boven` 813,1 · `yangtze` 92,7 (zeevaart) · `yangtze-boven` 683,6.
> **Nieuwe tool `v2/tools/toets_usace.py`** (USACE National Waterway Network, `GEO_CLASS='I'` + `FUNC_CLASS<>'N'`):
> mediaan **76 m** / p95 409 m over 760 punten (NL-bake-off ~80 m). De staart (3,8% >500 m, max 1.889 m) is
> **OSM-vs-USACE kanaalverschil, níet onze simplify** — de rúwe 801-punts lijn heeft dezelfde max (DP-simplify
> selecteert bestaande vertices); geconcentreerd op de oxbow-stretch lon −91,15…−91,49. **Beslissend is de lengte,
> niet de puntafstand** (een fout gevolgde oxbow ligt overal dicht bij íets): onze ketens samen **1.028,2 km = 638,9
> river miles** tegen de officiële span New Orleans (mile 95)→Memphis (mile 736) van **641 mijl** → **0,3%**.
> Bijvangst: USACE zet deep-draft (`FUNC_CLASS='B'`) t/m **river mile 237**, Baton Rouge ligt op ~229 — de
> scheidsrechter bevestigt het splitspunt van de zeevaart-vlag zelf. ⚠️ **De corridor-toets bewijst procesintegriteit,
> geen bronkwaliteit** (hij vergelijkt de keten met de bron waaruit hij gebakken ís → per definitie 0 m).
> **China zónder scheidsrechter: de havens bevestigen zichzelf** — negen searoute-havens (andere bron dan OSM) vallen
> vanzelf op de keten (Wuhan **0,7** · Jiangyin 1,2 · Wuhu 1,9 · Nanjing 2,5 · Anqing 2,9 · Zhenjiang 5,2 · Jiujiang 7,1 km);
> herbruikbare toets voor Paraná/Mekong/Congo.
> **Tests:** regressie exact tussen de oude knoop-ids (6818→9654 **19.610**, 6391→6818 **8.031**) · Amsterdam→Shanghai
> 19.677 via `noordzeekanaal` · R'dam→Nijmegen 172 via `waal` · New Orleans→Memphis **1.032 km** (officieel 641 river
> miles = 1.032) · Shanghai→Wuhan **1.016** · R'dam→Wuhan 20.626 · R'dam→Memphis 10.000 · beide labels in `vermijd` →
> geen route · snaps Memphis 532,7→**5,9** / Wuhan 528,4→**0,7** / Baton Rouge 87,6→**3,1** / Nanjing 77,9→**2,5** ·
> netwerk 9.698→**9.812** knopen, 15.945→**16.059** edges, bin 1.165→**1.170 KB**, havens >50 km 1.471→**1.452**.
> **⚠️ Overpass is nu de traagste + broosste stap** (~25 min voor 6 systemen vs ~1 min bakken): de mirrors gaven
> massaal 504's. Mijn eerste diagnose was fóút — "query te zwaar" → timeout 600 s, waardoor één overbelaste mirror de
> run tien minuten gijzelde vóór failover, terwijl de query gemeten **74 s** duurt. Gericht gefixt: client-timeout
> (180 s) **los van** server-timeout (300 s), **exacte tag-match i.p.v. naam-regex** (Overpass indexeert `key=value`),
> CEMT-clause alleen voor systemen mét CEMT-klasse (buiten de EU bestaat de tag niet en die clause heeft als enige géén
> naamfilter), `overpass.osm.jp` eruit (kapot certificaat), retry-rondes, en een **schijf-cache op de query-inhoud**
> zodat een herstart nooit opnieuw begint. **→ VOLGENDE: go/no-go wereldwijde uitrol**
> (Paraná, Irrawaddy/Yangon-stubs, Wolga, Mekong, Congo, Grand Canal) + restpunten [LAR-485]. Zie `memory/decisions.md` +
> [[2026-07-19-grondstoffen-atlas-lar487-488-vs-china-pilots]].

> **🎨 LOD-ONTWERPBRIEF VASTGELEGD (2026-07-19, ontwerpsessie zonder code) — M26 = HERONTWERP MET SEMANTISCHE
> ZOOM, startpunt [LAR-490] (High, Todo).** Spec = **`v2/design/lod-ontwerpbrief.md`** (commit `08f2341`;
> 3 referentiebeelden in `v2/design/referenties/` + als bijlage op het issue). Kern: inzoomen levert **nieuwe
> informatie** i.p.v. grotere pixels — semantische zoom in ~4–5 banden op `getAltitude()`, **hiërarchisch
> nodemodel** (`level`+`parent`, hotspots build-time geaggregeerd zoals de bakers), flows aggregeren mee
> (bundeling gratis via het M23-netwerk). Besluiten Lars: **glow-bollen géén hoogte-pilaren** (beeld 1 =
> stijlreferentie; doelbeeld = combinatie mockups + v1-look, go/no-go op de bol bij de koper-pilot) ·
> **lijndikte hybride** (meters op volume + pixel-minimum → ribbon/`Line2` + glow-shader vanaf het begin) ·
> **data-ambitie C** (koper-pilot volledige site-hiërarchie top-±15–30 échte sites op ~100 m + capaciteit;
> rest per grondstof, M5–M17-patroon) · **night-side** = voorkeur, testen met visuele check in de pilot.
> **Volgorde hard: M24 (bezig) → M25 → LAR-490** — M25 is een hárde afhankelijkheid (regionaal/lokaal =
> land-transport; zonder M25 zwevende lijnen). Technische valkuilen staan in de brief (tegel-schil-hoogte,
> geometrie-LOD <5 km, positionele juistheid uit M24/M25; tegelgrenzen zijn géén probleem — flows zijn eigen
> 3D-geometrie). Zie `memory/decisions.md` + [[2026-07-19-grondstoffen-atlas-lod-ontwerpbrief]].

> **✅ LAR-486 DONE (2026-07-19, laatste) — NL-PILOT AF; BRON-KEUZE DEFINITIEF: OSM = geometrie overal, UNECE/USACE =
> meetlat + klasse-bron** (Lars' go: *"ik zie geen fouten"*, varianten visueel identiek; doorslaggevend = OSM
> scriptbaar/wereldwijd vs UNECE Cloudflare-handwerk + EU-only). Restanten opgeruimd (`8458047`: toggle +
> `marnet-unece.*` weg, `?v=017`, na opruiming geverifieerd). **→ VOLGENDE: LAR-487 (Mississippi × USACE) /
> LAR-488 (Yangtze) — ~1 min per bake dankzij de verzoening-cache.** Hieronder de pilot-details: Lars vergelijkt
> [OSM](https://larswalters.github.io/grondstoffen-atlas/v2/?vers=016) vs
> [UNECE](https://larswalters.github.io/grondstoffen-atlas/v2/?vaarwegbron=unece&vers=016) en kiest de bron.**
> Gebouwd (commit `d9a9e0f`, `?v=016`): **`v2/tools/fetch_waterways.py`** — middellijnen per systeem met een
> bron-agnostische stitcher (dijkstra kortste waterpad anker-zee→anker-binnen over de segment-geometrie, DP-simplify
> 25 m); OSM via Overpass (scriptbaar), UNECE uit de Blue Book ArcGIS-laag `Transportobservatory/E_Waterways_ITIO`
> (⚠️ achter Cloudflare — via de Browser-pane; NL-extract mét CEMT + `SEA_VESSEL` in `build-cache/unece_eww_nl.geojson`).
> **`EXTRA_VAARWEGEN` in `bake_marnet.py`**: ketens `soort=1`, knoop per ~15 km, **passage-label per systeem**
> (`noordzeekanaal`, `waal` — meteen het `vermijd`/M21-mechanisme) + zeevaart-vlag in `meta.vaarwegen`;
> **corridor-toets** (elk punt ≤ 250 m van de bron-middellijn, gemeten 0 m) vervangt de vlak-toets; zee-overgang
> geldig bij NE-water óf `WATERWEG_ZONES` (Maasmond-knoop 6812 = `zone:nl-delta` — de eerste twee 40-min-bakes
> strandden op een water-only-check). **Verzoening-cache**: de deterministische M23-herberekening (~35–40 min) →
> `build-cache/verzoening_cache.json` (19 KB) → élke volgende bake ~1 min. **Browser**: `?vaarwegbron=unece` laadt
> de UNECE-set (bin+json+ports als sét — de haven-snap hangt aan de knopenlijst van die bake); ODbL/UNECE-attributie
> in de HUD; `window.HAVENS`/`window.zoekRoute` als test-handvat.
> **Tests (beide varianten groen):** zeenet exact onaangetast — R'dam→Shanghai **19.610** / Duluth→R'dam **8.031**
> tussen de **oude** knoop-ids (regressie in 2 lagen, aangescherpt door Lars: nieuwe snaps mógen verschuiven) ·
> **Amsterdam vaart via IJmuiden** (noordzeekanaal→gibraltar→suez→…, haven-tot-haven **−131 km**, visueel bevestigd) ·
> R'dam→Nijmegen 172 km over `waal` · snaps Amsterdam 15,1→**0,8** / Nijmegen 79→**2,1** / Dordrecht 15,9→**3,8** km ·
> netwerk 9.698 knopen / 15.945 edges, bin 1.165 KB. **Bake-off:** bronnen onderling mediaal ~80 m; advies =
> **OSM-geometrie + UNECE/USACE-meetlat** (UNECE: handwerk + EU-only). Ná de keuze: uitslag in LAR-485/486,
> variantbestanden (`marnet-unece.*`, `ports-unece.json`, toggle) opruimen, dan LAR-487/488 (~1 min per bake).
> Bijvangst: [LAR-489] AIS-realisme-check (EMODnet, backlog). Zie `memory/decisions.md` +
> [[2026-07-19-grondstoffen-atlas-lar486-nl-pilot-bake-off]].

> **🧭 M24 GEPLAND (2026-07-19, eerder) — BRONNENPLAN STAAT. → VOLGENDE: NL-pilot [LAR-486] (bake-off OSM vs UNECE) in een verse sessie.**
> Plansessie, géén code. **De corridor-toets vervangt de vlak-toets:** rivieren/kanalen bestaan niet als water in de
> NE-polygonen (dáárom waren de 29 `WATERWEG_ZONES` vrijstellingen en eindigt Yangon als stub) → elke binnenwater-edge
> wordt getoetst als "elk ~2 km-monster ≤ ε van een **bevaarbare-vaarweg-middellijn**"; de polygoon-toets blijft
> alleen op de zee-overgang gelden (mondings-knoop op een MARNET-knoop in NE-water). Een wereldwijde kant-en-klare
> bevaarbare-vaarwegen-dataset **bestaat niet** (geverifieerd) → **bake-off beslist de bron**: LAR-486 bouwt NZK +
> Waal (R'dam→Nijmegen) **twee keer** — uit **OSM** (enige wereldwijde bron mét kanálen + CEMT-tags; Overpass) én
> uit de **UNECE E-waterway-shapefile** (Blue Book) — en vergelijkt kwaliteit/moeite/beeld. **USACE NWN** = de
> VS-meetlat (LAR-487, Mississippi stroomopwaarts); China-pilot (LAR-488, Yangtze→Wuhan) bewust **zónder**
> scheidsrechter = de zwaarste controle-situatie, valideert de wereldwijde uitrol. NE-rivers (géén kanalen: geen
> NZK!) en HydroRIVERS (DEM-afgeleid) afgevallen. **Besluiten Lars:** pilots per regio vóór de uitrol · einddoel =
> **het complete commercieel bevaarbare net** (EU CEMT ≥ IV, VS USACE-net, elders de commerciële systemen — *"zodat
> een nieuwe grondstof de wegen gewoon kan gebruiken"*) · **labels nú meebakken** (passage-label per systeem +
> zeevaart-vlag NZK/Yangtze-t/m-Nanjing/Seaway; router permissief, filteren via `vermijd` = meteen M26/M21-klaar).
> OSM = ODbL → "© OpenStreetMap contributors" in de HUD. LAR-487/488 blocked by 486; de volledige besluiten-sectie
> staat in LAR-485. Acceptatie NL-pilot: **Amsterdam vaart via IJmuiden uit**, Nijmegen-snap 79 km → <5 km,
> regressie Duluth→R'dam 8.031 / R'dam→Shanghai 19.610 onveranderd. Zie `memory/decisions.md` +
> [[2026-07-19-grondstoffen-atlas-m24-bronnenplan]].

> **✅ M23 KLAAR (2026-07-18, eerder) — MARNET VERZOEND + HAVEN→HAVEN-ROUTERING. LAR-483 Done na Lars' go:**
> ***"het zee gedeelte lijkt klaar te zijn, het ziet er realistisch uit."*** **→ VOLGENDE: M24 · binnenwater ([LAR-485], Todo).**
> Lars' eigen test-vondst: Amsterdam vaart uit via IJsselmeer→Afsluitdijk→Den Helder i.p.v. het Noordzeekanaal —
> gemeten verklaard: **MARNET hééft geen Noordzeekanaal-edge** (Amsterdam snapt op de Markermeer-knoop, 15,1 km;
> zelfde patroon: Nijmegen 79 km / Hengelo 76 km / Born 93 km — geen Rijn/Waal in MARNET). Besluit Lars: geen
> quick-fix, netjes in M24. LAR-485 is zelfstandig leesbaar (EXTRA_VAARWEGEN-mechanisme, rivierhaven-stubs,
> de 2 restedges, binnenvaart-beleid).
> Live op https://larswalters.github.io/grondstoffen-atlas/v2/ t/m `b6867f7`. **LAR-483 exact uitgevoerd, maar tegen de
> 1:10M-vectorwereld** (vector = waarheid; het issue noemde nog `geo-data.js` 1:50M — dat was van vóór M22).
>
> **De verzoening (`v2/tools/bake_marnet.py`, deterministisch, build-time):** graaf **9.686 knopen / 15.933 edges**
> (lon genormaliseerd — ⚠️ MARNET heeft **15 knopen dubbel op lon +180 én −180**; zonder merge is de trans-Pacific
> bij de datumgrens doorgeknipt en rekent Yokohama→LA 32.000 km via Suez+Panama) · edges **grootcirkel-verdicht**
> (10 km) · getoetst op ~2 km met shapely tegen exact de gerenderde polygonen, **meren = water** (`ne_10m_lakes`;
> loste Grote Meren/Seaway, IJsselmeer, Wolga-stuwmeren in één klap op — 508→243 verdachte edges) · classificatie
> **aanloop** (≤5 km van een knoop: dokbekken/riviermond, ok) / **binnenwater** (93 edges in 29 zones: Suez, Panama,
> Mississippi, Seaway, Wolga-Don, Paraná, Elbe, Delaware, Hooghly, Yangtze, Gironde, Severn, ICW, Maracaibo, Congo,
> Columbia, Kuskokwim/Kobuk; als-is bewaard met `soort=1`) / **kapot** (150) · **148/150 omgelegd** — lokale A* in
> **vier trappen** (0,02° gebufferd → 0,01° gebufferd → 0,01° kaal → 0,02° kaal; de kustbuffer knijpt nauwe straten
> als de Dardanellen/Inside Passage dicht, dus de kale herkansing is verplicht) + simplify met land-bewijs +
> **eindtolerantie per uiteinde gemeten op de oorspronkelijke koorde** (knopen liggen soms zelf in een dokbekken).
> **2 onopgelost** (Södertälje-archipel, Channel Islands-koorde — origineel behouden, connectiviteit intact).
> Benodigd voor een rebake: `ne_10m_{land,minor_islands,lakes}.geojson` in `v2/build-cache/` (gitignored) +
> shapely/numpy/searoute (build-only).
>
> **Naar de browser:** `v2/data/marnet.bin`+`json` (**1,17 MB**, world-10m-varint-patroon) + `ports.json` (3.962
> searoute-havens gesnapt aan de dichtstbijzijnde knoop, mediaan 31 km). **`v2/src/marnet.js`**: het hele net als
> **één LineSegments** (vertex colors: blauw=zee, amber=binnenwater) · CSR-adjacency · **A\*-router ~3 ms** met
> **passage-restricties — default `northwest` dicht, exact searoute's eigen default** (kortste graafpad ≠
> commerciële route: zonder restrictie koos R'dam→Shanghai de Noordwest-Passage; géén arctis-straf nodig gebleken).
> **Dit restrictie-mechanisme ís M21**: "Suez dicht" = `"suez"` toevoegen aan `opties.vermijd`. HUD: laag-toggle +
> **route-test haven→haven** (datalist alle havens, km/ms/passages). ⚠️ Cache-discipline geldt óók voor data:
> `marnet.bin`/`ports.json` dragen `?v=` mee (nu 011) — bump bij elke bake.
>
> **Gemeten (allemaal realistisch):** R'dam→Shanghai **19.610 km** via gibraltar+suez+babalmandab+malacca
> (searoute ≈ 19,5k) · Antofagasta→Shanghai **18.915** op de 50°N-lane (**searoute 18.880 = de M18-benchmark**;
> v1 dwong 19.970 af via `wp-pac-zuid` — het netwerk vindt de echte lane nu vanzelf) · Yokohama→LA **9.111** ·
> Duluth→R'dam **8.031** dwars door Meren+Seaway (17 binnenwater-edges) · Novorossiysk→Shanghai **15.792** via
> bosporus+dardanelles+suez. **Daarmee zijn LAR-483's drie problemen structureel weg**: bundeling gratis (routes
> delen edges), één versie per edge, antipodaal deterministisch (Valparaíso→Shanghai 19.220, +1,9%).
>
> **Open:** visuele go Lars (dan LAR-483 Done, M22-precedent) · **cosmetisch → M24:** rivierhavens (Yangon e.d.)
> eindigen als rechte stub over land (rivier bestaat niet in de polygonen; binnen de gemeten eindtolerantie) + de
> 2 restedges. Zie `memory/decisions.md` + [[2026-07-18-grondstoffen-atlas-m23-marnet-netwerk-verzoend]].

> **✅ M22 KLAAR (2026-07-18) — DE NIEUWE WERELDBOL STAAT IN `v2/`. LAR-484 Done. → VOLGENDE: M23 (LAR-483).**
> Live op https://larswalters.github.io/grondstoffen-atlas/v2/ (t/m `4dd48d5`). **Buiten `v2/` is niets aangeraakt.**
> Lars' visuele go: *"dit is echt goed… nu kunnen we die vectorlijnen als bron van waarheid gebruiken en de view
> opties zijn top zo."*
>
> **Wat er staat:** Three **r185** + **ES-modules met importmap** (geen bundler, geen build-stap — Three levert
> sinds r150 geen `three.min.js` meer, dus het globals-patroon van v1 vervalt binnen `v2/`) · **ACES-beeldpijplijn**
> · **vectorwereld Natural Earth 1:10M** (481.675 punten, **1,64 MB**, één draw call) · **Esri-satelliettegels tot
> z19** met zoom tot **~1 km hoogte** · ondergrond (satelliet/kaart/egaal) en kustlijn (aan/uit) als **losse lagen**.
>
> **HET KERNBESLUIT: de vectorwereld is de WAARHEID, satelliet/tegels zijn een SKIN.** Daarmee is de kwaal die M22
> nodig maakte — drie wereldmodellen die het oneens zijn — structureel weg: routering rekent straks tegen exact
> dezelfde lijnen die Lars op zijn scherm ziet. Detailwinst t.o.v. het oude 1:50M: puntafstand **7,7 → 1,5 km**,
> grootste gat **628 → 55 km**, Japan 16× / Hormuz 94× / Baja 11× / Malakka 7× meer punten.
>
> **⚠️ VIER DINGEN VOOR WIE HIERNA CODE SCHRIJFT IN `v2/`:**
> 1. **lat/lon → 3D volgt EXACT v1's `latLonToVec3`** (`x = cos(lat)·cos(lon)`, `y = sin(lat)`,
>    `z = −cos(lat)·sin(lon)`). Moet tegelijk kloppen met de UV-afbeelding van `THREE.SphereGeometry` (lon 0 op +X)
>    **én** met de markers/routes die in M26 uit v1 komen. Een 90°-fout hier zag er onderling perfect uit (Sumatra
>    wás Sumatra) maar lag los van de bol — en had in M26 alles verschoven.
> 2. **Zoom rekent in HOOGTE boven het oppervlak**, niet in afstand tot het middelpunt. Alles wat met zoom schaalt
>    (sleepsnelheid, tegelniveau, de opheffing van de kustlijn) hangt aan `getAltitude()`. Dat was de eigenlijke rem:
>    de camera kwam nooit lager dan ~930 km.
> 3. **De `index.html` zelf zit in de Pages-cache** (`max-age=600`) en verwijst naar de oude `?v=`-assets →
>    cache-busting op assets helpt dan **niets**. Verifieer met `?vers=…` op de HTML **en** check
>    `performance.getEntriesByType('resource')` wélke versie geladen is. Ik trapte hier zelf bijna in.
> 4. **Tegels moeten onzichtbaar beginnen en invaden** (`opacity: 0`) — ze worden aangemaakt vóór hun textuur
>    binnen is. **En belangrijker: de bol eronder moet ZAKKEN** (`setSphereSink`, scale 0,998). Een tegel is een
>    plat lapje; zijn koorde duikt tussen de hoekpunten onder het boloppervlak en dan prikt de bol-textuur
>    eroverheen — horizontale banden langs de breedtegraden en een ringpatroon op de pool. v1 loste dat op door de
>    tegels op te tillen (`shellLift: 1.0016` = 3,8 km); **dat kan in v2 niet**, want op 1 km hoogte kom je dan
>    onder de tegellaag uit. `shellMeshDetail` hoort op **24** (v1's empirische waarde), niet lager.
>    **Meet het zo:** tel welk aandeel schermpixels verandert als je de bol eronder verbergt — 8,50% vóór de fix,
>    0,42% erna.
>
> **M26 is deels HERBOUW geworden, geen verhuizing** — bewuste prijs van de r185-keuze: `markers.js`/`flows.js`/
> `voyages.js` draaien op verdwenen r128-API's. De **landvulling is vervallen** (met tegels als oppervlak valt er
> niets te vullen). De schoonheidsslag (Rayleigh/Mie, oceaan-specular, dag/nacht-terminator) staat bewust ná de
> geometrie. Zie `memory/decisions.md` + [[2026-07-18-grondstoffen-atlas-m22-vectorwereld-en-tegels]].

> **🛑 BESLUIT 2026-07-18 (context) — DE V1-ATLAS OP DE ROOT IS BEVROREN. Kaartlaag opnieuw in fasen (M22→M26).**
> Lars: *"wat we nu hebben vind ik al wel erg mooi om te zien, alleen zitten er wel veel schoonheidsfoutjes in…
> als fixes na 2/3× niet lukken worden ze meestal niet beter."* **De huidige atlas blijft precies zoals hij is** —
> live op Pages, ongemoeid. **Alle M18-issues staan on hold** (LAR-474/475/476/477/478 → Backlog, `[ON HOLD]`).
> **Niet verder patchen aan de huidige routelaag.**
>
> **✅ Waar de nieuwe code leeft (besloten 2026-07-18): in `v2/` binnen deze repo.** Pages deployt 'm
> gratis mee op `…/grondstoffen-atlas/v2/`; gereedschap/data liggen ernaast zonder kopiëren; M26 wordt
> triviaal. **Harde regel: buiten `v2/` wordt NIETS aangeraakt** — de oude atlas op de root blijft bevroren.
>
> **De nieuwe volgorde** (Lars' eigen plan — eerst de kaart, pas als laatste de grondstoffen):
> **M22** gedetailleerd **vector-wereldmodel** = de waarheid ⬅️ **START: LAR-484 (Urgent)** ·
> **M23** **MARNET-zeeroutes** erop + testen haven→haven (kern: LAR-483) ·
> **M24** binnenwater (Rijn/Yangtze/Saint-Laurent/Kaspisch) ·
> **M25** land/spoor (bewust laatst: OSM = gigabytes) ·
> **M26** samenvoegen — de 14 grondstoffen erop terugzetten.
>
> **Waarom M22 eerst:** er bestaan **drie wereldmodellen** die het niet eens zijn — satellietbeeld (wat Lars
> ziet) · `LAND_POLYS` op **1:50 miljoen** (waar routes tegen gevalideerd worden) · MARNET's eigen kustlijn.
> Een route kan de test doorstaan én er op het scherm fout uitzien; **dan meten we langs elkaar heen.** Lars'
> oplossing: een gegenereerde **vectorwereld die scherp blijft bij inzoomen** wordt de waarheid, satelliet
> wordt een skin (*"satelliet heeft veel te veel kleuren en stukjes land die mogelijk gewoon een rots zijn
> die net uit water steekt"*). Bijvangst: lichter op mobiel.
>
> **Waarom M26 laatst kan:** `data/*.js` staat **volledig los van routering** — het is een verhuizing, geen
> herbouw. Lars: *"het opzoeken van mijnlocaties en raffinages is peanuts vergeleken met zo'n kaart maken."*
>
> **Vastgelegde ontwerpkeuzes:** netwerk **mee naar de browser** (anders geen echte simulator — met alleen
> kant-en-klare lijnen kun je niet herrouteren) · **dichtheid ≠ gladheid** (meer punten koopt land-nauwkeurigheid,
> niet schoonheid: een kortste pad over een fijn raster geeft trapjes) · **budget is geen beperking** (MARNET
> ≈ 310 KB tekst / ~100–130 KB gezipt; hersamplen op 5 km → ~260.000 knopen ≈ 1,2 MB, zoeken ≈ 0,1 s; de atlas
> bouwt nu al een raster van 1440×720 in **45 ms**) · doel **ruim op PC, werkbaar op mobiel** (Honor Magic V5) ·
> de **machine bewaakt de objectieve regels** zodat Lars' visuele check over *realisme* gaat, niet over bugs zoeken.

> **🏗️ ARCHITECTUURPRINCIPE SINDS 2026-07-18 — ONTKOPPELEN (lees dit vóór je aan routes/rendering werkt).**
> De atlas zat vast in een patch-spiraal: elke fix brak iets anders. Oorzaak: **één puntenlijst bediende drie
> taken met tegenstrijdige eisen** — de **vorm** van de lijn (wil weinig punten) · de **vaarsnelheid** van de
> schepen (wil punten gelijkmatig over afstand) · de **baan-klem** voor de 7 vaarbanen (wil juist véél punten in
> nauw water). Vereenvoudigen voor de vorm sloopte de klem (banen over Japan); verdichten voor de klem liet de
> schepen schokken en maakte lijnen hoekig. Lars zag het als eerste: *"anders blijven we heen en weer gaan zonder
> echt een fix."* **Nu zijn ze los:** `voyages.js` gebruikt **`getPointAt`** (booglengte, niet de curve-parameter),
> `lane_widths.js` schrijft een **apart profiel `wp`** (vrije ruimte per 20 km langs de boog) i.p.v. `w` per punt,
> `flows.js` voegt per-leg profielen samen (`mergeProfiles`), en de geometrie is puur vorm.
> **Toets bij elke wijziging: raakt dit meer dan één van die drie? Ontkoppel dan eerst.**
> Bewijs dat het klopt: alles verbeterde *tegelijk* — snelheidsvariatie **15,9× → 1,27×** (slechtste 47× → 2,3×),
> landtreffers **406 → 108**, Japan **8 → 0**, Baja **21 → 0**, Malakka **9 → 0**, geometrie 3.710 → 817 punten.
>
> **⚠️ CACHE-BUSTING IS VERPLICHT.** `index.html` laadde assets zónder versie terwijl GitHub Pages
> `Cache-Control: max-age=600` stuurt → Lars zag **drie fixes lang "geen verschil"** terwijl alles wél live stond.
> Dat was de grootste tijdvreter van 18 juli, niet de routing. **Draai `node tools/stamp_assets.js` vóór elke
> commit die assets raakt.** Vaste pipeline: `bake_searoutes.py` → `lane_widths.js` → `check_corridors.js` →
> `stamp_assets.js` → `build-standalone.py`.
>
> **⚠️ VERIFICATIE: meet over ALLE 7 vaarbanen, niet alleen de middellijn.** De eerste Japan-verificatie testte
> alleen de middelste baan en verklaarde het probleem ten onrechte opgelost — terwijl de klacht juist over de
> *buitenste* banen ging. Verder: de Browser-pane cachet script-tags zelfs op een nieuwe poort mét querystring
> (verifieer via `fetch(url,{cache:'no-store'})` → `<script>`-injectie), en `const SEAROUTES` is niet
> herdeclareerbaar (vervang bij injectie door `window.__SR2 =`).
>
> **→ VOLGENDE STAP = [LAR-483] (High, Todo), in een VERSE sessie.** Corridors worden nu per haven-paar gebakken;
> daardoor bundelen routes naar dezelfde bestemming niet, wordt dezelfde kapotte edge steeds opnieuw gerepareerd
> (7 corridors deelden hetzelfde Baja-trapje) en kiezen antipodale paren willekeurig een halfrond. **MARNET
> gemeten:** 15.840 segmenten / 9.646 knopen, segment mediaan 83 km maar **max 3.611 km** = een **grove graaf,
> geen waterkaart** → kaal over de bol leggen voorkomt land-treffers níet. Aanpak: het netwerk **één keer**
> verzoenen met `geo-data.js` en daarover routeren. Het issue is zelfstandig leesbaar geschreven.
> **⚠️ Werkende boom bevat een half-afgemaakte asymmetrische klem** (`src/util.js`, `tools/lane_widths.js`,
> `data/_searoutes.js` dirty) — `SIDE_SIGN = 1` is empirisch bevestigd; Baja-spreiding hersteld (143 km) maar
> Japan 0 → 52, waaier ±60° nog ongemeten. **Beslis eerst of dit nog nodig is** als LAR-483 doorgaat.

> **✅ WEERGAVE-FIXES BEVESTIGD (2026-07-17) — LAR-479 + LAR-481 Done, live op Pages.** Lars pauzeerde de koper-pilot
> bewust: *"als we dat eerst fixen voordat we de routes doen lijkt me beter."* Drie bugs, alle drie visueel bevestigd
> (*"ze werken zoals het hoort nu"*). **(1) Tegel-afkap (LAR-479)** — twee oorzaken: `maxTiles: 40` was **kleiner dan
> één patch** (42–72 tegels) terwijl `updateDetail` **noord→zuid** vulde → zuidelijke rijen structureel wazig; én
> `detailZoomFor()` miste **`cos(lat)`** (Mercator-tegel op 60° = halve grond → hoge breedten vroegen méér tegels voor
> dezelfde scherpte; Noorwegen 33%/0% dekking). Fix: `cos(lat)` + budget **96** + patch vult **van het midden naar
> buiten**. **(2) Zoom-evenredig draaien** — `dragSpeed`/`dragRefZoom`, geankerd op de startzoom (28,65°/100px
> onveranderd; volle zoom 3,13°). **(3) Marker-LOD vuurde AVERECHTS (LAR-481)** — `forced` overrulet tier voor **57 van
> de 63** koper-nodes → de tier-regel raakte **alléén de 6 context-mijnen zónder stroom**; Chuquicamata plofte in beeld,
> Los Pelambres (zelfde share, wél stroom) niet. **Markers verdwijnen niet meer op tier; `tier` stuurt alleen nog de
> labels.** Regressie 14 grondstoffen: pop-in 0. Commits `297016f` + `8dda38e`.
>
> ⚠️ **Twee engine-feiten die veranderd zijn — voor wie hierna code schrijft:**
> `CONFIG.markers.tierZoom` **bestaat niet meer** (tier ≠ marker-zichtbaarheid; alleen `labelZoomByTier` leeft nog), en
> `main.js` heeft **geen `usedNodeIds()`** meer (de `forced`-uitzondering was overbodig zodra markers niet meer op tier
> verdwijnen). De M16/LAR-471-notitie hieronder noemt de `usedNodeIds`-gate nog als onderdeel van het optionele-laag-
> patroon — **dat was juist tóén, maar geldt niet meer**; sectie I's stappenplan (5 plekken) was er nooit van afhankelijk
> en klopt onverkort. Zie `memory/decisions.md`.

> **🧭 KOERSWIJZIGING (2026-07-17) — EERST DE ROUTES, DAN DE FEATURES.** De atlas is inhoudelijk compleet
> (14 grondstoffen, backlog leeg), maar de volgende stap is bewust **géén 15e grondstof**: de routing is
> **aantoonbaar onrealistisch** en de drie geplande features **staan erop**. Lars: *"een boot zou daar nooit zo
> varen."*
>
> **Diagnose (`searoute.js`, 3 samenwerkende oorzaken):** (1) **`openRadiusDeg: 1.2`** = een schijf van ~130 km
> **geforceerd water** rond élk knelpunt — bedoeld om smalle straten (~35 km) open te houden in het grove raster,
> maar het zet óók land op "water" → A\* vaart vlak bij een knelpunt dwars over schiereilanden/eilandjes
> (**hoofdboosdoener**); (2) **8-richtingen-A\*** → trapjes (Golf→Rotterdam = **33 richtingswissels**); (3) **grof
> 0,25°-raster + `heuristicWeight: 1.35` + géén echte vaarlanen** → het vindt het kortste *watertraject*, niet de
> lane die schepen varen → kaarsrechte runs langs een breedtegraad.
>
> **Hard bewijs — Antofagasta→Shanghai:** grote-cirkel **18.526 km** · **searoute** (echte lanen, noordelijk tot
> 50,7°N) **18.880 km (+2%)** · **onze bol** (zuidelijk via `wp-pac-zuid` op 26°Z) **19.970 km (+8%)** → het
> **handgeplaatste vaarpunt dwingt ~1.090 km omweg af**. De `via`-ketens blijken grotendeels **handmatige
> compensatie voor een slechte router**.
>
> **→ M18 · Realistische zeeroutes (searoute):** routeren over een **echt scheepvaart-lanen-netwerk** (Eurostat
> MARNET, Python-pakket `searoute` 1.6.0 — al geïnstalleerd). **Precompute at build-time, gededupliceerd per
> haven-paar** (één gedeelde corridor-cache over alle 14 — *"routes zijn vaak hetzelfde"* → unieke corridors, niet
> elke flow); polylines in `data/_searoutes.js`, atlas rendert direct; **netwerk bewaren** zodat M21 een knelpunt
> blokkeert als *edge eruit → herrouteren*; **raakt alleen zee-legs** (land/lucht ongemoeid); runtime blijft pure
> JS, `searoute` = **build-dependency**. Bonus: A\* uit de runtime = lichter op mobiel.
>
> **Feature-trio hernummerd:** M18→**M19** (knelpunt-stress) / M19→**M20** (China-meta-view) / M20→**M21**
> (disruptie-simulator). **M21's aanpak is herijkt**: knelpunt blokkeren = *edge uit het netwerk*, niet een
> raster-cel-masker. **Pilot-first: koper** (LAR-474) → go/no-go Lars → dan de andere 13.
>
> **⚠️ Harde regel:** vergelijk **nooit** tegen een kale origin→dest A\*-run. De pilot van 2026-07-16 deed dat →
> "route A", een pad dat de bol **nergens tekent** (Lars: *"ik zie op onze wereldbol niets dat route A neemt"*).
> Vergelijk altijd tegen wat `flows.js` werkelijk rendert.
>
> **Open besluit (Lars, bij de pilot):** via-punten op zee-legs **opruimen** of **behouden als hint**.
> **Linear:** M18 · LAR-473..478 + **LAR-479** (High — tegel-patch wordt bij inzoomen afgekapt door `maxTiles: 40`;
> oorzaak bewezen) + **LAR-480** (Low — markers-contrast). Géén code gewijzigd in deze sessie.
> Zie `memory/decisions.md` + `memory/bugs-and-risks.md`.

> **BACKLOG LEEGGEWERKT (2026-07-16) — LAR-471 + LAR-447 + LAR-448, gepusht → live op Pages.** De 3 resterende
> backlog-issues afgerond. **LAR-471 · lab-grown-toggle (diamant)** = het **6e optionele-laag-patroon** (na goud-CB/koper-
> beurs/REE-recycle/olie-reserve/uranium-military): het `layer:"labgrown"`-patroon (zoals recycle, niet dedicated type) —
> 3 productie-nodes `type:"labgrown"` (China/Henan HPHT, India/Surat CVD, VS/Washington premium-CVD) + 6 flows die vooral de
> **VS-verlovingsringmarkt** ondergraven; 5 engine-plekken (config marker-size `labgrown:{size:0.030}` / main `showLabGrown`+
> `hasLabGrown()`+usedNodeIds-gate / flows-gate / markers-gate + **violette octaëder-marker** 0xB98BE0 / ui-chip "lab-grown"
> + TYPE_LABEL); default uit, chip alleen bij diamant; `dia-t-labgrown`-tension wijst nu naar de echte lab-grown nodes/flows.
> **LAR-447 · recycle-tooltip per-grondstof** = de gedeelde chip-tooltip was hard-coded REE-bewoord ("magneetschroot, <5%"),
> fout voor PGM (~25% autokat)/grafiet → nu via een `recycleHint`-veld op de resource + `main.recycleHint()` + generieke
> fallback in `ui.js` (hints op REE/PGM/grafiet). **LAR-448 · PGM-beursvoorraden-laag** (Lars akkoord ondanks de "één toggle
> per grondstof"-conventie) = PGM's **tweede** optionele toggle naast recycling; pure data, 0 engine-wijziging (hergebruik
> koper/nikkel/zilver-exchange-toggle): 3 kluis-nodes (LPPM/NYMEX/TOCOM) + 3 `layer:"exchange"`-bufferflows naar de autokat-
> markten → **PGM = eerste grondstof met twee toggles naast elkaar**. Headless (poort 8732 + verse load 8733): diamant **41
> legs (31 air+10 road) / 0 kapot / 0 straight / 0 degen** (toggle uit=35/25 aan=41/28, +34 scene-meshes); PGM **52 legs /
> 0 kapot** (exchange-toggle +3/+3; beide chips alleen bij PGM); regressievrij (`totalBroken=0`), 0 console-errors.
> **Cache-gotcha:** de Browser-pane cachet script-tag-files hardnekkig (geen no-cache op python `http.server`) → engine
> gevalideerd via in-memory injectie + een **tweede server-instance op 8733** (schone origin). `build-standalone.py` +4
> checks, `atlas-standalone.html` geregenereerd. Commits `f6c95f6` (feat 471) + `9feb8f2` (fix 447+448), **gepusht**
> (`5d4d469..9feb8f2`) → live op Pages. **Linear LAR-471/447/448 → Done; de backlog is nu leeg.** Toekomstig werk = alleen
> nog een nieuwe 15e grondstof of losse verfijningen. (Stale-notitie gecorrigeerd: M17-kolen stond al op origin/main.)

> **M15 · GAS UITGEVOERD (2026-07-16) — DE NIEUWE 12e GRONDSTOF (aardgas/LNG):** net als zilver (M13)/diamant/kolen een
> échte nieuwe grondstof (niet basis→uitgewerkt): nieuw `data/gas.js` (42 nodes / 51 flows / 6 tensions) + brief
> `design/gas.md` + `<script src="data/gas.js">` in `index.html` + 5 gas-checks in `build-standalone.py`. **De vorm = de
> natuurkunde: gas is nauwelijks te verplaatsen** → twee gescheiden leversystemen op de kaart: lage donkere **pijpleiding-
> arcs** (captive/regionaal — Rusland↔EU was, Power of Siberia→China, Turkmenistan→China, Noorwegen→EU) náást heldere
> **LNG-oceaan-arcs** (globaal). **De liquefactie-stap is de trechter** (institutioneel/kapitaal, geen zeestraat):
> capaciteit bij drie polen (VS-Golfkust/Qatar/Australië). Qatar via **Hormuz** (géén Yanbu/Fujairah-bypass — scherper dan
> olie). Stages: `erts` = veldgas + pijpleidinggas → `raffinaat` = LNG (het verhaal) → `product` = geleverd. Liquefactie=
> `refinery`, regas=`port`, opslag=`reserve`; schip + `pipeline` → **géén nieuwe render-modus/marker-types/chokepoint**
> (4e na nikkel/olie/zilver). 6 tensions (Hormuz, liquefactie-flessenhals, Europa-pivot 2022, Russische oost-pivot, drie
> prijszones, Panama-LNG-knelpunt); Iran = reserves≠export. **Opslag-laag = hergebruik olie-`reserve`-toggle, 0 engine-
> wijziging** (`hasReserves()` generiek, `src/main.js:23`): 4 reserve-nodes + 5 vul-flows; EU-winter-vulgraad = de metric.
> Headless (poort 8736): **gas 97 legs / 0 kapot / 0 straight / 0 onbekende via-ids**, regressievrij; de 2 Arctische Yamal-
> routes + captive-pijpleidingen routeren correct zónder nieuw vaarpunt (empirisch). `atlas-standalone.html` geregenereerd
> (5 gas-checks OK). Commits `040d2b7` (gas.js+gas.md) + `a8378ef` (build-checks), **gepusht → live op Pages** (alléén
> eigen bestanden; git-index-race met de diamant-sessie teruggedraaid met `reset`+`--only` — les: `git commit <paths>`/
> `--only` is race-bestendiger bij een gedeelde tree, sectie J). **Linear M15 · LAR-460/462/463/464/466 Done, 465 In
> Progress** (visueel = Lars). Milestones hernummerd: Gas=M15 / Diamant=M16 / Kolen=M17.

> **M16 · DIAMANT UITGEVOERD (2026-07-16) — DE NIEUWE 12e GRONDSTOF:** net als zilver (M13)/gas (M15) een échte nieuwe
> grondstof (niet basis→uitgewerkt): nieuw `data/diamond.js` (25 nodes / 35 flows / 6 tensions) + brief `design/diamant.md`
> + `<script src="data/diamond.js">` in `index.html` + 4 diamant-checks in `build-standalone.py`. Milestones liepen t/m M14
> (grafiet); M15 was door de gas-sessie bezet → diamant = **M16**. De vorm = **de scherpste DOWNSTREAM-trechter van de
> atlas**: winning verspreid (Rusland/Alrosa #1 op **volume**, Botswana/Debswana #1 op **waarde**, Canada, Angola, Zuid-
> Afrika, Zimbabwe, Namibië-marien, Lesotho; **Argyle gesloten 2020** = schaarste-verhaal; volume-vs-waarde via `note`),
> maar **~90-95% van álle diamant wordt geslepen/gepolijst in één stad: Surat (Gujarat)** — scherper nog dan de China-
> raffinage of Ganzhou-scheiding; alle rough-arcs convergeren op Surat. **Antwerpen** = het verplichte **G7-
> certificeringsknooppunt** (sanctie op Russische/Alrosa diamant, maart 2024) → fysieke omweg mijn→Antwerpen→Surat,
> terwijl de **Alrosa-rough zichtbaar om Antwerpen heen buigt** via Dubai/direct India ("de stroom buigt om, niet weg").
> De Beers-sights via Gaborone. Diamant **vlíégt** (beveiligde koeriers) → **hergebruik van de goud/PGM air-mode**
> (`mode:"air"`), **0 engine-wijziging, géén nieuw chokepoint, géén nieuwe marker-types** (`hub`=Antwerpen/Dubai/Gaborone/
> Mumbai; `refinery`=slijperij Surat/China). Korte hops binnen een land = `road`. Keten 3 stages (erts=rough → raffinaat=
> polished bij Surat → product=sieraad; VS #1 ~50%). 6 tensions: Surat-trechter, De Beers/Alrosa-duopolie, Antwerpen-
> certificering, Alrosa/G7-sanctie, **lab-grown-ontwrichting**, waarde-vs-volume + Botswana-beneficiation. **Twee "anders"-
> punten → aparte issues** (Lars' verzoek): LAR-470 (plumbing, zoals zilvers LAR-436) + de **lab-grown-toggle** (LAR-471,
> `layer:"labgrown"`, 5 engine-bestanden) **bewust in de backlog** i.v.m. de parallelle sessies (zoals uranium's LAR-414 /
> olie's LAR-432); in v1 leeft lab-grown als `tension`. Headless (poort 8734): **diamant 35 legs (27 air + 8 road) /
> 0 kapot / 0 straight / 0 degen**, 0 warnings, regressievrij; 1 kust-artefact-landhop (Dubai→Golf) → `air` voor 0 straight.
> `atlas-standalone.html` geregenereerd (4 diamant-checks OK). Commits `72d134c` (feat) + `7d06a0c` (build), **gepusht →
> live op Pages** (`8497f24..7d06a0c`, fast-forward, alléén eigen commits — 4 parallelle sessies grafiet/kolen/gas/diamant,
> sectie J; de meeliftende `gas.js`-tag verwees al naar de gecommitte gas.js → consistent, geen duplicaat). **Linear M16 ·
> Diamant + LAR-467..472:** 467/468/469/470 Done, 472 In Progress (visueel=Lars), 471 Backlog.

> **M17 · KOLEN UITGEVOERD (2026-07-16) — DE NIEUWE 12e GRONDSTOF:** na zilver (11e) de tweede écht nieuwe grondstof
> (kolen zit niet in de basis-10): nieuw `data/coal.js` (34 nodes / 33 flows / 6 tensions) + brief `design/kolen.md` +
> `<script src="data/coal.js">` in `index.html` + `grens-gashuunsukhait` (Mongolië-Gobi) in `_chokepoints.js` + 5 kolen-
> checks in `build-standalone.py`. De vorm is **fundamenteel anders**: **géén mondiale flessenhals** want kolen is
> overweldigend **binnenlands** — ~85% verstookt waar gedolven (China ~50% van de wereld, India, VS, Rusland), slechts
> ~15% van de ~8.700 Mt gaat over zee. De kaart toont grote binnenlandse blokken (`erts`+`product`) tegenover een dunnere
> **zeehandelslaag** (`raffinaat` = de internationaal verhandelde bulk, waar élk ban/her-routeringsverhaal leeft).
> **China = swing-koper** (grootste producent én importeur). **Twee kolen** (thermisch→stroom vs. cokeskool→staal) via
> `note`+`tension` (nikkel-patroon). **Drie her-routeringen** (tensions): China-Australië-ban (2020-2023), Rusland-oost-
> draai (2022→), Mongolië-Gobi-corridor. Grondstof-eigen "nieuwe element" = **één LANDknelpunt** `grens-gashuunsukhait`
> (Tavan-Tolgoi-cokeskool over de Gobi → Chinees staal; Kasumbalesa/Ruili-patroon; alléén kolen verwijst ernaar →
> regressievrij). Schip+land, **géén nieuwe render-modus, géén nieuwe marker-types, géén optionele toggle-laag** (kolen
> heeft geen zinvol CB/beurs/recycling-equivalent). Kolen = **4e** grondstof (na nikkel/olie/zilver) zonder nieuw **zéé**-
> knelpunt. Headless (poort 8735): **kolen 111 legs / 0 kapot / 0 straight / 0 degen**, regressievrij; route-bug empirisch
> gefixt (Canadese haven Roberts Bank ingesloten in de Salish Sea → **Ridley/Prince Rupert** open kust). Commit `75c3483`
> (lokaal, Claude-trailer, **alléén eigen bestanden** — 3 parallelle sessies grafiet/diamant/gas ongemoeid, sectie J: de
> gedeelde `index.html` kreeg diamond/coal/gas in één hunk → alléén de coal-regel gestaged via `git apply --cached`).
> **Linear M17 · Kolen + LAR-455..459 Done, 461 In Progress** (visuele bevestiging = Lars). De atlas telt nu **14
> grondstoffen** (basis-10 + zilver + gas M15 + diamant M16 + kolen M17); gas + diamant lopen in parallelle sessies.

> **M14 · GRAFIET UITGEVOERD (2026-07-15) — DE ATLAS IS INHOUDELIJK COMPLEET (11/11):** `data/graphite.js` van "basis"
> (10/3) → **uitgewerkt** (31 nodes / 26 flows / 6 tensions) + brief `design/grafiet.md` + 5 grafiet-checks in
> `build-standalone.py`. Grafiet was het **laatste basis-10-bestand** (bestond al + stond al in `index.html` →
> basis→uitgewerkt, géén nieuwe script-tag). De vorm = een **REE-achtige verwerkingstrechter met TWEE feedstocks**:
> **natuurlijk vlokgrafiet** (China #1 ~65%, Balama/Mozambique, Madagascar, Brazilië, Tanzania) én **synthetisch grafiet**
> uit petroleum-**naaldcokes** convergeren op de anode-verwerking die **~90%+ in China** zit (Shandong natuurlijk,
> Binnen-Mongolië synthetisch op goedkope kolenstroom) — **zelfs ex-China vlok vaart naar China** om verwerkt te worden
> (de Ganzhou-REE-parallel). Levende geopolitiek: de **China-exportvergunningen op grafiet (dec 2023)**. Dunne ex-China
> buildout (Syrah Vidalia/Louisiana uit Balama-vlok, Talga/Novonix/NMG/POSCO). Schip+land, **géén nieuwe render-modus,
> géén nieuw chokepoint** (4e na nikkel/olie/zilver); recycling-toggle hergebruikt het REE/PGM-patroon met **0 engine-
> wijziging** (bewust bescheiden, batterijgrafiet-recycling nog nascent). Headless (poort 8735): **grafiet 77 legs
> (57 zee + 20 land) / 0 kapot / 0 straight / 0 warnings**, toggle aan=80, regressie schoon (0 kapot overal). Route-bug
> gefixt (`gr-ref-japan→gr-mkt-korea-japan` road→ship). `atlas-standalone.html` geregenereerd (5 grafiet-checks OK).
> Commit `34b1ed4` (Claude-trailer, **alléén eigen bestanden** — sectie J; **gepusht** → live op GitHub Pages). **Linear
> M14 · Grafiet + LAR-449..454** (449–453 Done, 454 In Progress = visuele bevestiging Lars). **Geen grondstoffen meer op
> "basis".** ⚠️ **Repo-correctie:** de "repo lokaal-only"-notities hieronder zijn achterhaald — de repo staat op GitHub
> (`larswalters/grondstoffen-atlas`) en draait live op **GitHub Pages** (https://larswalters.github.io/grondstoffen-atlas/);
> elke `git push origin main` deployt.

> **M13 · ZILVER UITGEVOERD (2026-07-15):** de **eerste écht nieuwe grondstof** sinds de basis-10 (niet basis→uitgewerkt):
> nieuw `data/silver.js` (42 nodes / 37 flows / 6 tensions) + brief `design/zilver.md` + `<script src="data/silver.js">` in
> `index.html` + 5 zilver-checks in `build-standalone.py`. De vorm is **fundamenteel anders**: zilver heeft **géén enkel
> geografisch knelpunt** — de knijp is tweezijdig en structureel: (1) **aanbod-inelasticiteit** (~70-75% is **bijproduct** van
> zink/lood/koper/goud; mijn-nodes = eigenlijk andermans mijnen, elk met een hoofdmetaal-`note`), (2) **vraagconcentratie** (de
> energietransitie trekt zilver naar de **Chinese zonnepanelen-industrie**; PV = grootste + snelst groeiende toepassing) →
> een **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt. Schip+land (industrieel metaal, géén goud-luchtmodus),
> **géén nieuwe render-modus, géén nieuw chokepoint** (derde na nikkel/olie op de bestaande routekaart), géén nieuwe marker-types.
> Keten op de 3 stages: erts=mijn(bijproduct)→doré/concentraat / raffinaat=good-delivery baar / product=industrieel (solar/
> elektronica/sieraad). Mexico als winning+raffinage-anker (Fresnillo + Peñoles/Torreón). **Kluis-/beursvoorraden-laag** =
> hergebruik van de bestaande `exchange`-toggle met **0 engine-wijziging** (nikkel-patroon, 2e datagedreven hergebruik): 3
> exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows; recycling always-on. Twee route-bugs empirisch gefixt
> (VS-raffinage Tacoma→Astoria open kust; China-solar Suzhou-binnenland→Jiangsu-kust). Headless (poort 8734): **zilver 85 legs /
> 0 kapot / 0 straight / 0 warnings**, regressievrij (andere uitgewerkte grondstoffen 0/0). `atlas-standalone.html` geregenereerd
> (5 zilver-checks OK). Commit `e091848` (lokaal-only, Claude-trailer, **alléén eigen bestanden** — parallelle uranium-toggle-sessie
> op de gedeelde engine-files ongemoeid, sectie J). **Linear M13 · Zilver + LAR-434..438 Done, 439 In Progress** (visuele
> bevestiging Netlify/mobiel = Lars). M12 = PGM (uitgevoerd, zie onder); alleen **grafiet** nog op "basis".

> **M12 · PGM UITGEVOERD (2026-07-15):** `data/pgm.js` van "basis" (9/3) → **uitgewerkt** (38 nodes / 41 flows / 6 tensions).
> De **scherpste twee-landen/twee-metalen-concentratie** van de atlas: **Zuid-Afrika/Bushveld** = Pt/Rh (~70%/~80%, dichte
> kluwen schachtmijnen bij Rustenburg + Noord-/Oostrand), **Rusland/Norilsk** = Pd (~40%, Ni-Cu-bijproduct). PGM **vliegt**
> (per kilo even waardevol als goud) → **hergebruik van de goud-air-mode** (`mode:"air"`, JNB-gateway; tijdlijn toont
> automatisch "✈ vluchten" via `activeHasAir()`); concentraat/matte over land (Beitbridge/Kanaaltunnel/Baltische bruggen).
> **Géén nieuw chokepoint, géén engine-wijziging** (derde na koper/nikkel). **Recycling-toggle** (`layer:"recycle"`, ~25%
> autokat via JM/BASF/Umicore/Heraeus/Tanaka) = hergebruik van het REE-patroon met **0 engine-wijziging** (chip via
> `hasRecycle()`). 6 tensions: twee-landen-concentratie, autokat-leiband + Pt↔Pd-substitutie, rodium-spof, palladium/Rusland-
> sanctie, waterstof-hedge (Pt/Ir PEM-elektrolyse), Eskom-stroomcrisis. Headless (poort 8732): **pgm 49 legs / 0 kapot /
> 0 straight / 0 degenerate arcs**, regressievrij (SAMECELL-fix: Japan-recycler uit Tokyo Bay → Kanagawa). `atlas-standalone.html`
> geregenereerd (4 PGM-checks OK). Commit `2c4b668` (lokaal-only, Claude-trailer, **alléén eigen bestanden** — parallelle
> zilver-/uranium-toggle-sessie ongemoeid, sectie J). **Linear M12 · PGM + LAR-440..448** (5 Done, 445 In Progress = visuele
> bevestiging Lars, 446 Done na de build, 447/448 Backlog = afwijkingen: REE-bewoorde recycle-tooltip + optionele Pt/Pd-exchange-laag).

> **M11 · OLIE UITGEVOERD (2026-07-15):** `data/oil.js` van "basis" (18/15) → **uitgewerkt** (45 nodes / 46 flows /
> 6 tensions). Olie's vorm is bewust **anders dan alle eerdere**: geen enkele trechter maar het **hele knelpunten-
> netwerk dat tegelijk oplicht** — data bevestigt Hormuz #1 (15 stromen), Malakka, Taiwan, Suez/Bab, Bosporus, Panama,
> Kaap (10 knelpunten). Daarom **géén nieuw chokepoint** (= het eigen aha); wel 3 olie-only navigatie-vaarpunten
> (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`. Drie levende verhalen: de **Hormuz-bypass-
> pijpleidingen** (Saoedi→Yanbu, UAE→Fujairah), de **Rusland-omleiding 2022→** (Europese crude → India/China via
> Primorsk/Novorossiysk/ESPO-Kozmino/Druzhba) en de **Amerikaanse schalie-ommekeer** (Corpus Christi export). Keten op
> 3 stages: erts=ruwe olie / raffinaat=producten / product=petrochemie; schip+pijpleiding, **géén nieuwe render-modus**.
> Optionele **SPR-voorraden-toggle** (`layer:"reserve"`) eerst uitgesteld tijdens de parallelle nikkel-sessie, **daarna
> alsnog gebouwd** (LAR-432 Done, commit `86c8c1f`) = het **vierde** optionele-laag-patroon (goud-CB/koper-beurs/REE-recycling/
> olie-reserve): 5 SPR-nodes (`type:"reserve"`, `stock` mln vaten) + 5 vul-flows + tension, olie-amber tank-marker, chip
> "voorraden" alleen bij olie. Headless: **olie 210 legs / 0 kapot / 0 straight** (232 incl. reserve); toggle uit=45/46,
> aan=50/51; regressievrij. `atlas-standalone.html` geregenereerd (olie- + reserve-checks OK). Commits `1d4ece5` (data) +
> `86c8c1f` (toggle), lokaal-only, Claude-trailer. **Linear M11 · LAR-428..432 Done, 433 In Progress.** Rest = visuele bevestiging Netlify/mobiel (Lars).

> **M10 · NIKKEL UITGEVOERD (2026-07-15):** `data/nickel.js` van "basis" (13/4) → **uitgewerkt** (50 nodes / 46 flows /
> 6 tensions). De nikkel-"aha": de **trechter staat op z'n kop** t.o.v. koper — waar koper/lithium breed graven en in
> China raffineren, heeft **Indonesië in tien jaar de mijn ÉN de raffinage** naar zich toe getrokken via de **exportban
> op ruw erts** (IMIP Morowali / IWIP Weda Bay, Chinees kapitaal Tsingshan/Huayou); het erts blíjft in het land (korte
> mijn→smelter-hops). Plus **twee nikkels** (class-1 batterij/sulfaat vs class-2 roestvrij/NPI, met HPAL→MHP/matte als
> brug), de **prijscrash-shakeout** (BHP Nickel West stilgelegd 2024, Nieuw-Caledonië in crisis), de **LME-nuance**
> (alleen class-1 leverbaar + de 2022-squeeze) en het **Filipijnse ruw-erts-contrast** (geen ban). Schip+land, **géén
> nieuwe render-modus, géén nieuw chokepoint** (hergebruikt Makassar/Lombok/SCS/Taiwan/Deense-Straten/Panama/Saint-Laurent).
> **Beursvoorraden-laag (LME)** hergebruikt de **bestaande** exchange-toggle van koper met **0 engine-wijziging**
> (bevestigd generiek); recycling always-on. Headless: **nikkel 91 legs (63 zee + 18 land + 10 korte hops) / 0 kapot /
> 0 straight**, regressie schoon (0 kapot over alle grondstoffen). `atlas-standalone.html` geregenereerd (nikkel-checks OK).
> Commit `08aa4f5` (lokaal-only, Claude-trailer). **Linear M10 · LAR-422..426 Done, 427 In Progress** (visuele bevestiging =
> Lars). Overige op "basis": grafiet, PGM (olie loopt in een parallelle sessie).

> **M8 · ZELDZAME AARDMETALEN UITGEVOERD (2026-07-15):** `data/rare-earths.js` van "basis" (9/5) → **uitgewerkt**
> (41 nodes / 38 flows / 6 tensions) in de **magneet-REE-framing** (NdPr licht + Dy/Tb zwaar; `symbol: NdPr`,
> `unit: kt magneet-REO/jaar`). De **extreemste trechter** van de atlas: winning breed verspreid, scheiding ~85–90%
> Zuid-China (**Ganzhou**). Vier kern-aha's: Ganzhou-scheidingstrechter, **Dy/Tb-landstroom Myanmar→China** over de
> nieuwe grenscorridor **`grens-ruili`** (`_chokepoints.js`, Kasumbalesa-patroon), de **Mountain-Pass-rondreis**
> (concentraat heen over de Stille Oceaan, oxide terug) en de **NdFeB-magneet-waaier** vanuit China. Nieuwe
> **recycling-toggle** (`layer:"recycle"`, default uit) = het derde optionele-laag-patroon (goud=CB, koper=beurs,
> REE=recycling), bewust via `layer` op flows én nodes zodat koper's always-on recyclers ongemoeid blijven. Headless:
> **rare-earths 90 legs / 0 kapot / 0 straight**, regressievrij. `atlas-standalone.html` geregenereerd (REE-checks OK).
> **Linear M8 · LAR-416..420 Done, 421 In Progress.** Rest = visuele bevestiging Netlify/mobiel (Lars). Repo lokaal-only, `main`.

> **M9 · URANIUM UITGEVOERD (2026-07-15):** `data/uranium.js` van "basis" (9/2) → **uitgewerkt** (38 nodes / 36 flows /
> 6 tensions). Eerste grondstof met een bewust *andere vorm* — een **4-staps kernbrandstofketen** (winning → conversie →
> verrijking → splijtstof → reactor) met de **verrijking (~44% Rusland) als raffinaat-flessenhals**. Nieuw: de
> **Trans-Kaspische route** om Rusland heen (3 Kaspische vaarpunten + Dardanellen in `_chokepoints.js`), de **VVER-lock-in**
> en de **CANDU-uitzondering**. Headless: **uranium 54 legs / 0 kapot**, regressievrij. Commits `d016ab8` (brief) + `76c0333`
> (data). Linear-milestone **M9 + LAR-410..415**. Rest = visuele bevestiging (LAR-415). **Militaire-kringloop-toggle (LAR-414)
> ALSNOG GEBOUWD (2026-07-15, commit `6a6d062`):** het 5e optionele-laag-patroon (`type:"military"`/`layer:"secondary"`, down-blend/
> tails/reserves; Megatons-to-Megawatts) — headless uranium 60 legs / 0 kapot / 0 straight, toggle +4 nodes/+5 flows, chip alleen bij uranium.

> **STATUS VAN DEZE MAP (2026-07-14):** ✅ code-root (modulaire atlas als **git-repo**). **M0–M7 done** (op de
> visuele check na): naast lithium+kobalt+goud is nu **koper volledig uitgewerkt** (`data/copper.js`, 69 nodes/50 flows)
> — de **Andes-concentraat-trechter** → Chinese smelters + de **Copperbelt-kathode** over land (Kasumbalesa), plus een
> nieuwe **beursvoorraden-laag** (LME/SHFE/COMEX-toggle, zelfde patroon als de goud-CB-laag). Headless geverifieerd:
> **koper 145 legs / 0 kapot**, regressie **388 legs / 0 kapot** over alle 10 grondstoffen. **Modulair = bron van
> waarheid**; `build-standalone.py` genereert `atlas-standalone.html`. **Gecommit** (`main`, code `233b882` +
> wrapup-docs `7e46092`, lokaal-only); **Linear LAR-404..409 → Done**. Rest: alleen nog de **visuele bevestiging op
> Netlify/mobiel** (WebGL-screenshot lukt niet headless). Draaien lokaal: `python -m http.server 8732` (launch.json-entry `grondstoffen-atlas`).

## A - What this folder is

De grondstoffen atlas is een **interactieve 3D-wereldbol** die per kritieke grondstof de complete
handelsketen toont: waar het uit de grond komt (mijnen), waar het geraffineerd wordt, waar het
eindproduct gemaakt wordt, en langs welke **echte routes** (zee + land) het reist. De kern van het
verhaal zijn de **knelpunten**: Straat van Malakka, Lombok, Suez, en de structurele afhankelijkheid
van Chinese raffinage.

Geen abstracte bogen door de lucht: schepen varen over water, treinen/trucks over land, en op de
plekken waar alles samenknijpt zie je dat letterlijk gebeuren.

## B - The Goal

- **Waarom:** de geopolitiek van kritieke grondstoffen tastbaar en visueel navolgbaar maken — één
  bol waarop je de afhankelijkheden en knelpunten van de wereldhandel ziet.
- **Werkwijze (belangrijk):** *eerst ontwerpen, dan bouwen.* Per grondstof eerst een lijst met de
  belangrijkste knopen en stromen opstellen, pas daarna in de atlas zetten.
- **Template:** lithium is de volledig uitgewerkte referentie (34 knopen, 31 stromen). Kobalt is de
  tweede. De overige grondstoffen staan op detailniveau "basis" en wachten op uitwerking.
- **Volgende inhoudelijke stap:** eerst M5 (visuele bugs + routecorrecties), daarna nieuwe grondstof-
  ketens uitwerken. Kandidaten: koper (op de roadmap) en **goud** (Lars' huidige focus).

## C - Stack & locatie

- **Tech:** vanilla JS + Three.js. **Geen bundler** — losse globals-bestanden met vaste laadvolgorde
  via `<script>`-tags in `index.html`.
- **Huidige code-locatie:** ✅ **deze projectmap** (`Projects\General\grondstoffen-atlas`, git-repo). De modulaire
  code (config/geo-data/index/style/src/data/textures) is hier de werkbasis. Referenties op het bureaublad:
  single-file `C:\Users\lars\Desktop\globe\atlas-lithium-kobalt.html` (M5-referentie/deploy-build) en de oude
  modulaire backup `C:\Users\lars\Desktop\globe-oud\grondstoffen-atlas-v2\atlas\` — beide **onaangeraakt**, mogen
  weg zodra de repo visueel op Netlify/mobiel bevestigd is.
- **✅ Beslist + uitgevoerd (2026-07-14): modulair = bron van waarheid** (single-file = gegenereerde build). Code
  verplaatst + `git init`; M5-fixes geport (214 legs, 0 kapotte routes geverifieerd).
- **Deploy:** ✅ **live op GitHub Pages** — https://larswalters.github.io/grondstoffen-atlas/ (repo `larswalters/grondstoffen-atlas`, public, branch `main` root, met een `.nojekyll` zodat `data/_registry.js`/`data/_chokepoints.js` geserveerd worden). **Elke `git push origin main` werkt de live site bij** (~1-2 min rebuild) — dit is nu de "bekijk-op-elk-apparaat"-deploy (2026-07-15). Netlify (drag-and-drop van de single-file) blijft als alternatief bestaan. NB: directe Google-API-egress is op deze machine geblokkeerd (Drive-upload via SA lukt niet vanaf hier; GitHub werkt wél).
- **Bestandsindeling (modulaire opzet — in deze map):**
  - `config.js` — alle instellingen op één plek
  - `geo-data.js` — landpolygonen (`LAND_POLYS`)
  - `index.html` — vaste script-laadvolgorde
  - `src/` — `util.js`, `globe-core.js`, `basemap.js`, `tiles.js`, `searoute.js`, `markers.js`,
    `flows.js`, `voyages.js`, `ui.js`, `main.js`
  - `data/` — `_registry.js`, `_chokepoints.js` + **per grondstof een `.js`** (`lithium.js`,
    `cobalt.js`, `copper.js`, `graphite.js`, `nickel.js`, `oil.js`, `pgm.js`, `rare-earths.js`,
    `uranium.js`) — lithium+kobalt uitgewerkt, de rest op "basis". **Naast elke `.js` een leesbare
    brief `<grondstof>.md`** (bijv. `lithium.md` = het voorbeeld) die je invult vóór je codeert.

## D - Decisions

Zie `memory/decisions.md`. Kernbesluiten: geen bundler (globals + script-tags); A\* over een
1440×720 land/zee-raster voor echte routes; knelpunten worden als water geforceerd; één `data/<grondstof>.js`
per grondstof volgens het lithium-schema; "eerst ontwerpen, dan bouwen".

- **2026-07-19 · LAR-504: een vaarwegsysteem mag OVERAL op zijn voorganger aanhaken** — `volgtOp`
  hechtte alleen aan het ketenuiteinde; daarmee bak je lijnen, geen netwerk. `hecht_aan_keten()` knipt
  nu de moederedge door op een **bestaande geometrie-vertex** (dus zonder één coördinaat te
  verplaatsen → corridor-toets blijft per constructie geldig), met hetzelfde passage-label op beide
  helften. Verworpen: rivieren vooraf opknippen bij elke aftakplek — dat dwingt bij elke nieuwe
  zijrivier een rebake van de moeder en versnippert de labels zonder betekenis.
- **2026-07-19 · LAR-492: splits een rivier op de VERSTORING, niet op de zeevaartgrens** — de
  zeevaart-vlag is alleen metadata (de browser leest er enkel `bron` uit) en het voorgestelde
  splitspunt bij Keulen sprak zichzelf tegen met `waal`. Elk segment is een eigen `vermijd`-knop, dus
  knip waar M21 iets aan heeft: de Rijn bij **Bingen** (Kaub-laagwater 2018/2022).
- **2026-07-19 · LAR-492: namen opzoeken is nu gereedschap, en rangschikt op lengte MÉT strekking** —
  `v2/tools/survey_vaarwegen.py`. De lon/lat-strekking laat zien of de whitelist een *doorlopend*
  traject dekt; ving `Boven-Rijn` (mét koppelteken) en de grensnaam `Le Rhin / Rhein`.
- **2026-07-19 · LAR-492: kijk waar de GEUL ligt, niet welke landen de rivier raakt** — de vaargeul
  Basel–Straatsburg ligt in het Grand Canal d'Alsace op Frans grondgebied (extract `fr-alsace`, anders
  een gat van 72,9 km). Complement: **water ≠ vaarweg** — `Vieux Rhin / Altrhein` bewust niet
  gewhitelist, want de Restrhein heeft geen bevaarbare geul.
- **2026-07-19 · M25: compleet hoofdspoornet i.p.v. corridor-scope** — een netwerk beantwoordt vragen die
  je niet vooraf hebt uitgerekend; met corridor-scope kan M21 alleen verstoringen tonen die we vooraf
  bedachten (blokkeer Kasumbalesa en Lobito/Dar es Salaam moeten dan al gebakken zijn). Gelaagd zoals
  water: compleet spoor = MARNET-rol, verhalende corridors = `EXTRA_VAARWEGEN`-rol met passage-label.
  Geaccepteerde prijs: een dedup-stap die corridor-scope niet nodig had.
- **2026-07-19 · M25: op land is LENGTE de enige echte controle** — de corridor-toets werkte op water
  omdat water schaars is; op land ligt élke verkeerde route ook dicht bij een weg. En dedupliceer eerst:
  dubbelspoor is meestal als twéé losse lijnen gemapt, dus China leest +142% (266.146 vs 109.767 route-km).
- **2026-07-19 · M25: spoor filteren door UITSLUITING** — 40–43% van de spoor-ways draagt geen `usage`-tag,
  dus `usage=main` eisen sloopt precies Afrika en Zuidoost-Azië. Houden `railway` in (`rail`,
  `narrow_gauge`); weg alles met `service=`, `usage` in (`tourism`,`military`) en disused/abandoned/razed.
  Tool: `v2/tools/meet_spoor.py`.
- **2026-07-19 · M25: bron per modus, want de drie zijn niet gelijk bedeeld** — spoor heeft goede
  geometrie én een meetlat (NARN); weg heeft geometrie maar géén scheidsrechter (GRIP4 valt af op
  licentie-onduidelijkheid) → klein houden; pijpleiding heeft een meetlat (operator-lengtes) maar
  wisselvallige OSM-dekking → aanvullen uit GEM's **openbare** GitHub-repo (formulier onnodig; repo mist
  wel een LICENSE-bestand). Droezjba blijft bewust een benadering.

- **2026-07-19 · LAR-487/488: `volgtOp`-ketening — één rivier, meerdere labels met eigen zeevaart-vlag** — het
  zeevaart-beleid past niet in één keten met één vlag, dus een vervolgsegment hangt aan het **binneneinde van zijn
  voorganger** i.p.v. aan MARNET, zónder polygoon-toets (dat punt ligt al op een corridor-getoetste keten).
  Vervolgsystemen staan later in `SYSTEMEN` en hun `anker_zee` = het `anker_binnen` van hun voorganger
  (`VERVOLG_MAX_KM` 5 km, gemeten 0,00). Levert per segment meteen een eigen `vermijd`-knop voor M21/M26.
- **2026-07-19 · LAR-487: de corridor-toets bewijst procesintegriteit, niet bronkwaliteit** — hij vergelijkt de keten
  met de bron waaruit hij gebakken ís (per definitie ~0 m), dus een onafhankelijke tweede bron blijft nodig. En
  **lengte is de beslissende controle, niet de puntafstand**: een fout gevolgde oxbow ligt overal dicht bij íets, maar
  verraadt zich in de totale kilometers (1.028,2 km = 638,9 river miles vs officieel 641 → 0,3%). Meetlat als eigen
  tool `v2/tools/toets_usace.py` (`GEO_CLASS='I'` + `FUNC_CLASS<>'N'`); `FUNC_CLASS='B'` toetst meteen de zeevaart-vlag.
- **2026-07-19 · LAR-488: waar geen officieel net bestaat, laten de havens de geometrie bevestigen** — negen
  searoute-havens (andere bron dan OSM) vallen vanzelf binnen enkele km op de Yangtze-keten. Herbruikbaar voor de
  wereldwijde uitrol (Paraná, Mekong, Congo).
- **2026-07-19 · Overpass: exacte tag-match, conditionele CEMT-clause, gescheiden timeouts, cache op query-inhoud** —
  Overpass indexeert `key=value`; een `^(...)$`-regex selecteert hetzelfde maar dwingt een scan af. De CEMT-clause
  heeft als enige géén naamfilter en bestaat buiten de EU niet → alleen voor systemen mét CEMT-klasse. Client-timeout
  (180 s) los van server-timeout (300 s), anders gijzelt één overbelaste mirror de run.
- **2026-07-19 · LAR-486: zee-overgang = NE-water óf waterweg-zone; verzoening gecached; varianten als sets** —
  een aansluitknoop in een dokbekken (Maasmond 6812, `zone:nl-delta`) is geldig (M23-aanloop-principe); de dure
  M23-herberekening (~35–40 min) staat nu in `build-cache/verzoening_cache.json` (élke volgende bake ~1 min;
  les: bewaarpunt éérst bij dure pijplijnen); bake-off-varianten bakken als set bin+json+ports (haven-snap hangt
  aan de knopenlijst), tijdelijk naast elkaar via `?vaarwegbron=`. Winst-metingen niet vanaf een knoop óp het
  nieuwe kanaal (label dicht = geïsoleerd) maar vanaf de oude snap-knoop. UNECE-data niet scriptbaar (Cloudflare).
- **2026-07-19 · M24: corridor-toets vervangt vlak-toets + bake-off beslist de bron** — rivieren/kanalen bestaan
  niet als water in de NE-polygonen → binnenwater-toets = afstand tot een bevaarbare-vaarweg-middellijn (~2 km-
  monsters, ≤ ε); NL-pilot (LAR-486) bouwt NZK + Waal uit OSM én UNECE en beslist de bron-rolverdeling; pilots
  NL→VS→China (elk één controle-situatie), daarna het complete commercieel bevaarbare net (EU CEMT ≥ IV / VS
  USACE-net / elders commerciële systemen); binnenwater-edges krijgen bij de bake passage-labels + zeevaart-vlag
  (filteren = M26/M21 via `vermijd`); OSM = ODbL → HUD-attributie.
- **2026-07-18 · M23: verzoenen tegen de 1:10M-vectorwereld, meren = water** — routering rekent tegen exact de
  gerenderde lijnen (vector = waarheid); `ne_10m_lakes` als water maakt de Seaway/Grote Meren/IJsselmeer/Wolga-Don
  legitiem bevaarbaar in de toets. Binnenwater = flag (`soort=1`, 29 zones), geen "fix".
- **2026-07-18 · M23: lon-normalisatie verplicht in graafbouw** — MARNET heeft 15 dubbele ±180-knopen; zonder merge
  is de trans-Pacific doorgeknipt (Yokohama→LA 32.000 km via Suez+Panama).
- **2026-07-18 · M23: passage-restricties in de router, default `northwest` dicht** (= searoute's eigen default) —
  kortste graafpad ≠ commerciële route (R'dam→Shanghai koos anders de Noordwest-Passage). Meteen het M21-mechanisme.
- **2026-07-18 · M23: omleggen in vier trappen (0,02°/0,01° × gebufferd/kaal) + eindtolerantie per uiteinde uit de
  oorspronkelijke koorde** — buffer beschermt open zee maar knijpt straten dicht; knopen in dokbekkens hebben
  aanloopruimte nodig. 148/150 omgelegd, 2 onopgelost (origineel behouden).
- **2026-07-18 · M22: géén globe-library, Three r185 + ES-modules** — globe.gl is een wrapper om wat we al hebben;
  Cesium brengt eigen imagery/terrein mee = een **vierde wereldmodel**; deck.gl = tweede renderstack. Lars koos
  expliciet voor écht upgraden (r128 → r185), met als geaccepteerde prijs dat **M26 deels herbouw** wordt.
  WebGPU bewust niet: koopt doorvoer, geen schoonheid.
- **2026-07-18 · De vectorwereld (NE 1:10M) is de bron van waarheid; satelliet/tegels zijn een skin** — door Lars
  bevestigd. Formaat: quantiseren 1e-4° + delta + zigzag-varint = 3,3 byte/punt (481.675 punten in 1,64 MB).
- **2026-07-18 · Zoom rekent in hoogte boven het oppervlak** (niet afstand tot het middelpunt) + meeschuivend
  nabij-vlak + `logarithmicDepthBuffer` → van 22.000 km tot ~1 km met gelijk zoomgevoel.
- **2026-07-18 · Esri + OSM als tegelbronnen, Google uitgesloten** — earth3dmap geeft bij straatniveau over aan een
  ingesloten Google Maps; die tegels mogen niet in een eigen 3D-bol. Esri gaat zelf tot z19, mét bronvermelding in beeld.
- **2026-07-18 · Belichting en tone mapping horen bij elkaar** — ACES zónder hogere belichting maakt het beeld
  *donkerder*; ingemeten paar zon 6,0 + belichting 1,6 (0% uitgebrande pixels vs 0,03%). Correctie op een eerdere
  te stellige claim: v1's kleurdomein was niet kapot, de winst zit in tone mapping + fysieke belichting van r155+.
- **2026-07-18 · Verifieer tegen een onafhankelijke scheidsrechter** — de 90°-uitlijnfout is gevonden/uitgesloten met
  `earth-water.png` als land/water-orakel (80–83% van de kustpunten op een grens vs 4,8% willekeurig; oude formule 8%).
- **2026-07-18 · Vorm, vaarsnelheid en baan-klem zijn ONTKOPPELD** — zie de architectuurbanner bovenaan. Eén
  puntenlijst droeg alle drie met tegenstrijdige eisen; elke fix brak de ander. Nu: geometrie = vorm ·
  `getPointAt` (booglengte) = snelheid · apart `wp`-profiel per 20 km = klem. Alles verbeterde tegelijk.
- **2026-07-18 · Cache-busting hoort in de pipeline** (`tools/stamp_assets.js`, inhouds-hash `?v=<sha1>`) —
  ongeversioneerde assets + Pages `max-age=600` lieten Lars drie fixes lang de vorige versie zien.
- **2026-07-18 · Een antipodale stabilisator moet op een DICHT stuk netwerk liggen** — bijna-antipodale paren
  hebben een onbepaalde geodeet (MARNET kiest willekeurig). Via 50°N/180° ontstond een kaarsrechte interpolatie
  door leeg water (één artefact voor een ander ingeruild); via **−10°/−80°** (vóór Peru, op de zusterlane) deelt
  Valparaíso→Ningbo nu **95 van z'n 100 punten** met Antofagasta→Ningbo. Kosten +2,5% → +5,8% boven de grote
  cirkel: **vorm boven lengte**.
- **2026-07-18 · Trapjes horen in de baker opgeruimd** (`simplify_water()`): punt weg alleen als het <12 km van
  de lijn buur→buur ligt **en** de kortsluiting over water blijft (zelfde bewijslast als `dezigzag`), met **fijne**
  bemonstering (≥10 monsters) — met de standaard 12 km-stap glipten de Channel Islands door een segment van 15 km.
- **2026-07-18 · MARNET blijft de router; AIS wordt een aparte laag (LAR-482)** — AIS toont *schepen*, geen
  *lading*, en gratis wereldwijde historische AIS bestaat praktisch niet.
- **2026-07-18 · Weergave apart van routing** — *"je kan het water niet goed onderscheiden op deze kaart"* is
  contrast/basemap (LAR-480), bewust gescheiden gehouden.
- **2026-07-17 · `tier` stuurt de LABELS, niet de markers (LAR-481)** — de tier-LOD verborg in de praktijk alléén de
  context-nodes zónder stroom: `forced` (uit `usedNodeIds`) overrulet tier, en dat gold voor **57 van de 63** koper-
  nodes. Chuquicamata (share 1,6, géén stroom) plofte in beeld terwijl Los Pelambres (1,6, wél stroom) bleef staan →
  zichtbaarheid hing af van een toevallig lijntje, niet van belang. Markers staan er nu altijd; de **labels**
  (`labelZoomByTier` + botsingsdetectie) doen het decluttering-werk — dat is ook wat de kaart werkelijk rustig houdt.
  `tierZoom` + de `forced`/`usedNodeIds`-uitzondering **verwijderd** (het gevaar dat ze afdekten kan niet meer
  optreden). Alternatief "stromen óók tieren" bewust ná M18 (raakt `flows.js` = pilot-code, en alle 14).
- **2026-07-17 · Tegelbudget = noodrem, niet dagelijkse limiet + `cos(lat)` in de tegel-zoom (LAR-479)** — `maxTiles: 40`
  was kleiner dan één patch (42–72) → liep bij normaal inzoomen áltijd leeg, en de noord→zuid-vulling gooide dat verlies
  op de onderste rijen. Budget → **96**, patch vult **van het midden naar buiten** (bij een hit verlies je de bolrand,
  niet de halve onderkant). Losse tweede oorzaak: `detailZoomFor()` miste **`cos(lat)`** → hoe noordelijker, hoe méér
  tegels voor dezelfde scherpte (verspilling én de reden dat hoge breedten veel erger waren). `shellMaxZ: 3` ongemoeid.
- **2026-07-17 · Draaien schaalt met de camera-afstand, geankerd op de STARTZOOM** — een vaste rad/px maakte de bol op
  volle zoom ~9× te gevoelig (je ziet dan 9× minder wereld). Bewust niet fysisch 1:1 gemaakt: Lars klaagde alleen over
  ingezoomd, en 1:1 zou de startzoom 4,4× trager maken. De wet is identiek aan 1:1 (evenredig met camera→oppervlak),
  alleen de gain komt uit het bestaande gevoel. Knoppen: `CONFIG.globe.dragSpeed` + `dragRefZoom`.
- **2026-07-17 · De zee-A\* wordt vervangen door een echt vaarlanen-netwerk (M18)** — de routing is aantoonbaar
  onrealistisch (`wp-pac-zuid` dwingt ~1.090 km omweg af op Antofagasta→Shanghai: onze bol +8% vs. grote-cirkel,
  searoute +2%) en de features M19/M20/M21 stáán erop. Precompute at build-time, **gededupliceerd per haven-paar**;
  netwerk bewaren voor M21 (*edge eruit → herrouteren*); **alleen zee-legs**; `searoute` = build-dependency.
  Pilot-first met koper. **Feature-trio hernummerd** M19/M20/M21. Open besluit (Lars): via-punten opruimen of als hint houden.
- **2026-07-17 (pilot) · "MARNET beslist"** — zee-corridors kaal **haven→haven**, óók echte knelpunten niet meer
  als via afdwingen (de pilot vond `wp-taiwan` in ketens waar het niet hoort: +1.497 km); knelpunt-ringen +
  `laneShape`-ankers worden **afgeleid uit de geometrie** (≤`chokeAnchorKm` 150). Diagnose-correctie: de 1.090 km
  was een route-A-meetfout (antipodaal; echt 231 km) — de winst is **−9,3% + gladheid + M21**, zie `design/zeeroutes.md`.
- **2026-07-17 (pilot) · Corridor-reparaties horen in de baker, verificatie op de gétekende curve** — de-zigzag +
  lokale A\*-landomleiding met kustbuffer (`tools/bake_searoutes.py`), kwaliteitscheck `tools/check_corridors.js`;
  én `util.js` bemonstert curves nu **adaptief** (invoerpunten nooit overslaan — uniforme sampling sneed spline over
  schiereilanden terwijl de data al schoon was). **Pilot-status: gebouwd, in visuele test — Japan-observatie +
  wereldbal-duidelijkheid open (zie `memory/next-actions.md`).**
- **2026-07-17 · Verificatie-regel: vergelijk nooit tegen een kale origin→dest A\*-run** — de atlas routeert altijd
  langs de `via`-keten; een kale run produceert paden die de bol nergens tekent ("route A", 16 juli). Vergelijk tegen
  wat `flows.js` werkelijk rendert. Idem methodisch: meet niet in een verborgen Browser-pane (`document.hidden` →
  rAF pauzeert; `GLOBE.start()` draait z'n body synchroon als workaround).
- **2026-07-16 · LAR-471 lab-grown-toggle = het 6e optionele-laag-patroon, via `layer` (niet dedicated type)** — de
  uitgestelde diamant-toggle gebouwd. Recycle-stijl `layer`-patroon (`type:"labgrown"` marker + `layer:"labgrown"` gate op
  nodes én flows), niet reserve/military-dedicated-type — want lab-grown is schaduw-*aanbod* dat de product-arcs ondergraaft.
  `hasLabGrown()` op `f.layer==="labgrown"`. 3 productie-nodes (Henan-HPHT/Surat-CVD/VS-CVD) + 6 flows naar vooral de VS-markt;
  violette octaëder-marker; 5 engine-plekken; default uit, chip alleen bij diamant.
- **2026-07-16 · LAR-447 recycle-tooltip per-grondstof via `recycleHint`-resourceveld** — de gedeelde `ui.js`-tooltip was
  hard-coded REE-bewoord ("<5% magneetschroot"), fout voor PGM (~25% autokat)/grafiet. `recycleHint`-veld + `main.recycleHint()`
  + generieke fallback; hints op REE/PGM/grafiet. Koper (recyclers zonder layer) ongemoeid.
- **2026-07-16 · LAR-448 PGM krijgt een TWEEDE optionele toggle (beursvoorraden) — conventie bewust doorbroken** — Lars akkoord
  ondanks "één toggle per grondstof". Pure data, 0 engine-wijziging (hergebruik exchange-toggle): 3 kluis-nodes (LPPM/NYMEX/
  TOCOM) + 3 `layer:"exchange"`-flows. PGM = eerste grondstof met twee toggles; precedent: een grondstof mag meerdere lagen dragen.
- **2026-07-16 · verificatie-gotcha: Browser-pane cachet script-tag-files** (geen no-cache op python `http.server`) — valideer
  via in-memory injectie + een tweede server-instance op een andere poort (schone origin), niet via `reload()`.
- **2026-07-16 · M17 kolen = de binnenlands-grondstof, géén trechter** — kolen heeft als eerste grondstof **géén enkele
  mondiale flessenhals**: ~85% wordt verbrand waar gedolven (China ~50%, India, VS, Rusland), ~15% zeehandel. Stages als
  ketenpositie: `erts` = mijn→haven/centrale · `raffinaat` = de **internationaal verhandelde bulk** (zeekruisingen +
  landcorridor, waar élk ban/her-routeringsverhaal leeft) · `product` = stroom/staal → binnenlandse kolen (erts+product)
  leest visueel anders dan verhandelde (mét raffinaat-zeeboog). **Twee kolen** (thermisch/cokeskool) via `note`+`tension`
  (nikkel-patroon, niet via stage). China = swing-koper; drie her-routeringen als tensions (Australië-ban/Rusland-oost-draai/
  Mongolië-corridor). **Géén render-modus/marker-types/toggle-laag.** Nieuwe 14e grondstof (plumbing als eigen issue LAR-457).
- **2026-07-16 · M17 één nieuw LANDknelpunt `grens-gashuunsukhait`** (Mongolië-China-Gobi, `kind:"grensovergang"`) in een eigen
  COAL-blok in `_chokepoints.js` — Kasumbalesa/Ruili-patroon; alléén kolen verwijst ernaar → regressievrij. Kolen = 4e grondstof
  (na nikkel/olie/zilver) zonder nieuw zéé-knelpunt. Route-bug: Canadese haven Roberts Bank ingesloten in de Salish Sea (dicht in
  het grove raster) → verplaatst naar Ridley/Prince Rupert (open kust; empirisch getest, zilver-Tacoma→Astoria-les herbevestigd).

- **2026-07-14 · modulair = bron van waarheid, uitgevoerd** — code → deze map + `git init`; M5-fixes geport.
- **2026-07-14 · grensovergang als landpunt** — `kind: "grensovergang"` stempelt de LANDkaart open (niet de
  zeekaart); `isSeaPoint` behandelt hem als landpunt. Per-waypoint `openRadius` voor smalle rivieren (Saint-Laurent).
- **2026-07-14 · Seto-brug** als `LAND_LINK` — Shikoku is een apart raster-eiland → landroute Niihama→Osaka.
- **2026-07-14 · M6 luchtroute-modus** — `mode:"air"` = 3e route-type: buiten de A\*-routering om (`&& !airMode`
  in `flows.js`), altijd een opgetilde great-circle-boog (`flat:false` + `arcStyle`-lift, hoogte ∝ afstand), óók
  in route-view. Korte hops blijven road/rail. Reden: goud vliegt écht die boog (voor lithium was hij fout).
- **2026-07-14 · M6 optionele CB-laag via `layer`-filter** — `type:"cb"`-nodes + `layer:"cb"`-flows filteren op
  `filters.showCentralBanks` (default uit); chip alleen bij grondstoffen met CB-data. Herbruikbaar patroon voor
  toekomstige optionele lagen (bv. koper-beursvoorraden). Nieuwe marker-types airport/hub/cb/recycler.
- **2026-07-14 · M6 single-file als gegenereerde build** — `build-standalone.py` lijnt CSS + lokale scripts uit
  `index.html` inline (three.js-CDN blijft extern) → `atlas-standalone.html`. Niet handmatig editen; regenereren.
- **2026-07-14 · M7 koper = schip/land, geen nieuwe render-modus** — hergebruikt zee-A\*/land-A\* (M3) + scheeps-voyages
  (M4). Twee productvormen via `stage`: sulfide-concentraat (`erts` → smelter, de Andes→China-trechter) vs. SX-EW-kathode
  (`raffinaat` al bij de bron, direct als metaal). Recycling **always-on** (net als goud, niet achter de toggle).
- **2026-07-14 · M7 Copperbelt-landcorridor via het kobalt-patroon** — land-flow mijn→haven (`mode: road/rail`,
  `via: ["grens-kasumbalesa"]`) + aparte ship-flow haven→markt. In een ship-flow worden twee opeenvolgende landpunten
  een rechte lijn → splitsen op de haven. **Elke ship-leg moet op een kustpunt (`port`/`coastal`/`wp-`) landen.**
- **2026-07-14 · M7 beursvoorraden-laag** (`type:"exchange"` / `layer:"exchange"`, filter `showExchangeStocks`) — LME/
  SHFE/COMEX als optionele toggle, default uit, exact het CB-laag-patroon (vier filterplekken + config + ui-chip +
  marker). Marker = koperkleurige CylinderGeometry-spoel, grootte ∝ √`stock`. Herbevestigt: optionele lagen zijn een
  herbruikbaar patroon.
- **2026-07-15 · M8 zeldzame aardmetalen voorbereid (magneet-REE-framing)** — ontwerp-skelet `design/zeldzame-aardmetalen.md`;
  framing = **magneet-REE (NdPr + Dy/Tb)** (optie 2 na Lars' "is REE niet te generiek?": REE is intrinsiek een groep,
  winning blijft gemengd erts, scheiding = de knijp). Magneet = stage `product`; schip+land (géén nieuwe render-modus);
  nieuw Myanmar→China `grens-*`-knelpunt bij de bouw; recycling = optionele toggle. Nog niet gebouwd; Linear M8 aan te
  maken (MCP-auth ontbrak). Details in `memory/decisions.md`.
- **2026-07-15 · M9 uranium = 4-staps keten op 3 stages** — winning + conversie = `erts` (feed), **verrijking = `raffinaat`
  (de flessenhals)**, splijtstof = `product`, reactoren = `market`. Node-types alle bestaand → géén nieuwe marker-styling.
  De verrijkings-knijp (~44% Rusland) draagt via een `tension`, geen `wp-` — zoals Ticino bij goud. Schip+land, geen nieuwe modus.
- **2026-07-15 · M9 Kaspische oversteek + Dardanellen** (`_chokepoints.js`) — 3 vaarpunten (`wp-kaspisch-n/-m/-z`) forceren
  een watercorridor Aktau↔Bakoe (Kaspische Zee = ingesloten zee, valt deels als land in het raster); `wp-dardanellen` houdt
  naast `wp-bosporus` de Zwarte-Zee-uitgang open (anders geen weg Poti→Middellandse Zee). Alleen uranium gebruikt ze → geen
  impact op andere grondstoffen. Landlocked-routering (Kazachstan/Niger) = het kobalt/koper-corridorpatroon (land-flow →
  haven + aparte ship-flow). **CANDU-uitzondering** eerlijk gemodelleerd (natuurlijk uranium, geen verrijking). Details in `memory/decisions.md`.
- **2026-07-15 · M9 militaire-kringloop-toggle uitgesteld → ALSNOG GEBOUWD** (LAR-414 Backlog → **Done**, commit `6a6d062`) — de
  optionele `layer:"secondary"`-laag vereiste code in `flows/ui/main/config/markers`, destijds dirty door de parallelle M8-sessie →
  eerst alleen de data-laag. Op Lars' verzoek afgemaakt zodra de engine schoon was: het **5e** optionele-laag-patroon
  (`type:"military"`-nodes + `layer:"secondary"`-flows + `showMilitary`/`hasMilitary()`), exact het olie-`reserve`-patroon in 5 plekken.
  4 military-nodes (Rosatom down-blend/HEU, tails-herverrijking, US DOE, US strategische reserve) + 5 `secondary`-flows (o.a. de
  historische Megatons-to-Megawatts-stroom Rusland→VS via `u-fab-us` `coastal:true`) + tension `u-t-military`. Headless: uranium 60 legs /
  0 kapot / 0 straight; toggle uit→aan +4 nodes/+5 flows; chip alleen bij uranium. Sectie J: alleen mijn 6 bestanden gestaged (PGM/silver-sessie ontzien).
- **2026-07-15 · M8 magneet-REE-framing gebouwd** — `data/rare-earths.js` "uitgewerkt" (41/38/6): `id` blijft `rare-earths`,
  `symbol: NdPr`, `unit: kt magneet-REO/jaar`. Scheiding én magneetfabrieken beide `type:"refinery"` (het `erts`/`raffinaat`/
  `product`-stagekleur draagt het onderscheid concentraat→NdPr/Dy-oxide→NdFeB-magneet); magneet = stage `product` (geen 4e stage).
  Schip+land, géén nieuwe render-modus. Reden: één scherp verhaal (NdPr+Dy/Tb), winning blijft eerlijk gemengd erts → scheiding = de knijp.
- **2026-07-15 · M8 grenscorridor `grens-ruili`** (`_chokepoints.js`, `kind:"grensovergang"`, 24.02/97.85) — Myanmar→China, exact
  het Kasumbalesa-patroon (landpunt, houdt de landkaart open). Draagt de Dy/Tb-landstroom Kachin→Ganzhou; alleen REE gebruikt het.
- **2026-07-15 · M8 recycling-toggle** (`layer:"recycle"`, `showRecycle`, default uit) = het **derde** optionele-laag-patroon (na
  CB en exchange). Bewust `layer:"recycle"` op flows **én** recycler-nodes: de node-gate zit op `node.layer==="recycle"` (niet op
  `type==="recycler"`) en `hasRecycle()` op `f.layer==="recycle"`, zodat **koper's always-on recyclers** (zónder `layer`) ongemoeid
  blijven en alleen REE de toggle/chip krijgt. Vijf plekken: `config.js`/`main.js`/`flows.js`/`markers.js`/`ui.js`.
- **2026-07-15 · M8 co-located nodes ~30–45 km uit elkaar** — twee nodes van dezelfde grondstof in één 0,25°-cel geven een 1-punts
  route (`degDist:0`, onzichtbare arc). Ref/magneet/recycler in dezelfde stad (Baotou/Ganzhou/MP/La Rochelle/Fort Worth) verschoven
  zodat de lokale scheiding→magneet-arcs zichtbaar renderen én de headless-teller schoon op 0 kapot blijft.
- **2026-07-15 · M10 nikkel = de omgekeerde trechter, koper als template** — nikkel is een schip/land-grondstof (géén luchtvracht →
  koper, niet goud, is het model). De "aha" is dat Indonesië via de **exportban op ruw erts** de mijn ÉN de raffinage aan land trok:
  het erts blíjft in het land (korte mijn→smelter-hops, `stage:"erts"`, `mode:"road"`) en gaat pas als NPI/matte/MHP de zee op —
  andersom dan koper/lithium waar het erts/concentraat naar China vaart. Class-1 (batterij/sulfaat) vs class-2 (roestvrij/NPI) gedragen
  via `stage` + `note` + een `tension` (geen 4e stage). Het Filipijnse ruw-erts (`stage:"erts"` naar China, géén ban) = het contrast.
- **2026-07-15 · M10 géén nieuw chokepoint (tweede na koper)** — nikkel draait volledig op de bestaande routekaart (Makassar/Lombok/
  SCS/Taiwan; Deense Straten voor Fins/Baltisch class-1; Panama + Pacific-vaarpunten voor Cuba/NC; de Saint-Laurent-keten voor
  Voisey's Bay→Sudbury). Bewust zo — óók om de gedeelde `_chokepoints.js` niet te raken terwijl de parallelle olie-sessie die dirty had.
- **2026-07-15 · M10 beursvoorraden-laag (LME) = 0 engine-wijziging** — de optionele exchange-toggle van koper (`type:"exchange"`/
  `layer:"exchange"`, `showExchangeStocks`) is generiek: `hasExchangeStocks()` vuurt op elke actieve grondstof met een exchange-node,
  en de flow-gate/marker/chip zijn niet koper-specifiek. Nikkel voegt dus 4 LME-nodes + 5 `layer:"exchange"`-flows toe **zonder één
  `src/*`/`config.js`-regel te wijzigen** — de eerste keer dat een optionele laag puur via de data-laag wordt hergebruikt. Nuance eerlijk
  gemodelleerd: **alleen class-1 is LME-leverbaar** (NPI/MHP/sulfaat niet) → LME-prijs ≠ fysieke markt (de 2022-squeeze als `tension`).
  Recycling **always-on** (koper-patroon, `type:"recycler"` zónder `layer`).
- **2026-07-15 · M11 olie = het knelpunten-netwerk, géén nieuw chokepoint** — olie's vorm is bewust anders dan alle eerdere: geen
  enkele trechter maar het **hele bestaande net van zeestraten dat tegelijk oplicht** (Hormuz #1 met 15 stromen, dan Malakka/Suez/Bab/
  Bosporus/Panama/Kaap). Bewust géén nieuw knelpunt toegevoegd — dat olie het hele net laat oplichten ís de boodschap. Wél 3 kleine
  **navigatie-vaarpunten** (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in een gelabeld OIL-blok in `_chokepoints.js`, om de VS/
  Venezuela-routes op het water te houden; olie-only → regressievrij. Keten op de 3 stages met **petrochemie als 3e daad**
  (`erts`=crude → `raffinaat`=producten → `product`=nafta→kraker→kunststof). Schip + `mode:"pipeline"`, géén nieuwe render-modus;
  crude-stromen starten bij de mijn met de export-terminal als 1e via-punt (gathering-leg routeert auto als land). Kust-raffinaderijen `coastal:true`.
- **2026-07-15 · M11 SPR-voorraden-toggle uitgesteld → alsnog gebouwd** (LAR-432 Backlog → **Done**, commit `86c8c1f`) — de
  optionele `layer:"reserve"`-laag (strategische petroleumreserves, olie's CB/beurs/recycling-equivalent) raakt de 5 gedeelde
  engine-bestanden; tijdens de parallelle M10-nikkel-sessie eerst alleen de data-laag gebouwd (zoals uranium's LAR-414, sectie J).
  Zodra de tree schoon was (Lars: "de voorraden bij olie is een goed idee") de toggle alsnog toegevoegd = het **vierde** optionele-laag-
  patroon, exact het koper-`exchange`-patroon (dedicated `type:"reserve"`, `hasReserves()` op `n.type`) + olie-amber tank-marker.
  5 SPR-nodes + 5 vul-flows + tension `oil-t-spr`. Headless: toggle uit=45/46, aan=50/51 (+5/+5), 0 kapot/0 straight, chip alleen bij olie, regressievrij.

- **2026-07-15 · M13 zilver = de eerste écht nieuwe grondstof (11e), niet een basis-upgrade** — nieuw `data/silver.js` +
  `<script>`-tag in `index.html` + 5 zilver-checks in `build-standalone.py` (LAR-436, apart issue want het is het concrete
  "anders" t.o.v. het patroon). De vorm: **géén geografisch knelpunt** — de knijp is tweezijdig/structureel (bijproduct-aanbod
  ~70-75% inelastisch + vraagconcentratie in de Chinese zonnepanelen-industrie → tekort dat de kluisvoorraden aftapt). Het
  grondstof-eigen "nieuwe element" is dus geen chokepoint maar het **by-product-winning-model** (mijn-nodes = zink/lood/koper/
  goud-mijnen met hoofdmetaal-`note`). Schip+land (koper/nikkel-model, géén goud-lucht), géén nieuwe render-modus, **géén nieuw
  chokepoint** (derde na nikkel/olie). Keten erts(doré)→raffinaat(good-delivery baar)→product(solar/elektronica/sieraad).
- **2026-07-15 · M13 kluis-/beursvoorraden = exchange-toggle hergebruikt, 0 engine-wijziging** — zilver-kluizen (LBMA/COMEX/SGE)
  ZIJN beurs-/kluisvoorraden → de bestaande koper/nikkel-`exchange`-semantiek (`type:"exchange"`/`layer:"exchange"`,
  `showExchangeStocks`) past exact; géén dedicated `type` nodig (anders dan olie-reserve). 2e puur-datagedreven hergebruik na
  nikkel: 3 exchange-nodes + 3 `layer:"exchange"`-aftap-flows (tonen het tekort), chip "beursvoorraden" verschijnt automatisch.
  Recycling always-on (~15-18%, koper/nikkel-patroon). Details in `memory/decisions.md`.
- **2026-07-15 · M13 twee route-bugs empirisch gefixt** — kandidaat-coördinaten eerst door `Routing.sea` gehaald, dán verplaatst:
  VS-raffinage Tacoma→Astoria (Puget Sound valt dicht in het grove raster) + China-solar Suzhou-binnenland→Jiangsu-kust. Sectie J
  gevolgd: alléén eigen bestanden gecommit (`e091848`) — parallelle sessie's engine-files (uranium-toggle) ongemoeid.
- **2026-07-15 · M12 PGM = luchtvracht (hergebruik goud-air-mode), géén nieuw element** — geraffineerd Pt/Pd/Rh is per kilo even
  waardevol als goud → luchtvracht (`mode:"air"`, JNB-gateway; "✈ vluchten" via `activeHasAir()`); concentraat/matte over land.
  Het grondstof-eigen "nieuwe element" is bewust géén nieuw element: derde grondstof na koper/nikkel die niets aan
  `_chokepoints.js` toevoegt en 0 engine-wijziging vergt. De vorm = de scherpste twee-landen/twee-metalen-concentratie
  (ZA/Bushveld = Pt/Rh, Rusland/Norilsk = Pd); de knijp is structureel (6 tensions), niet geografisch (geen `wp-`).
- **2026-07-15 · M12 recycling-toggle = REE-patroon hergebruikt, 0 engine-wijziging** — autokat-recycling (~25% van het aanbod,
  via dezelfde westerse huizen JM/BASF/Umicore/Heraeus/Tanaka) als optionele toggle: `type:"recycler"` + `layer:"recycle"` op
  nodes én flows, chip via `hasRecycle()`. Bewust recycling (niet de exchange-laag) als PGM's ene toggle = het dominantere PGM-
  verhaal. SAMECELL-fix: Japan-recycler zat in Tokyo Bay → snapte naar Tanaka's cel → verplaatst naar Kanagawa (`degDist:0`).
  Afwijkingen als aparte issues (Lars' verzoek): LAR-447 (recycle-chip-tooltip nog REE-bewoord, raakt gedeelde `ui.js`) + LAR-448
  (optionele Pt/Pd-exchange-laag, pure data). Sectie J: alléén `data/pgm.js`+`design/pgm.md` gecommit (`2c4b668`). Details in `memory/decisions.md`.

## E - Memory Map

De projectgeschiedenis en werkgeheugen leven in `memory/` (6 files, conventie zoals de andere projecten):

- `project-brief.md` — wat het is, huidige baseline, richting, harde grenzen
- `current-strategy.md` — hoe we nu bouwen (architectuur, sjabloon, aanpak per grondstof)
- `next-actions.md` — concrete volgende stappen (M5 + goud-ontwerp)
- `decisions.md` — vastgelegde technische/inhoudelijke keuzes
- `bugs-and-risks.md` — openstaande bugs (M5) en risico's
- `session-summaries.md` — per sessie een samenvatting

Daarnaast `design/`:
- `_brief-template.md` — **herbruikbare template voor de grondstof-brief** (alle nodes/stromen op een rij
  vóór het code wordt; sluit 1-op-1 aan op het `.js`-schema). Kopieer → `data/<grondstof>.md` en vul in.
- `goud.md` — het uitgewerkte goud-ontwerp (wordt bij LAR-397/398 een volledig ingevulde brief).

De browsbare wiki-samenvatting staat onder `Portable LLM brain\wiki\projects\General\grondstoffen-atlas\`.

## F - References

- Linear: project "Grondstoffen Atlas" — https://linear.app/error-logger/project/grondstoffen-atlas-ace3a91b93fb
- Issues M0–M5: LAR-378 t/m LAR-396.

## G - Project-specific overrides

- **Taal:** UI-teksten en annotaties in de atlas zijn **Nederlandstalig**.
- **Geen framework/bundler introduceren** zonder expliciete afstemming — de globals-opzet is bewust.
- Coördinaten zijn `lat`/`lon` (west = negatief). Fouten hierin zijn een terugkerende bron van
  verkeerde routes (zie M5).

## H - Onboarding-checklist

1. [x] M5 door aparte CC-sessie klaar + geverifieerd (2026-07-14); LAR-393/394/395/396 Done.
2. [x] Wiki-pagina + `now.md`-regel + Pinecone-gist (eerste wrapup, 2026-07-14).
3. [x] Beslist: **modulair = bron van waarheid** (single-file = gegenereerde build).
4. [x] Modulaire code **verplaatst** naar deze map + `git init` = werkbasis. ✅ **GitHub-remote live (2026-07-15):** `larswalters/grondstoffen-atlas` (public) + **GitHub Pages** → https://larswalters.github.io/grondstoffen-atlas/ (elke `git push origin main` deployt).
5. [x] **M5-fixes geport** uit de single-file naar de modulaire code + geverifieerd (214 legs, 0 kapotte routes). Visuele check op Netlify/mobiel rest nog (WebGL-screenshot lukte niet).
6. [x] **M6 · Goud uitgevoerd** (2026-07-14): research LAR-397/398 → `data/goud.js` LAR-401 + luchtroute-modus LAR-399 + voyages-lucht LAR-400 + CB-toggle LAR-402. Headless geverifieerd (371 legs/0 kapot). LAR-403 rest = visuele bevestiging Netlify/mobiel.
7. [x] **M7 · Koper uitgevoerd** (2026-07-14): `data/copper.js` "uitgewerkt" (69 nodes/50 flows/5 tensions) — Andes-concentraat-trechter + Copperbelt-kathode over land (Kasumbalesa) + beursvoorraden-laag (LAR-408, `layer:"exchange"`). Headless geverifieerd: koper 145 legs / 0 kapot, regressie 388/0. Rest = visuele bevestiging Netlify/mobiel + code-commit (Lars' seintje) + Linear LAR-404..409 → Done (MCP-auth ontbrak).
8. [x] **M9 · Uranium uitgevoerd** (2026-07-15): `design/uranium.md` (`d016ab8`) → `data/uranium.js` "uitgewerkt" (38 nodes/36 flows/6 tensions) + Kaspische oversteek/Dardanellen in `_chokepoints.js` (`76c0333`). 4-staps keten met verrijking als flessenhals (~44% Rusland) + Trans-Kaspische route + VVER-lock-in + CANDU-uitzondering. Headless: 54 legs/0 kapot, regressievrij. **Linear M9 · Uranium + LAR-410..415** aangemaakt (410-413 Done; 414 Backlog = uitgestelde militaire-kringloop-toggle; 415 In Progress = visuele bevestiging). Rest = visuele bevestiging Netlify/mobiel.
9. [x] **M8 · Zeldzame aardmetalen uitgevoerd** (2026-07-15): `data/rare-earths.js` van "basis" (9/5) → "uitgewerkt" (41 nodes/38 flows/6 tensions), magneet-REE-framing (NdPr+Dy/Tb) + `grens-ruili` (Myanmar→China) in `_chokepoints.js` + recycling-toggle (`layer:"recycle"`, 5 plekken). Ganzhou-scheidingstrechter + Dy/Tb-landstroom + Mountain-Pass-rondreis + NdFeB-waaier. Headless: 90 legs/0 kapot/0 straight, regressievrij. **Linear M8 · LAR-416..420 Done; 421 In Progress** (visuele bevestiging Netlify/mobiel = Lars).
10. [x] **M10 · Nikkel uitgevoerd** (2026-07-15): `data/nickel.js` van "basis" (13/4) → "uitgewerkt" (50 nodes/46 flows/6 tensions) + `design/nikkel.md` + nikkel-checks in `build-standalone.py`. Indonesië-onshoring-trechter (exportban: mijn+raffinage in tien jaar, IMIP/IWIP) + twee nikkels (class-1 batterij vs class-2 roestvrij) + prijscrash-shakeout (Nickel West 2024) + LME-nuance (2022-squeeze). Schip+land, géén nieuw chokepoint; beursvoorraden-laag hergebruikt de bestaande exchange-toggle (**0 engine-wijziging**); recycling always-on. Headless: **nikkel 91 legs / 0 kapot / 0 straight**, regressie schoon. Commit `08aa4f5` (lokaal-only, Claude-trailer). **Linear M10 · LAR-422..426 Done, 427 In Progress**. Overige op basis: grafiet, PGM.
11. [x] **M11 · Olie uitgevoerd** (2026-07-15): `data/oil.js` van "basis" (18/15) → "uitgewerkt" (45 nodes/46 flows/6 tensions) + `design/olie.md` + 4 olie-checks in `build-standalone.py`. Het **knelpunten-netwerk dat tegelijk oplicht** (Hormuz #1 met 15 stromen, Malakka, Suez/Bab, Bosporus, Panama, Kaap) → **géén nieuw chokepoint** (eigen aha), wel 3 olie-only vaarpunten (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in `_chokepoints.js`. Drie verhalen: Hormuz-bypass-pijpleidingen (Yanbu/Fujairah) + Rusland-omleiding 2022→ (India/China) + VS-schalie-ommekeer. Keten 3 stages (erts/raffinaat/petrochemie), schip+pijpleiding, géén nieuwe render-modus. Headless: **olie 210 legs / 0 kapot / 0 straight**, regressievrij (baseline 5 = lithium 4 + goud 1). Commit `1d4ece5` (lokaal-only, Claude-trailer). **SPR-voorraden-toggle (`layer:"reserve"`) daarna alsnog gebouwd** (LAR-432 Done, commit `86c8c1f`) = het vierde optionele-laag-patroon; toggle uit=45/46, aan=50/51, chip "voorraden" alleen bij olie. **Linear M11 · LAR-428..432 Done, 433 In Progress**. Overige op basis: grafiet, PGM.

12. [x] **M13 · Zilver uitgevoerd** (2026-07-15): de **eerste écht nieuwe grondstof** sinds de basis-10 — nieuw `data/silver.js` (42 nodes/37 flows/6 tensions) + `design/zilver.md` + `<script src="data/silver.js">` in `index.html` + 5 zilver-checks in `build-standalone.py`. Géén winnings-trechter: ~70-75% **bijproduct** van zink/lood/koper/goud (aanbod inelastisch); de concentratie zit downstream — de **Chinese zonnepanelen-industrie** trekt zilver weg → **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt. Schip+land, géén nieuwe render-modus, **géén nieuw chokepoint** (derde na nikkel/olie). Kluis-/beursvoorraden-laag = hergebruik van de bestaande exchange-toggle (**0 engine-wijziging**, nikkel-patroon); recycling always-on. 2 route-bugs empirisch gefixt (Tacoma→Astoria; solar Suzhou→Jiangsu-kust). Headless: **zilver 85 legs / 0 kapot / 0 straight**, regressievrij. Commit `e091848` (lokaal-only, Claude-trailer, alléén eigen bestanden — sectie J). **Linear M13 · LAR-434..438 Done, 439 In Progress**.

13. [x] **M12 · PGM uitgevoerd** (2026-07-15): `data/pgm.js` van "basis" (9/3) → "uitgewerkt" (38 nodes/41 flows/6 tensions) + `design/pgm.md` + 4 PGM-checks in `build-standalone.py`. De scherpste twee-landen/twee-metalen-concentratie: **Zuid-Afrika/Bushveld = Pt/Rh** + **Rusland/Norilsk = Pd**. PGM **vliegt** → hergebruik van de goud-air-mode (`mode:"air"`, JNB-gateway); concentraat/matte over land. **Géén nieuw chokepoint, géén engine-wijziging** (derde na koper/nikkel). **Recycling-toggle** (`layer:"recycle"`, ~25% autokat via JM/BASF/Umicore/Heraeus/Tanaka) = hergebruik van het REE-patroon met **0 engine-wijziging**. 6 tensions (concentratie, autokat + Pt↔Pd, rodium-spof, palladium/Rusland, waterstof-hedge, Eskom). Headless: **pgm 49 legs / 0 kapot / 0 straight / 0 degenerate arcs**, regressievrij (SAMECELL-fix Japan-recycler → Kanagawa). Commit `2c4b668` (lokaal-only, Claude-trailer, alléén eigen bestanden — sectie J). **Linear M12 · PGM + LAR-440..448** (5 Done, 445 In Progress; 446 Done na de build; 447/448 Backlog = afwijkingen: REE-bewoorde recycle-tooltip + optionele Pt/Pd-exchange-laag). **Alleen grafiet nog op "basis".**

## I - Runbook: "werk grondstof X uit" (self-serve)

Vaste flow om een grondstof uit te werken, identiek aan hoe goud/koper/uranium/REE/zilver/kolen zijn gedaan.
**De basis-10 is compleet** (grafiet/M14 was de laatste). De groei zit nu in **nieuwe grondstoffen** (niet basis→uitgewerkt maar
een nieuw `data/<x>.js` + `<script>`-tag + build-check, het zilver/kolen-patroon — leg dat "anders"-punt als eigen issue vast,
zoals LAR-436/457). Gedaan als nieuwe grondstof: zilver (M13), kolen (M17); diamant + gas lopen parallel. Doe de stappen op
volgorde; commit code en wrapup-docs apart. **Let bij parallel werk streng op sectie J** (alléén eigen bestanden stagen; bij een
gedeelde `index.html` met meerdere nieuwe script-regels in één hunk: stage alléén je eigen regel via `git apply --cached`).

**0. Oriënteer.** Lees `memory/current-strategy.md` (architectuur + sjabloon) + `memory/decisions.md` (de vaste patronen) +
   `design/_brief-template.md`. Kijk naar een recent uitgewerkt bestand als voorbeeld — `data/copper.js` (schip/land + optionele
   toggle) of `data/uranium.js` (tension-knijp + nieuw chokepoint) liggen het dichtst bij de meeste grondstoffen.

**1. Linear vastleggen vóór het codewerk.** Maak (via de Linear-MCP die zónder OAuth werkt — de `331d1eb1…`-server met
   `save_milestone`/`save_issue`, **niet** de auth-vereiste `plugin:engineering:linear`; zie [[linear-mcp-two-surfaces]]) een
   **milestone** `M<n> · <Grondstof>` in project "Grondstoffen Atlas" (team **Lars/LAR**) + de standaard **±6 issues**, gespiegeld op M6/M7/M9:
   - research upstream (winning/mijnbouw) · research downstream (raffinage/consumptie/recycling)
   - het grondstof-eigen **nieuwe element** (nieuw chokepoint/corridor, of een render-modus) — sla over als de grondstof volledig bestaande routes hergebruikt
   - `data/<x>.js` van "basis" → "uitgewerkt"
   - de optionele **toggle-laag** (CB/beurs/recycling-stijl) — alleen als de grondstof er een heeft
   - verificatie (headless) + single-file build + visuele bevestiging Netlify/mobiel
   Research mag inline in de brief (stap 2) — die research-issues gaan Done zodra de brief staat.

**2. Ontwerp eerst (brief).** Kopieer `design/_brief-template.md` → `design/<x>.md` en vul alle knopen/stromen in
   (operators, capaciteiten, `lat`/`lon`, transportmodi, de "aha"/knijp van deze grondstof). Eerst ontwerpen, dan bouwen.

**3. Bouw `data/<x>.js`** volgens het lithium-schema (zie `data/_registry.js` voor het veld-schema):
   - Metadata: `id`/`name`/`symbol`/`color`/`unit`/`blurb`, `detail:"uitgewerkt"`.
   - Nodes (`mine`/`refinery`/`port`/`market` + evt. `recycler`/`exchange`/`cb`), flows met `stage` (`erts`→`raffinaat`→`product`)
     + `mode` (`ship`/`rail`/`road`) + `via:[...]` langs havens en `wp-*`/`grens-*`, en `tensions` voor de knijppunten.
   - **Registratie is er al** voor de bestaande 10 grondstoffen (script-tag in `index.html`). Een *nieuwe 11e* grondstof: voeg een
     `<script src="data/<x>.js">` toe in `index.html` (de build leest die volgorde).
   - **Harde regel:** elke ship-leg moet op een kustpunt landen (`port` / `coastal:true` / `wp-*`), anders valt hij op de landkaart terug
     of vindt geen pad. Landlocked → kobalt/koper-corridorpatroon (land-flow mijn→haven `via:["grens-…"]` + aparte ship-flow haven→markt).
   - Nieuw chokepoint/corridor nodig? Voeg het toe aan `data/_chokepoints.js` (`kind:"grensovergang"` voor een landgrens; `wp-…` + evt.
     `openRadius` voor een zeestraat/ingesloten zee). Twee nodes in dezelfde 0,25°-cel geven een onzichtbare `degDist:0`-arc → ~30–45 km uit elkaar.

**4. Engine-wijziging (alleen als nodig).** Een nieuwe **optionele toggle-laag** = het vaste patroon op vijf plekken
   (`config.js` marker-size · `main.js` filters-default + `has…()` + voyages-gate · `flows.js` flow-gate · `markers.js` node-gate · `ui.js` chip).
   Een nieuwe **render-modus** (zoals goud-lucht) raakt `flows.js`. Zie sectie J vóór je gedeelde `src/*`-bestanden aanraakt bij parallel werk.

**5. Verifieer headless in de draaiende atlas.** Start de dev-server (launch.json-entry, zie sectie J voor de poort), open 'm in de
   Browser-pane, en draai via `javascript_tool` een legs-check die per flow de stops (`from`+`via`+`to`) langs `Routing.sea`/`Routing.land`
   routeert en telt: **doel = <grondstof> X legs / 0 kapot / 0 straight**, plus **regressie** over alle grondstoffen (globaal blijft 5 kapot =
   de bekende `degDist:0` lithium(4)+goud(1)-baseline; nieuwe grondstof voegt 0 toe). Check ook: geen console-warnings (onbekende via-/node-ids),
   toggle aan/uit voegt de juiste flows/nodes toe. Visueel het emergente plaatje bekijken (screenshot); **volledige visuele bevestiging op
   Netlify/mobiel = Lars** (WebGL-screenshot lukt niet betrouwbaar headless).

**6. Build + wrapup.** `python build-standalone.py` (voeg een REE-stijl sanity-check toe voor je grondstof) → `atlas-standalone.html`.
   Dan de **`wrapup`-skill**: die voert de Definition of Done uit (vault-sessiesamenvatting + integratie in projectpagina/`now.md`/`index.md`/
   `log.md`/`timeline.md`, project-`memory/`-sync, `CLAUDE.md`/checklist, Linear op Done, Pinecone-gist, code + docs committen). Commit code en
   wrapup-docs als **twee aparte commits** met de Claude-trailer; repo is **lokaal-only** (geen remote → geen push).

## J - Parallel werken (meerdere sessies tegelijk)

Twee sessies kunnen **verschillende grondstoffen tegelijk** uitwerken (is al gebeurd: M7+M8, en M9 naast M8). Elke grondstof heeft z'n
eigen `data/<x>.js` + `design/<x>.md` — die botsen nooit. Frictie zit alleen op het **gedeelde oppervlak**. Regels:

1. **Stage alleen je eigen bestanden — nooit `git add -A`/`git add .`.** De working tree bevat de half-af bestanden van de andere sessie.
   Voorbeeld: `git add data/<x>.js design/<x>.md` (+ je eigen `_chokepoints.js`-toevoeging als je die deed). Veeg je alles op, dan commit
   je hun onvoltooide werk. Twijfel je of een gewijzigd bestand van jou is? Laat het ongestaged en noem het.
2. **Gedeelde engine-bestanden = `src/*.js`, `config.js`, `data/_chokepoints.js`, `build-standalone.py`.** Raakt jouw grondstof die, en heeft
   de andere sessie ze dirty? **Bouw dan eerst alleen de data-laag en stel de engine-wijziging uit** (zoals uranium's militaire-toggle → LAR-414
   Backlog). Voeg de toggle/modus later toe als de tree schoon is.
3. **Nieuwe chokepoints append je in een eigen, gelabeld blok** in `data/_chokepoints.js` en commit dat vroeg/apart — losse toevoegingen aan het
   eind conflicteren zelden textueel. Alleen jouw grondstof mag ernaar verwijzen (geen impact op de andere 9).
4. **Eigen dev-server-poort per sessie** (launch.json): `grondstoffen-atlas` (8732) · `grondstoffen-atlas-2` (8733) · `-3` (8734) · `-4` (8735).
   Laat niet twee sessies dezelfde poort binden. (Één draaiende server delen kan ook — het is statische file-serving; elke browser-load leest vers.)
5. **Wrapups sequentieel, `git pull --rebase` eerst.** De vault is een gedeelde repo: `log.md`/`index.md`/`timeline.md` mergen automatisch
   (`merge=union`), maar `now.md` en de projectpagina niet — laat één sessie helemaal afwrappen (incl. vault-push) vóór de ander z'n vault-write doet.
   Linear (aparte milestones/issues) en Pinecone zijn onafhankelijk en botsen niet.
6. **Maximale isolatie (optioneel):** geef elke sessie een eigen **git-worktree** (aparte werkmap, eigen branch) → de working trees zijn fysiek
   gescheiden en conflicten komen pas netjes bij het mergen boven i.p.v. als rommelige gedeelde tree. Werkt ook op deze lokaal-only repo; kost een merge-stap.
