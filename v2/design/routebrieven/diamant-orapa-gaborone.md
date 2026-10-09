# Routebrief (licht) · Diamant · Orapa → Gaborone (Botswana)

**stroom-id:** `diamant-orapa-gaborone` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** ruwe diamant van de Debswana-mijn Orapa (Central District, Botswana) gaat in één wegbeen
(A30 → A14 → A1, ~529 wegkm) naar de DTCB/DBGSS-campus in Gaborone, waar De Beers sorteert, waardeert en verkoopt
(hergebruikt anker uit `diamant-gaborone-surat.md`). Eenbeensketen; de vervoerswijze is niet gebrond (zie §7).
**Welke as van het verhaal:** Botswana-binnenland: de tweede Debswana-mijn naar de sorteer- en verkoopknoop, naast
het bestaande `diamant-jwaneng-antwerpen` — Orapa 9,02 Mct in 2023 [9]; ~10,8 Mct/j volgens Wikipedia [4]; 2012 circa
11 Mct bij een capaciteit van bijna 20 Mct [3]. Waarde per karaat laag tot middel (volume-mijn, mix edelsteen/near-gem).

## BINDENDE aanpassing op het ketenontwerp (haalbaarheidstoets [2])
Truck blijft; het been is **aannemelijk: één bron** (alleen de bestemming Gaborone is gebrond [3][8], de wijze niet).
Geen vlucht ORP → GBE zonder vrachtbron. Het mijnanker snapt 0,57 km van de weg: bevinding in §7, geen via-punt
bijschuiven. Profiel (lon, lat), extract botswana, refs A14, A1, A30, gepubliceerdKm 529, vensterKm 40.

## 1 · Ketenkaart
```
Orapa-mijn `dia-orapa-mine` ──(b1 truck · A30 → A14 → A1 · ~529 wegkm, aannemelijk: één bron)──►
DTCB/DBGSS-campus Gaborone `dia-gaborone-dtc` (hergebruikt anker) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Orapa-mijn → DTCB/DBGSS-campus Gaborone | A30 (~6 km) → A14 (Orapa–Palapye, ~248 km [5]) → A1 (Palapye–Mahalapye–Gaborone) | 529,1 wegkm (rome2rio, aggregator, geen overheidsopgave) [6]; eigen OSM-route 525,0 km (−0,8%) [12]; hemelsbreed 368,7 | maak_stroombeen_weg | nee — doorgetrokken |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-orapa-mine` | mijn (kop) | Orapa-mijn, Debswana (sitelaag `w-orapa`, hergebruikt) | -21.3083, 25.3694 | [4][9][13] | bron-gelegd (z14 gezien: kruis midden in de ovale hoofdput met groenig water, tailingsvelden rondom, Orapa-dorp ~3 km zuid, Orapa Airport-baan ~7 km WNW) |
| `dia-gaborone-dtc` | sorteer-/verkoopknoop (eind) | DTCB/DBGSS-campus, Gaborone (hergebruikt uit `diamant-gaborone-surat.md` §3) | -24.5859, 25.9144 | [8][11][13] | bron-gelegd (z15 opnieuw gezien: kantoor- en loodscomplex met zonnepaneel-carport aan de weg ten zuiden van de luchthaven en het Diamond Technology Park-stratenpatroon) |

## 4 · Via-punten (b1; reisvolgorde, alle ≤ 0,01 km van de gescande weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | A30/A14-knooppunt, 6,5 km oost van de mijn | -21.3285, 25.4285 | splitsing: A30 gaat oost naar Francistown, de A14 zuid; vervangt het ontwerp-punt in Letlhakane-dorp (geen stadscentrum) |
| b1 | 2 | A14 bij Serowe (5 km ZO van het centrum, op de ontsluiting die Serowe passeert [5]) | -22.4209, 26.7439 | pint de A14 (omleiding rond Serowe) tegen de B145 Serowe → Mahalapye, die de A1-corridor via Palapye zou overslaan |
| b1 | 3 | A14/A1-knooppunt Palapye (westrand, niet het centrum) | -22.5410, 27.0879 | wisseling A14 → A1; gedeelde OSM-knoop van beide wegen |
| b1 | 4 | A1 bij Mahalapye (oostrand van het dorp) | -23.1064, 26.8352 | houdt de A1 vast op de doorgaande trunk tot Gaborone |
Scan van de Botswana-PBF (eigen lezer, 12 s): ook zonder via-punten kiest de router dezelfde weg (525,0 km): geen
omweg-risico. Tussenstanden: junctie 8,7 · Serowe 219,4 · Palapye 258,1 · Mahalapye 328,7 · DTC 525,0 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Orapa-mijn (put + fabriek) | Debswana (De Beers/Botswana 50/50) | erts (20 Mt/j) → ruwe diamant, gereinigd en verpakt | ~10,8 Mct/j [4]; 9,02 Mct in 2023 [9] | [3][4][9] |
| DTCB/DBGSS-campus Gaborone | De Beers / Botswana (DTC Botswana) | ruwe diamant van de Debswana-mijnen → gesorteerd en gewaardeerd, sights vanaf 2013 | tot 45 Mct/j verwerkingscapaciteit; Debswana levert 200.000–500.000 ct per week [3][8] | [3][8] |

## 6 · Stoppunt
De brief stopt bij de DTCB/DBGSS-campus: dat is het enige gebrond volgende station ("ready for transport to Gaborone for
sorting and valuing, and ultimately for sale" [3]); de verdere aftap (Surat, Antwerpen, Dubai) loopt al in
`diamant-gaborone-surat`, `diamant-jwaneng-antwerpen` en `diamant-dubai-surat`, dus fase D vervalt hier.

## 7 · Open punten
- **De vervoerswijze Orapa → Gaborone is niet gebrond.** GIA zegt alleen "ready for transport to Gaborone" [3]; het
  v1-model van de atlas heeft `mode:"road"` [10]. Beide steunen op één bron voor de bestemming, niet op de wijze. Een
  beveiligd wegtransport is plausibel maar niet aangetoond.
- **Geen vlucht getekend.** Orapa Airport (ORP, -21.2667, 25.3181 volgens Wikipedia [7]; baan op de satelliet gezien) is
  eigendom van Debswana, heeft geen lijndienst en vraagt toestemming 48 uur vooraf. Dat het De Beers-bedrijfsvliegtuigen
  naar Gaborone laat vliegen staat alleen in Wikipedia-spiegels, zonder vracht of diamant. Vindt een volgende ronde een
  vrachtbron: vervang b1 door lucht ORP → GBE (grootcirkel ~371 km tussen twee vrachtterminals) met een korte
  stippel last mile aan de airside-kant.
- **Mijnanker snapt 0,57 km van de weg** (net boven de norm van 0,5 km): de put ligt midden in het mijnterrein; geen
  via-punt bijschuiven, als bevinding in §9 laten staan.
- **529 km is een aggregator** (rome2rio [6], geen overheidsopgave, geen genoemde wegen); de eigen OSM-route komt op
  525,0 km uit, maar dat is dezelfde bron als de scan, dus consistent en niet onafhankelijk. Wikipedia noemt de A14 op
  ~248 km [5] (OSM 249,4 km): in lijn.
- **Het ontwerp noemde Letlhakane als via-punt**; dat is een dorp. Vervangen door het A30/A14-knooppunt (§4).
- **Wikipedia meldt een sluiting van A14 Serowe–Orapa door regen (december 2025) [5]**: tijdelijk, er is geen
  alternatief in het net; het been blijft op de A14.
- **De sorteerhistorie in Gaborone** (de toets noemde een sorteercentrum sinds 1983) is binnen het budget niet bevestigd;
  gebrond is DTCB sinds 2012 en de verhuizing van de sights in 2013 [8].
- **Eén lang been is dun**: geen tussenoverslag gebrond, geen fase D/E, volume per mijn geschat (geen Debswana-jaarverslag).

## 8 · Bronnen
[1] Ketenontwerp (orchestrator-invoer, M31 golf 8) — `diamant-orapa-gaborone`, been A truck ~529 wegkm.
[2] Haalbaarheidstoets (orchestrator-invoer, BINDEND) — haalbaar; truck + aannemelijk; profiel, extract botswana, vensterKm 40.
[3] GIA Gems and Gemology, Summer 2014, Weldon, "Botswana: A Scintillating Moment" — Orapa 11 Mct in 2012 (capaciteit bijna 20 Mct), "ready for transport to Gaborone", Debswana 200.000–500.000 ct/week naar DTC Botswana. https://www.gia.edu/gems-gemology/summer-2014-weldon-botswana-scintillating-moment
[4] Wikipedia, "Orapa diamond mine" — coördinaat -21,3083 / 25,3694, Debswana, ~10,8 Mct/j, 20 Mt erts/j, 7 dagen/week. https://en.wikipedia.org/wiki/Orapa_diamond_mine
[5] Wikipedia, "A14 road (Botswana)" — A14 van de A30 bij Orapa tot de A1 bij Palapye, ~248 km, passeert Serowe, sluiting december 2025. https://en.wikipedia.org/wiki/A14_road_(Botswana)
[6] Rome2rio, Orapa → Gaborone — 529,1 km, 5 u 28 min (aggregator). https://www.rome2rio.com/s/Orapa/Gaborone
[7] Wikipedia, "Orapa Airport" — ORP/FBOR, -21,2667 / 25,3181; Debswana-eigendom, geen lijndienst (diamantvracht niet vermeld). https://en.wikipedia.org/wiki/Orapa_Airport
[8] GIA 4Cs blog, "Botswana diamonds" — DTCB-sorteercentrum Gaborone geopend 2012, sights verhuisd 2013, 45 Mct/j. https://4cs.gia.edu/en-us/blog/botswana-diamonds/
[9] `v2/design/diamant-sitelaag.md` [B1] — Orapa 9,02 Mct in 2023 (mining-technology.com-ranking, KPCS/USGS-samenvatting).
[10] `data/diamond.js` en `design/diamant.md` §4a — v1-flow `dia-orapa → dia-gaborone`, mode road, 11 Mct.
[11] `v2/design/routebrieven/diamant-gaborone-surat.md` §3 — hergebruikt anker `dia-gaborone-dtc` (-24,5859 / 25,9144).
[12] OpenStreetMap-extract Geofabrik `botswana-latest` (2026-07-22), eigen pure-Python-scan (A1, A14, A30; 6.992 wegdelen): 525,0 km, via-punten tot 0,01 km van de weg.
[13] Esri World Imagery via `v2/tools/sat_check.py` (z14 mijn, z15 DTC): `v2/build-cache/satcheck/sat-diamant-orapa-gaborone-mijn.png` en `sat-diamant-orapa-gaborone-dtc.png`.
[14] National Jeweler, "Malca-Amit creates the Gaborone Express" — alleen de vlucht Johannesburg–Gaborone, geen Orapa-vlucht (afgewezen als bron voor een vlucht). https://www.nationaljeweler.com/diamonds-gems/supply/1266-malcaamit-creates-the-gaborone-express

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-diamant-orapa-gaborone.json` (contract v2, lonlat, 77,2 KB, 3.770 punten, 2 markers). **Functie:** `bak_diamant_orapa_gaborone` in `v2/tools/bak_stromen.sh`; **profiel:** `diamant-orapa-gaborone-orapa-dtc` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | been | km gemeten | km brief | afwijking | naad | stippel |
|---|---|---|---|---|---|---|---|
| b1 | truck | Orapa-mijn → DTCB/DBGSS-campus Gaborone (A30, A14, A1; aannemelijk: één bron) | 530,0 (wegscan 529,4 + 0,57 km first mile) | 529,1 wegkm (rome2rio, aggregator) | +0,2% (binnen ±15%) | n.v.t. (één been) | nee, doorgetrokken |

**Markers (2):** `dia-orapa-mine` (-21.3083, 25.3694; bron-gelegd) en `dia-gaborone-dtc` (-24.5859, 25.9144; hergebruikt anker, bron-gelegd). Beide liggen op de lijn (de lijn begint en eindigt op de ankers).

**Recept.** `python v2/tools/wegscan_puur.py --profiel diamant-orapa-gaborone-orapa-dtc` (weg-slot, extract botswana, 88 MB, scan 26 s, pure-Python-PBF-lezer); daarna `bash v2/tools/bak_stromen.sh diamant-orapa-gaborone`. Via-punten (lon, lat in het profiel) exact uit §4; refs A14, A1, A30; vensterKm 40; geen corridorKlassen of eindToegangPrivaat nodig. Segmenten: mijn → A30/A14-knoop 11,7 km (incl. first mile), → Serowe 211,1, → Palapye 38,6, → Mahalapye 70,9, → Gaborone 197,0 km. Alle via-punten snapten ≤ 0,01 km, het eindanker 0,04 km.

**Geen stippel, geen haven-aanloop, geen vlucht, geen kopie, geen leiding.** Een wegbeen zonder zeeknoop; de onzekerheid (vervoerswijze niet gebrond, §7) staat in de beennaam, niet in de lijnstijl. Fase D/E vervalt (§6).

**Toets.** ±15%-toets OK (+0,1% op de wegscan tegen 529); geen naad; markers 0,0 km van de lijn; `toets_knikken`: 20 knikken, 2 omkeringen (169,5 en 168,3 graden bij -22.39965, 26.75558, ten noorden van Serowe, door het tool als "scherpe bocht, echt" geclassificeerd), 0 terugloop; de overige knikken zijn spikes van 5 tot 57 m rond first/last mile en de via-knopen; `toets_rechte_benen` geeft geen melding voor dit been; json.load OK, versie 2, lonlat, modaliteit truck, ≥ 2 punten.

**Bevindingen.**
- Mijnanker snapt 0,57 km van de weg (norm 0,5 km): de put ligt midden in het mijnterrein; first mile 2,59 km over kleine klassen (residential, unclassified), last mile 0,67 km (service, unclassified). Geen via-punt bijgeschoven, zoals in §7 aangekondigd.
- 529 km blijft consistent maar niet onafhankelijk: rome2rio en de OSM-scan zijn dezelfde bron; Wikipedia A14 ~248 km tegen OSM 249,4 km.

**Lessen.** (1) In `bak_stromen.sh` met een Python-heredoc een functie schrijven: een backslash-regelcontinuatie verdwijnt in een gewone string; gebruik `chr(92)` en controleer met `bash -n`. (2) Parallelle agenten schrijven in hetzelfde bestand; een syntaxfout na mijn functie (regel ~9356, andermans functie) verscheen na de bake als `syntax error near unexpected token`: de bake draaide wel, maar meld dit centraal.
