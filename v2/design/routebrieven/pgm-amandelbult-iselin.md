# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-amandelbult-iselin` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) · **status:** gebakken
**Keten in één zin:** platina/palladium/rodium van Valterra Platinum's Amandelbult-mijn (Noord-Bushveld) per **truck** naar Rustenburg PMR, per **truck** (N4/N1, letterlijke kopie van `pgm-rustenburg-shanghai` b1) naar de vrachtterminal van OR Tambo (JNB), per **vrachtvlucht** (grootcirkel) naar de vrachtterminal van JFK (New York), per **truck** (NJ Turnpike/I-95) naar Metivo (ex-BASF Environmental Catalyst and Metal Solutions), Iselin NJ — de Amerikaanse autokatalysator-/edelmetaalrecyclingmarkt.
**Welke as van het verhaal:** Zuid-Afrika/Bushveld (eigen mijn Amandelbult, Noordrand) → VS-katalysatormarkt (Iselin NJ). Reserve-as uit golf 3, behouden in golf 4 omdat de VS-katalysatormarkt door geen enkele bestaande PGM-stroom werd bediend (Stillwater→Columbus is zuiver binnenlands VS). Jaarvolume Amandelbult: 14,5 t 4E/j (Pt+Pd+Rh+Au), Anglo American Platinum/Valterra jaarverslag 2023, ~465 koz 4E [1]; geen site-specifiek volume voor déze bestemmingsas gevonden.

## 1 · Ketenkaart
```
Amandelbult mijn `pgm-amandelbult` ──(b1 truck · R510 Noord-Bushveld · hemelsbreed ~96,6 km, geen wegkm)──►
  Rustenburg PMR `pgm-rustenburg-pmr` ──(b2 truck · N4/N1, letterlijke kopie pgm-rustenburg-shanghai b1 · ~120 km ontwerp / 178,0 km gebakken)──►
  JNB-vrachtterminal `pgm-jnb-cargo` ──(b3 lucht · vlucht JNB → JFK, grootcirkel · ~12.831,5 km)──►
  JFK-vrachtterminal `pgm-jfk-cargo` (= `dia-jfk-cargo`) ──(b4 truck · NJ Turnpike/I-95 · ~69 km)──►
  Metivo/BASF ECMS Iselin NJ `pgm-basf-ecms-iselin` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Amandelbult mijn → Rustenburg PMR | R510 (Rustenburg–Northam–Thabazimbi) | hemelsbreed ~96,6 km, geen wegkm [2][toets-bindend] | maak_stroombeen_weg | nee |
| b2 | A/B | truck | Rustenburg PMR → OR Tambo (JNB) vrachtterminal | N4 (Rustenburg–Brits–Pretoria) → N1/R21 — **letterlijke kopie van `pgm-rustenburg-shanghai` been b1** | ontwerp ~120 [3] / gebakken 178,0 (identiek aan de bestaande stroom) | maak_stroombeen_weg (hergebruik geojson) | nee |
| b3 | B | lucht | OR Tambo (JNB) → JFK (New York) | vrachtvlucht JNB→JFK, grootcirkel | ~12.831,5 (berekend, grootcirkel op de twee ankers) | maak_luchtbeen | nee — doorgetrokken (bakhandleiding §2) |
| b4 | C | truck | JFK-vrachtterminal → Metivo/BASF ECMS, Iselin NJ | NJ Turnpike/I-95 → Wood Avenue South | ~69 (43 mijl), reëel wegkm [4] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-amandelbult` | mijn / vertrekpunt | Amandelbult-mijn (Anglo American Platinum / Valterra Platinum), Noordrand Bushveld | -24.8080, 27.2650 | [1][5] | **bron-gelegd — hergebruikt letterlijk** uit `v2/design/pgm-sitelaag.json` (`w-amandelbult`, satelliet z14: kruis op mijnterrein) |
| `pgm-rustenburg-pmr` | raffinaderij / overslag | Rustenburg PMR + Waterval-smelter-/RBMR-complex (Valterra Platinum) | -25.6750, 27.3180 | [3][6] | **bron-gelegd — hergebruikt letterlijk** uit `pgm-rustenburg-shanghai.md` §3 (z16–z17 gezien: industrieel proces­complex met schoorsteen, tanks, spooraansluiting bij Waterval) |
| `pgm-jnb-cargo` | vrachtterminal (luchtanker) | O.R. Tambo International Airport — vrachtplatform/-loodsen | -26.1380, 28.2270 | [3][6] | **bron-gelegd — hergebruikt letterlijk** uit `pgm-rustenburg-shanghai.md` §3 (z16–z17: verhard platform met wijdrompvrachttoestellen naast vrachtloodsen) |
| `pgm-jfk-cargo` | vrachtterminal (luchtanker) | JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens, New York | 40.6587, -73.7952 | [7] | **bron-gelegd — hergebruikt letterlijk** = `dia-jfk-cargo` uit `stroomroute-diamant-mumbai-newyork.json` (zelfde vrachtterminal, andere grondstof) |
| `pgm-basf-ecms-iselin` | katalysator-/edelmetalenfabriek | Metivo (voorheen BASF Environmental Catalyst and Metal Solutions, ECMS — carve-out juli 2023), 33 Wood Ave South, Iselin NJ 08830 | 40.5650, -74.3288 | [8][9] | **bron-gelegd** (z17 gezien: laag kantoorgebouw met eigen parkeerterrein in het Metro Park-kantorenpark, direct bij de GSP/NJ Turnpike-aansluiting en het Metropark-station — beeld: `sat-pgm-amandelbult-iselin-basf-ecms-33woodave.png`). Was in `pgm-sitelaag.json` (`w-basf-iselin`) nog *aannemelijk* op een grovere coördinaat (40,57/-74,32) — deze pas tilt de status naar bron-gelegd; **sitelaag zelf niet gewijzigd** (buiten scope, zie §7) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Northam (R510-doorgangsplaats) | -24.9500, 27.2660 | enige doorgaande verharde route tussen Amandelbult/Thabazimbi-omgeving en Rustenburg loopt via Northam op de R510 [2]; geen andere corridorkeuze gevonden binnen het webbudget — open punt voor de wegbake (§7) |
| b2 | 1–4 | Brits · Pretoria (N4/N1-knoop) · Midrand · Kempton Park | zie `pgm-rustenburg-shanghai.md` §4 | **letterlijke kopie** — dezelfde vier via-punten als been b1 van die stroom, want het is dezelfde N4/N1-corridor Rustenburg→OR Tambo |

## 5 · Verwerkingsknopen
Geen tussenliggende verwerkingsknoop: Rustenburg PMR levert al geregistreerd Pt/Pd/Rh-raffinaat (vertrekvorm voor de export), en Metivo/Iselin is zelf de eindfabriek (fase D, geen fase E — geen bron noemt een volgende locatie na de katalysator-/recyclingfabriek).

## 6 · Stoppunt
De brief stopt bij Metivo (ex-BASF ECMS), 33 Wood Ave South, Iselin NJ: dit is de door de haalbaarheidstoets bindend voorgeschreven eindsite (Precious Metals Services & Recycling + Mobile Emissions Catalysts), nu met een eigen satellietblik van *aannemelijk* naar *bron-gelegd* getild. Fase E vervalt — geen bron noemt een afnemer ná deze fabriek.

## 7 · Open punten
- **b1 heeft geen bronvolle wegcorridor**, alleen de R510 als bekende route en Northam als enig gevonden doorgangspunt; de eindkilometers en eventuele extra via-punten moeten bij het bakken uit de Geofabrik-scan van `zuid-afrika` volgen (`maak_stroombeen_weg.py`). Km blijft tot dan **hemelsbreed ~96,6 km** (toets-bindend; het ontwerpcijfer "~40 km" wordt niet overgenomen).
- **b3 (luchtvracht) is niet apart gebrond voor déze as** — aangenomen als industriestandaard (PGM reist als beveiligde luchtvracht), dezelfde aanname als bij de andere golf-3-PGM-luchtbenen (zie `verhaal_grondstof` in het ketenontwerp). Geen tussenlanding aangenomen.
- **`pgm-basf-ecms-iselin` is inhoudelijk een carve-out ván een carve-out**: BASF's Precious Metals Services-tak werd juli 2023 "BASF Environmental Catalyst and Metal Solutions" (ECMS), en draait inmiddels onder het merk **Metivo** — nog steeds op hetzelfde adres/dezelfde rol, maar strikt genomen geen "BASF" meer en zelfs niet meer als "ECMS" [8]. De brief benoemt dit expliciet i.p.v. kaal "BASF".
- **De sitelaag (`v2/design/pgm-sitelaag.json`, `w-basf-iselin`) is niet aangepast** — dat bestand valt buiten deze brief (JE RAAKT ALLEEN JE EIGEN BESTANDEN). Aanbeveling voor de orkestrator: coördinaat 40,57/-74,32 → 40,5650/-74,3288 en status `aannemelijk` → `bron-gelegd`, met de nieuwe naam/rol uit deze brief.
- Geen site-specifiek jaarvolume voor déze bestemmingsas (alleen het algemene Amandelbult-productiecijfer, zie boven).
- b2 is een letterlijke kopie: bij het bakken het bestaande geojson/de beenregel van `pgm-rustenburg-shanghai` hergebruiken, geen tweede versie bakken (werkwijze-regel).

## 8 · Bronnen
[1] Anglo American Platinum / Valterra Platinum, jaarverslag/productierapportages 2023 — Amandelbult 14,5 t 4E/j, ~465 koz 4E (uit `v2/design/pgm-sitelaag.md`, regel `w-amandelbult`).
[2] Wikipedia, "R510 (South Africa)" — R510 verbindt Rustenburg via Northam met Thabazimbi/Stockpoort-grenspost. https://en.wikipedia.org/wiki/R510_(South_Africa) · Major Mines & Projects, "Amandelbult Complex" — "located 94 km north from Rustenburg". https://miningdataonline.com/property/1567/Amandelbult-Complex.aspx · Wikipedia-coördinaat Northam, South Africa (-24,95/27,266) via MediaWiki prop=coordinates.
[3] Ketenontwerp golf 3/4 (orkestrator-invoer) + `v2/design/routebrieven/pgm-rustenburg-shanghai.md` §1/§2/§9 — been b1 van die stroom (Rustenburg PMR → OR Tambo, N4/N1, ontwerp ~120 km, gebakken 178,0 km) letterlijk hergebruikt.
[4] Travelmath.com, "Driving Distance from JFK to Iselin, NJ" — 43 mijl / ~69 km, ~55 min. https://www.travelmath.com/drive-distance/from/JFK/to/Iselin,+NJ
[5] `v2/design/pgm-sitelaag.json`, entry `w-amandelbult` — coördinaat -24,8080/27,2650, coord_bron Wikipedia-geohack + satelliet z14 (kruis op mijnterrein), status bron-gelegd.
[6] `v2/design/routebrieven/pgm-rustenburg-shanghai.md` §3 en §8[6] — satellietbeelden `sat-pgm-rustenburg-shanghai-waterval-*.png` / `sat-pgm-rustenburg-shanghai-jnb-*.png`.
[7] `v2/data/stroomroute-diamant-mumbai-newyork.json`, marker "dia-jfk-cargo" — JFK South Cargo Area, 40,6587/-73,7952, bron-gelegd (hergebruikt over grondstoffen heen, zelfde fysieke terminal).
[8] BASF persbericht, "BASF divests Battery Materials... Environmental Catalyst and Metal Solutions" (juli 2023) en Metivo (voorheen basf-catalystsmetals.com), locatiepagina Iselin NJ — adres 33 Wood Ave South, Iselin NJ 08830; "corporate functions, Precious Metals Services & Recycling and Mobile Emissions Catalysts". https://www.basf.com/global/en/media/news-releases/2023/07/p-23-274 · https://metivo.com/en/company/locations/iselin-nj
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15/z17) — `v2/build-cache/satcheck/sat-pgm-amandelbult-iselin-basf-ecms-iselin.png` (eerste, grove pas op de oude sitelaag-coördinaat) en `sat-pgm-amandelbult-iselin-basf-ecms-33woodave.png` (definitieve pas op 33 Wood Ave South, kantoorgebouw + parkeerterrein in het Metro Park-kantorenpark).
[10] Valterra Platinum persberichten — Amandelbult na de overstroming van februari 2025 hersteld naar steady-state productie, Q3/Q4-2025-productierapporten bevestigen doorlopende output (haalbaarheidstoets-webcheck). https://www.valterraplatinum.com/media/press-releases/2025/18-07-2025 · https://www.valterraplatinum.com/media_centre/press-releases-2025-28-10-2025/

## 9 · Bakstatus

**Gebakken (2026-09-28, lichte werkwijze, M31 golf 4).** 4 benen · **13.178,2 km** · 5.335 punten · 5 markers.
Recept: `bak_pgm_amandelbult_iselin()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh
pgm-amandelbult-iselin`). Geen naad > 0,00 km tussen de vier benen. `toets_knikken.py`: geen structurele
omkeringen behalve één pre-existente terugloop in het letterlijk hergebruikte geojson van been b2 (zie
hieronder — niet aangeraakt, want dat bestand is niet van deze stroom). `toets_rechte_benen.py --min-km 5`:
geen bevindingen voor deze stroom. JSON: versie 2, `punt_formaat` lonlat, modaliteiten `{truck, lucht}` (beide
toegestaan), elk been ≥ 2 punten, bestand 109,6 KB.

| # | modaliteit | km | brief-cijfer | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | truck | 113,0 | hemelsbreed ~96,6 (geen wegkm) | +15,3% | nee |
| b2 | truck | 178,2 | 178,0 (letterlijke kopie pgm-rustenburg-shanghai b1) | +0,1% (afronding) | nee |
| b3 | lucht | 12.831,5 | ~12.831,5 (berekende grootcirkel) | 0,0% | nee — doorgetrokken |
| b4 | truck | 55,5 | ~69 (routeplanner-schatting) | −19,5% | nee |

**b1 (Amandelbult → Rustenburg PMR, R510 via Northam).** Eigen profiel `pgm-amandelbult-iselin-amandelbult-
rustenburg` in `maak_stroombeen_weg.py`, extract `zuid-afrika` (al aanwezig). Gebakken 111,4 km ruw / 113,0 km
getekende lijn (incl. anker-verbindingen) tegen de hemelsbrede indicatie van 96,6 km = **+15,3%**. Geen fout:
de brief zelf zegt dat de ±15%-toets bij een hemelsbrede schatting een indicatie is, geen norm (routebrief §7,
toets-bindend "geen wegkm" totdat een echte routekm bestond — die is er nu). Anker-verbinding plant → weg
1,46 km [⚠️ > 0,5 km, bevinding]: Amandelbult is een uitgestrekt open-pit-mijnterrein, het OSM-wegnet raakt het
terrein zelf niet exact aan. Northam-via-punt (het enige gevonden corridorpunt op de R510) sneed goed aan
(snap 0,15 km).

**b2 (Rustenburg PMR → OR Tambo (JNB), letterlijke kopie).** Hergebruikt het bestaande geojson van
`pgm-rustenburg-shanghai` been b1 (`pgm-rustenburg-shanghai-weg-rustenburg-jnb.geojson`, 178,2 km getekend/
178,0 km gepubliceerd in die stroom) **ongewijzigd** — niet opnieuw gebakken, conform de werkwijze-regel
(routebrief §7) en de bak-aanwijzing. `toets_knikken.py` meldt op dit been 2 omkeringen (1 terugloop bij
-26.13446,28.22503) — dit is **pre-existente geometrie van `pgm-rustenburg-shanghai`**, niet van deze stroom;
buiten scope (JE RAAKT ALLEEN JE EIGEN BESTANDEN). Gemeld voor het rapport, niet gerepareerd.

**b3 (OR Tambo (JNB) → JFK, vlucht).** `maak_luchtbeen.py` tussen de twee bron-gelegde vrachtterminals:
12.831,5 km grootcirkel, 515 punten — exact het berekende cijfer uit de brief. Doorgetrokken (bakhandleiding
§2), geen stippel, geen tussenlanding aangenomen (niet apart gebrond voor déze as, zie brief §7).

**b4 (JFK South Cargo Area → Metivo/BASF ECMS, Iselin NJ).** ⚠️ **Bevinding op de opdracht/brief:** de
bak-aanwijzing noemde alleen `us-new-jersey` als benodigd/aanwezig extract, maar het JFK-anker ligt in Queens
(New York) — een eerste poging met alleen `us-new-jersey` gaf een anker-snap van **19,31 km** voor het
JFK-uiteinde (het extract dekt de terminal niet). Extract `us-new-york` toegevoegd aan het profiel (al
aanwezig op schijf, `us-new-york-latest.osm.pbf` — geen nieuwe download, en al gebruikt door het bestaande
profiel `diamant-mumbai-newyork-jfk-47th` voor exact hetzelfde JFK-anker). Na de toevoeging: snap 0,01 km /
0,03 km, beide OK. Gebakken 55,5 km tegen de routeplanner-schatting van ~69 km (Travelmath.com, geen
officiële overheids-/bedrijfsopgave) = **−19,5%**, buiten de ±15%-indicatie maar geen fout — de bake-uitvoer
is hier bewust de echte controle (brief §7). Geen `eindToegangPrivaat` nodig gebleken: de kleine wegklassen
(residential/service/tertiary/unclassified) rond het Metro Park-kantorenpark deden gewoon mee (last mile 0,66
km).

**Open punten voor de orkestrator (ongewijzigd t.o.v. brief §7, plus deze bake-bevinding):**
- Het extract us-new-york ontbrak in de bak-aanwijzing van de brief/opdracht maar was al aanwezig; toegevoegd
  aan het profiel. Geen impact op andere stromen (eigen profielsleutel).
- De pre-existente terugloop in het hergebruikte b2-geojson (`pgm-rustenburg-shanghai`) is niet gerepareerd —
  buiten scope van deze brief/bake.
- De sitelaag `v2/design/pgm-sitelaag.json` (`w-basf-iselin`) staat nog op de oude, grovere coördinaat en
  status `aannemelijk` — niet door deze bake aangepast (buiten scope, zie brief §7); aanbeveling voor de
  orkestrator om dat centraal door te voeren naar 40,5650/-74,3288, bron-gelegd.
- b3 (luchtvracht) is niet apart gebrond voor déze as (aannemelijk/industriestandaard), zoals de brief al
  vermeldt.

**Lessen:** het extract-lijstje in een bak-aanwijzing kan onvolledig zijn wanneer een anker in een ander land/
staat ligt dan de eindsite van hetzelfde been (JFK ligt in NY, de fabriek in NJ) — controleer bij een
cross-state-been altijd welke extract(s) het VERTREKPUNT dekken, niet alleen de bestemming.
