# Routebrief (licht) · Kolen · Dendrobium → Kemira Valley Branch → BlueScope Port Kembla (Australië)

**stroom-id:** `kolen-dendrobium-portkembla` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** cokeskool van de ondergrondse Dendrobium-mijn (Mount Kembla, NSW; nu GEAR en M Resources, tot 2024 South32) per **spoor** over de Kemira Valley Branch (OSM: Nebo Main Line) naar de hoogoven-/cokesovenzijde van BlueScope Port Kembla Steelworks; stoppunt = de staalfabriek, de kool wordt daar tot cokes en staal. Geen zeebeen.
**Welke as van het verhaal:** Australisch **binnenlands** staal: Illawarra-cokeskool naar de enige geintegreerde Australische hoogovenroute aan de oostkust, een kleine keten naast de exportassen. Dendrobium ~3,5 Mt ROM in 2025 (capaciteit 5,2 Mt) [2]; South32 leverde ~60% van BlueScopes cokeskool [4]; het contract (Illawarra Coal Blend uit Appin en Dendrobium) loopt tot 2033 [3].

## 1 · Ketenkaart
```
Dendrobium-mijn (ondergrondse band) -> laadstation Kemira Valley `kolen-dendrobium-laad`
  --(b1 spoor, Kemira Valley Branch / Nebo Main Line, daarna Port Kembla-emplacement, 10,1 km gemeten)-->
BlueScope Port Kembla Steelworks, hoogoven-/cokesovenzijde `kolen-portkembla-hoogoven`  [stoppunt]
```
Appin (tweede bron van dezelfde blend) gaat per truck naar de Port Kembla Coal Terminal [1] en hoort niet in deze keten.

## 2 · Benen
| # | fase | modaliteit | van -> naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-dendrobium-laad` -> `kolen-portkembla-hoogoven` | Kemira Valley Branch (OSM-naam Nebo Main Line) naar Port Kembla, daar het yardspoor tot de staalfabriek | **gepubliceerd 7 km** Kemira Valley -> Dendrobium-kolenwasserij (CPP) op het terrein in Port Kembla [1]; **gemeten 10,1 km** tot de hoogovenzijde (hemelsbreed 8,0) | toets_spoorroute (BAKE_SUFFIX=-raw, extract australie, --hoofd-km=30 --max-snap=10) | nee (snap 0,26 en 0,02 km) |

Afwijking 7 vs 10,1 km: de bron geeft alleen de afstand tot de CPP, niet tot de hoogovenzijde; de gemeten route passeert na 7,1 km het westelijke staalwerkterrein (-34.4637, 150.8743) en loopt daarna via het Port Kembla-yard (zuidlus tot -34.4716) naar de hoogovenzijde. De CPP-plek zelf is niet gevonden (open punt). De +44% is dus geen bewezen fout maar een ander eindpunt; de bake toetst op 10,1 km +-15%.

## 3 · Ankers (een per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-dendrobium-laad` | mijn / laadstation (kop) | Dendrobium, laadlus Kemira Valley | -34.4190, 150.8255 | [2][6][9] | bron-gelegd (z15 gezien: ronde donkere laadlus met stockpile en bandinstallatie in het bos op de escarpment, spoor loopt zuidwaarts naar Mount Kembla). GEM-mijnpunt -34.419776, 150.826135 ligt 0,1 km ernaast |
| `kolen-portkembla-hoogoven` | losplek / staalfabriek (staart, stoppunt) | BlueScope Port Kembla Steelworks, hoogoven- en cokesovenzijde | -34.4647, 150.8929 | [3][5][9] | bron-gelegd (z14 en z15 gezien: zwarte kolenstapels en cokesovenbatterij tegen de roestrode hoogovenzijde, binnenhaven direct noordoost) |

Niet gebruikt: Port Kembla Coal Terminal (~ -34.455, 150.899, zichtbaar op z15 aan de oostkust): export, geen deel van deze keten.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen. Het lokale spoornet is een component van 36 km zonder alternatief tussen de twee ankers; de vrije Dijkstra geeft zonder via-punt 0 keerpunten (bochten >= 60 graden: 0).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in -> uit | capaciteit | bron |
|---|---|---|---|---|
| Dendrobium-kolenwasserij (CPP), Port Kembla | GEAR en M Resources (GM3) | ROM-kool -> cokeskool (Illawarra Coal Blend met Appin) | Dendrobium 3,5 Mt ROM (2025), 5,2 Mt capaciteit | [1][2][3] |
| BlueScope Port Kembla Steelworks | BlueScope | cokeskool -> cokes -> ruwijzer -> staal | niet gevonden | [3][5] |

## 6 · Stoppunt
De brief stopt bij de hoogoven-/cokesovenzijde van BlueScope Port Kembla: een bron noemt de afnemer (BlueScope-contract tot 2033 [3]); de kool gaat daar op in een geintegreerd proces en geen bron volgt een vervolgzending per lading.

## 7 · Open punten
- **Jaarvolume voor deze streng:** alleen Dendrobium-ROM 3,5 Mt (2025) [2] en een aandeel van ~60% in BlueScopes cokeskool [4]; de tonnage Dendrobium -> BlueScope apart is niet gebrond (GEM noemt de staalfabriek en Whyalla als hoofdklanten, 2010-document).
- **Plek van de Dendrobium-CPP** op het staalwerkterrein niet gevonden; daardoor ligt het eindanker op de hoogoven-/cokesovenzijde en niet op de CPP (7 km vs 10,1 km, zie §2).
- **Hoe de product-kool van CPP naar de cokesovens gaat** (band, spoor, interne weg) is niet gebrond; Wikipedia noemt wel dagelijkse Pacific National-kooltreinen naar de hoogovenzijde [5], maar niet uit welke mijn.
- **Appin-aandeel in de blend** niet getekend: Appin gaat per truck naar het kolenterminal [1], de blendverhouding is niet gevonden.
- **Kort been:** 10,1 km is op wereldschaal bijna een stip; de keten draagt de nieuwe regio en rol, niet de lengte.
- **Mijnstatus:** consent loopt tot 2030, uitbreiding tot 2041 stopgezet in 2022 [1][2]; het jaar 2025 is peiljaar.

## 8 · Bronnen
[1] Australian Mining Review, "Appin and Dendrobium" (2026-01): Kemira Valley-laadfaciliteit, 7 km spoor naar de Dendrobium-CPP in Port Kembla, Appin per truck naar PKCT. https://australianminingreview.com.au/issue/2026/01/appin-and-dendrobium/
[2] Global Energy Monitor, Dendrobium Coal Mine: coordinaat -34.419776, 150.826135, ROM 3,535 Mt (2025), capaciteit 5,2 Mt, eigenaar GM3. https://www.gem.wiki/Dendrobium_mine
[3] BlueScope, ASX-bericht 28 mei 2024: Illawarra Coal Blend uit Appin en Dendrobium, CSA met IMC tot 2033, koper GEAR en M Resources (tekst uit de PDF gelezen). https://bluescope.com/content/dam/bluescope/corporate/bluescope-com/investor/documents/2024_ASX_BlueScope_supports_sale_of_IMC_improved_terms.pdf
[4] Illawarra Mercury (2019, bijgewerkt 2023), South32 levert ~60% van BlueScopes cokeskool uit Dendrobium en Appin. https://www.illawarramercury.com.au/story/6292834/steelworks-could-close-if-we-dont-expand-warns-south32
[5] Wikipedia, Port Kembla, NSW: Pacific National-kooltreinen naar het Inner Harbour en de hoogovenzijde; havenkolenkades. https://en.wikipedia.org/wiki/Port_Kembla,_New_South_Wales
[6] Wongm's Rail Gallery, Kemira Valley Branch: aftakking Port Kembla -> mijn op de escarpment, nu voor Dendrobium. https://railgallery.wongm.com/nsw-stations/kemira-valley-branch/
[7] Wikipedia, South Coast railway line (Illawarra-lijn): aansluiting van de industrie in Port Kembla op het Sydney-vrachtnet. https://en.wikipedia.org/wiki/South_Coast_railway_line,_New_South_Wales
[8] OpenStreetMap via Overpass (ODbL): way "Nebo Main Line" bij -34.4177, 150.8273; Port Kembla-yards (Down/Up North Sidings) bij -34.4716, 150.895. https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-kolen-dendrobium-portkembla-laad.png` (z15), `-hoogoven.png` (z14), `-hoogoven15.png` (z15).
[10] Submissie aan het Australische parlement (zoekresultaat, niet zelf gelezen): een 5 km eigen spoorlijn van Illawarra Coal uit de 1800s. https://aphref.aph.gov.au/house/committee/trs/networks/subs/sub166.pdf

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-kolen-dendrobium-portkembla.json` (2,3 KB, versie 2, lonlat) · functie `bak_kolen_dendrobium_portkembla` in `v2/tools/bak_stromen.sh` · 1 been, 82 punten, 2 markers.

| # | modaliteit | been | km gebakken | brief | stippel |
|---|---|---|---|---|---|
| b1 | spoor | trein Dendrobium-laadlus Kemira Valley -> BlueScope Port Kembla (Kemira Valley Branch / Nebo Main Line, Port Kembla-yard) | **10,2** (10,18 uit de punten) | 10,1 gemeten (+1%); 7 km gepubliceerd naar de CPP, ander eindpunt | nee, doorgetrokken |

**Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=-34.4190,150.8255 --naar=-34.4647,150.8929 --naam=kolen-dendrobium-portkembla-laad-hoogoven --hoofd-km=30 --max-snap=10` (extract australie, geen via; 50 edges, snap 0,26 en 0,02 km) -> `spoorroute-kolen-dendrobium-portkembla-laad-hoogoven.geojson` (FeatureCollection) -> `bash v2/tools/bak_stromen.sh kolen-dendrobium-portkembla`. De spoorrun was al gedraaid en is hergebruikt; alleen de bake draaide nu (zwaar-slot).

**Toets:** enige been, dus geen naden. Markers 0,255 km (laadlus) en 0,022 km (hoogovenzijde) van de lijn. `toets_knikken`: 0 knikken, 0 omkeringen. `toets_rechte_benen --min-km 5`: geen treffer. json.load: versie 2, punt_formaat lonlat, modaliteit spoor, 82 punten, 2,3 KB.

**Stippel / haven-aanloop / vlucht / leiding:** geen. Geen zeebeen: Appin gaat per truck naar de Port Kembla Coal Terminal en hoort niet in deze keten; stoppunt = hoogoven-/cokesovenzijde.

**Lessen / meldingen:** (1) De lengtetoets 7 vs 10,2 km is geen norm: de bron meet tot de Dendrobium-CPP, de CPP-plek is niet gevonden en het anker ligt op de hoogovenzijde; de lijn passeert na ~7,1 km het westelijke staalwerkterrein. (2) Het eerste punt van de lijn ligt 0,26 km van het laadlus-anker (zichtbare korte naad, binnen de 0,5 km-norm). (3) Tijdens het bakken was de console-uitvoer van de router ruim; de bake zelf duurde enkele seconden na de 12 s graaf-load. (4) Geen wijziging aan sitelagen, register of bundel; centrale registratie volgt.
