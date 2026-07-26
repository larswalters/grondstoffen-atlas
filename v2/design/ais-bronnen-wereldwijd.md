# Open AIS-bronnen wereldwijd — het bronbesluit per regio (M28)

*Onderzocht 2026-07-27 door vier parallelle research-agents (Europa/Scandinavië ·
Canada/Oceanië · Azië · Z-Amerika/Afrika/globaal); alle claims door de agents zelf
geverifieerd met echte requests waar mogelijk. Dit document is de bron voor de
werklijst; details en URL-recepten staan per sectie.*

**De vraag:** waar bestaat een MarineCadastre-equivalent (historische bulk-dumps van
ruwe posities, gratis, liefst zonder registratie)? **Het antwoord in één regel:**
op drie plekken — VS, Denemarken, Australië (+ Noorwegen via API); de rest is óf
zelf verzamelen (live feeds), óf rasters/afgeleiden, óf bestaat niet open.

## Laag 1 — historische bulk (MarineCadastre-klasse) → direct inladen

| bron | dekking | periode | vorm | licentie | registratie |
|---|---|---|---|---|---|
| **MarineCadastre (NOAA/USACE)** ✅ in gebruik | heel VS incl. binnenrivieren + spillover Canada (BC/Vancouver, Canadese Grote Meren, Seaway-grens — empirisch geteld) | 2009→ (kwartaal-achterstand) | dag-CSV.zst ~285 MB | publiek domein | geen |
| **Denemarken — DMA** | Kattegat, Belten, west-Oostzee, Noordzee-DK | **2006→ gisteren** (D+2-3) | dag-CSV in zip ~500 MB, anonieme S3 (path-style!) | "free for download" | **geen** |
| **Australië — AMSA** | hele SAR-regio **mét satelliet-AIS**, Torres Strait | **2012-09 → nu** (maanddumps) | punt-shapefile in zip (→ `ogr2ogr` naar CSV) | **CC BY-NC 3.0 AU** (niet-commercieel — past bij de atlas, attributie in HUD) | geen (POST met ContentItemId) |
| **Noorwegen — Kystdatahuset** | Noorse EEZ + Svalbard | ~2011→ | query-API (bbox+tijd → JSON), anoniem; parquet-bulk (`hais.kystverket.no`) waarschijnlijk maar onbevestigd | NLOD (open) | geen |

Deense S3: `https://s3.eu-central-1.amazonaws.com/aisdata.ais.dk/aisdk-YYYY-MM-DD.zip`
AMSA: `POST https://www.operations.amsa.gov.au/spatial/DataServices/Download` met
`ContentItemId=<id>&TermsAccepted=true` (id's staan als `openDownload(<id>)` in de paginabron).
Noorwegen: `POST https://kystdatahuset.no/ws/api/ais/positions/within-bbox-time`.

## Laag 2 — live feeds → zelf verzamelen (collector-model)

| bron | dekking | opmerking |
|---|---|---|
| **eigen aisstream-collector** ✅ draait | wereld-terrestrisch; dicht in NW-Europa, Japan/Korea, Middellandse-Zeekust deels | ~850 MB/dag; Europa dikt vanzelf aan |
| **Finland — Digitraffic** | Finse kust + **Saimaa-binnenwater** | live REST/MQTT, CC BY 4.0, geen archief → alleen nuttig met eigen poller |
| **Noorwegen — live NMEA** | Noorse EEZ | `153.44.253.27:5631`, NLOD, geen registratie |
| **Donau — EuRIS** (RIS COMEX, 13 landen) | **Rijn+Donau-binnenwater** — de enige route naar het gemeten Donau-onder-gat | API "AisTracks", gratis account + OAuth2; ⚠️ GDPR-clausule — of tracks van derden echt terugkomen is onbevestigd tot we een account testen |
| **Singapore — MPA OCEANS-X** | havenwateren SG (3-min-snapshots) | registratie; alleen live → zelf archiveren |

## Laag 3 — rasters & afgeleiden (geen tracks, wel geometrie/gewichten)

- **Global Fishing Watch** (gratis token, CC BY-NC): *presence*-raster 1 pos/schip/uur,
  **filterbaar op cargo/tanker/tug**, 2012→(−96 u), wereldwijd — China/ZO-Azië sinds
  ~2022 duidelijk beter; *port visits*-API (haven-nodes); per-schip track-CSV's
  (handmatig, steekproef per corridor). Dé aanvulling voor de nul-dekking-corridors.
- **World Bank density** ✅ in build-cache (2015-2021, CC BY) — blijft de fallback
  voor China/Yangtze zoals besloten.
- **IMF PortWatch** (open CSV/GeoJSON, wekelijks): dagelijkse transits voor 28
  chokepoints (Suez/Hormuz/Panama/Malakka…) + portcalls 2.065 havens — edge-gewichten.

## Bestaat niet open (blijft MARNET + density, evt. GFW-raster)

China (ruwe posities structureel dicht — Data Security Law; density/GFW is het legale
maximum) · India · Vietnam · Filipijnen · Indonesië · Thailand · Brazilië-cargo (dus
óók de Amazone; alleen vissers-VMS via GFW) · Argentinië/Paraná · Chili/Peru (alleen
vissers-VMS via GFW — het koperbeen blijft dicht) · Zuid-Afrika · Golf/Suez/Egypte/
VAE/Saoedi/Iran · Nieuw-Zeeland (alleen op aanvraag) · Zweden (te koop, niet open) ·
Duitsland/Polen/Baltische staten (nationale feeds dicht; Oostzee-overlap deels via DK,
historie evt. via een HELCOM-dataverzoek) · Canada-St. Lawrence beneden Montréal.

## Werklijst (volgorde van rendement)

1. **Denemarken inladen** — converter DMA-CSV → collector-JSONL (kolomnamen wijken af
   van NOAA), zelfde `bouw_tracks.py`-pad; 4 weken binnenhalen.
2. **AMSA inladen** — shapefile→CSV-stap (`ogr2ogr`), id→maand-mapping scrapen,
   4 weken; attributie + BY-NC-notitie in de HUD.
3. **EuRIS-account aanmaken en `AisTracks` testen** — beslist of het Donau-gat met
   echte tracks dicht kan; anders blijft Donau-onder op fallback.
4. **GFW-token aanmaken** — presence-raster (cargo/tanker) voor de dichte-deur-regio's
   + port-visits als node-bron; per-corridor een steekproef tracks als validatie.
5. **Noorwegen** — pas relevant bij een corridor daar (Narvik-erts); API staat klaar.
6. Finland/Singapore-pollers: alleen als een stroom erom vraagt.
