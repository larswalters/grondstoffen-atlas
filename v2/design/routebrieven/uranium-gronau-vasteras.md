# Routebrief (licht) · uranium — Urenco Gronau (Duitsland) → Rostock → Trelleborg → Westinghouse Västerås (Zweden)

**stroom-id:** `uranium-gronau-vasteras` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** Verrijkt uraniumhexafluoride (UF6) van Urenco Gronau rijdt per **truck** (A31/A30, A1 via Bremen en Hamburg, A20) naar de veerterminal
van Rostock, vaart per **veerboot** (Scandlines/Stena, tot eind 2014) naar Trelleborg en rijdt per **truck** (E6, E4, Rv 50, E18) naar de splijtstoffabriek
van Westinghouse in Västerås — **stoppunt**. Peiljaar **2014**; UF6 gaat sinds 2015 niet meer per veer [1].
**Welke as van het verhaal:** *Westers verrijkt uranium voor Zweedse en VVER-splijtstof.* Volume per bestemming niet gepubliceerd. Gronau-product: 83 vrachtwagens in 2020,
alle klanten samen [2]; sitelaag Gronau ~4.550 t U feed-eq./j (schatting); Västerås maakt ~400 t splijtstof/j [3]. Eenheid t U; per bestemming: **volume onbekend**.

## 1 · Ketenkaart
```
Urenco Gronau `u-gronau` ──(b1 truck · A31/A30 → A1 Bremen–Hamburg → A1/A20 Lübeck → Rostock · OSM-scan 495,5 km, OSRM-indicatie 501, geen wegkm ·
   aannemelijk: bron noemt "de Rostocker Hafen", niet de route [1])──► Rostock veerterminal `u-rostock-veer`
──(b2 zee · veer Rostock–Trelleborg · MARNET 149,3 km tegen ~150 km (81 zeemijl) [4] · tot eind 2014 [1])──► Trelleborg veerhaven `u-trelleborg-veer`
──(b3 truck · E6 → E4 Jönköping → Rv 50 → Örebro → E18 · OSM-scan 632,7 km, OSRM-indicatie 632, hemelsbreed 517 km, geen wegkm · aannemelijk)──►
Westinghouse Västerås `u-westinghouse-vasteras` (onzeker) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Gronau → Rostock veerterminal | A31 → A30 → A1 (Bremen, Hamburg) → A20 (aannemelijk: één bron, corridor eigen afleiding) | geen wegkm; hemelsbreed 398; OSM-scan 495,5 (OSRM 501) | maak_stroombeen_weg (`uranium-gronau-vasteras-gronau-rostock`) | nee |
| b2 | D | zee | Rostock veerterminal → Trelleborg | veer Rostock–Trelleborg (Kadetrinne) [1][4] | ~150 km [4]; MARNET 149,3 | MARNET kade → kade | aanloop: nee (3,9 en 1,1 km) |
| b3 | D | truck | Trelleborg → Västerås | E6 → E4 (Helsingborg, Jönköping) → Rv 50 → E18 (aannemelijk) | geen wegkm; hemelsbreed 517; OSM-scan 632,7 (OSRM 632) | maak_stroombeen_weg (`uranium-gronau-vasteras-trelleborg-vasteras`) | nee |
Totaal gemeten ca. 1.277 km. Een gepubliceerde wegkilometer ontbreekt voor b1 en b3 ("hemelsbreed X km, geen wegkm"): de ±15%-toets is alleen indicatie. Zee: −0,5% op [4].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-gronau` | verrijking (kop) | Urenco Deutschland, Gronau | 52.2154, 7.0739 | letterlijk uit `uranium-gronau-novouralsk.md` (DE-wikipedia [2]) | bron-gelegd (z15 gezien: scheidingshallen met schakelstation en omheining, kruis op de hallen). Routeanker 7.0723, 52.2184 (zie §7) |
| `u-rostock-veer` | overslag truck → veer | Seehafen Rostock, veerterminal Rostock–Trelleborg | 54.1507, 12.0975 | OSM-node van de terminal [5]; veer door de Rostocker Hafen [1] | bron-gelegd (z15 gezien: kadekop in de Unterwarnow met rijbanen vol trailers) |
| `u-trelleborg-veer` | overslag veer → truck | Trelleborg hamn, veerhaven (oostelijk bekken) | 55.3694, 13.1553 | eigen keuze op de veerrampen; lijn eindigt hier [4] | aannemelijk (z15 gezien: pier met rampen en rangeerterrein; geen bron noemt de ramp) |
| `u-westinghouse-vasteras` | splijtstoffabriek (eind) | Westinghouse Electric Sweden, Västerås (Finnslätten) | 59.6383, 16.5836 | Nominatim-wijkpunt Finnslätten; WP-EN: fabriek in Finnslätten [6] | onzeker (z15 gezien: industriegebied met grote fabriekshallen langs de spoorlijn; geen fabrieksbron) |

## 4 · Via-punten (wegbenen; knopen uit de OSM-scan, nooit stadscentra)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | AK A31/A30 bij Schüttorf | 52.3417, 7.2585 | A31 noord → A30 oost i.p.v. een omweg via Münster/A1 |
| b1 | 2 | AK Lotte/Osnabrück (A30/A1) | 52.2684, 7.9273 | pint de overgang naar de A1 noord |
| b1 | 3 | Bremer Kreuz (A1/A27) | 53.0416, 8.9832 | pint A1 langs Bremen i.p.v. A27/A7 |
| b1 | 4 | Maschener Kreuz (A1/A7) | 53.3808, 10.0064 | Hamburg via A1, niet via A7/Elbtunnel |
| b1 | 5 | Dreieck Hamburg-Ost (A1/A24) | 53.5616, 10.1727 | A1 door Hamburg-Oost |
| b1 | 6 | AK Lübeck (A1/A20) | 53.8502, 10.5927 | A1 → A20 richting Rostock |
| b3 | 1 | Lund E6/E20/E22 | 55.6367, 13.1069 | E6 langs Malmö i.p.v. E22 via Kristianstad |
| b3 | 2 | Helsingborg E4/E6/E20 | 56.0563, 12.7834 | E4 vanaf Helsingborg (de corridor van het ontwerp) |
| b3 | 3 | Jönköping E4 | 57.7742, 14.2075 | E4 i.p.v. Rv 23/Alvesta |
| b3 | 4 | Mjölby E4/Rv 50 | 58.3386, 15.1330 | Rv 50 naar Örebro i.p.v. E4 naar Norrköping |
| b3 | 5 | Örebro E18/E20/Rv 50 | 59.2730, 15.1782 | E18 naar Västerås (ringweg, 3 km buiten het centrum) |
| b3 | 6 | Västerås E18/Rv 56 | 59.6247, 16.5437 | afrit Rv 56 naar Finnslätten |
Alle zes snappen op ≤ 0,02 km; de OSM-scan routeert b1 en b3 zonder omweg (scan-uitvoer in `v2/build-cache/ais/graaf/uranium-gronau-vasteras-weg-*.geojson`).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Urenco Gronau | Urenco | natuurlijk UF6 → verrijkt UF6 + tails | 4.550 t U feed-eq./j (sitelaag, schatting) | [2] |
| Westinghouse Västerås | Westinghouse | verrijkt UF6 → splijtstof (BWR/PWR/VVER) | ~400 t splijtstof/j | [3][6] |

## 6 · Stoppunt
De brief stopt bij de fabriek in Västerås: de enige Zweedse UF6-ontvanger en de afnemer die [2][6] aan Urenco-uranium koppelen. Reactoren (fase E) vervallen.

## 7 · Open punten
- **Bron noemt alleen "Schweden" en de Rostocker Hafen** [1], niet Trelleborg of Västerås. Trelleborg volgt uit de veerlijn [4]; Västerås uit [2] (Urenco-uranium voor Westinghouse-fabriek) en [3] (enige Zweedse fabriek).
- **Peiljaar 2014:** UF6 per veer alleen tot eind 2014; sinds 2015 rijdt de veerlijn geen UF6 meer; wat daarna de route is, is niet gevonden [1].
- **Västerås-anker onzeker:** Westinghouse staat niet op naam in Nominatim of Photon. Alternatief: Fredholmsgatan 22 (Devex "Building 399") 59.6331, 16.5880, 0,6 km ZO, op satelliet een klein gebouw bij het bos [7]. De sitelaag heeft geen Västerås-site; v1 `u-fab-se` 59.62, 16.55 (2 decimalen) ligt 2,3 km zuidwest.
- **Routeanker Gronau:** de dichtstbijzijnde OSM-knoop van het plantanker (0,12 km) ligt op een los plantwegje en geeft "geen wegpad"; b1 start op 7.0723, 52.2184 (verbonden net, 0,35 km); marker blijft `u-gronau`.
- **Geen wegkm gepubliceerd:** b1 hemelsbreed 398 km, b3 hemelsbreed 517 km; de OSM-scan (495,5 en 632,7) is de indicatie, OSRM 501 en 632 de kruiscontrole.
- **Keerlussen gesnoeid** door de scan (dubbel gereden stukken, geen via-fout): b1 ~3,4 km (Hamburg-Ost 1,30; Lotte 1,01; Bremer Kreuz 0,88), b3 ~5,4 km (Mjölby 5,33: de via-knoop ligt op de E4-oprit, de afslag naar Rv 50 wordt een pendel).
- **Corridor Gronau → Rostock is eigen afleiding** (ontwerp); [1] geeft geen route. Fase D alleen op één bron.
- **Rostock-kade ligt 3,9 km van MARNET-zeeknoop 8886** (onder de 5 km: geen haven-aanloop); Trelleborg 1,1 km (knoop 8883).

## 8 · Bronnen
[1] urantransport.de, "Transporte zur und von der Urananreicherungsanlage in Gronau" (exporten naar Schweden tot eind 2014 via Scandlines/Stena door de Rostocker Hafen; UF6 sinds 2015 niet meer; Schweden onder de ontvangers 2012-2017). https://urantransport.de/hintergrund/transporte-zur-und-von-der-urananreicherungsanlage-in-gronau/
[2] Wikipedia (DE), "Urananreicherungsanlage Gronau" (coördinaat; 2020: 83 Lkw product; Urenco-uranium voor Westinghouse Västerås). https://de.wikipedia.org/wiki/Urananreicherungsanlage_Gronau
[3] World Nuclear Association, "Sweden" (Westinghouse Västerås ~400 t BWR/PWR-splijtstof/j). https://world-nuclear.org/information-library/country-profiles/countries-o-s/sweden
[4] Wikipedia (DE), "Fährverbindung Rostock–Trelleborg" (circa 150 km, 81 zeemijl). https://de.wikipedia.org/wiki/F%C3%A4hrverbindung_Rostock%E2%80%93Trelleborg
[5] OSM-node veerterminal Rostock (54.1507, 12.0975), via ontwerp en Nominatim; z15 gezien (zie [sat]).
[6] Wikipedia (EN), "Västerås" (Westinghouse Sweden in Finnslätten, noord-Västerås). https://en.wikipedia.org/wiki/V%C3%A4ster%C3%A5s · World Nuclear News, 2016-04-29, "Westinghouse expands fuel production capacity" (Västerås, VVER-1000). https://www.world-nuclear-news.org/Articles/Westinghouse-expands-fuel-production-capacity
[7] Devex, "Westinghouse Electric Sweden AB" (Fredholmsgatan 22, Building 399, Västerås); Westinghouse EMEA, postadres SE-721 63 Västerås. https://www.devex.com/organizations/westinghouse-electric-sweden-ab-51872 · https://westinghousenuclear.com/About/Regional-Operations/EMEA
[8] Eigen briefs en data: `uranium-gronau-novouralsk.md` (u-gronau), `uranium-sitelaag.json` (w-urenco-gronau), `data/uranium.js` (u-fab-se).
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-uranium-gronau-vasteras-gronau.png`, `…-rostock.png`, `…-trelleborg.png`, `…-vasteras.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Recept:** `bash v2/tools/bak_stromen.sh uranium-gronau-vasteras` → `v2/data/stroomroute-uranium-gronau-vasteras.json` (versie 2, lonlat, 237 KB, 3 benen, 12.309 punten, 4 markers, totaal 1.277,6 km, 0% stippel). Functie `bak_uranium_gronau_vasteras`; wegprofielen `uranium-gronau-vasteras-gronau-rostock` en `uranium-gronau-vasteras-trelleborg-vasteras` (al in `maak_stroombeen_weg.py`, gescand met `wegscan_puur.py`, geojson in `v2/build-cache/ais/graaf/uranium-gronau-vasteras-weg-*.geojson`).

| # | modaliteit | been | km gemeten | km brief | naad naar vorig been |
|---|---|---|---|---|---|
| 1 | truck | Urenco Gronau → Rostock veerterminal | 495,5 | hemelsbreed 398, geen wegkm (OSRM 501) | 0 |
| 2 | zee | veer Rostock → Trelleborg (MARNET, kade → kade) | 149,3 | ~150 (81 zeemijl) → −0,5% | 3,90 km (kade ↔ zeeknoop 8886) |
| 3 | truck | Trelleborg veerhaven → Westinghouse Västerås | 632,8 | hemelsbreed 517, geen wegkm (OSRM 632) | 1,06 km (kade ↔ zeeknoop 8883) |

**Toets:** zee binnen ±15% van de bron; de twee wegbenen hebben geen gepubliceerde wegkm, dus de ±15%-toets is indicatie (OSM-scan en OSRM vallen binnen 1,2%). Markers: Rostock, Trelleborg en Västerås 0,0 km van de lijn; `u-gronau` 0,35 km (plantanker, de lijn start op het routeanker, brief §7). `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom gemeld. Geen stippel, geen haven-aanloop, geen leiding, geen lucht, geen kopie.

**Toelichting:**
- **Geen haven-aanloop:** beide kaden liggen < 5 km van hun MARNET-zeeknoop (Rostock 3,9 km naar 8886; Trelleborg 1,1 km naar 8883); de naden van 3,9 en 1,1 km zijn procesgat, geen aanloop (handleiding §5).
- **Aannemelijk, geen stippel:** één bron (urantransport.de) noemt Gronau → Schweden door de Rostocker Hafen; corridor en Trelleborg/Västerås zijn afleiding. Dat staat in de beennamen en in §7, niet in de lijnstijl.
- **Peiljaar 2014:** UF6 per veer alleen tot eind 2014; het veerbeen is dus historisch en de stroom beschrijft die periode.
- **Västerås-anker onzeker** (Finnslätten-wijkpunt, geen fabrieksbron); de lijn eindigt precies op dat wijkpunt (snap 0,015 km).

**Bevindingen (niet bijgeschoven):**
- `toets_knikken.py`: b1 heeft één terugloop op 52.3421,7.2584 (via-punt AK A31/A30 Schüttorf ligt ~0,3 km voorbij de afrit; route rijdt door tot het via-punt en komt terug, ~0,3 km pendel) en een scherpe echte bocht bij AK Lotte (52.2681,7.9345, 170°). b3 heeft twee scherpe bochten, echt (v 1,2–1,4) bij 58.0553,14.5088 (Jönköping-oostzijde) en 58.3267,15.0940 (Mjölby E4/Rv 50, de lus waarvan de scan 5,3 km snoeide). De overige knikken zijn spikes van enkele meters in opritten/knopen.
- Totaal gemeten 1.277,6 km tegen de ~1.277 km uit §2.

**Lessen:** (1) de tussenuitvoer van de ontwerpronde (profielen, geojson, satcheck-beelden) stond compleet; het bakken was één functie plus één run. (2) Een via-punt op een afrit geeft een kleine pendel van ~0,3 km: liever het via-punt 100 m vóór de afrit op de doorgaande weg leggen; hier niet bijgeschoven (geen km-effect).
