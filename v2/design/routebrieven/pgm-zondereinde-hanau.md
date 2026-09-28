# Routebrief (licht) · PGM — Zondereinde (Bushveld) → OR Tambo → Frankfurt → Hanau (Duitsland)

**stroom-id:** `pgm-zondereinde-hanau` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** PGM-concentraat (Pt+Pd+Rh+Au, "4E") van Northam's Zondereinde-mijn/smelter/basismetaalraffinaderij (noordrand Bushveld, Limpopo) per **truck** naar de vrachtterminal van OR Tambo (JNB), per **vrachtvlucht** (grootcirkel) naar Frankfurt (FRA), en per **truck** naar Heraeus Precious Metals in Hanau, waar het concentraat wordt **toll-geraffineerd** tot 99,95% zuiver metaal.
**Welke as van het verhaal:** *Zuid-Afrika/Bushveld (Northam Zondereinde) → Hanau (Heraeus)* — de derde, kleinere PGM-as naast de Amplats/Implats-stromen: Northam heeft een eigen smelter + basismetaalraffinaderij op één site, maar **geen eigen edelmetaal-eindraffinage** — die zit sinds de start van het bedrijf bij Heraeus (Hanau + Port Elizabeth), sinds kort aangevuld met Johnson Matthey [2].

## 1 · Ketenkaart
```
Zondereinde mijn+smelter+BMR `pgm-zondereinde-mijnsmelter` ──(b1 truck · R510/N4/N1 · ~140 km)──► OR Tambo vrachtterminal `pgm-ortambo-vracht` (JNB)
   ──(b2 lucht · vlucht JNB → FRA, grootcirkel · ~8.900 km, aannemelijk: industriestandaard)──► Frankfurt vrachtterminal `pgm-frankfurt-vracht` (FRA, Cargo City Süd)
   ──(b3 truck · A66 · ~25 km)──► Heraeus Precious Metals Hanau `pgm-heraeus-hanau` — stoppunt (toll-raffinage tot 99,95%)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Zondereinde mijn/smelter → OR Tambo vrachtterminal | R510 (Northam→Thabazimbi-richting is fout; corridor loopt zuidwaarts via Marikana) / N4 / N1 | ~140 [ontwerp] | maak_stroombeen_weg | nee |
| b2 | B | lucht | OR Tambo (JNB) → Frankfurt (FRA) | vrachtvlucht JNB→FRA (grootcirkel) | ~8.900 [ontwerp; grootcirkel JNB–FRA ≈ 8.870] | maak_luchtbeen | nee — doorgetrokken (vlucht tussen twee gelegde vrachtterminals is geen gat) |
| b3 | C | truck | Frankfurt vrachtterminal → Heraeus Hanau | A66 Frankfurt–Hanau | ~25 [ontwerp] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-zondereinde-mijnsmelter` | mijn / smelter / BMR (laadplek) | Northam Zondereinde-complex, Thabazimbi LM, Limpopo | -24.8333, 27.3669 | [1][2][7][10] | bron-gelegd (z16 gezien: ommuurd industrieterrein met proces­gebouwen, schoorsteen/rookpunt en opslagvlakken, 1,9 km NO van de Northam-zonnepark-OSM-node en 2,0 km ZW van de Zondereinde-tailingsfaciliteit — geometrie past bij mijn+smelter tussen krachtvoorziening en stortplaats) |
| `pgm-ortambo-vracht` | vrachtterminal (lucht, vertrek) | OR Tambo International Airport, vrachtplatform, Kempton Park | -26.1290, 28.2330 | [3][8] | bron-gelegd (z14 gezien: vrachtloodsen + apron met vrachttoestellen direct zuid-oost van de hoofdterminal, aan de westzijde van de start-/landingsbanen) |
| `pgm-frankfurt-vracht` | vrachtterminal (lucht, aankomst) | Flughafen Frankfurt am Main, Cargo City Süd | 50.0244, 8.5552 | [4][8] | bron-gelegd (z14 gezien: loodsencluster + apron met vrachttoestellen zuidelijk van de start-/landingsbanen, OSM landuse "Cargo City Süd") |
| `pgm-heraeus-hanau` | raffinaderij (losplek / stoppunt) | Heraeus Precious Metals, Hanau | 50.1328, 8.9315 | [5][8] | bron-gelegd (z15 gezien: industrieterrein met proces- en kantoorgebouwen tussen de Kinzig en het spooremplacement, OSM landuse "Heraeus") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Northam (dorp aan het R510-begin bij de mijn) | -24.9575, 27.2656 | corridor begint hier op het R510-tracé zuidwaarts (OSM-town-node) |
| b1 | 2 | Marikana (R510/N4-omgeving, Bojanala) | -25.6879, 27.4915 | corridor snijdt hier het Rustenburgse PGM-mijndistrict voordat hij oostwaarts naar de N4 buigt |
| b1 | 3 | Brits (N4, Madibeng) | -25.6297, 27.7842 | vaste doorgaande knoop op de N4 tussen Rustenburg-richting en Pretoria |
| b1 | 4 | Pretoria (N4/N1-knoop) | -25.7461, 28.1881 | hier stapt de corridor over van de N4 op de N1 zuidwaarts naar Johannesburg/Kempton Park |
| b3 | 1 | Maintal (A66, tussen Frankfurt en Hanau) | 50.1439, 8.8371 | vaste doorgaande knoop op de A66-corridor, geen zijtak |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zondereinde smelter + BMR | Northam Platinum | UG2/Merensky-erts → PGM-matte → basismetaal­verwijdering → filter-/droogconcentraat | smelter uitgebreid naar 35 MW, > 1 miljoen oz/jaar verwerkingscapaciteit | [2] |
| Heraeus Hanau (+ Port Elizabeth) | Heraeus Deutschland | concentraat (toll) → individuele metalen op 99,95% | toll-raffinage sinds de start van Northam; recent aangevuld met Johnson Matthey ter diversificatie | [2] |

## 6 · Stoppunt
De brief stopt bij de poort van Heraeus Hanau: dat is waar Northam's concentraat volgens de eigen bronvermelding wordt toll-geraffineerd tot verhandelbaar metaal (99,95%) [2]; een afnemersfabriek ná de raffinage is niet gebrond (fase D/E vervallen — geen bron noemt een specifieke klant van de gereedmetalen uit déze partij).

## 7 · Open punten
- **De bindende "aanpassing" uit de haalbaarheidstoets is met bronwerk beantwoord, niet toegepast:** Zondereinde raffineert zélf geen edelmetaal-baren, maar de eindraffinage gebeurt niet bij een Zuid-Afrikaanse toll-raffinaderij (Rustenburg PMR/Impala Springs) — Northam's eigen metallurgische-operaties-pagina noemt expliciet dat het filterconcentraat rechtstreeks naar **Heraeus Hanau én Heraeus Port Elizabeth** gaat voor toll-raffinage [2]. De oorspronkelijke as (Zondereinde → Hanau, met lucht via JNB→FRA) blijft dus overeind; reserve-as P10 is niet nodig.
- **Jaarvolume, twee cijfers, geen van beide voor déze vlucht apart gebrond:** het ketenontwerp geeft FY2023 ≈ 450–500 koz 4E (≈ 14–16 t 4E/jaar, Northam-jaarverslag, niet zelf teruggevonden binnen het budget); Northam's eigen Zondereinde-pagina noemt losstaand "ongeveer 300.000 oz per jaar" zonder peiljaar [1]. Beide zijn 4E (Pt+Pd+Rh+Au), niet zonder meer gelijk aan 3E. Welk deel van dit volume daadwerkelijk via JNB→FRA vliegt (i.p.v. bv. Port Elizabeth-poot) is niet gebrond.
- **Luchtvracht zelf is aannemelijk, niet apart gebrond voor déze stroom** — geen bron noemt expliciet "per vliegtuig" voor het Zondereinde-concentraat; dit volgt de industriestandaard voor Zuid-Afrikaans PGM-concentraat/-baren naar Europese raffinaderijen (zoals bij de Amplats/Implats-assen), en de aanname staat hier expliciet vermeld.
- Via-punten van b1 en b3 zijn corridorpunten (dorpen/knopen op de doorgaande weg), niet zelf satelliet-gelegd — dat is bij de lichte werkwijze alleen verplicht voor de vier ankers.
- `pgm-ortambo-vracht` is hier voor het eerst gelegd binnen deze golf (geen eerdere PGM/goud/diamant-brief met dit anker gevonden in `v2/design/routebrieven/`); latere ketens met dezelfde luchthaven horen dit punt te hergebruiken i.p.v. opnieuw te leggen.
- Northam's positie als kleinste van de drie grote ZA-PGM-producenten met één smelt-/raffinagelocatie (enkelvoudig-punt-risico) is niet verder gekwantificeerd binnen het budget.

## 8 · Bronnen
[1] Northam Platinum, "Zondereinde" — mijnbeschrijving, ~300.000 oz/jaar 4E uit eigen operaties, UG2/Merensky-erts. https://www.northam.co.za/about-northam/zondereinde
[2] Northam Platinum, "Metallurgical operations" — smelter (35 MW, >1 Moz/jaar), BMR, filterconcentraat verzonden naar Heraeus-raffinaderijen in Hanau (Duitsland) en Port Elizabeth (Zuid-Afrika), toll-raffinage tot 99,95%; sinds de start van het bedrijf, recent aangevuld met Johnson Matthey. https://www.northam.co.za/about-northam/metallurgical-operations
[3] Wikipedia, "O. R. Tambo International Airport" — IATA JNB, Kempton Park, coördinaten -26.13333,28.25 (luchthavencentrum; vrachtterminal-anker apart satelliet-gelegd, zie §3). https://en.wikipedia.org/wiki/O._R._Tambo_International_Airport
[4] OpenStreetMap (Nominatim/Photon) — "Flughafen Frankfurt am Main", locality "Cargo City Süd", 50.02441/8.55520. https://www.openstreetmap.org
[5] OpenStreetMap (Nominatim) — landuse "Heraeus", Hanau Südost, 50.13282/8.93153. https://www.openstreetmap.org
[6] Northam Platinum, bedrijfswebsite (algemeen, mijnen Zondereinde/Booysendal/Eland). https://www.northam.co.za/about-namibia
[7] OpenStreetMap (Overpass) — node "ZONDEREINDE" (landmeetpunt 2427-103), way "Zondereinde Tailings Storage Facility" (-24.8211,27.3766), power-plant "Zondereinde" (Northam, solar 80 MW, 2025, -24.8469,27.3651). https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live) — `v2/build-cache/satcheck/sat-pgm-zondereinde-verken.png`, `sat-pgm-zondereinde-zoom.png`, `sat-pgm-ortambo-cargo.png`, `sat-pgm-frankfurt-cargo.png`, `sat-pgm-heraeus-hanau.png`.
[9] Wikipedia, "Bushveld Igneous Complex" (achtergrond, geologische context van de Zondereinde-mijn op de noordrand van het westelijke lidmaat). https://en.wikipedia.org/wiki/Bushveld_Igneous_Complex
[10] OpenStreetMap (Photon) — "Northam" (dorp, Thabazimbi LM, 27.26556/-24.9575), "Marikana" (27.49154/-25.68794), "Brits" (27.78417/-25.62972); Wikipedia-coördinaten Pretoria (28.18806/-25.74611); Photon "Maintal" (8.83713/50.14387). https://www.openstreetmap.org · https://en.wikipedia.org/wiki/Pretoria

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `pgm-zondereinde-hanau`** → `v2/data/stroomroute-pgm-zondereinde-hanau.json` — 3 benen (truck fase A →
lucht fase B → truck fase C → stoppunt), **9.005,2 km**, 4.193 punten, 4 markers, 83,7 KB. Recept: `bak_stromen.sh`
(functie `bak_pgm_zondereinde_hanau`); twee nieuwe wegprofielen `pgm-zondereinde-hanau-zondereinde-ortambo` en
`pgm-zondereinde-hanau-frankfurt-hanau` in `maak_stroombeen_weg.py`.

**b1 (truck, nieuw profiel, extract `zuid-afrika`, vensterKm 40):** `maak_stroombeen_weg.py --profiel
pgm-zondereinde-hanau-zondereinde-ortambo --bron geofabrik` — **281,4 km** geroute (getekende lijn 281,8 km incl.
anker-verbindingsstukjes 0,28/0,10 km, beide OK) over de vier via-punten uit de brief §4 (Northam-dorp → Marikana
→ Brits → Pretoria), R510 zuidwaarts → N4 oostwaarts → N1 zuidwaarts, geen alternatieve corridor gevonden. 38
keerlussen gesnoeid (289,6 → 281,4 km, dubbel gereden stukken, vooral bij Brits en rond het OR Tambo-
vrachtplatform). First mile 8,65 km / last mile 2,24 km over kleine wegklassen (residential/service/tertiary/
unclassified).

**⚠️ Lengtetoets BUITEN de norm:** 281,4 km tegen het ~140 km-ontwerpcijfer (routebrief §1/§2, "niet apart
gebrond") = **+101,0%**, ruim boven ±15%. **Bevinding, geen fout**: de hemelsbrede afstand tussen de twee ankers
(Zondereinde -24,8333/27,3669 → OR Tambo -26,1290/28,2330) is zelf al ~168 km — het ontwerpcijfer van 140 km was
dus intern al te laag, los van enige routering. De vier via-punten uit de brief pinnen de enige doorgaande
corridor R510→N4→N1 (Northam-dorp/Marikana/Brits/Pretoria); geen via-punt bijgeschoven om het getal te halen. De
bake-uitvoer (281,4 km) is de echte controle, niet het ontwerpcijfer (bakhandleiding §5/§6). Vergelijkbaar met de
+48,4%- en +59,8%-bevindingen op de zuster-PGM-ketens `pgm-rustenburg-shanghai` en `pgm-springs-zurich` (zelfde
golf, zelfde regio, zelfde soort indicatief ontwerpcijfer).

**b2 (lucht, `maak_luchtbeen.py`, DOORGETROKKEN):** `python v2/tools/maak_luchtbeen.py --van "OR Tambo
vrachtterminal|-26.1290,28.2330" --naar "Frankfurt vrachtterminal|50.0244,8.5552" --uit
$BEEN/pgm-zondereinde-hanau-lucht-ortambo-frankfurt.geojson` — grootcirkel **8.688,0 km**, 349 punten. Tegen het
brief-ontwerpcijfer ~8.900 km (−2,4%, ruim binnen elke redelijke marge, en dichter bij de eigen "grootcirkel
JNB–FRA ≈ 8.870"-schatting uit de opdracht) — een luchtbeen heeft geen ±15%-km-toets (zijn km = grootcirkel per
constructie, bakhandleiding §5). Geen tussenlanding: geen bron in de brief noemt een hub (§7), dus één directe
vrachtvlucht JNB → FRA conform §2 "Lucht", aannemelijk als industriestandaard voor Zuid-Afrikaanse PGM-luchtvracht
naar Europese raffinaderijen.

**b3 (truck, nieuw profiel, extract `de-hessen`, `eindToegangPrivaat: True`, vensterKm 40):**
`maak_stroombeen_weg.py --profiel pgm-zondereinde-hanau-frankfurt-hanau --bron geofabrik` — **35,3 km** geroute
(getekende lijn 35,4 km incl. anker-verbindingsstukjes 0,01/0,03 km, beide OK), A66 Frankfurt–Hanau. 60 keerlussen
gesnoeid (35,4 → 35,3 km). First mile 3,83 km / last mile 0,80 km over kleine wegklassen.

**⚠️ Maintal (brief §4, b3-1) NIET als via-punt meegenomen — afwijking, gemotiveerd.** De eerste scanpoging
(zonder Maintal, vensterKm 15) faalde op "geen wegpad tussen punt 0 en 1" tussen het Frankfurt-vrachtterminal-
anker en Maintal — het Frankfurt-anker ligt op de vrachtterminal binnen Cargo City Süd, overwegend
`highway=service access=private`-wegen (bevestigd met een losse pyosmium-scan op `de-hessen`, 364 zulke ways
binnen 200 m van het anker); `eindToegangPrivaat: True` toegevoegd, venster naar 40 km verbreed — nog steeds "geen
wegpad". Een aparte connectiviteitscontrole (BFS over motorway/trunk/primary/secondary/tertiary/unclassified/
residential + `service`+`access=private` binnen 6 km van elk anker, op dezelfde `de-hessen`-extract) liet zien
dat het Maintal-punt (Bahnhofstraße/Edmund-Seng-Straße, Maintal-centrum) in een ANDER verbonden wegennet zat dan
het Frankfurt-vrachtterminalanker, terwijl Frankfurt-vrachtterminal en Heraeus Hanau elkaar wél rechtstreeks
bereiken. De brief zelf onderbouwt dit al impliciet: Maintal is "een vaste doorgaande knoop..., geen zijtak" (§4)
— geen corridorkeuze die gepind moet worden (routebrief-licht.md §1: via-punten alleen waar een corridorkeuze
bestaat). b3 routeert daarom rechtstreeks Frankfurt-vrachtterminal → Heraeus Hanau over de A66; geen via-punt
bijgeschoven om een wegpad te forceren.

**⚠️ Lengtetoets BUITEN de norm:** 35,3 km tegen het ~25 km-ontwerpcijfer (routebrief §1/§2, "niet apart gebrond")
= **+41,3%**, buiten ±15%. Bevinding, geen fout: dezelfde klasse als b1 en de zuster-ketens hierboven — een
indicatief ontwerpcijfer, geen gepubliceerde bronlengte om tegen te toetsen; de A66-corridor via de aansluitingen
rond Maintal/Hanau is de enige doorgaande verharde route tussen de twee ankers.

**Toetsen:** `toets_knikken.py` — b1 (truck): 23 knikken ≥60°, **0 omkeringen, 0 terugloop**; b2 (lucht): 0
knikken, 0 omkeringen (per constructie recht); b3 (truck): 13 knikken ≥60°, **0 omkeringen, 0 terugloop** — alle
36 knikken zijn kleine-straal-spikes (1–97 m) bij kruispunten/bochten, geen enkele hoort volgens de toets-
documentatie gerepareerd te worden. `toets_rechte_benen.py --min-km 5 --alles` — geen ⚠️-vlag voor deze stroom:
lucht op omwegfactor 1,000 (per ontwerp, wordt overgeslagen), b1 op 1,675 en b3 op 1,203 (beide ruimschoots geen
verdachte rechte lijn). `json.load` slaagt: `versie` 2, `punt_formaat` lonlat, modaliteiten `{truck, lucht}` ⊂
toegestane set, elk been ≥ 2 punten (2.664 / 349 / 1.180), bestandsgrootte 83,7 KB (ruim onder ~300 KB). Naden
tussen b1↔b2 en b2↔b3: **0,000 km** (elk been-geojson start exact op het eindpunt van het vorige, gecontroleerd
via de bake-console-coördinaten). Markers: alle vier ankers zijn letterlijk het eindpunt van hun been (0,000 km
tot de lijn) — routeerpunt = anker op elke overslag.

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippel in deze stroom. Geen zeebeen dus geen haven-
aanloop. Eén vlucht (b2), doorgetrokken conform bakhandleiding §2: anker = de satelliet-gelegde vrachtterminals
aan beide kanten (brief §3, bron-gelegd), geen tussenlanding aangenomen (§7). De truckbenen sluiten rechtstreeks
aan op het vrachtplatform-eind van de vlucht — geen apart terminalbeen nodig, want het OR Tambo- resp. Frankfurt-
vrachtterminalanker ís al het overslagpunt truck ↔ lucht.

**Gereedschapslessen:** `eindToegangPrivaat` was nodig voor het Frankfurt-vrachtterminal-anker (Cargo City Süd)
— zonder de vlag faalde `maak_stroombeen_weg.py` op "geen wegpad tussen punt 0 en 1", ook na verbreding van
vensterKm 15 → 40; met de vlag routeert hij over de private service-wegen tot het anker (snap 0,01 km). Anders
dan bij eerdere `eindToegangPrivaat`-gevallen loste dit een tweede, apart probleem NIET automatisch op: het
Maintal-via-punt bleef "geen wegpad" geven omdat het in een ander verbonden wegennet lag dan het Frankfurt-anker
— pas het weglaten van dat via-punt (in plaats van nóg breder venster of nóg meer klassen) loste het op. Les:
bij "geen wegpad" tussen twee specifieke punten kan het probleem bij ÉÉN van de twee punten liggen, en is een
losse connectiviteitscontrole (BFS op de eigen extract) sneller dan het venster/de klassen blind ophogen. Eerste
keer dat een PGM-luchtbeen zonder tussenlanding zowel bij vertrek als aankomst een `eindToegangPrivaat`-achtige
airside-situatie combineert met een via-punt dat moest sneuvelen.
