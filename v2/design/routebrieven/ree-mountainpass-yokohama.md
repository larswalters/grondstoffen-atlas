# Routebrief (licht) · zeldzame aardmetalen — Mountain Pass → Long Beach → Yokohama (Japan, aannemelijk)

**stroom-id:** `ree-mountainpass-yokohama` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** NdPr-oxide van MP Materials' Mountain Pass gaat per truck (aannemelijk: modaliteit niet gepubliceerd) over I-15, Cajon Pass en I-10/I-710 naar de containerkade van Long Beach en per containerschip over de noordelijke Stille Oceaan naar Japan — aannemelijk: Honmoku Futo, Yokohama (de 10-K noemt Japan, geen Japanse haven).
**Welke as van het verhaal:** de Amerikaanse NdPr-oxide die de gestopte China-lus vervangt (alle verkoop aan China gestaakt juli 2025). MP produceerde in 2025 2,6 kt NdPr-oxide (1,99 kt verkocht) uit 50,7 kt REO in concentraat; Japan loopt via Sumitomo, exclusief distributeur t/m 2030 — het Japanse aandeel is niet gepubliceerd [1][2].

**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** beennaam en titel noemen "aannemelijk: Yokohama"; truck via het profiel us-california met één corridorpunt (Cajon Pass), km in de brief = hemelsbreed 311, geen wegkm; Long Beach-aanloop is de omgekeerde kopie van `ree-yunsheng-longbeach`; Honmoku-aanloop is de kopie van `ree-kuantan-japan`. Stoppunt Honmoku (bij bezwaar tegen de aanname: eindig bij Long Beach).

## 1 · Ketenkaart
```
Mountain Pass `ree-mp-laad` ──(b1 truck · I-15 → Cajon Pass → I-215/I-10 → I-710 · hemelsbreed 311 km, geen wegkm)──►
Long Beach containerkade `ree-longbeach-kade` ──(b2 haven-aanloop, stippel · 8,5 km)──► zeeknoop 4488
──(b3 zee · MARNET · ~9.112 km)──► zeeknoop 9065 ──(b4 haven-aanloop, stippel · 7,8 km)──►
Honmoku Futo, Yokohama `ree-honmoku-kade` ⏹ stoppunt (aannemelijk)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (aannemelijk: niet gepubliceerd) | `ree-mp-laad` → `ree-longbeach-kade` | I-15 (Barstow) → Cajon Pass → I-215/I-10 → I-710 | hemelsbreed 311 km, geen wegkm; 10-K: "four-hour drive" [1]; scan 372,1 km (indicatie, niet norm) | maak_stroombeen_weg, profiel `ree-mountainpass-yokohama-mountainpass-longbeach` (gescand, us-california) | nee |
| b2 | B | zee (haven-aanloop) | `ree-longbeach-kade` → zeeknoop 4488 (33.7039, -118.1945) | Long Beach-havenbekken | 8,5 (letterlijk omgekeerde kopie `ree-yunsheng-longbeach`, handgelegd) | `--stippel-geojson` `ree-mountainpass-yokohama-aanloop-longbeach-uit.geojson` | ja: kade 6,47 km van de knoop (> 5 km, LAR-586) |
| b3 | B | zee (aannemelijk: Yokohama niet gebronnen) | zeeknoop 4488 → zeeknoop 9065 (35.3661, 139.6857) | noordelijke Stille Oceaan | getest 9.111,6 (router); grootcirkel kade-kade 8.854 | MARNET | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop 9065 → `ree-honmoku-kade` | Tokiobaai/Honmoku | 7,8 (kopie `--stippel` in `bak_ree_kuantan_japan`) | stippel (1:10M-kust kent de haven niet; geen tweede pad-poging) | ja: kade 7,8 km van de knoop (> 5 km) |

Beennaam b3: "… (aannemelijk: Japan via Sumitomo, haven Yokohama niet gebronnen)". Geen luchtbeen: de 10-K noemt alleen ocean freight [1].

## 3 · Ankers (één per site en per overslag; alle drie hergebruikt)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-mp-laad` | mijn + scheiding (kop b1) | Mountain Pass, MP Materials, San Bernardino County, CA | 35.4786, -115.5325 | [3] + `ree-mountainpass-fortworth.md` §3, sitelaag `w-mountainpass` | bron-gelegd (eigen z15 gezien: kruis op de open pit, indikkers/tailingsbekkens W en verwerkingsgebouwen O) |
| `ree-longbeach-kade` | overslag truck → zee | containerkade Long Beach, westkade oostelijk havenbekken (terminal niet bevestigd) | 33.7600, -118.2132 | [4] + `ree-yunsheng-longbeach.md` §3 | aannemelijk (eigen z15 gezien: portaalkranen langs de kade, containerstapels, spoorbundel ernaast) |
| `ree-honmoku-kade` | losplek zee (voorgestelde invoerhaven) | Honmoku Futo-containerterminal, Yokohama | 35.4356, 139.6727 | [5] + `ree-kuantan-japan.md` §3 | bron-gelegd als terminal (eigen z15 gezien: opgespoten pier met kranen en containerstapels); haven zelf aanname |

## 4 · Via-punten (alleen b1: de enige corridorkeuze is de pas)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Cajon Pass, op I-15 | 34.3114, -117.4747 | pint de I-15-doorgang door de San Gabriel/San Bernardino-bergen i.p.v. een omweg; daarna vindt de router I-215/I-10/I-710 vanzelf (scan 133,0 km pas → kade, 239,6 km anker → pas) |
Wegen gescand: I-15, I-215, I-10, I-710 (extract us-california, venster 50 km). Het anker snapt op 1,00 km van de weg (bevinding, zelfde als `ree-mountainpass-fortworth`; mijnwegen dun gekarteerd), kade 0,27 km; doorgetrokken, niet gestippeld.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mountain Pass | MP Materials | REO-concentraat → NdPr-oxide (eigen scheiding) | 2,6 kt NdPr-oxide geproduceerd, 1,99 kt verkocht (2025); site 50,7 kt REO/j | [1] |
| Japanse afnemers (niet getekend) | Sumitomo Corporation of Americas als distributeur | NdPr-oxide/-metaal → Japanse klanten | aandeel niet gepubliceerd | [1] |

## 6 · Stoppunt
Op de kade van Honmoku: de 10-K noemt Japan en Sumitomo als distributeur maar geen Japanse haven of magneetfabriek, dus fase D/E vervalt en de haven is een aanname die in de beennaam staat.

## 7 · Open punten
- **Yokohama niet gebronnen:** geen bron noemt een Japanse haven of afnemer met naam en adres; Honmoku is hergebruikt uit `ree-kuantan-japan` (zelfde aanname). Bij bezwaar: eindig bij Long Beach.
- **Wegkm b1 onbekend** (hemelsbreed 311 km); de 372 km scan is OSM-afgeleid, geen publicatie. Truck is aannemelijk (10-K noemt "four-hour drive" naar de havens en I-15, geen modaliteit).
- **Long Beach of Los Angeles:** de 10-K noemt beide als primaire havens; Long Beach is de keuze van het id. Terminal en rederij niet bekend.
- **Japans aandeel in het MP-volume** niet gepubliceerd (1,99 kt verkocht is totaal); ook Zuid-Korea en "broader Asia" worden genoemd [1].
- Aanloop b2 en b4 zijn schematisch (b2 handgelegd door de oostelijke golfbrekergap, b4 een rechte lijn) en de zeeknopen liggen in open water.
- Datum van stopzetting China-verkoop (juli 2025) uit de 10-K; de eerdere Reuters-datum 2025-04-17 (concentraatzendingen) is een ander feit [6].

## 8 · Bronnen
[1] MP Materials Corp., Form 10-K FY2025 (SEC): ceased all sales to China juli 2025; Sumitomo Corporation of Americas exclusief distributeur NdPr-oxide/-metaal naar Japanse klanten t/m 2030; NdPr via ocean freight; LA en Long Beach primaire havens; Mountain Pass langs I-15, vier uur rijden van de havens; 2025: 50.692 t REO, 2.599 t NdPr-oxide geproduceerd, 1.994 t verkocht. https://www.sec.gov/Archives/edgar/data/1801368/000180136826000008/mp-20251231.htm
[2] MP Materials Corp., Form 10-K FY2024 (SEC): NdPr-oxide "primarily to customers in Japan, South Korea and broader Asia". https://www.sec.gov/Archives/edgar/data/1801368/000180136825000009/mp-20241231.htm
[3] Wikipedia, "Mountain Pass Rare Earth Mine": 35.4786, -115.5325. https://en.wikipedia.org/wiki/Mountain_Pass_Rare_Earth_Mine
[4] Wikipedia, "Port of Long Beach" (Pier J; havencoördinaat lag in het water, anker uit `ree-yunsheng-longbeach.md`). https://en.wikipedia.org/wiki/Port_of_Long_Beach
[5] OpenStreetMap via Nominatim, "本牧ふ頭" (Honmoku Futo), Yokohama, via `ree-kuantan-japan.md` §8 [6]. https://www.openstreetmap.org
[6] Reuters via TradingView, 2025-04-17: MP stopt China-bound concentraatzendingen (via `ree-mountainpass-fortworth.md` §8 [3], niet opnieuw gelezen). https://www.tradingview.com/news/reuters.com,2025:newsml_L4N3QV1OL:0-mp-materials-stops-china-bound-rare-earth-shipments-over-tariffs/
[7] Esri World Imagery via `sat_check.py`, z15: `v2/build-cache/satcheck/sat-ree-mountainpass-yokohama-{mp,lb,honmoku}.png`.
[8] `v2/design/ree-sitelaag.json`, site `w-mountainpass`; `v2/design/routebrieven/ree-mountainpass-fortworth.md`, `ree-yunsheng-longbeach.md`, `ree-kuantan-japan.md` (hergebruikte ankers, aanlopen en zeeknopen 4488 / 9065).
[9] OSM/Geofabrik `us-california-latest.osm.pbf` (ODbL), wegscan b1 (`maak_stroombeen_weg.py`, 2026-10-29: 372,1 km, plant 1,00 km / kade 0,27 km snap); MARNET `hecht_marnet.py route`, zee 9.111,6 km, naden 0,000 km (testrun, niet bewaard).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
`bash v2/tools/bak_stromen.sh ree-mountainpass-yokohama` → `v2/data/stroomroute-ree-mountainpass-yokohama.json` (67,6 KB, contract versie 2, lonlat). Functie `bak_ree_mountainpass_yokohama` in `bak_stromen.sh` (LF, 0 CRLF), profiel `ree-mountainpass-yokohama-mountainpass-longbeach` in `maak_stroombeen_weg.py`. Totaal 9.501,3 km, 3.212 punten, 3 markers. Tussenuitvoer uit de eerdere (afgebroken) poging hergebruikt: wegscan-geojson en aanloop-geojson, ongewijzigd.

| # | modaliteit | km | punten | naad | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 373,4 | 2.262 | 0 | `--been-geojson` wegscan us-california (I-15 → Cajon Pass → I-215/I-10 → I-710), doorgetrokken |
| b2 | zee, stippel | 8,5 | 9 | 0 | `--stippel-geojson`, letterlijk omgekeerde kopie van `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (kade 6,47 km van zeeknoop 4488) |
| b3 | zee | 9.111,6 | 939 | 0 | MARNET 4488 → 9065, snap 0,000 km beide kanten, doorgetrokken |
| b4 | zee, stippel | 7,8 | 2 | 0 | rechte `--stippel`, letterlijke kopie uit `bak_ree_kuantan_japan` (kade 7,8 km van knoop 9065) |

**Toets.** b1 373,4 km tegen hemelsbreed 311 (geen wegkm; 10-K "four-hour drive"): omwegfactor 1,20, plausibel voor I-15/Cajon/I-10 en geen norm; b3 9.111,6 = testrun. Naden alle 0,00 km. Markers 0,000 km van de lijn. `toets_rechte_benen`: alleen b4 (stippel met reden). `json.load` ok, modaliteiten {truck, zee}, elk been ≥ 2 punten.

**Stippels.** b2 en b4 zijn haven-aanlopen (kade > 5 km van zijn MARNET-zeeknoop); schematisch, de zeeknopen liggen in open water. Het opgegeven "aannemelijk: één bron" voor truck en voor Honmoku zit in de beennamen en in §3/§7, niet in de lijnstijl.

**Bevindingen.** (1) `toets_knikken` meldt één TERUGLOOP op b1 bij 34.0656,-118.1641 (I-10/I-710-knooppunt, East Los Angeles): een heen-en-terug-spoor van ca. 0,3 km per kant over het knooppunt (router-artefact in het wegnet), ca. 0,6 km op 373 km; niet bijgesneden (geen handmatige ingreep in de wegscan). Verder 7 spikes ≤ 67 m rond de ankerstubs (Mountain Pass en Long Beach) en 5 krappe bochten op de zeeroute in havenbekkens/baai (verwacht). (2) Plant snapt op 1,00 km van de weg (mijnwegen dun gekarteerd, zelfde als `ree-mountainpass-fortworth`).

**Lessen.** Een bestaande afgebroken poging (functie, profiel, geojsons) bleek compleet en is vervangen noch gedupliceerd: alleen bakken en toetsen. Tijdens de run gaf `bash -n` kortstondig een syntaxfout op regel 11586 (een gelijktijdige edit van een andere agent buiten mijn functie); bij de nacontrole was `bash -n` weer schoon en LF 0 CRLF.
