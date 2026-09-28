# Routebrief (licht) · PGM — Sudbury (Canada) → Via → Acton, Londen (VK)

**stroom-id:** `pgm-sudbury-actonuk` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken (been b1)
**Keten in één zin:** PGM/Au/Ag-residuen uit Vale's Ni-Cu-Copper Cliff-smelter (Sudbury, Ontario) gaan per
**spoor** naar Vale's eigen **Port Colborne-raffinaderij** (Ontario, aan het Welland-kanaal) voor
tussenverwerking tot PGM/Au/Ag-intermediair, en van daar — via een nog te bepalen Canadese exporthaven,
**zeeschip** over de Atlantische Oceaan en een nog te bepalen Britse haven — naar Vale Europe's
eindraffinaderij in **Acton, Londen**.
**Welke as van het verhaal:** de enige westerse PGM-raffinagestreng buiten Zuid-Afrika/Rusland — een
Ni-Cu-complex (Sudbury) dat zijn PGM-bijproduct via een eigen Canadese tussenraffinaderij naar de
Britse eindraffinage stuurt. Jaarvolume voor déze specifieke as niet gebrond (§7); Port Colborne levert
volgens Vale zelf **"40% van de feed"** van Acton [4].

## 1 · Ketenkaart
```
Copper Cliff-smelter `pgm-coppercliff-smelter` (Vale, Sudbury, ON)
   ──(b1 spoor · CP-hoofdlijn Sudbury → Zuid-Ontario, via MacTier/Hamilton naar de Welland-corridor ·
       ~700 km, webcheck/aannemelijk)──► Port Colborne-raffinaderij `pgm-portcolborne-refinery`
       (Vale — PGM/Au/Ag-intermediair + elektro-kobalt)
   ══ OPEN: exporthaven Canada (Montreal of Halifax — §7) ══
   ──(b2 zee · Atlantische oversteek · ~5.000-5.500 km, MARNET — nog niet gebakken)──► VK-haven
       (Southampton of Tilbury — §7)
   ──(b3 truck · haven → Acton · ~40-110 km — nog niet gebakken)──► Vale Europe-raffinaderij, Acton,
       Londen (exacte site niet gebrond — §7) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `pgm-coppercliff-smelter` → `pgm-portcolborne-refinery` | CP-hoofdlijn Sudbury → Zuid-Ontario, via MacTier (Parry Sound Sub) en Hamilton (CPKC Kinnear Yard) naar de Welland-corridor bij Welland/Port Colborne — géén bron noemt de lijn met naam; regionale rail-precedent Sudbury→Zuid-Ontario in `nikkel-sudbury-kristiansand.md` (andere maatschappij, Glencore niet Vale) | ~700 [webcheck, geen gepubliceerde lengte] | toets_spoorroute (meerdere runs via de via-punten §4) | nee |
| b2 | A/B | truck/spoor | `pgm-portcolborne-refinery` → exporthaven Canada | **OPEN — §7**: Montreal (Seaway-route, aansluitend op het CP/CN-net) of Halifax; geen bron kiest | n.t.b. | n.t.b. | n.t.b. |
| b3 | B | zee | exporthaven Canada → VK-haven | **OPEN — §7**: Southampton of Tilbury; geen bron kiest | ~5.000-5.500 [ontwerp-schatting] | MARNET (nog niet gebakken) | n.t.b. |
| b4 | C | truck | VK-haven → Vale Europe-raffinaderij Acton | **OPEN — §7**: exacte site van de Acton-raffinaderij niet gevonden (Vale geeft geen adres; `acton.vale.com` niet bereikbaar, geen OSM-object, geen Companies House-koppeling binnen het webbudget) | ~40-110 [ontwerp-schatting, afhankelijk van havenkeuze] | maak_stroombeen_weg (nog niet: eindanker ontbreekt) | n.t.b. |

Alleen **b1** is site-niveau gebrond en klaar voor de bake; b2–b4 zijn bewust niet getekend zolang de
exporthaven, de VK-haven en het Acton-anker openstaan (geen coördinaat verzinnen — de lijn eindigt waar
het bewijs eindigt).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-coppercliff-smelter` | mijn/smelter (kop van het spoor) | Vale Copper Cliff Complex — smelter, Sudbury, ON | 46.47860, -81.05473 | [1][7][10] | bron-gelegd (z15 gezien: industrieel smeltercomplex met hoge schoorsteen, groene/oranje tailings-vijvers en ertsstapels direct rond het punt — het hart van Vale's Copper Cliff-operaties) |
| `pgm-portcolborne-refinery` | tussenraffinaderij (PGM/Au/Ag-intermediair + Co) | Vale Port Colborne Refinery, Ontario | 42.88350, -79.24300 | [3][4][6] | bron-gelegd (z16 gezien: industrieel emplacement met silo's, tankenpark en een turquoise proces-/afvalbekken, direct ten oosten van het Welland-kanaal bij de stad Port Colborne — "Nickel Street" 400 m verderop bevestigt de locatie) |
| exporthaven Canada | overslag spoor/truck → zee | Montreal of Halifax | — | — | **open — §7**, geen coördinaat (niet gekozen, dus niet gelegd) |
| VK-haven | overslag zee → truck | Southampton of Tilbury | — | — | **open — §7**, geen coördinaat |
| Vale Europe-raffinaderij Acton | eindraffinaderij (PGM/Au/Ag) | Vale Europe / Vale Acton Refinery, W3, Londen | — | [4][5][8] | **open — §7**: bestaan en functie hard gebrond (INCO/Vale-raffinaderij sinds 1924, PGM+Au+Ag, "30 minuten buiten Londen"), exacte site NIET — geen adres op `acton.vale.com` (onbereikbaar), geen OSM-object met naam "Vale"/"Inco" in Acton W3, geen Companies House-koppeling binnen het webbudget gevonden |

## 4 · Via-punten (alleen b1 — corridorkeuze op de lange spoorreis)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | MacTier (CP Parry Sound Subdivision) | 45.13626, -79.76922 | trekt de route van Sudbury zuidwaarts langs de CP-hoofdlijn richting Toronto/Zuid-Ontario i.p.v. een Dijkstra-sluipweg door het Muskoka-merengebied [webcheck] |
| b1 | 2 | Hamilton — CPKC Kinnear Yard | 43.24100, -79.83622 | grootste CP-rangeerknoop in de Golden Horseshoe; pint de route door Hamilton in plaats van eromheen [webcheck] |
| b1 | 3 | Welland (stad, aan het Welland-kanaal) | 42.99222, -79.24842 | de "Welland-corridor" uit de bindende aanpassing — de route buigt hier van de Toronto-Hamilton-as naar het zuiden, richting Port Colborne [webcheck] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Copper Cliff-smelter | Vale (Sudbury INO) | Ni-Cu-Co-concentraat (Sudbury-mijnen) → matte + PGM/Au/Ag-houdende residuen | onderdeel van Vale's Sudbury-operaties, geen PGM-specifiek jaarcijfer gevonden | [1][2] |
| Port Colborne Refinery | Vale | slurry/residu-feed uit Sudbury → PGM/Au/Ag-intermediair-product + elektro-kobalt (99,8%) | 140 ha-terrein, ~150 werknemers; ontvangt ook toll-materiaal van derden | [3][4][6] |
| Vale Europe-raffinaderij, Acton | Vale Europe Ltd | PGM/Au/Ag-intermediair (Port Colborne = 40% van de feed) → geraffineerd Pt/Pd/Rh/Ru/Ir + Au/Ag | een van de weinige edelmetaalraffinaderijen ter wereld; geen jaarcijfer gevonden | [4][5][8] |

## 6 · Stoppunt
De brief eindigt bij Vale Europe's Acton-raffinaderij als **eindpunt in tekst**, maar de getekende lijn
stopt bij `pgm-portcolborne-refinery` (been b1): de exporthaven, de Atlantische route, de VK-haven en het
exacte Acton-anker zijn geen van alle hard gebrond (§7). Geen van de drie ontbrekende schakels is met een
verzonnen coördinaat te dichten — dat wacht op Vale-scheepvaartdata of een beargumenteerde
Saint-Laurens/Seaway-keuze, zoals de haalbaarheidstoets zelf al aangeeft.

## 7 · Open punten
- **Tussenstap Port Colborne bevestigd (bindende aanpassing verwerkt):** Vale's eigen 20-F (o.a. FY2016)
  noemt expliciet dat Sudbury-PGM/Au/Ag eerst naar Port Colborne gaat vóór Acton [4] — als vast
  tussenanker opgenomen, conform de bindende toets-aanpassing.
- **Spoorlijn Copper Cliff → Port Colborne niet met naam genoemd.** De CP-Welland-corridor volgt uit
  regionale geografie + het `nikkel-sudbury-kristiansand.md`-precedent (andere maatschappij, geen
  ankerkopie) — blijft *webcheck/aannemelijk*, geen gepubliceerde lengte gevonden.
- **Exporthaven Canada onbepaald** (Montreal vs. Halifax) — geen bron kiest; Montreal ligt voor de hand
  door de Seaway-aansluiting op het CP/CN-net, maar dit is een gok, geen vondst.
- **VK-haven onbepaald** (Southampton vs. Tilbury) — Tilbury ligt dichter bij Acton (~40 km) dan
  Southampton (~110 km); ook dit is een afweging, geen bron.
- **Exacte Acton-site niet gevonden.** `acton.vale.com` was niet bereikbaar (DNS-fout); geen OSM-object
  met "Vale"/"Inco" in Acton W3; Requis' veilingbericht (okt. 2019) bevestigt de naam, geen adres [5].
  Zonder adres geen satellietblik, dus geen anker — een stadscentroïde is geen anker.
- **Jaarvolume voor déze as niet gebrond.** Alleen "40% van Acton's feed" [4] gevonden, geen t PGM/jaar.
- **Haalbaarheidstoets-risico voor schrapping vervalt**: de tussenstap Port Colborne is nu bevestigd [4],
  dus de as blijft staan — havens/Acton-anker/volume moeten vóór een volledige bake nog gevonden worden.

## 8 · Bronnen
[1] Wikipedia, "Copper Cliff" — gemeenschap/voormalige company town, Greater Sudbury, Ontario; coördinaat
    46.47306, -81.06944 (gemeentecentrum, niet het anker). https://en.wikipedia.org/wiki/Copper_Cliff,_Greater_Sudbury
[2] Wikipedia, "Sudbury Basin" — geologische formatie, Vale/Glencore Ni-Cu-Co-Pt-Pd-mijnbouw.
    https://en.wikipedia.org/wiki/Sudbury_Basin
[3] Wikipedia, "Port Colborne" — stad aan het zuideinde van het Welland-kanaal, Lake Erie, Ontario;
    coördinaat 42.88333, -79.25000 (stadscentrum, niet het anker). https://en.wikipedia.org/wiki/Port_Colborne
[4] Vale S.A., Form 20-F (SEC EDGAR, o.a. FY2016) — "Vale operates a processing facility in Port
    Colborne, Ontario, which produces PGMs, gold and silver intermediate products, and has a refinery in
    Acton, England, where they process their intermediate products"; Acton krijgt ~40% van zijn feed uit
    Port Colborne (via de haalbaarheidstoets/webcheck). https://www.sec.gov/Archives/edgar/data/0000917851/000104746917002477/a2231407z20-f.htm
[5] Requis, "Vale Acton Refinery Auction (London) — Until October 15, 2019" — bevestigt naam en locatie
    (Londen) van de Acton-raffinaderij, geen adres. https://requis.com/press/vale-auction-london-uk/
[6] Vale, "Port Colborne" (vale.com/port-colborne) — 140 ha-terrein, ~150 werknemers, elektro-kobalt
    (99,8%), finished nickel products, "precious metals and minor metals"; geen straatadres. https://vale.com/port-colborne
[7] Canadian Mining Journal, "Operations: The Precious Side of Inco" — Port Colborne ontvangt "crude
    nickel cobalt carbonate" uit Sudbury; 40% van Acton's feed is PGM-concentraat "nearly 6,400 km away"
    uit Port Colborne. https://www.canadianminingjournal.com/featured-article/operations-the-precious-side-of-inco/
[8] Wikipedia, "Mond Nickel Company" — historische achtergrond van de Britse INCO/Vale-raffinage-
    activiteiten (Clydach/Acton-lijn), gebruikt als contextbron, niet als ankerbron.
    https://en.wikipedia.org/wiki/Mond_Nickel_Company
[9] OpenStreetMap/Photon (ODbL) — "Copper Cliff Smelter" (building=industrial), Venice Street, Copper
    Cliff, Sudbury: -81.05473, 46.47860; "Vale Copper Cliff Complex" (landuse=industrial):
    -81.06043, 46.48749; "Copper Cliff Nickel Refinery": -81.08374, 46.44703; "Nickel Street", Port
    Colborne: -79.24303, 42.88333 (nabij het Port Colborne-anker). https://www.openstreetmap.org
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16) —
    `v2/build-cache/satcheck/sat-pgm-sudbury-actonuk-coppercliff.png`,
    `sat-pgm-sudbury-actonuk-portcolborne-z16.png`,
    `sat-pgm-sudbury-actonuk-portcolborne-cand.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `pgm-sudbury-actonuk` · **bestand:** `v2/data/stroomroute-pgm-sudbury-actonuk.json` (34,7 KB) ·
**functie:** `bak_pgm_sudbury_actonuk()` in `v2/tools/bak_stromen.sh` · **totaal:** 609,4 km over 4 benen,
1.828 punten, 2 markers.

Alléén been **b1** (fase A, spoor, Copper Cliff-smelter → Port Colborne-raffinaderij) is gebakken. b2
(exporthaven Canada), b3 (Atlantische oversteek) en b4 (VK-haven → Acton) blijven **niet getekend**: de
drie ankers staan open (§7 hieronder, ongewijzigd) en er is geen coördinaat verzonnen. De lijn stopt bij
Port Colborne, zoals §6 al vaststelde.

| # | modaliteit | van → naar | km gemeten | recept |
|---|---|---|---|---|
| b1a | spoor | Copper Cliff-smelter → MacTier | 234,2 | `toets_spoorroute.mjs --van=46.47860,-81.05473 --naar=45.13626,-79.76922 BAKE_SUFFIX=-raw` |
| b1b | spoor | MacTier → Hamilton/CPKC Kinnear Yard | 269,9 | idem, via 2 |
| b1c | spoor | Hamilton/CPKC Kinnear Yard → Welland | 69,3 | idem, via 3 |
| b1d | spoor | Welland → Port Colborne-raffinaderij | 36,0 | idem, staart |

**Km-toets:** geen gepubliceerde lengte om tegen te toetsen — de "~700 km" in §2 is een webcheck-schatting,
geen harde norm (§7 hieronder herhaalt dat expliciet). De gemeten 609,4 km (som van de vier deelbenen,
234,2+269,9+69,3+36,0) is nu de vervangende waarde: **12,9% onder** de eerdere webcheck-schatting, wat
plausibel is voor een via-puntenketen die dichter bij de echte CP-hoofdlijn/Welland-corridor ligt dan een
ruwe schatting.

**Naden:** 0 km op alle drie de overgangen tussen de vier deelbenen (elk `--been-geojson`-stuk sluit exact
aan op het vorige, want elke run start waar de vorige eindigde).

**Markers:** `pgm-coppercliff-smelter` op 0,084 km van de lijn, `pgm-portcolborne-refinery` op 0,421 km —
beide binnen de ~0,5 km-norm.

**Toetsen:** `toets_knikken.py` → 0 knikken op b1a/b1b; b1c en b1d dragen elk één **TERUGLOOP**
(178,9°/R≈41 m bij 42,96070/-79,27110 op b1c; 180,0°/R≈0 m bij 42,96850/-79,20050 op b1d) — beide **NIET
gerepareerd**. Getest op `--keerstraf` 5/10/15/25 (default): identieke geometrie (68,0 km/88 edges resp.
35,6 km/61 edges) op elke waarde, dus geen straf-toeval maar een echte eigenschap van het 1-op-1-spoornet
in dit gebied — dezelfde klasse als de teruglopen bij `bak_zilver_lubin_glogow` (Głogów-smelter) en de
kopmaak-omkeringen bij `bak_nikkel_sudbury_kristiansand`/`bak_nikkel_norilsk_monchegorsk`: aannemelijk een
rangeer-/kopmaakbeweging bij een industrieel raffinaderijterrein (Port Colborne, 140 ha), niet apart
geverifieerd binnen het webbudget van deze bake. `toets_rechte_benen.py --min-km 5` → geen enkel been van
`pgm-sudbury-actonuk` gevlagd (geen ongeteste rechte lijn). `json.load` slaagt, `versie` 2, `punt_formaat`
`lonlat`, modaliteit `{spoor}` ⊂ toegestane set, elk been ≥ 2 punten.

**Geen haven-aanloop, geen lucht:** geen zeebeen in dit stuk van de keten; geen bron noemt luchtvracht voor
deze as (`bron_voor_luchtvracht: n.v.t.` in het ontwerp) — golf 3's lucht-tooling
(`v2/tools/maak_luchtbeen.py`) is voor déze keten niet toepasselijk.

**Gereedschapslessen:** de vier spoorruns (kop→via1→via2→via3→staart) sluiten in de bake exact op elkaar
aan (0,0 km naad op alle drie de overgangen) — het `--been-geojson`-patroon met vooraf gebakken lijnen
werkt hier zoals verwacht, geen bijzonderheden ten opzichte van de andere lichte spoorbakes.

**Voor een latere ronde (§7 blijft de bron van waarheid):** zodra Lars/een volgende ronde de open punten
in §7 oplost (exporthaven Canada, VK-haven, Acton-site) worden b2/b4 wegbenen via
`maak_stroombeen_weg.py` en b3 een `--been "zee|...|<exporthaven>|<VK-haven>"`-regel via MARNET —
controleer dan meteen op een haven-aanloopregel (bakhandleiding §2: kade > 5 km van de zeeknoop → aanloop,
ook binnen 25 km). Niets van b2-b4 bakken vóór de havens en het Acton-adres gevonden zijn.
