# Routebrief (licht) · Kolen · Quintette-mijn (Conuma) → CN via Prince George → Trigon Pacific Terminals, Prince Rupert (Canada)

**stroom-id:** `kolen-conuma-princerupert` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) ·
**status:** gebakken
**Keten in één zin:** cokeskool (steelmaking coal) van Conuma's Quintette-mijn bij Tumbler Ridge (NE-BC) gaat per trein
over de ex-BC Rail Tumbler Ridge-lijn naar Prince George en dan over de CN-hoofdlijn langs Smithers en Terrace naar
Trigon Pacific Terminals (voorheen Ridley Terminals) op Ridley Island, Prince Rupert. Andere mijn, spoorlijn en kade
dan `kolen-elkview-neptune`. De lijn stopt bij de kade: geen bron legt lading op een bestemming.
**Welke as van het verhaal:** de noordelijke Canadese cokeskoolcorridor naar Azie, naast de zuidelijke (Neptune/Roberts Bank).
Quintette: capaciteit 2,1 Mt kolen/jaar, productie 2024 slechts 0,2 Mt (herstart sept. 2024) [3]. Trigon: capaciteit
18,5 Mt/jaar [4]; kolen via Trigon 2024 -23 % [6]. Aannemelijk: een bron (Globe and Mail) noemt Conuma's mijnen als
vooral herkomst van Trigon-cokeskool, niet Quintette-specifiek [5].

## 1 · Ketenkaart
```
Quintette-laadstation, Tumbler Ridge BC  `kolen-conuma-quintette-laad`
  ──(b1 spoor · last mile, stippel · 3,3 km · OSM-spoor eindigt hier voor het laadstation)──►
spooraansluiting 55.0281, -120.9711
  ──(b2 spoor · Tumbler Ridge-lijn -> Prince George -> CN Prince Rupert-lijn · 988,5 km geroute, aannemelijk: een bron)──►
Trigon Pacific Terminals, Ridley Island, Prince Rupert  `kolen-trigon-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-conuma-quintette-laad` → spooraansluiting 55.0281,-120.9711 | eigen laadspoor Quintette, geen net op deze korrel | ~3,3 [haalbaarheidstoets, hemelsbreed] | stippel | ja: last mile (geen net op deze korrel) |
| b2 | A | spoor | spooraansluiting → `kolen-trigon-kade` | Tumbler Ridge-lijn (ex BC Rail) -> Prince George -> CN: Vanderhoof, Burns Lake, Smithers, Hazelton, Kitwanga, Terrace -> Ridley Island [8][9] | hemelsbreed 607 km, geen spoorkm gepubliceerd; geroute 988,5 km (indicatie, verhouding 1,6: de lijn volgt twee gebergtecorridors) | maak_spoorbeen_raw (extract canada) | nee |

Geen zeebeen, dus geen haven-aanloop: de kade is het eindpunt van het spoor, dat 24 m van het Trigon-anker eindigt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-conuma-quintette-laad` | mijn / laadstation | Quintette-laadstation (kolenwasserij + laadlus), Conuma Resources, Tumbler Ridge | 54.9992, -120.9853 | [1][3] + haalbaarheidstoets | bron-gelegd (z15 gezien: kolenwasserij met opslagtorens en transportbanden, laadlus ten noorden ervan met een rechte spoorlijn die naar het noorden vertrekt; eigen beeld `v2/build-cache/satcheck/sat-kolen-conuma-princerupert-quintette.png`) |
| `kolen-trigon-kade` | overslag spoor -> zeeschip | Trigon Pacific Terminals, Ridley Island, Prince Rupert | 54.2283, -130.3307 | [4][5] + haalbaarheidstoets | bron-gelegd (z15 gezien: groot kolenterrein met stapels en spoorlussen direct oostelijk, laadbrug en pier met een schip aan de westkust; het punt ligt op de toegangsweg tussen terrein en kust, ~0,4 km van de kade-ligplaats; beeld `v2/build-cache/satcheck/sat-kolen-conuma-princerupert-trigon.png`) |
| (marker) `kolen-conuma-spooraansluiting` | last-mile-uiteinde | eerste OSM-spoor | 55.0281, -120.9711 | tool (maak_spoorbeen_raw, snap 3 m) | aannemelijk (geen aparte satellietblik; ligt 3,3 km noord van de laadlus op de lijn die het beeld noordwaarts toont) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen. Tussen Tumbler Ridge en Ridley Island bestaat geen alternatieve spoorcorridor; de kale Dijkstra over de ruwe OSM-ways
loopt zelf door Prince George (0,7 km ernaast), Vanderhoof, Burns Lake, Smithers, Hazelton, Kitwanga en Terrace (0,3-0,6 km)
zonder omkeringen (0 bij 150 graden). Conform de bindende haalbaarheidstoets: geen via nodig.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in -> uit | capaciteit | bron |
|---|---|---|---|---|
| Quintette-kolenwasserij | Conuma Resources (van Teck, feb. 2023, 120 mln USD; herstart sept. 2024) | ruwe kool -> gewassen cokeskool | 2,1 Mt/jaar; 0,2 Mt productie 2024 | [1][2][3] |
| Trigon Pacific Terminals | Riverstone/AMCI 90 %, Lax Kw'alaams + Metlakatla 10 % | cokeskool/thermisch (trein) -> bulkschip | 18,5 Mt/jaar; 9,1 Mt totale bulk 2024 | [4][6][7] |

## 6 · Stoppunt
Bij de Trigon-kade: Trigon verscheept cokeskool en thermische kool naar Azie zonder een per lading gedocumenteerde haven of
afnemer, en geen bron legt Quintette-kool op een bestemming; een zeebeen zou een gok zijn.

## 7 · Open punten
- **Quintette-specifiek:** de bron voor Conuma -> Trigon is een krantenartikel (Dec. 2023, vooral Conuma-mijnen) [5], geen Quintette-lading; Wolverine is dicht, Brule en Willow Creek zijn stil/onzeker, Quintette is de enige verifieerbare laadplek.
- **Last mile 3,3 km:** de OSM-spoorlijn eindigt 3,3 km voor het laadstation; het getekende stuk is een stippel (hemelsbreed). `toets_spoorroute` snapt het uiteinde 13,7 km ernaast (bladsnoei): gebruik daarom `maak_spoorbeen_raw`.
- **Spoorkm:** geen gepubliceerde spoorlengte Quintette -> Prince Rupert; 988,5 km is een routerindicatie. Wikipedia noemt wel 132 km voor de hele Tumbler Ridge Subdivision [8], maar niet het aansluitpunt op de hoofdlijn.
- **Rails ontbreken deels:** de lijn Teck-Quintette is na 2000 deels opgebroken en de rest tot Wakely stond stil (sporen bleven liggen) [8]; OSM toont het bestaande spoor, niet de huidige bedrijfsstatus.
- **Coordinaat Quintette-mijn:** GEM 54.9954, -120.9921 [3] (hier niet gebruikt; anker = laadstation, 0,5 km ernaast). Wikipedia-lijst van mijnen noemt een afwijkende lengtegraad voor Quintette; niet nagegaan.
- **Trigon-anker:** ligt ~0,4 km van de pier; geen zeebeen, dus geen gevolg voor de naden.
- **Trigon-kolenvolume 2024:** alleen het percentage (-23 %, cokeskool -29 %) [6], geen absoluut kolencijfer gevonden.

## 8 · Bronnen
[1] Conuma Resources, "Quintette Ships its First Coal", eerste trein 18-9-2024. https://conumaresources.com/quintette-ships-its-first-coal/
[2] Wikipedia, "Tumbler Ridge" (Quintette geopend 1982, gesloten 2000, Conuma sinds 2023; 5 Conuma-mijnen, ~5 Mt/jaar). https://en.wikipedia.org/wiki/Tumbler_Ridge
[3] Global Energy Monitor, "Quintette Coal Mine" (54.9954, -120.9921; 2,1 Mtpa; 0,2 Mt in 2024). https://www.gem.wiki/Quintette_Coal_Mine
[4] Global Energy Monitor, "Trigon Pacific Coal Terminal" (18,5 Mtpa; Riverstone/AMCI 90 %). https://www.gem.wiki/Trigon_Pacific_Coal_Terminal
[5] The Globe and Mail, "BC coal terminal sues federal agency in attempt to diversify exports", dec. 2023 (cokeskool vooral uit Conuma-mijnen). https://theglobeandmail.com/business/article-bc-coal-terminal-sues-federal-agency-in-attempt-to-diversify-exports/
[6] Railway Age, "PRPA achieves cargo milestone in 2024" (Trigon-kolen -23 %). https://www.railwayage.com/intermodal/prpa-achieves-cargo-milestone-in-2024-during-expansion-phase/
[7] Port Technology, "Port of Prince Rupert moves 23 million tonnes in 2024" (Trigon 9,1 Mt bulk). https://www.porttechnology.org/news/port-of-prince-rupert-moved-23-million-tonnes-of-cargo-in-2024
[8] Wikipedia, "BC Rail" (Tumbler Ridge Subdivision 132 km; kolentreinen naar Prince George, CN naar Prince Rupert). https://en.wikipedia.org/wiki/BC_Rail
[9] Wikipedia, "Prince Rupert, British Columbia" (kolen op de Prince Rupert-hoofdlijn). https://en.wikipedia.org/wiki/Prince_Rupert,_British_Columbia
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-kolen-conuma-princerupert-quintette.png`, `...-trigon.png`; routebeen `v2/build-cache/ais/graaf/spoorroute-kolen-conuma-princerupert-quintette-trigon-raw.geojson` (maak_spoorbeen_raw, extract canada, 988,5 km, 9.394 punten, snap 3 m / 24 m).
[11] Rupertport.com (Trigon) was onbereikbaar tijdens het onderzoek; niet gebruikt. Sitelaag `kolen-sitelaag.json` heeft geen Quintette- of Trigon-entry.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Bestand:** `v2/data/stroomroute-kolen-conuma-princerupert.json`, 200,9 KB, versie 2, lonlat, 2 benen, 3 markers. **Titel:** Kolen · Quintette (Conuma, Tumbler Ridge) → Trigon Prince Rupert (Canada).

| # | modaliteit | been | km gemeten | km brief | afwijking | naad |
|---|---|---|---|---|---|---|
| 1 | spoor (stippel) | last mile Quintette-laadstation (geen net op deze korrel) | 3,3 (2 punten) | ~3,3 hemelsbreed | 0% | n.v.t. |
| 2 | spoor | trein Quintette naar Trigon Prince Rupert (Tumbler Ridge-lijn, Prince George, CN; aannemelijk: een bron) | 988,5 (9394 punten) | geen spoorkm gepubliceerd; hemelsbreed 607 | indicatie, verhouding 1,63 | 0,004 km |

**Markers (3):** Quintette-laadstation (54.9992, -120.9853) 0,0 km van de lijn; spooraansluiting (55.0281, -120.9711) 0,0 km; Trigon-kade (54.2283, -130.3307) 0,024 km van het lijneinde. Geen haven-aanloop, geen vlucht, geen leiding, geen letterlijke kopie, geen via-punten.

**Recept:** (1) `python v2/tools/maak_spoorbeen_raw.py --extract canada --van 55.0281,-120.9711 --naar 54.2283,-130.3307` gaf `spoorroute-kolen-conuma-princerupert-quintette-trigon-raw.geojson` (988,5 km, snap 3 m en 24 m, 0 omkeringen); (2) functie `bak_kolen_conuma_princerupert()` in `v2/tools/bak_stromen.sh` met een `--stippel "spoor|last mile ..."`, een `--been-geojson "spoor|..."` en drie `--marker`; (3) `bash v2/tools/bak_stromen.sh kolen-conuma-princerupert`.

**Toelichting stippel:** been 1 is de enige stippel (3,3 km): de OSM-spoorlijn eindigt voor het laadstation, er is geen net op deze korrel. Het is een rechte lijn tussen laadstation en eerste OSM-spoor, dus geen gemeten spoor. Geen zeebeen: geen bron legt Quintette-kool op een haven of afnemer; de keten stopt bij de kade.

**Toelichting km:** er is geen gepubliceerde spoorlengte; 988,5 km is een routerindicatie via twee gebergtecorridors (Tumbler Ridge-lijn naar Prince George, CN naar Prince Rupert). De ±15%-toets geldt dus niet als norm. OSM toont het spoor, niet de bedrijfsstatus van de deels stilgelegde lijn.

**Toets:** `toets_knikken.py` 0 knikken en 0 omkeringen; `toets_rechte_benen.py --min-km 5` meldt de stroom niet; naad 0,004 km (max); json.load, versie 2, lonlat, modaliteit spoor, elk been >= 2 punten, bestand 200,9 KB (onder 300 KB).

**Lessen:** `toets_spoorroute` is hier niet bruikbaar (uiteinde 13,7 km ernaast door bladsnoei); `maak_spoorbeen_raw.py` over de ruwe OSM-ways levert wel een aaneengesloten lijn zonder omkeringen. Het tussenbestand staat in build-cache (gitignored): bij herbak eerst het raw-tool opnieuw draaien.
