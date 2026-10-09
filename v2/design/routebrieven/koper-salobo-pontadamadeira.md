# Routebrief (licht) · Koper · Salobo → Parauapebas → Ponta da Madeira (Brazilië)

**stroom-id:** `koper-salobo-pontadamadeira` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** koperconcentraat (36–40% Cu) van de Salobo-mijn en -concentrator (Vale Base Metals, Marabá, Pará) per **truck** over de OSM-weg VS-12 naar Vale's spoorterminal in Parauapebas en per **spoor** (Estrada de Ferro Carajás, EF-315) naar Vale's exportterminal **Terminal Marítimo da Ponta da Madeira** in São Luís (Maranhão) — daar stopt de brief.
**Welke as van het verhaal:** Brazilië als reserve-as: de grootste kopermijn van Brazilië via dezelfde Carajás-spoorlijn die het ijzererts draagt. Salobo produceerde in 2024 een record van ~200 kt Cu (in concentraat), ruim de helft van Vale's 348 kt koper [1][2].

## 1 · Ketenkaart
```
Salobo-concentrator `cu-salobo-laad` ──(b1 truck · VS-12 · hemelsbreed 74 km, OSM-pad ~100 km, geen wegkm)──►
  Parauapebas-station `cu-parauapebas-efc` ──(b2 spoor · EFC/EF-315 · gepubliceerd ~892 km, gemeten 872 km ·
  gedeeld been met nikkel-oncapuma-saoluis)──► Ponta da Madeira, EFC-einde `cu-pontadamadeira-efc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-salobo-laad` → `cu-parauapebas-efc` | OSM-weg ref VS-12 (OSRM: 92,7 van 102,4 km); wegnaam in bronnen niet genoemd, deels Vale-weg niet uit te sluiten [1][3][5] | hemelsbreed 74 km, OSM-pad 100 km (toets 99,8; OSRM 102,4), geen wegkm gepubliceerd — ±15%-toets = indicatie | maak_stroombeen_weg (nieuw profiel `koper-salobo-parauapebas`, extract brazilie) | nee |
| b2 | B | spoor | `cu-parauapebas-efc` → `cu-pontadamadeira-efc` | Estrada de Ferro Carajás (EF-315): Parauapebas–Marabá–Açailândia–Santa Inês–São Luís [1][3][6] | gepubliceerd ~892 [6]; gemeten 872,0 km (−2,2%) | LETTERLIJKE KOPIE punten[0:1288] van b2 uit `stroomroute-nikkel-oncapuma-saoluis.json` | nee |

Geen zeebeen, geen haven-aanloop, geen last-mile-stippel: de keten stopt aan Vale's terrein (zie §6). Het nikkelbeen loopt 12 punten (2 km) door naar Itaqui; de kopie wordt bij Ponta da Madeira afgekapt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-salobo-laad` | mijn + concentrator | Salobo (Vale Base Metals), Marabá | -5.7852, -50.5263 | [1][3][4] | bron-gelegd (z15 gezien: lange witte verwerkingsgebouwen aan de noordoostrand van de grote open put, aan het stuwmeer met tailings; tweede complex ~1,5 km ZO) |
| `cu-parauapebas-efc` | overslag weg → spoor | Parauapebas-station / Vale-spoorterminal (EFC) | -5.9942, -49.8949 | letterlijk uit `nikkel-oncapuma-saoluis` (`ni-parauapebas-efc`); [3] | aannemelijk (z15 opnieuw gezien: EFC met spoorknoop bij de rivieroversteek aan de rand van de stad, Vale-installatie 0,6 km ZW; exacte containerhal niet gepubliceerd) |
| `cu-pontadamadeira-efc` | stoppunt (haven) | Ponta da Madeira, EFC-einde / ertsterminalemplacement, São Luís | -2.5646, -44.3614 | [1][3]; laatste punt van de gekopieerde b2 | aannemelijk (z15 gezien: spoorlussen, erts-stapelhal met reclaimers en transportband naar de piers; kade voor koperconcentraat niet aangewezen) |

Niet gebruikt: pier -2.5511,-44.3787 (kop van een ijzerertspier) en Itaqui-kade -2.5768,-44.3667 (openbare haven).

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Eén doorgaande weg, geen alternatief (OSRM `alternatives=true`: 1 route); via-punten dienen alleen om de scan op VS-12 te houden en niet via een zijtak of door Parauapebas-stad te laten lopen. Punten = OSRM-vertices op VS-12 (voorspelling, geen bron), bake-agent laat de OSM-scan zelf kiezen.
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | VS-12 km ~20 | -5.9119, -50.4399 | houdt de weg zuidoostwaarts langs de put weg van zijpaden |
| b1 | 2 | VS-12 km ~40 | -5.9329, -50.3125 | midden van het smalle venster |
| b1 | 3 | VS-12 km ~60 | -5.9412, -50.1480 | |
| b1 | 4 | VS-12 km ~80 | -5.9713, -50.0013 | |
| b1 | 5 | VS-12 km ~90 | -5.9974, -49.9441 | zuidwestelijke aanloop Parauapebas, vóór de stad en de rotonde (-5.998, -49.898) |
Venster ≥ 75 km (OSM-pad 100 km), `corridorKlassen` [tertiary, unclassified]; eindKlassen default (service/residential nodig aan de uiteinden; zonder die klassen geen doorlopend pad, toets). Extract `brazilie` (reus; max 2 scans tegelijk).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Salobo-concentrator (Salobo I–III) | Vale Base Metals | Cu-erts → concentraat 36–40% Cu | verwerking 36 Mt erts/j (Salobo III erbij); ~200 kt Cu in concentraat 2024 | [1][2][4] |

## 6 · Stoppunt
Bij het EFC-einde in Vale's Ponta da Madeira-terminal: Vale en Wheaton noemen alleen "klanten wereldwijd" zonder afnemer, smelter of kade voor concentraat [1][3] — dus geen fase C.

## 7 · Open punten
- Wegverbinding Salobo–Parauapebas: geen naam of wegkm gebrond; VS-12 is de OSM-ref, mogelijk deels privé-Vale-weg.
- Kade voor koperconcentraat in Ponta da Madeira niet gevonden; lijn eindigt aan het ertsemplacement.
- Salobo-aandeel via Ponta da Madeira is niet gekwantificeerd (Vale noemt dit als route; Barcarena niet gezien voor Salobo).
- Salobo staat niet in `koper-sitelaag.json` (centraal toevoegen: -5.7852, -50.5263, ~200 kt Cu/j 2024 [2]).
- ~90% van de km is gedeeld met `nikkel-oncapuma-saoluis` b2 (kopie, geen tweede versie).
- Exacte overslagplek Parauapebas niet gepubliceerd (aannemelijk).

## 8 · Bronnen
[1] Vale Base Metals, Salobo — "transported to Parauapebas … Carajás Railway … Ponta da Madeira", concentraat 36–40% Cu, 36 Mt/j — https://valebasemetals.com/our-operations/salobo/
[2] Industrial Info, "Vale surpasses iron ore production guidance for 2024" — Salobo record 200 kt Cu; Vale koper 348 kt — https://www.industrialinfo.com/news/article/vale-surpasses-iron-ore-production-guidance-for-2024--338453
[3] Wheaton Precious Metals, Salobo — "by road … to Vale's existing rail terminal in Parauapebas", dan Carajás-spoor naar Ponta da Madeira — https://www.wheatonpm.com/portfolio/operating-mines/salobo/default.aspx
[4] Mongabay 2025-10, "Copper rush pushes Vale to ramp up mining near Amazonian protected areas" (Vale-koper 348 kt, Salobo-gedreven) — https://news.mongabay.com/2025/10/copper-rush-pushes-vale-to-ramp-up-mining-near-amazonian-protected-areas/
[5] OSRM (router.project-osrm.org, driving), 2026-10-09 — Salobo → Parauapebas 102,4 km, 92,7 km op VS-12, één route; haalbaarheidstoets: OSM-pad 99,8 km (secondary 47,9 · tertiary 34,8 · unclassified 9,3 · service 5,7 · residential 2,1)
[6] `v2/design/routebrieven/nikkel-oncapuma-saoluis.md` (EFC-been 874 km, Parauapebas-anker) en haalbaarheidstoets 2026-10-09 (router Parauapebas → -2.5655,-44.3590: 872,0 km, −2,2% t.o.v. ~892; Wikipedia Vale S.A./Carajás Railway)
[7] Satellietblik Esri z15, `v2/build-cache/satcheck/`: `sat-koper-salobo-pontadamadeira-salobo.png` · `-parauapebas.png` · `-pontamadeira.png`

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
Bestand `v2/data/stroomroute-koper-salobo-pontadamadeira.json` (versie 2, lonlat, 58,6 KB) · functie `bak_koper_salobo_pontadamadeira` in `bak_stromen.sh` · profiel `koper-salobo-pontadamadeira-salobo-parauapebas` in `maak_stroombeen_weg.py`.

| # | modaliteit | km gemeten | punten | brief | naad naar volgend been |
|---|---|---|---|---|---|
| b1 | truck | 96,0 | 1.667 | OSM-pad 100 (toets 99,8; OSRM 102,4); hemelsbreed 73,6, omwegfactor 1,30 | 0,00 km |
| b2 | spoor | 872,1 | 1.288 | ~892 gepubliceerd, 872,0 gemeten (nikkel b2) | — |
| | | **968,1** | 2.955 | | |

**Markers (3):** `cu-salobo-laad` -5.7852,-50.5263 · `cu-parauapebas-efc` -5.9942,-49.8949 · `cu-pontadamadeira-efc` -2.5646,-44.3614 — alle op 0,000 km van de lijn (punt-tot-punt). Naad b1 → b2 0,02 km (de spoorsnap -5.9941,-49.8951 tegen het wegeinde), geen naad > 5 km.

**Recept.**
- b1: `wegscan_puur.py --profiel koper-salobo-pontadamadeira-salobo-parauapebas` (extract brazilie, 451 s, weg-slot + reus-slot), refs VS-12, `corridorKlassen` tertiary+unclassified, `vensterKm` 75, de 5 via-punten uit §4. Alle via-snaps ≤ 0,09 km, segmenten 20,2 · 19,9 · 20,0 · 19,9 · 10,0 · 5,8 km (geen omweg). Het eerste stuk loopt over service/tertiary (35,8 km kleine klassen aan de Salobo-kant, 0,5 km aan de stadskant); anker-stubs 0,09 en 0,05 km.
- b2: LETTERLIJKE KOPIE punten[0:1288] van b2 uit `stroomroute-nikkel-oncapuma-saoluis.json` (`spoorroute-koper-salobo-pontadamadeira-parauapebas-pontamadeira.geojson`, 872,0 km, 229 edges, laatste punt -2.5646,-44.3614); in het bestand byte-gelijk aan die punten (gecontroleerd). Geen eigen spoorrouter-run, dus geen tweede versie van dezelfde corridor.

**Toelichting.**
- Geen stippel, geen haven-aanloop, geen zeebeen, geen vlucht, geen leiding: de keten stopt aan Vale-terrein (§6); pier -2.5511,-44.3787 en Itaqui-kade niet gebruikt.
- b1 is de ±15%-toets ALLEEN als indicatie (geen gepubliceerde wegkm): 96,0 tegen 100 (OSM-pad) is -4,0%, tegen OSRM 102,4 -6,3%. Dat het pad 30% om de grootcirkel gaat past bij één doorgaande weg zonder alternatief.
- `toets_knikken.py`: spoor 0 knikken; truck 6 knikken ≥ 60° (115, 107, 98, 90, 79, 65 graden), allemaal op 3–55 m boogstraal binnen ~300 m van de Salobo-concentrator of de Parauapebas-stubs (spikes in de terreinwegen, geen omkering ≥ 150°, geen terugloop). Niet gerepareerd: dat zijn de service-wegen op het Vale-terrein en dat is geen corridorkeuze.
- `toets_rechte_benen.py --min-km 5`: geen recht been in deze stroom.
- Niets in dit bestand is "aannemelijk" door de lijnstijl; wel in de beennamen en markernamen (Parauapebas en Ponta da Madeira zijn aannemelijk, één bron).

**Lessen.**
- `wegscan_puur.py` op de brazilie-reus kost ~7,5 min voor een venster van 75 km en is daarna gecachet (`koper-salobo-pontadamadeira-pbfways-*.json`); de eerste 40 s zijn nodes, de rest ways.
- Een gedeeld been kopiëren is hier de hele spoorbake: één bestand, één functieregel, geen zwaar-slot voor de router (alleen voor `hecht_marnet.py`, 20 s).
- Salobo ontbreekt nog in `koper-sitelaag.json` (centraal toevoegen, §7); het register moet de nieuwe stroom nog krijgen.
