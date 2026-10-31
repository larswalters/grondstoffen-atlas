# Routebrief (licht) · olie — Fahud → PDO Main Oil Line → Mina al-Fahal (Oman)

**stroom-id:** `olie-fahud-minaalfahal` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** Ruwe olie van het PDO-pompstation bij Fahud (Binnenland-Oman) per **leiding** (PDO Main Oil Line, 276 km, N-Z gekarteerd als twee OSM-ways) naar het tankenpark Saih al-Maleh / Mina al-Fahal bij Muscat, waar de olie op tankers voor export gaat; de lijn eindigt bij het tankenpark, geen bron noemt een losplaats.
**Welke as van het verhaal:** *Oman: crude uit het binnenland naar een kust die buiten de Straat van Hormuz ligt* (Hormuz-bypass-as, ~95% van de export naar China). Volume: Omaanse ruwe-olie-export 230,6 mln vaten jan-sep 2024 = ~842 kb/d (eigen deling over 274 dagen), China 219,6 mln vaten [3]; jan-feb 2024 ~874 kb/d, 80-90% China [4]. Doorzet van de leiding zelf niet gepubliceerd; het nationale cijfer is een bovengrens voor wat hier doorheen gaat.

## 1 · Ketenkaart
```
PDO-pompstation Fahud `ol-fahud-pompstation` (22.2218, 56.5597) ──(b1 leiding · PDO Main Oil Line · 276,9 km OSM,
  2 ways gestikt, doorgetrokken, 0 stippel)──► tankenpark Saih al-Maleh / Mina al-Fahal `ol-minaalfahal-tankenpark`
  (23.6214, 58.5129) ── stoppunt (SBM-monoboeien offshore + tanker niet in OSM: niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Fahud-pompstation → tankenpark Mina al-Fahal | PDO Main Oil Line (Fahud - Saih al-Maleh) | eigen OSM-som 276,9 [5][6][8]; gepubliceerd 276 (Wikipedia [1]) = +0,3%; hemelsbreed 253,4 | OSM-ways 149963619 (227 nodes, N-Z dus omgekeerd) + 586118047 (19 nodes), naad 0,0 m op 23.5764, 58.4087, `maak_leidingbeen_olie_fahud_minaalfahal.py` (FeatureCollection) | nee, volledig doorgetrokken |
Naam van het been: "PDO Main Oil Line: Fahud → Saih al-Maleh / Mina al-Fahal (2 OSM-ways, gemeten, aannemelijk: één bron voor de identiteit, naamloze Bing-way, lengte 276 km gepubliceerd)". Geen zeebeen (bindende toets): geen bron noemt afnemer of losplaats van de lading, dus geen MARNET-snap en geen haven-aanloop. Zijtak way 586118045 en de zuidelijke PDO-takken tot 18,2 N horen niet bij deze keten.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-fahud-pompstation` | kop van de leiding / veldzijde | PDO-pompstation Fahud (leidingbegin) | 22.2218, 56.5597 | [5][8] OSM-begin way 149963619; [1] Fahud-veld, begin van de leiding | bron-gelegd (z15 gezien: op 60 m ten noorden van het punt een compact installatiecomplex met tankgroep en manifold in de woestijn, leidingstroken en pistes erlangs) |
| `ol-minaalfahal-tankenpark` | einde van de leiding / opslag vóór export | Tankenpark Saih al-Maleh / Mina al-Fahal (PDO), Muscat | 23.6214, 58.5129 | [6][8] OSM-einde way 586118047; [1][2] tankpark en SBM-monoboeien bij Saih al-Maleh = Mina al-Fahal | bron-gelegd (z14 gezien: industrieterrein Mina al-Fahal tegen de bergrand boven de kust; z16: op ~220 m NW drie grote dakopslagtanks in één bund, eromheen meer tankgroepen) |

## 4 · Via-punten (b1 is een gestikte OSM-lijn: geen routering; alleen controlepunten op de lijn)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | ketenkm 62 (begin van de dichte kartering) | 22.4700, 57.0749 | koorde van 15,2 km tussen km 47 en 62: grof gekarteerd stuk [8] |
| b1 | 2 | ketenkm 175,7 | 23.0922, 57.8256 | controle midden van de corridor [8] |
| b1 | 3 | stikplek ways (ketenkm 264,6) | 23.5764, 58.4087 | naad 0,0 m, hier begint de tweede (12,3 km) way [6][8] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fahud-veld / pompstation | PDO (Staat Oman 60%, Shell 34%, TotalEnergies 4%, Partex 2%) | ruwe olie uit de velden → leiding | niet gebrond | [1] |
| Tankenpark + SBM Mina al-Fahal | PDO (twee monoboeien), Shell Oman Marketing (derde); raffinaderij 104 kb/d (Oman Refinery Co.) ernaast | leiding → tankopslag → tankerlading via onderzeese buis naar SBM | exportvolume nationaal 842 kb/d (jan-sep 2024) [3] | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij het tankenpark Mina al-Fahal: de lading gaat daar op tankers, maar geen bron noemt een losplaats, raffinaderij of schip bij naam (Chinese afname is een aggregaat over heel Oman [3][4]). Fase D en E vervallen; geen zeebeen.

## 7 · Open punten
- **Eén-been-keten zonder havenbewijs** (precedent Agadem-Seme): geen bron noemt een Chinese losplaats, dus er is geen zeebeen en de Hormuz-bypass-as blijft in de titel en niet in de lijn zichtbaar.
- **Identiteit OSM-lijn:** beide ways hebben geen naam of operator (way 149963619: source Bing, usage transmission); de koppeling aan de PDO Main Oil Line steunt op de lengte (276,9 tegen 276 km [1]) en het begin- en eindpunt (Fahud, Saih al-Maleh).
- **Tankenpark niet te onderscheiden:** op z16 staan meerdere tankgroepen rond het OSM-einde; welke daarvan PDO is, is niet gebronnen. De OSM-lijn eindigt ~220 m SE van de drie-tankgroep op 23.6227, 58.5113; geen rechte naad, het einde ís het OSM-uiteinde.
- **Offshore stuk** (onderzeese buis naar de monoboeien [2]) staat niet in OSM en geen bron geeft er coördinaten van: niet getekend.
- **Grof gekarteerd stuk:** 245 punten over 277 km, koorden tot 15 km (km 47-62), 8 km en 7 km; de echte buis is iets langer en bochtiger.
- **Doorzet van de leiding en het aandeel van PDO in de Omaanse export** zijn niet gepubliceerd; 842 kb/d is het nationale exportcijfer (productie jan-sep 2024 994,2 kb/d [3]). Cijfers over twee periodes (842 en 874 kb/d) verschillen door de periode, niet door een fout.
- v1-checklist (`data/oil.js`, `design/olie.md`) en de olie-sitelaag bevatten geen Omaanse site: geen coördinaat om te hergebruiken.

## 8 · Bronnen
[1] Wikipedia, "Petroleum Development Oman" — aandeelhouders, leiding van 276 km naar Saih al Maleh (later Mina al Fahal) met tankpark en monoboeien, eerste export 27 juli 1967; ruwe olie wordt in Mina al Fahal opgeslagen en geladen. https://en.wikipedia.org/wiki/Petroleum_Development_Oman
[2] Wikipedia, "Mina Al Fahal" — voorheen Saih al Maleh; tankers laden via onderzeese buis en SBM's, PDO bezit twee monoboeien, Shell Oman Marketing de derde; raffinaderij 104 kb/d; 23°38′N 58°32′E (gebiedsniveau). https://en.wikipedia.org/wiki/Mina_Al_Fahal
[3] Hellenic Shipping News, "Oman's oil exports hit 230.6m barrels by September" — 230,6 mln vaten jan-sep 2024, productie 994,2 kb/d; China-aandeel ~95% (eigen berekening uit de bron, 219,6 mln vaten). https://www.hellenicshippingnews.com/omans-oil-exports-hit-230-6m-barrels-by-september-official-data/
[4] QCIntel, "Oman maintains crude export volumes despite Duqm reaching capacity" — 52,43 mln vaten jan-feb 2024 (~874 kb/d), 80-90% van het maandprogramma naar China. https://www.qcintel.com/article/oman-maintains-crude-export-volumes-despite-duqm-reaching-capacity-22950.html
[5] OpenStreetMap (ODbL), way 149963619 via de OSM-API 2026-10-31: `man_made=pipeline`, `substance=oil`, `usage=transmission`, `source=Bing`, versie 13. https://www.openstreetmap.org/way/149963619
[6] OpenStreetMap (ODbL), way 586118047: `man_made=pipeline`, `substance=oil`, 19 nodes, 23.5764, 58.4087 → 23.6214, 58.5129. https://www.openstreetmap.org/way/586118047
[7] Esri World Imagery via `v2/tools/sat_check.py`, `v2/build-cache/satcheck/sat-olie-fahud-minaalfahal-*.png`: fahud (z15), saihalmaleh (z14), tanks (z16).
[8] Eigen pure-Python pbf-scan van de lokale Geofabrik-extract gcc-staten, 2026-10-31 (`maak_leidingbeen_olie_fahud_minaalfahal.py --schrijf`): 245 punten, 276,9 km, kop 22.22184, 56.55973, staart 23.62138, 58.51288.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)

**Recept:** `bash v2/tools/bak_stromen.sh olie-fahud-minaalfahal` (zwaar-slot, 14 s) -> `v2/data/stroomroute-olie-fahud-minaalfahal.json` (5,5 KB). Eén `--been-geojson "leiding|..."` met de vooraf gestikte FeatureCollection `v2/build-cache/ais/graaf/olie-fahud-minaalfahal-leiding-pdo.geojson` (uit `maak_leidingbeen_olie_fahud_minaalfahal.py --schrijf`), twee markers. Geen profiel, geen extract in de bake, geen zee/MARNET, geen haven-aanloop, geen stippel, geen kopie, geen vlucht.

| # | modaliteit | km | punten | naad | stippel |
|---|---|---|---|---|---|
| 1 | leiding (PDO Main Oil Line, 2 OSM-ways) | 276,9 | 245 | 0 | nee |

Totaal 276,9 km, 2 markers (Fahud-pompstation 5 m en Mina al-Fahal-tankenpark 3 m van de lijn). Brief 276,9 (OSM-som) tegen 276 gepubliceerd = +0,3%; gebakken km = brief-km. `toets_knikken`: 0 knikken, 0 omkeringen. `toets_rechte_benen`: geen rechte lijn voor dit been. json: versie 2, punt_formaat lonlat, modaliteit leiding, 5,5 KB.

**Leiding:** volledig doorgetrokken; geen offshore-stuk (onderzeese buis en SBM-monoboeien staan niet in OSM, niet getekend). Identiteit van de lijn steunt op lengte en begin/eind (naamloze Bing-ways), zoals in §7.

**Lessen:** (1) de bake van een leidingbeen met een kant-en-klare FeatureCollection draait in seconden en heeft geen slot-pool buiten `zwaar` nodig. (2) `bash v2/tools/bak_stromen.sh` leest het bestand incrementeel: bij gelijktijdige edits door andere agenten verscheen na de gelukte bake een ruis-foutmelding (regel 15204, andermans tekst); de stroom zelf was al volledig geschreven en gecontroleerd. (3) Gedeeld bak-bestand bleef LF (0 CRLF) en `bash -n` schoon.
