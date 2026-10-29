# Routebrief (licht) · PGM — Mogalakwena via de Polokwane-smelter naar ACP Rustenburg (Zuid-Afrika)

**stroom-id:** `pgm-mogalakwena-rustenburg` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat van de Mogalakwena-concentrator (Valterra, Mokopane, Limpopo) per **truck** over de N11
en de N1 naar de **Valterra Polokwane-smelter** [1][3][4]; de matte per **truck** (aannemelijk: modaliteit niet in de bron)
via de R37/N1-aansluiting en de N1/N4 naar het **Anglo Converter Plant (ACP)** in het Waterval-complex bij Rustenburg [2] —
zelfde eindanker als `pgm-rustenburg-pmr`. Stoppunt.
**Welke as van het verhaal:** de grootste PGM-mijn ter wereld (open pit, Noordelijke rand) levert 80-90% van de voeding van
de Polokwane-smelter [4] en is daarmee de dikste concentraatstroom naar de Rustenburg-converting. ~29,5 t PGM/j (zie §7).

## 1 · Ketenkaart
```
Mogalakwena-concentrator `pgm-mogalakwena-mijn` ──(b1 truck · N11 → N1 Mokopane–Polokwane · hemelsbreed 56 km, geen wegkm,
  eigen OSM-scan ~96 km)──► Polokwane-smelter `pgm-polokwane-smelter`
  ──(b2 truck · R37 noord · 13,0 km gebakken, LETTERLIJKE KOPIE pgm-modikwa-rustenburg b2a, aannemelijk)──► R37/N1-aansluiting
  ──(b3 truck · N1 → N4 · 359,9 km, LETTERLIJKE KOPIE pgm-modikwa-rustenburg b2b, aannemelijk)──►
  Rustenburg ACP/PMR `pgm-rustenburg-pmr` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-mogalakwena-mijn` → `pgm-polokwane-smelter` | N11 (mijn → Mokopane) → N1 Mokopane–Polokwane → R37 (smelter) | hemelsbreed 56 km, geen wegkm; indicatie ~96 km (eigen OSM-scan [7]; mijn "54 km W van Polokwane" [3]) | maak_stroombeen_weg (nieuw profiel) | nee |
| b2 | B | truck | `pgm-polokwane-smelter` → R37/N1-aansluiting (-23.9431, 29.4439) | R37 noord (aannemelijk: één bron) | 13,0 gebakken (kopie) [10] | kopie geojson, geen nieuw bestand | nee |
| b3 | C | truck | R37/N1-aansluiting → `pgm-rustenburg-pmr` | N1 Polokwane–Pretoria → N4 (aannemelijk: één bron) | 359,9 gebakken (kopie) [10] | kopie geojson, geen nieuw bestand | nee |

Geen zee-, spoor-, binnenvaart-, leiding- of luchtbeen; geen haven-aanloop; geen fase D/E (geen bron noemt een afnemer ná ACP).
**Terugloop is echte logistiek:** b1 rijdt de N1 Mokopane → Polokwane (~52 km) en de R37 (~11 km) heen, b3 en b2 rijden die
corridor terug (concentraat gaat naar de oven, matte keert terug naar het ACP); de lijnen vallen over ~65 km op elkaar.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-mogalakwena-mijn` | mijn + concentrator | Mogalakwena-concentrator, Valterra, Mokopane, Limpopo — **hergebruikt letterlijk** uit `pgm-mogalakwena-londen.md` (= sitelaag `w-mogalakwena`) | -23.9805, 28.9160 | [3][8][9][12] | bron-gelegd (z15 hier opnieuw gezien: ertsverwerkingscomplex met conveyors en silo's tussen twee tailingsdammen, open pits W en ZW) |
| `pgm-polokwane-smelter` | smelter (elektrische oven) | Valterra Polokwane-smelter, OSM way 804571574 — **hergebruikt letterlijk** uit `pgm-modikwa-rustenburg.md` | -24.0281, 29.4694 | [1][2][10] | bron-gelegd (z15 hier opnieuw gezien: ovengebouw met schoorstenen, donkere slakdam ZW, R37 op ~1,3 km westelijk) |
| `pgm-rustenburg-pmr` | losplek / converting (ACP) | Waterval-complex, Valterra, Rustenburg — **hergebruikt letterlijk** uit `pgm-unki-rustenburg.md` | -25.6838, 27.3272 | [2][11] | bron-gelegd (overgenomen; z15 gezien bij die brief) |

## 4 · Via-punten (alleen b1; lat, lon; alle op de weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | N11 bij de D3525-aansluiting (optioneel) | -24.0157, 28.9729 | op de N11 (0,0 km snap); pint de N11 naar Mokopane i.p.v. zijwegen langs de mijn. Valt de route toch door het centrum van Mokopane (lat -24.18, lon 29.01), dan dit punt laten staan en het volgende bijsturen |
| b1 | 2 | N1 oost van Mokopane | -24.1673, 29.0899 | op de N1 (0,0 km); N1 Polokwane-richting i.p.v. de R518/R101 het stadje in |
| b1 | 3 | N1 | -24.0765, 29.2051 | op de N1 (0,0 km); houdt de autoweg vast, R101 ligt 3 km ernaast |
| b1 | 4 | N1 | -24.0030, 29.3245 | op de N1 (0,01 km); R101 loopt 0,8 km parallel, de N1 is de truckroute |
| b1 | 5 | R37/N1-aansluiting Polokwane-zuid | -23.9431, 29.4439 | gelijk aan het eindpunt van b2 (naad 0); op de N1-aansluiting (0,0 km) |

Punten 2-5 komen uit de haalbaarheidstoets en zijn hier nagemeten tegen de OSM-extract (alle op `highway=motorway ref=N1`).
b1 eindigt via de R37 (~11 km, refs R37) op de smelter-ankers. Refs voor het profiel: N1, R37 (N11 zacht mee). Venster 40 km.
Geofabrik-regio: `zuid-afrika` (alle benen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mogalakwena-concentrator | Valterra Platinum | open-pit erts → PGM-concentraat | ~948 koz PGM (2025) | [5] |
| Polokwane-smelter | Valterra Platinum | concentraat (80-90% Mogalakwena) → ovenmatte; zes-in-lijn-oven + SO2-installatie | niet in t/j gepubliceerd | [2][4] |
| Anglo Converter Plant (Waterval) | Valterra Platinum | ovenmatte → converter-matte | niet in t/j gepubliceerd | [2] |

## 6 · Stoppunt
De brief stopt bij ACP Rustenburg (Waterval-complex, zelfde anker als de PMR): geen bron noemt een gedocumenteerde volgende
locatie of vervoerswijze voor de converter-matte.

## 7 · Open punten
- **Wegkm niet gepubliceerd.** b1: hemelsbreed 56 km, geen wegkm. Indicatie ~96 km = som van een eigen OSM-routering over de
  via-punten (38,9 + 15,8 + 15,1 + 14,9 + 11,4 km; zuid-afrika-extract, 2026-10-29) [7]; een directe D-wegen-route zou ~81 km zijn
  maar is niet de truckroute. De ±15%-toets is een indicatie, geen norm.
- **Koppeling Mogalakwena → Polokwane** rust op secundaire bronnen: Valterra-verklaring in Engineering News/Mining Weekly
  (80-90% van de Polokwane-voeding, 21% minder trucks) [4] en een mijndatabase [3]; de Valterra-site noemt de koppeling niet [1].
- **Aandeel via Polokwane:** geen bron zegt dat alle Mogalakwena-concentraat naar Polokwane gaat; hier aangenomen (een
  tweede smelter noemt geen bron).
- **Matte-modaliteit** Polokwane → ACP staat niet in de bron ("transported", [2]); truck is aanname — daarom "aannemelijk".
- **Bestaande `pgm-mogalakwena-londen` b1** loopt direct mijn → Rustenburg (N1/R24, 336,7 km) en slaat Polokwane over; die
  schakel is dus twijfelachtig naast deze brief. Niet gewijzigd, hier gemeld.
- **Volume:** Valterra Q4 2025 productierapport: Mogalakwena ~948 koz in 2025, basis niet gespecificeerd (via zoekresultaat; 6E/PGM)
  = 29,5 t/j (÷ 32,15) [5]; 2023 ~1.090 koz 4E = 33,9 t (sitelaag [12]); eigen brief londen 900 koz 3E = 28 t. Mix niet eenduidig.
- **Overlap:** b2 en b3 zijn 100% gedeeld met `pgm-modikwa-rustenburg` en `pgm-mototolo-rustenburg` (373 km van ~470); alleen b1 is nieuw.
  Eerste ~31 km van b1 delen de mijn-Mokopane-corridor met `pgm-mogalakwena-londen` b1.
- **R37/N1-aansluiting (-23.9431, 29.4439)** is geen anker maar een naad; het N1-stuk Mokopane–Polokwane noemt Wikipedia niet in km [6].

## 8 · Bronnen
[1] Valterra Platinum, Processing operations (Polokwane = primair smelter; converter plant Rustenburg), https://www.valterraplatinum.com/mine-to-market/processing-operations/
[2] SAIMM, Snodgrass e.a., Pyrometallurgy 2024 (concentraat per truck naar de smelters; ovenmatte naar het ACP), https://www.saimm.co.za/Conferences/files/pyrometallurgy-2024/16_646-Snodgrass.pdf
[3] Mining Data Online, Mogalakwena Mine (54 km W van Polokwane; concentraat naar de Polokwane-smelter; 4E-tabel 2015-2019), https://miningdataonline.com/property/731/Mogalakwena-Mine.aspx
[4] Engineering News / Mining Weekly, Jameson cells (2026-02-26 en 2026-09-23/10-09; 80-90% van de Polokwane-voeding uit Mogalakwena, minder trucks; via zoekresultaat, pagina's 403), https://www.engineeringnews.co.za/article/jameson-cells-ringing-efficiency-bells-at-valterra-platinum-2026-02-26
[5] Valterra Platinum, Q4 2025 production report (Mogalakwena ~948 koz; via zoekresultaat, pdf 404 bij ophalen), https://www.valterraplatinum.com/~/media/Files/V/Valterra-Platinum/Platinum/press-releases/2025/q4-production-report-2025.pdf
[6] Wikipedia, N1 road (South Africa) (Polokwane Eastern Bypass; N11 raakt de N1 bij Mokopane), https://en.wikipedia.org/wiki/N1_road_(South_Africa)
[7] Eigen OSM-wegscan (Geofabrik zuid-afrika, `wegscan_puur.scan`, bb 28,8-29,6 E / -24,35 tot -23,8; 2026-10-29): via-punten 2-5 op N1 motorway, mijn → N1 38,9 km via N11/D1603/D1231/R101
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-pgm-mogalakwena-rustenburg-mijn.png`, `…-polokwane-smelter.png`
[9] `v2/design/routebrieven/pgm-mogalakwena-londen.md` (anker `pgm-mogalakwena-mijn`, z16 bron-gelegd; b1 N1/R24)
[10] `v2/design/routebrieven/pgm-modikwa-rustenburg.md` (anker `pgm-polokwane-smelter`; b2a/b2b geojson `pgm-modikwa-rustenburg-weg-smelter-r37n1.geojson`, `…-weg-polokwane-rustenburg.geojson`); zelfde kopie in `pgm-mototolo-rustenburg`
[11] `v2/design/routebrieven/pgm-unki-rustenburg.md` (anker `pgm-rustenburg-pmr`)
[12] `v2/design/pgm-sitelaag.json` w-mogalakwena (-23.9805, 28.916; 33,9 t 4E)
[13] Engineering News (2026-10-02), Mogalakwena: 900.000-1 miljoen oz 6E-doel per jaar (via zoekresultaat), https://www.engineeringnews.co.za/print-version/exciting-mogalakwena-mine-has-300-year-plus-resource-life-valterra-platinum-2026-10-02

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
`bash v2/tools/bak_stromen.sh pgm-mogalakwena-rustenburg` -> `v2/data/stroomroute-pgm-mogalakwena-rustenburg.json` (65,1 KB, contract versie 2, lonlat, 3 benen, 3 markers, totaal 471,7 km, 3.142 punten).

| # | modaliteit | km | naad naar vorig been | geometrie |
|---|---|---|---|---|
| b1 | truck | 98,8 | - | NIEUW: profiel `pgm-mogalakwena-rustenburg-mogalakwena-polokwane` (zuid-afrika, wegscan_puur, 1.011 punten) |
| b2 | truck | 13,0 | 0,000 | LETTERLIJKE KOPIE `pgm-modikwa-rustenburg-weg-smelter-r37n1.geojson` (aannemelijk) |
| b3 | truck | 359,9 | 0,000 | LETTERLIJKE KOPIE `pgm-modikwa-rustenburg-weg-polokwane-rustenburg.geojson` (aannemelijk) |

**Toets.** b1 98,4 km (lijn 98,8) tegen de indicatie ~96 km uit de brief = +2,5% (geen gepubliceerde wegkm, dus indicatie, geen norm; hemelsbreed 56 km). Snaps van alle via-punten 0,00-0,15 km, smelter-anker 0,28 km. Naden 0 km. Markers 0,0 km van de lijn. Geen stippel, geen haven-aanloop, geen vlucht, geen leiding. `toets_knikken`: b1 13 knikken (spikes op kleine radii, 0 omkeringen); de omkering en de terugloop (-25.70456, 27.25575) zitten in de gekopieerde b2/b3 en zijn niet van deze stroom.

**Via-punten.** Alle vijf uit §4 gebruikt, geen verplaatst. Punt 5 (R37/N1-aansluiting) is ook het eindpunt van b2 (naad 0).

**Bevinding Mokopane.** De lijn volgt N11 en R518 naar Mokopane en gaat via de R101 dwars door het centrum (0,04 km van -24.18, 29.01) naar het N1-knooppunt; in OSM is dat de verbinding tussen N11 en N1. Niet bijgestuurd: een bypass-via-punt zou een gok zijn. Dit stuk (~8 km) is voor een eventuele verfijning.

**Terugloop.** b1 rijdt de N1 Mokopane-Polokwane en de R37 heen; b3 en b2 rijden die corridor terug (~65 km op elkaar), echte logistiek zoals in de ketenkaart.

**Lessen.** (1) Wegscan zuid-afrika 207 s, daarna cache. (2) De N11 loopt in OSM door Mokopane-centrum: via-punt 1 pint de N11 maar voorkomt de stadsdoorsnede niet. (3) Register en bundel niet aangeraakt (centraal).
