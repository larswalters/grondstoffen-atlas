# Routebrief (licht) · zilver — Buenavista → La Caridad (Mexico)

**stroom-id:** `zilver-buenavista-lacaridad` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** zilverhoudend koperconcentraat van de Buenavista-concentrators (Southern Copper, Cananea, Sonora) per **truck** (aannemelijk: één bron, SCC zegt "rail and truck"; spoor is geen optie, OSM-spoor stopt voor Nacozari) over SON 89 en de Bacoachi–Fronteras-weg naar MEX 17 en de La Caridad-smelter/edelmetaalraffinaderij bij Nacozari — één landbeen, geen zee, stoppunt = de raffinaderij.
**Welke as van het verhaal:** Mexicaanse zilverbijproductie: het zilver zit in het koperconcentraat en komt als edelmetaalslik uit de koperraffinage; La Caridad raffineert **262,3 t Ag/j** (2025; 246,6 in 2024) [1]. Het aandeel van Buenavista daarin is niet gepubliceerd (de smelter neemt ca. 40,5% van het OMIMSA-concentraat van Buenavista [1]); de eigen La Caridad-molen is de grootste bron en staat niet in deze keten (§7).

## 1 · Ketenkaart
```
Buenavista-concentrators `ag-buenavista-kop` ──(b1 truck · SON 89 → Bacoachi → MEX 17 · OSM-pad 125,5 km, hemelsbreed 84 km)──►
La Caridad-smelter + edelmetaalraffinaderij `ag-lacaridad-smelter` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ag-buenavista-kop` → `ag-lacaridad-smelter` | Cananea → SON 89 (Cananea–Arizpe) → Bacoachi-oost → secundaire weg naar MEX 17 → MEX 17 zuidwaarts → smeltertoegang [1][4][6] | hemelsbreed 84 km, geen wegkm; OSM-pad 125,5 km (geschreven met `maak_stroombeen_weg`, snaps ≤ 0,09 km); alternatief via MEX 2 → Agua Prieta → MEX 17 ca. 190 km (eigen OSM-graaf) — de ±15%-toets is een indicatie, geen norm | maak_stroombeen_weg (extract mexico) | nee; first mile 4,6 km en last mile 5,3 km over kleine klassen zijn onderdeel van de lijn |

Beennaam voor de bak: `truck (aannemelijk: één bron: SCC 10-K zegt rail en truck) Buenavista-concentrators → SON 89 → Bacoachi → MEX 17 → La Caridad-smelter`. Geen zeebeen, geen haven-aanloop, geen stippel, geen kopie.
**Corridorkeuze (vastgelegd):** de smalste verharde route via SON 89 en Bacoachi (125,5 km), niet de kust-/grensroute via Agua Prieta (ca. 190 km). Reden: het 10-K noemt verharde wegen van Buenavista naar Nacozari in het zuidoosten (en een aparte naar Agua Prieta) [1]; OSM kent precies één kortere doorgaande verbinding, de oostelijke weg ten zuiden van Bacoachi [4]. Welke van de twee de trucks werkelijk nemen is niet gebrond (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-buenavista-kop` | mijn/concentrator (laad) | Buenavista del Cobre, concentrators + verdikkers, Cananea | 30.9722, -110.3140 | [1][8] | bron-gelegd — letterlijk hergebruikt uit `koper-buenavista-guaymas.md` §3 (z15 gezien daar: concentratorcomplex met ronde verdikkers) |
| `ag-lacaridad-smelter` | smelter + edelmetaalraffinaderij (los, stoppunt) | La Caridad, Fundición Mina La Caridad (OSM way 193506161), Nacozari | 30.4941, -109.6355 | [1][6][7] | bron-gelegd (z14 en z15 gezien: langwerpig, noord-zuid gelegen smelter-/raffinaderijcomplex met schoorstenen en procesgebouwen, spooremplacement, donkere slakkenhoop ten O en een stuwmeer ten ZO; de landingsbaan van 2,5 km ligt 1,5 km ten W; het kruis ligt midden op het complex) |

## 4 · Via-punten (b1: corridorkeuze SON 89 tegenover MEX 2 / Agua Prieta)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | V1 | SON 89 ten ZO van Cananea, 34 km | 30.8645, -110.0749 | op de doorgaande SON 89; pint de keuze bij Cananea: zuidoost (SON 89) in plaats van oost (MEX 2 naar Agua Prieta) [4] |
| b1 | V2 | secundaire weg Bacoachi → MEX 17, 17 km ten O van Bacoachi | 30.6455, -109.8070 | op de oostelijke weg buiten het dorp (niet in Bacoachi zelf); pint de oversteek van SON 89 naar de MEX 17-aansluiting [4] |
| b1 | V3 | MEX 17 bij de aansluiting | 30.6363, -109.6151 | op MEX 17 (primary) ten noorden van Nacozari; pint het zuidwaartse stuk MEX 17 naar de smeltertoegang [4] |
Runs: kop→V1 33,9 km · V1→V2 51,3 · V2→V3 20,9 · V3→smelter 19,5 = **125,5 km** (snap van alle via-punten ≤ 0,04 km, staart 0,09 km). Refs voor het profiel: `MEX 17`, `SON 89`. Extract: `mexico`; `vensterKm` 40.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Buenavista-concentrators | Southern Copper | sulfide-erts → koperconcentraat ca. 24% Cu (met zilver) | niet per zilver gepubliceerd | [1] |
| La Caridad-smelter + edelmetaalraffinaderij | Southern Copper | concentraat Buenavista, Santa Barbara, Charcas, La Caridad → anodes → kathode + zilver/goud | smelter 1,0 Mt/j; **zilver 262,3 t (2025)**, goud 914 kg (2025) | [1] |

## 6 · Stoppunt
De brief stopt bij de La Caridad-raffinaderij: het 10-K noemt geen afnemer of exportroute van het geraffineerde zilver — fase D en E vervallen. Eén landbeen is bewust de hele keten; het ontwerp zegt zelf "dun als alleen dit been".

## 7 · Open punten
- **Modaliteit niet gebrond:** het 10-K zegt "rail and truck" voor concentraat naar de smelter [1]; gekozen is truck omdat OSM-spoor ca. 14 km voor Nacozari stopt (haalbaarheidstoets). Het aandeel per modaliteit is onbekend.
- **Corridor niet bevestigd door een bron:** de gekozen route (125,5 km) volgt OSM; de bedrijfsroute kan via Agua Prieta lopen (ca. 190 km). De Bacoachi–MEX 17-verbinding heeft in OSM geen ref en geen surface-tag; "verhard" is dus een afleiding uit de wegklasse (secondary) plus het 10-K [1][4].
- **Aandeel Buenavista in het zilver is onbekend:** de smelter neemt ca. 40,5% van het OMIMSA-concentraat van Buenavista [1], maar de grootste zilverbron is de eigen La Caridad-molen (niet in de keten), plus Santa Barbara, Charcas en IMMSA. Het jaarvolume 262,3 t is het totaal van de raffinaderij, niet de lading van dit been.
- **Kop gedeeld met `koper-buenavista-guaymas`:** zelfde ankerpunt, andere bestemming; geen lijnoverlap (hun spoor gaat naar Nogales/Guaymas). Een deel van de lading kan naar Guaymas gaan.
- **Afstandsclaim 10-K:** "airstrip 36 km north of Nacozari, less than one kilometer from the smelter" [1] klopt niet met de gemeten 13 km (smelter 30.4941 tegen Nacozari 30.3833); het complex zelf is op de satelliet en in OSM eenduidig.
- Geen sitelaag voor zilver bij La Caridad of Buenavista; centraal beslissen of de coördinaten worden toegevoegd.

## 8 · Bronnen
[1] Southern Copper Corp, Form 10-K FY2025 (La Caridad: smelter en raffinaderij 24 km van de mijn; "transported by rail and truck"; ca. 40,5% OMIMSA-concentraat Buenavista; raffinaderij zilver 262,3/246,6/230,1 duizend kg 2025/24/23; Buenavista verbonden met Agua Prieta, Nacozari, Imuris). https://www.sec.gov/Archives/edgar/data/1001838/000110465926021492/scco-20251231x10k.htm
[2] Wikipedia, "Mexican Federal Highway 17" (Agua Prieta–Moctezuma, 169 km). https://en.wikipedia.org/wiki/Mexican_Federal_Highway_17
[3] Wikipedia, "Nacozari de García" (Fed. 17; afstand Agua Prieta 123 km; coördinaat 30.3833, -109.6833). https://en.wikipedia.org/wiki/Nacozari_de_Garc%C3%ADa
[4] OpenStreetMap (ODbL), Geofabrik-extract Mexico, eigen pbf-scan en `maak_stroombeen_weg` (wegscan_puur): MEX 2 Cananea–Agua Prieta, MEX 17 Agua Prieta–Nacozari, SON 89 Mazocahui–Arizpe–Cananea, secundaire weg Bacoachi–MEX 17; geschreven geojson `v2/build-cache/ais/graaf/zilver-buenavista-lacaridad-weg-buenavista-lacaridad.geojson` (125,5 km, 2.433 punten).
[5] Wikipedia, "Fronteras, Sonora" (30.8961, -109.5583) en "Naco, Sonora" (31.3269, -109.9478) — ligging van de alternatieve corridor. https://en.wikipedia.org/wiki/Fronteras
[6] OpenStreetMap, way 193506161 "Fundición Mina La Caridad" 30.4941, -109.6355 (door de haalbaarheidstoets aangeleverd en op de satelliet bevestigd).
[7] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-zilver-buenavista-lacaridad-smelter.png` (z14) en `…-smelter15.png` (z15).
[8] `v2/design/routebrieven/koper-buenavista-guaymas.md` §3 (anker `cu-buenavista-kop`, satelliet-gelegd) en `sat-koper-buenavista-guaymas-kop.png`.
[9] Wikipedia, "Bacoachi" (gemeente grenst aan Cananea, Fronteras, Nacozari, Naco, Arizpe — plausibiliteit van de SON 89-route). https://en.wikipedia.org/wiki/Bacoachi
[10] Haalbaarheidstoets keten `zilver-buenavista-lacaridad` (orkestrator, 2026-10-09): OSM Overpass MEX 17 primary tot 4 km west van de smelter; OSM-spoor stopt ca. 14 km voor Nacozari.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-zilver-buenavista-lacaridad.json` (52,6 KB, contract versie 2, lonlat). **Recept:** `bash v2/tools/bak_stromen.sh zilver-buenavista-lacaridad` (functie `bak_zilver_buenavista_lacaridad`); profiel `zilver-buenavista-lacaridad-buenavista-lacaridad` in `maak_stroombeen_weg.py`, scan via `wegscan_puur.py` (extract mexico, 290 s, pbf-cache nieuw omdat het profiel-hash anders was dan het concept-scratchprofiel).
| # | modaliteit | been | km | punten | naad |
|---|---|---|---|---|---|
| b1 | truck | Buenavista-concentrators → SON 89 → Bacoachi → MEX 17 → La Caridad-smelter (aannemelijk: één bron: SCC 10-K zegt rail en truck) | 125,7 | 2.433 | n.v.t. |
**Markers (2):** `ag-buenavista-kop` (30.9722, -110.3140) en `ag-lacaridad-smelter` (30.4941, -109.6355), beide 0,0 km van de lijn.
**Toets:** km 125,7 tegen OSM-pad 125,5 uit de brief (+0,2%); er is geen gepubliceerde wegkm (hemelsbreed 84 km), dus de ±15%-toets is een indicatie. Snaps: via-punten 0,00-0,04 km, staart 0,09 km, kop 0,04 km. Eén been, dus geen naden. `toets_knikken`: 11 knikken ≥ 60 gr (alle met straal 3-26 m op de first/last mile en de MEX 17-aansluiting, spike-klasse), 0 omkeringen, 0 terugloop. `toets_rechte_benen --min-km 5`: dit been staat er niet in (omwegfactor > 1). `json.load` ok: versie 2, punt_formaat lonlat, modaliteit truck, 2.433 punten.
**Stippel / haven-aanloop / vlucht / leiding:** geen. Geen zeebeen (dus geen zeeknoop of aanloop), geen kopie, geen stippel; first mile 4,6 km en last mile 5,3 km over kleine klassen zijn onderdeel van de doorgetrokken lijn.
**Lessen:** (1) de scratch-geojson uit de concept-fase bleek reproduceerbaar: dezelfde 125,5 km en 2.433 punten, ook nu met een officieel profiel. (2) Corridor en modaliteit blijven aannemelijk (één bron, OSM-routering); de bedrijfsroute kan via Agua Prieta (ca. 190 km) lopen. (3) Een Bacoachi-MEX 17-verbinding zonder ref/surface in OSM is een afleiding, geen waarneming. (4) Zilver heeft geen sitelaagpunt voor Buenavista of La Caridad; de gloed leunt dus alleen op de twee stroommarkers tot dat centraal wordt besloten.
**Register (centraal):** `{ sleutel: "ag-bl", bestand: "stroomroute-zilver-buenavista-lacaridad.json", grondstof: "zilver", label: "Buenavista → La Caridad", aan: true, noot: "M31 · golf 9 (2026-10-09): ..." }`.

