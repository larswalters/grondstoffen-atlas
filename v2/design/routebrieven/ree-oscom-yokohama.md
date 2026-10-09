# Routebrief (licht) · Zeldzame aardmetalen · OSCOM Chatrapur → Toyotsu (Atchutapuram) → Visakhapatnam → Yokohama (Japan)

**stroom-id:** `ree-oscom-yokohama` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** IREL-materiaal van de Rare Earth Extraction Plant (OSCOM, Chatrapur, Odisha) gaat per **truck**
(aannemelijk) over NH-16 naar Toyotsu Rare Earths India (TREI, APSEZ Atchutapuram), per truck naar de Visakha
Container Terminal (VCT, aannemelijk) en per **zeeschip** door Straat Malakka naar Honmoku Futo, Yokohama
(aannemelijk) — de India-Japan-export van Toyota Tsusho, levering opgeschort 14-06-2025 (peiljaar 2024).
**Welke as van het verhaal:** India als niet-Chinese leverancier van Japan: circa 1,0 kt zeldzame-aardmaterialen per jaar
(peiljaar 2024, "meer dan 1.000 t", een derde van IREL's 2.900 t; REO-gehalte niet gepubliceerd, dus kt materiaal, geen kt REO)
[1][2]. OSCOM-capaciteit 11.200 tpa MRCL [2].

## 1 · Ketenkaart
```
OSCOM REEP, Chatrapur `ree-oscom-reep` (hergebruikt, ree-oscom-aluva.md)
  ──(b1 truck · NH-16 oostkust via Berhampur–Srikakulam–Vizianagaram tot Anakapalle · 303,1 km gemeten (kopie)
     + Anakapalle→TREI hemelsbreed 19 km, geen wegkm; aannemelijk: modaliteit)──►
Toyotsu Rare Earths India, APSEZ Atchutapuram `ree-oscom-yokohama-trei` ⏹ verwerking/handel (aannemelijk: één bron voor de plant)
  ──(b2 truck · Anakapalle–Pudimadaka Road → Anakapalle → NH-16 → Gajuwaka → havenweg · hemelsbreed 39 km, geen wegkm;
     aannemelijk: geen bron noemt de uitvoerhaven)──►
Visakha Container Terminal `ree-oscom-yokohama-vct-kade`  ··aanloop 13,2 km (stippel)··►
  ──(b3 zee · Baai van Bengalen → Straat Malakka → Zuid-Chinese Zee → Luzon/Taiwanstraat · MARNET ~8.351 km;
     aannemelijk: geen bron noemt de Japanse haven)──►  ··aanloop 7,8 km (stippel, kopie)··►
Honmoku Futo, Yokohama `ree-kuantan-japan-honmoku-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | C | truck (aannemelijk: modaliteit niet bevestigd) | `ree-oscom-reep` → Anakapalle (17.6894, 83.0035) | NH-16 oostkust, Anakapalli Main Road | 303,1 gemeten; hemelsbreed 274 km, geen wegkm | LETTERLIJKE KOPIE punt 0–3053 van `ree-oscom-aluva-weg-oscom-aluva.geojson` | nee |
| b1b | C | truck | Anakapalle → `ree-oscom-yokohama-trei` | Anakapalle–Pudimadaka Road | hemelsbreed 19 km, geen wegkm | maak_stroombeen_weg (extract `india`) | nee; site binnen APSEZ |
| b2 | C | truck (aannemelijk: uitvoerhaven niet genoemd) | TREI → `ree-oscom-yokohama-vct-kade` | Anakapalle – NH-16 – Gajuwaka – havenweg (b2 loopt ~20 km over b1 terug, reëel) | hemelsbreed 39 km, geen wegkm | maak_stroombeen_weg (extract `india`) | nee; havenpoort kan privé zijn |
| b3a | C | zee-aanloop | VCT-kade → zeeknoop 5355 (17.6221, 83.3898) | — | 13,2 (maak_havenaanloop, gemeten) | geojson `ree-oscom-yokohama-aanloop-vizag.geojson` | **ja**: kade 12,1 km van zeeknoop |
| b3b | C | zee (aannemelijk: Japanse haven niet genoemd) | zeeknoop 5355 → zeeknoop 9065 (35.3661, 139.6857) | Malakka–Luzon/Taiwan | MARNET ~8.351 (toets); eigen schatting 8.500–9.000; hemelsbreed 5.859 | MARNET | nee |
| b3c | C | zee-aanloop | zeeknoop 9065 → Honmoku-kade | — | 7,8 (kopie uit `ree-kuantan-japan`) | `--stippel` zoals in `bak_ree_kuantan_japan` | **ja**: kade 7,8 km van zeeknoop |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-oscom-reep` | fabriek (start) | OSCOM REEP, Chatrapur | 19.3261, 84.9449 | [2][5]; hergebruikt uit `ree-oscom-aluva.md` | bron-gelegd (daar z16 gezien: gebouwencomplex met witte daken, bekken, roodbruine grond aan OSCOM Road) |
| `ree-oscom-yokohama-trei` | verwerking/handel | Toyotsu Rare Earths India Pvt Ltd, plot 2D/2E APSEZ | 17.5195, 82.9833 | [3][4] OSM-way 801380959 (man_made=works) | bron-gelegd (z15 gezien: fabrieksperceel met gebouwen en tanks tussen andere APSEZ-fabrieken, kruis op het perceel) |
| `ree-oscom-yokohama-vct-kade` | overslag truck → zee | Visakha Container Terminal, Visakhapatnam | 17.6934, 83.3031 | [6] OSM landuse industrial; geen bron noemt deze haven | aannemelijk (z15 gezien: containeryard met kranen, stapels en schepen langs de kade; alternatief Gangavaram 17.6366, 83.2240 niet gelegd) |
| `ree-kuantan-japan-honmoku-kade` | losplek zee (einde) | Honmoku Futo, Yokohama | 35.4356, 139.6727 | hergebruikt uit `ree-kuantan-japan.md` | bron-gelegd (daar z14 gezien: opgespoten pier, stapels, kranen); 7,8 km van zeeknoop 9065 |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1a | — | geen nieuwe via-punten: de kopie draagt Vijayawada-corridor-keuze van `ree-oscom-aluva` (NH-16) tot punt 3053 | 17.6894, 83.0035 | eindpunt ligt op Anakapalli Main Road (OSM primary, Nominatim), de afslag naar de Pudimadaka Road; geen stadscentrum-via |
| b1b | 1 | Anakapalle, begin Anakapalle–Pudimadaka Road | 17.6894, 83.0035 | zelfde punt als einde b1a, zodat de naad 0 is |
| b2 | — | 0–2 via-punten toegestaan; alleen toevoegen als de Dijkstra een omweg kiest, dan op NH-16 bij Sabbavaram/Gajuwaka (coördinaat nog te leggen, niet verzonnen) | — | corridorkeuze is niet gebrond |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| OSCOM REEP | IREL (India) Ltd | monaziet → MRCL, trinatriumfosfaat | 11.200 tpa MRCL | [2] |
| TREI | Toyota Tsusho (Japan) | IREL-materiaal → oxiden/carbonaat voor Japan | niet gepubliceerd; plan 2010 tot 4.000 t/j | [1][3][7] |

## 6 · Stoppunt
De brief stopt bij Honmoku Futo: geen bron noemt een Japanse haven of magneetfabriek voor deze lading (Shin-Etsu, TDK en
Proterial zitten verspreid, zie `ree-kuantan-japan.md`); fase D/E vervallen.

## 7 · Open punten
- **Product-aanname:** Wikipedia en TREI-site noemen oxiden/carbonaat; Reuters-samenvattingen zeggen "neodymium" zonder vorm. Het Industryweek-bericht uit 2010 noemt plant in Orissa, geen IREL of chloride. OSCOM als herkomst is aannemelijk, niet door een bron op de stroom bevestigd (oxiden worden bij RED Aluva gemaakt, niet bij OSCOM).
- **Ligging TREI:** het 2010-bericht zegt Orissa; OSM en de TREI-site zeggen APSEZ Atchutapuram (Andhra). Brief volgt OSM/site; valt de plant in Odisha, dan vervalt b2 en wordt b1b zeer kort.
- **Uitvoerhaven VCT en Japanse haven Honmoku zijn aannemelijk** (geen bron); Nagoya is het alternatief gezien Toyota Tsusho; Gangavaram het alternatief voor Vizag.
- **Geen gepubliceerde wegkm** voor b1b en b2 (hemelsbreed 19 en 39 km); alleen b1a is gemeten (303,1 km, hemelsbreed 274 km, +10,6%). ±15%-toets is indicatie.
- **Opschorting 14-06-2025:** volume is peiljaar 2024; huidige stand 2026 niet gevonden.
- Eindpunt b1a ligt op een primary road in Anakapalle; de bak-agent controleert dat b1b daar zonder naad aansluit.
- VCT-havenpoort/terminal kan privéweg zijn: `eindToegangPrivaat` of korte stippel last mile (privéterrein).

## 8 · Bronnen
[1] Reuters via Autocar Professional, "India suspends rare earth exports to Japan" (2025-06): 2012-akkoord, TREI, >1.000 t in 2024 (een derde van 2.900 t). https://www.autocarpro.in/news/india-suspends-rare-earth-exports-to-japan-as-china-tightens-global-supply-controls-127013
[2] Wikipedia, "IREL (India)": OSCOM REEP, MRCL 11.200 tpa, TREI verkoopt IREL-oxiden/carbonaat, opschorting 14-06-2025. https://en.wikipedia.org/wiki/IREL_(India)
[3] Toyotsu Rare Earths India, about: plot 2D/2E APSEZ Atchutapuram, Anakapalle district. https://trei.co.in/about.html
[4] OpenStreetMap way 801380959 "Toyotsu Rare Earths India Pvt. Ltd" (Nominatim 17.5195, 82.9833). https://www.openstreetmap.org/way/801380959
[5] OSM/Nominatim "OSCOM Road" en USGS-record Chatrapur, via `ree-oscom-aluva.md`. https://www.openstreetmap.org
[6] Wikipedia, "Visakhapatnam Port" (grootste haven aan de oostkust van India). https://en.wikipedia.org/wiki/Visakhapatnam_Port
[7] Industryweek, "Toyota Tsusho to build plant processing rare earths in India" (2010-12-08): plant in Orissa, tot 4.000 t/j voor Japan. https://www.industryweek.com/industry-clusters/toyota-tsusho-build-plant-processing-rare-earths-india
[8] Nominatim reverse 17.6894, 83.0035: Anakapalli Main Road, OSM way 405705896 (primary). https://nominatim.openstreetmap.org
[9] Esri World Imagery via `sat_check.py` z15: `v2/build-cache/satcheck/sat-ree-oscom-yokohama-trei-z15.png`, `sat-ree-oscom-yokohama-vct-z15.png`.
[10] MARNET-zeeknopen 5355 en 9065 en `maak_havenaanloop.py` (13,2 km, 0,43 km land aan het uiteinde), eigen meting 2026-10-09; kopie van `ree-kuantan-japan.md` voor Honmoku.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)

**Bestand:** `v2/data/stroomroute-ree-oscom-yokohama.json` · 6 benen · 8.747,7 km · 4.960 punten · 4 markers · 96,3 KB.
**Recept:** functie `bak_ree_oscom_yokohama()` in `v2/tools/bak_stromen.sh`; profielen `ree-oscom-yokohama-anakapalle-trei` en
`ree-oscom-yokohama-trei-vct` in `maak_stroombeen_weg.py` (extract india, wegscan via `wegscan_puur.py`, want pyosmium is geblokkeerd).

| # | modaliteit | km | naad | geometrie |
|---|---|---|---|---|
| b1a | truck | 303,1 | 0 | LETTERLIJKE KOPIE van het wegbeen van `ree-oscom-aluva` (punt 0-3053), geen eigen scan |
| b1b | truck | 21,6 | 0,000 | wegscan, 246 punten; gemeten 21,4 km tegen hemelsbreed 19 (+12,6%, indicatie) |
| b2 | truck | 50,8 | 0,000 | wegscan, 793 punten; gemeten 50,6 km tegen hemelsbreed 39 (+29,7%, indicatie) |
| b3a | zee, STIPPEL | 13,2 | 0,000 | haven-aanloop VCT-kade naar zeeknoop 5355 (maak_havenaanloop, 0,43 km over land aan het uiteinde) |
| b3b | zee | 8.351,2 | 0,000 | MARNET zeeknoop 5355 naar 9065, tegen brief-toets ~8.351 (0,0%) |
| b3c | zee, STIPPEL | 7,8 | 0,000 | rechte stippel zeeknoop 9065 naar Honmoku, kopie van `ree-kuantan-japan` |

**Toets.** `json.load` ok, versie 2, punt_formaat lonlat, alle modaliteiten geldig, elk been >= 2 punten. Alle naden 0,000 km (de
kopie sluit bij Anakapalle op 0 aan b1b). Alle 4 markers 0,0 km van de lijn. `toets_knikken`: 0 omkeringen en 0 terugloop; 47
knikken >= 60 graden in b1b/b2 met 2-43 m boogstraal (OSM-rotonde- en kruispuntvertices, geen omweg). `toets_rechte_benen`: alleen de
twee bedoelde stippels (b3a is een gemeten aanloop, b3c recht).

**Toelichting.**
- **Geen gepubliceerde wegkm voor b1b en b2:** de +-15%-toets is een indicatie. b2 (+29,7% op hemelsbreed) is geen fout: Atchutapuram
  ligt aan de andere kant van het kustgebied en de weg volgt het wegennet. De brief verwachtte dat b2 ~20 km over b1b terugliep via
  Anakapalle; de kortste route blijkt directer (kortste afstand tot Anakapalle 11,1 km). Er is geen via-punt bijgeschoven.
- **Stippels:** b3a (VCT-kade 12,1 km van zeeknoop 5355, boven de 5 km-norm) en b3c (Honmoku 7,8 km van zeeknoop 9065) zijn
  "hier reikt het net niet"; b3b is gemeten en doorgetrokken. "Aannemelijk" staat in de beennamen, niet in de lijnstijl.
- **Titel:** het eindpunt klopt met het id (Yokohama); geen afwijking van het ontwerp.
- **Geen last-mile-stippel:** plant naar weg 0,00 km en weg naar kade 0,21 resp. 0,02 km (b1b/b2); b1b/b2 eindigen op het anker.
- **Geen vlucht, leiding of spoor.**

**Lessen.** (1) Een tweede scan van India voor het tweede profiel kost opnieuw ~10 minuten: de scancache is per profiel gehasht,
dus bij twee benen in dezelfde extract loont het om ze in één profiel met een via-punt te zetten wanneer de naad niet op een
eigen anker hoeft. (2) Een kopie van een bestaand wegbeen sluit zonder naad aan zodra het eerste via-punt van het volgende profiel
het laatste punt van de kopie is (83.003463, 17.689409).
