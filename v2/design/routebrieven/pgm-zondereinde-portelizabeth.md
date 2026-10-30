# Routebrief (licht) · PGM — Zondereinde (Bushveld) → N1/N9/N10 → Heraeus Port Elizabeth (Zuid-Afrika)

**stroom-id:** `pgm-zondereinde-portelizabeth` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** PGM-filterconcentraat (Pt+Pd+Rh+Au, "4E") van Northam's Zondereinde-mijn/smelter/BMR (noordrand Bushveld, Limpopo) per **truck** (aannemelijk: één bron voor de bestemming) over R510, N4, N1, N9 en N10 naar de Heraeus-raffinaderij in Port Elizabeth (Gqeberha, Oost-Kaap), waar het concentraat wordt toll-geraffineerd. Eén landbeen, geen zee, spoor of lucht.
**Welke as van het verhaal:** *Bushveld → Oost-Kaapkust* — de binnenlandse tak van Northam's toll-raffinage: Northam noemt twee Heraeus-raffinaderijen als bestemming, Hanau (al getekend als `pgm-zondereinde-hanau`, per vlucht) en Port Elizabeth (deze brief, per weg) [1][2]. Volume: Zondereinde 330.769 oz 4E in FY2025 ≈ 10,3 t 4E/j [6]; het aandeel dat naar Port Elizabeth gaat is niet gebrond.

## 1 · Ketenkaart
```
Zondereinde mijn+smelter+BMR `pgm-zondereinde-mijnsmelter` ──(b1 truck · R510 → N4 → N1 → N9 → N10 · hemelsbreed 1.017 km, geen wegkm; indicatie ~1.340 km · aannemelijk: één bron)──►
  Heraeus Port Elizabeth `pgm-heraeus-portelizabeth` — stoppunt (toll-raffinage)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | Zondereinde → Heraeus Port Elizabeth | R510 (Northam–Rustenburg) → N4 (Marikana, Brits, Pretoria-oost) → N1 (Johannesburg, Bloemfontein) → N9 (Colesberg–Middelburg) → N10 (Cradock–Gqeberha) | hemelsbreed 1.017 km, geen wegkm; indicatie ~1.340 km (Johannesburg–PE ~1.060 + 282 km Zondereinde–Pretoria-oost, uit de haalbaarheidstoets, geen bron) | maak_stroombeen_weg (nieuw profiel) | nee |

Geen gedeeld been: de eerste ~280 km volgen dezelfde corridor als b1 van `pgm-zondereinde-hanau` (R510/N4/N1), maar die eindigt bij OR Tambo; hier loopt de lijn na Pretoria door naar Gqeberha. Niet kopiëren, wel hetzelfde profiel-patroon. Proefbake (eigen scratchpad, niet geregistreerd): **1.360,9 km**, +1,6% tegen de indicatie, alle via-snaps ≤ 0,04 km.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-zondereinde-mijnsmelter` | mijn / smelter / BMR (laadplek) | Northam Zondereinde-complex, Thabazimbi LM, Limpopo — **hergebruikt letterlijk uit `pgm-zondereinde-hanau`** | -24.8333, 27.3669 | [8] | bron-gelegd (in die brief z16 gezien: ommuurd industrieterrein met procesgebouwen, schoorsteen en opslagvlakken) |
| `pgm-heraeus-portelizabeth` | raffinaderij (losplek / stoppunt) | Heraeus PGM, Kurland Road, Perseverance, Gqeberha | -33.8421, 25.5589 | [4][5] | bron-gelegd (z15 en z17 gezien: industrieperceel aan Kurland Road met gebouwen en grote zonnepaneelvlakken, met een spoorlijn aan de zuidkant en een doorgaande weg aan de noordkant; geen naambord zichtbaar, alleen de OSM-naam "Heraeus") |

Satellietbeelden: `v2/build-cache/satcheck/sat-pgm-zondereinde-portelizabeth-heraeus.png` (z15) en `…-heraeus-z17.png`.

## 4 · Via-punten (b1, reisvolgorde; elk punt is een OSM-vertex op de genoemde weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | R510 bij Northam (way/1218957980) | -24.9564, 27.2616 | pint de R510 zuidwaarts uit de mijn |
| b1 | 2 | N4 bij Marikana (way/374081795, motorway) | -25.7470, 27.5097 | pint N4 oostwaarts, niet de R104/N14-route langs Krugersdorp |
| b1 | 3 | N4 bij Brits (way/994850525) | -25.6794, 27.8183 | houdt de lijn op de N4 naar Pretoria-oost |
| b1 | 4 | N1 Johannesburg-noord/Buccleuch (way/622909118) | -26.0426, 28.1022 | N1 door Johannesburg zuidwaarts; vervangt het ontwerppunt -26.0380, 28.0980 (0,66 km ernaast, op de M1) |
| b1 | 5 | N1 Bloemfontein-omleiding (way/55761473) | -29.0864, 26.1737 | pint N1 via Bloemfontein tegen N12/N10 via Kimberley en De Aar |
| b1 | 6 | N9 zuid van Colesberg (way/61238686) | -30.7502, 25.0857 | corridorkeuze: N9 Colesberg–Middelburg, niet N1 via Hanover (Hanover ligt 49 km van de lijn) |
| b1 | 7 | N10 noord van Cradock (way/55925589) | -31.9670, 25.4771 | pint N10 via Cradock en Cookhouse, niet N9 via Graaff-Reinet naar Uitenhage |

Geofabrik-regio: `zuid-afrika` (hele been). Refs: R510, N4, N1, N9, N10; vensterKm 40; geen corridorKlassen nodig. Niet in een stad: Colesberg, Cradock en Pretoria zijn bewust niet als punt gebruikt; de lijn raakt Colesberg (N1/N9-knoop) en Cradock (N10) vanzelf.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zondereinde smelter + BMR | Northam | concentraat van eigen mijnen → matte → filterconcentraat | 35 MW, > 1 Moz/j | [1] |
| Heraeus Port Elizabeth | Heraeus PGM SA | filterconcentraat (toll) → geraffineerd PGM | eerste fase geopend feb 2007; capaciteit niet gevonden | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij de Heraeus-vestiging in Port Elizabeth: Northam noemt haar als raffinaderij voor zijn concentraat [1][2]; wat Heraeus daarna met het raffinaat doet (klanten, export) is niet gebrond, dus fase D/E vervallen.

## 7 · Open punten
- **Aandeel Port Elizabeth niet gebrond:** de bronnen zeggen "verzonden naar Hanau en Port Elizabeth" zonder verdeling [1][2]; vervoer per truck is aannemelijk (geen luchthaven in beeld, 1.017 km hemelsbreed), maar geen bron noemt de modaliteit.
- **Adres alleen via OSM:** één OSM-way (aeroway=helipad, naam "Heraeus", Kurland Road, Perseverance, way/1224384664) markeert de vestiging [4]; de Heraeus-locatiepagina noemt geen Zuid-Afrikaans adres [10], en een zoekactie vond geen straatadres. Gezien op satelliet: een industrieperceel, geen bord. Status "bron-gelegd" met die beperking.
- **Wegkilometer:** hemelsbreed 1.017 km, geen wegkm; de 1.340 km-indicatie komt uit de haalbaarheidstoets en is zelf geen gepubliceerde bronlengte. De ±15%-toets geldt als indicatie.
- **Volume:** 330.769 oz 4E is Zondereinde totaal (eigen raffinaat-equivalent, FY2025, trading-update vóór de jaarresultaten) [6]; mix Pt/Pd/Rh/Au niet gegeven.
- Heraeus' 20-jarig akkoord (2015) is oud; of Port Elizabeth nu nog evenveel ontvangt (Johnson Matthey erbij) is niet nagegaan [2].
- Locatie volgens het ontwerp: LPPM noemt Heraeus PGM SA als erkende raffinadeur; die lijst is niet zelf geopend.

## 8 · Bronnen
[1] Northam Platinum, "Metallurgical operations": finaal concentraat klaar voor verzending naar de Heraeus-raffinaderijen in Hanau (Duitsland) en Port Elizabeth (Zuid-Afrika) en naar Johnson Matthey (VK). https://www.northam.co.za/about-northam/metallurgical-operations
[2] Mining-technology, 2015-10-25, "Heraeus and Northam Platinum sign agreement to extend partnership": 20-jarig akkoord, concentraat naar Port Elizabeth en Hanau, Heraeus koopt tot 40% van het raffinaat. https://www.mining-technology.com/news/newsheraeus-and-northam-platinum-sign-agreement-to-extend-partnership-4701106/
[3] Freight News, 2007-02-23, "New PE refinery boosts catalytic industry": Heraeus-raffinaderij in Port Elizabeth, in het hart van de Zuid-Afrikaanse autokatalysatorindustrie (geen straatadres). https://www.freightnews.co.za/article/new-pe-refinery-boosts-catalytic-industry
[4] OpenStreetMap (Nominatim, geopend 2026-10-30): way/1224384664 "Heraeus", aeroway=helipad, Kurland Road, Perseverance, Nelson Mandela Bay, -33.84207, 25.55885. https://nominatim.openstreetmap.org/
[5] Esri World Imagery via `v2/tools/sat_check.py` (z15, z17, live): `v2/build-cache/satcheck/sat-pgm-zondereinde-portelizabeth-heraeus.png`, `…-heraeus-z17.png`.
[6] Northam Platinum, voluntary production update 2025-07-23 (SENS): Zondereinde 330.769 oz 4E equivalent refined metal in FY2025 (FY2024 328.513). https://sharedata.co.za/sens.asp?id=519808
[7] OpenStreetMap via Geofabrik `zuid-afrika-latest.osm.pbf` en `v2/tools/wegscan_puur.py` (proefprofiel in scratchpad): way-id's en refs van de via-punten in §4; routelengte 1.360,9 km.
[8] Routebrief `pgm-zondereinde-hanau` (2026-09-28): anker `pgm-zondereinde-mijnsmelter` en corridor R510/N4/N1. v2/design/routebrieven/pgm-zondereinde-hanau.md
[9] OpenStreetMap (Nominatim): Colesberg -30.7211, 25.0967; Cradock -32.1644, 25.6208; Hanover -31.0675, 24.4436; Middelburg (EC) -31.4939, 25.0067 (alleen gebruikt om de corridorkeuze in §4 te toetsen). https://nominatim.openstreetmap.org/
[10] Heraeus Precious Metals, locatiepagina Zuid-Afrika (geopend, geen adres of activiteit voor Port Elizabeth genoemd). https://www.heraeus-precious-metals.com/en/lp/locations/south-africa/

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)

**Stroom `pgm-zondereinde-portelizabeth`** → `v2/data/stroomroute-pgm-zondereinde-portelizabeth.json` — 1 been (truck, fase C), **1.361,2 km**, 11.300 punten, 2 markers, 230,0 KB. Geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie. Naden: n.v.t. (één been). Recept: `bak_stromen.sh` functie `bak_pgm_zondereinde_portelizabeth`; nieuw wegprofiel `pgm-zondereinde-portelizabeth-zondereinde-portelizabeth` in `maak_stroombeen_weg.py` (extract `zuid-afrika`, refs R510/N4/N1/N9/N10, vensterKm 40, 7 via-punten uit §4 in reisvolgorde, gepubliceerdKm 1340 als indicatie).

**b1 (truck, `wegscan_puur.py`, doorgetrokken):** geroute **1.360,9 km** (getekende lijn 1.361,2 km incl. ankerstukjes 0,28 km plant → weg en 0,04 km weg → kade, beide OK) tegen de indicatie ~1.340 km = **+1,6%** (de brief geeft geen echte wegkm: hemelsbreed 1.017 km, dus de ±15%-toets is indicatie, geen norm). Alle via-snaps 0,00-0,04 km; segmenten: 22,1 / 121,4 / 32,6 / 101,4 / 419,7 / 230,5 / 160,9 / 272,3 km. First mile 8,65 km, last mile 0,46 km over kleine wegklassen; geen `eindToegangPrivaat` nodig. 17 keerlussen gesnoeid (lengte ongewijzigd). Identiek aan de proefbake uit de brief.

**Markers (2):** `pgm-zondereinde-mijnsmelter` (-24.8333, 27.3669, letterlijk hergebruikt uit `pgm-zondereinde-hanau`) en `pgm-heraeus-portelizabeth` (-33.8421, 25.5589); beide 0,00 km van de lijn. De Heraeus-markernaam draagt "aannemelijk: één bron"; de beennaam ook.

**Toetsen:** `toets_rechte_benen --min-km 5`: geen melding voor deze stroom. `toets_knikken`: 19 knikken, bijna allemaal korte spikes (6-184 m straal) op complexe aansluitingen en bij de kade; **1 TERUGLOOP** (174,5 graden, 76 m, -25.63396, 28.27601): de route rijdt bij het N4/N1-knooppunt oost van Pretoria (Derdepoort) ~0,35 km over de noordwaartse N1-rijbaan en keert via de zuidwaartse rijbaan terug (U-draai op een aansluiting, ~0,7 km extra). Dat is wegtopologie van OSM, niet door een via-punt veroorzaakt (de dichtstbijzijnde via-punten zijn Brits en Buccleuch) en niet gerepareerd: de lengtetoets haalt het en 0,7 km is op bolschaal onzichtbaar. `json.load`: versie 2, punt_formaat lonlat, modaliteit {truck}, 11.300 punten.

**Lessen / open:** (1) aandeel Port Elizabeth, modaliteit, Heraeus-adres (alleen OSM-helipad-way), huidige verdeling met Johnson Matthey en volume-mix blijven open (§7). (2) Het U-draai-stukje bij Derdepoort is niet nagegaan voor andere stromen met de N4 -> N1-corridor (bv. `pgm-zondereinde-hanau` b1). (3) `wegscan_puur.py` nodig omdat pyosmium geblokkeerd is; ~3 min scan op `zuid-afrika`.
