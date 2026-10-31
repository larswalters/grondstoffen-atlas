# Routebrief (licht) · olie — Europoort (Rotterdam) → Rotterdam-Rijn-Pijpleiding → Köln-Godorf (Duitsland)

**stroom-id:** `olie-europoort-godorf` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** Ruwe olie die in Rotterdam (Europoort/Maasvlakte) per tanker wordt gelost, gaat via de Rotterdam-Rijn-Pijpleiding (RRP, 36 inch, ondergronds) 176 km naar het Venlo-tankpark en daarna door de 24-inch-zuidtak naar de Shell-raffinaderij Rheinland, Werk Nord in Köln-Godorf: **twee doorgetrokken OSM-leidingbenen (175,6 + 80,3 km) en een stippelslot van 12,3 km** (Hurth → Godorf, niet in OSM); geen zee-, weg-, spoor- of luchtbeen.
**Welke as van het verhaal:** *Nederland als doorvoerland voor Rijnlandse raffinage* — Rotterdam voert crude aan (95–100 Mt/j de haven in, de helft naar raffinaderijen in Vlissingen, Antwerpen en Duitsland [4]); de RRP is de pijp die het Duitse deel levert. **Capaciteit ruwe-oliepijp 22 Mt/j ≈ 442 kb/d** (nl.wikipedia, geen peiljaar) [1]; afnemer Godorf **9 Mt/j ≈ 181 kb/d** verwerkingscapaciteit (stand 2017) [2]. **Werkelijke doorvoer niet gevonden**; RRP als geheel (ruwe olie plus producten) 25 Mt/j [3].

## 1 · Ketenkaart
```
(tankers, herkomst per haven niet gebronnen; Europoort/Maasvlakte-crudeterminals)
  ──► RRP-station Europoort `ol-europoort-rrp-begin`
  ──(a1 leiding · Rotterdam-Rijn-Pijpleiding ruwe olie 36 inch · 175,6 km OSM-som, 176 gepubliceerd)──►
  RRP-tankpark Venlo `ol-venlo-rrp-tankpark`  (11 tanks, 212.000 m3)
  ──(a2 leiding · Rotterdam-Rhein-Pipeline 24 inch, ref RRP 8 · 80,3 km OSM)──► OSM-leidingeinde Köln-Hurth (50.9285, 6.8464)
  ──(a3 STIPPEL leiding · RRP-slot, niet in OSM · 12,3 km hemelsbreed)──► Werk Nord Godorf `ol-godorf-werk-nord` ── stoppunt
```
Geen zeebeen: geen bron koppelt deze lading aan een laadhaven of terminal. Geen via-punten: elk been is één OSM-leidingstreng, gestikt op gedeelde nodes.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| a1 | A | leiding | RRP-station Europoort → Venlo-tankpark | Rotterdam-Rijn-Pijpleiding Europoort - Venlo, 36 inch [1][5] | **175,6 OSM-som tegen 176 gepubliceerd** [1]: −0,2% | `maak_leidingbeen_olie_europoort_godorf.py` (10 OSM-ways) | nee |
| a2 | A | leiding | Venlo → Köln-Hurth (OSM-eind) | Rotterdam-Rhein-Pipeline 24 inch, ref RRP 8 [5] | **80,3 OSM**; gepubliceerd 103 km Venlo → raffinaderij [1] (zie a3) | zelfde tool (2 OSM-ways) | nee |
| a3 | A | leiding | Köln-Hurth (OSM-eind) → Godorf Werk Nord | RRP-slot, niet gekarteerd | **hemelsbreed 12,3 km, geen leidingkm** | `--stippel "leiding\|…"` | **ja: hier reikt het net niet** (OSM mist het slot) |

a1: 175,6 km tegen 176 = −0,2%, binnen de norm. a2 + a3 = 92,6 km (80,3 + hemelsbreed 12,3) tegen 103 gepubliceerd = −10%: binnen ±15%, maar het slot is hemelsbreed en de werkelijke leiding is langer. Totaal 268,2 km tegen 279 gepubliceerd (176 + 103) = −3,9%. Stippelaandeel 12,3 van 268,2 km = 4,6%.
Ways a1 in volgorde: 849066299, 849069178, 972208482, 972208481, 849221217 (onderwater, kruising Hollands Diep), 849221219, 849069176, 307504353, 319472294, 849069175 (0 naden). a2: 139710565, 298322327 (naad a1 → a2: 27 m bij Venlo). Niet gestikt: de productleiding Pernis - Venlo (way 849221218, 949714698 e.a.), de noordtak naar Gelsenkirchen (43 km) en de RMR-productleiding.
Fase C/D/E vervallen: Godorf is de afnemer die [2] noemt; geen bron noemt een vervolg van deze lading.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-europoort-rrp-begin` | begin leiding | RRP-station Europoort, Moezelweg 403 (OSM landuse "Rotterdam-Rijn Pijpleiding Europoort", way 755355922; leidingbegin way 849066299) | 51.9386, 4.1441 | [5][6] | **bron-gelegd** (z15 gezien: het punt ligt aan de zuidrand van een groot tankenpark (tientallen witte drijfdaktanks), naast een klein gebouwencomplex aan de Moezelweg vlak boven de Dintelhavenbrug; de terminal die levert is niet te herkennen) |
| `ol-venlo-rrp-tankpark` | tussenstation / tankpark | RRP-tankpark Venlo, Manegeweg 20 (OSM-kantoor RRP, node 2924710587; leiding op 80 m) | 51.3789, 6.2160 | [3][5][6] | **bron-gelegd** (z15 gezien: rond een dozijn drijfdaktanks in een boskader met gebouwen en pompstation, naast een snelweg; de leiding passeert 80 m oostwaarts) |
| `ol-godorf-werk-nord` | eindafnemer / raffinaderij | Shell Energy and Chemicals Park Rheinland, Werk Nord Godorf | 50.8597, 6.9844 | [2][7] | **bron-gelegd** (z15 gezien: het punt ligt midden in het raffinaderijterrein, tussen tankrijen en procesinstallaties, Rijn 1,5 km zuidoostwaarts) |

Geen anker: het OSM-leidingeinde Köln-Hurth (50.9285, 6.8464). z15: Autobahnkreuz met bos en woonwijk, geen site (onzeker; alleen het beginpunt van het stippelslot). Hergebruik: geen letterlijk gedeeld been; `olie-wilhelmshaven-koeln` eindigt 1,7 km verderop (50.9438, 6.8503) op een **andere** leiding (NWO); `olie-corpuschristi-rotterdam` heeft de Maasvlakte Olie Terminal (51.97273, 4.06243) alleen als zeekant (niet gedeeld). Sitelaag `olie-sitelaag.json`: geen Europoort-, Venlo- of Godorf-site; Shell Pernis (`w-pernis`, 51.8827, 4.3833, onzeker) is een andere raffinaderij en wordt niet hergebruikt.

## 4 · Via-punten
Leiding: geen corridorkeuze. Naden: a1 heeft er geen (de Hollands Diep-kruising is met de ways 972208482/972208481/849221217 aaneengesloten), a1 → a2 27 m bij Venlo; a2 → a3 begint op het OSM-eind. Geen haven-aanloop (geen zeebeen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| RRP (Rotterdam-Rijn Pijpleiding Maatschappij) | Shell Petroleum 45,6%, Ruhr Oel 22,2%, BP Olex Fanal 22,2%, Shell Deutschland Oil 10% (2011) | crude van Europoort-terminals → Venlo → Duitsland | ruwe-oliepijp 22 Mt/j; netwerk 475 km, 25 Mt/j alle producten | [1][3] |
| Venlo-tankpark | RRP | crude, splitsing noord (Gelsenkirchen 43 km) en zuid (103 km) | 11 tanks, 212.000 m3 | [1][3] |
| Godorf, Werk Nord | Shell Deutschland | crude → producten | 9 Mt/j (2017) | [2] |

## 6 · Stoppunt
De brief stopt bij Werk Nord Godorf: [1] noemt de Rheinland-raffinaderij als eindbestemming van de zuidtak en [2] zegt dat beide Shell-werken hun crude van de RRP krijgen; Wesseling stopte de ruwe-olieverwerking in 2025, Godorf blijft draaien. Geen bron noemt een volgende locatie voor deze lading; geen zeebeen voor Europoort omdat geen laadhaven gebronnen is.

## 7 · Open punten
- **Werkelijke doorvoer onbekend.** 22 Mt/j is pijpcapaciteit [1]; een zoekresultaat citeert een Concawe-poster met 16 Mt/j (36 inch) en 7 Mt/j (24 inch), ongedateerd, niet zelf gelezen. Wesseling-vraag is in 2025 weggevallen, dus reële vraag lager dan capaciteit.
- **Terminal in Europoort niet gebronnen**: het anker is het RRP-station (OSM), niet een benoemde terminal; omliggende parken heten o.a. TEAM Terminal (51.9422, 4.1497) en Shell Europoort Terminal (51.9471, 4.1404) volgens OSM, de aanvoer ernaartoe is niet getekend.
- **Het RRP-slot Hurth → Godorf (12,3 km hemelsbreed) ontbreekt in OSM** en wordt gestippeld; of het slot Hurth aandoet is niet gebronnen, het OSM-eind valt in een knooppuntzone.
- **Herkomst crude niet gebronnen** per tanker; Rotterdam krijgt vooral VS en Noordzee [4], geen koppeling aan deze pijp.
- **Km a2 + a3 = −10%** tegen 103 (gepubliceerd tot de raffinaderij); de 103 km wordt niet uit een leidingbron bevestigd.
- Productleiding Pernis → Venlo (153 km, RMR-aansluiting) loopt parallel en is bewust niet getekend.

## 8 · Bronnen
[1] Wikipedia (nl), "Rotterdam-Rijn Pijpleiding Maatschappij" — 176 km Europoort → Venlo, 36 inch, 22 Mt/j, 3.000 m3/u; zuidtak 103 km naar de Rheinland-raffinaderij, noordtak 43 km; aandeelhouders (2011); 475 km netwerk. https://nl.wikipedia.org/wiki/Rotterdam-Rijn_Pijpleiding_Maatschappij
[2] Wikipedia (de), "Rheinland Raffinerie" — Werk Nord Godorf 9 Mt/j, Werk Wesseling 7 Mt/j (Rohöl-Verarbeitung 2025 beendet), Rohöl für beide Werke über die Rotterdam-Rhein-Pipeline; coördinaat Godorf. https://de.wikipedia.org/wiki/Rheinland_Raffinerie
[3] RRP, home — 475 km eigen netwerk, 25 Mt/j ruwe olie en producten, 11 tanks in Venlo met 212.000 m3, Venlo Manegeweg 20. https://www.rrpweb.nl/
[4] Port of Rotterdam, "Crude oil" — 95–100 Mt/j crude, helft naar raffinaderijen in de haven, de rest naar Vlissingen, Antwerpen en Duitsland; terminals Europoort en Maasvlakte. https://www.portofrotterdam.com/en/logistics/cargo/liquid-bulk/crude-oil
[5] OpenStreetMap (ODbL) — 12 ways via api.openstreetmap.org/api/0.6 (gemeten 2026-10-31, cache `v2/build-cache/olie-europoort-godorf-osmapi-cache.json`), bbox-controle Hollands Diep, pyosmium-scan de-nrw rond Godorf (alleen werkterrein-fragmenten, geen RRP-slot). https://api.openstreetmap.org/api/0.6/way/849066299
[6] OpenStreetMap via Photon: landuse "Rotterdam-Rijn Pijpleiding Europoort" (W755355922), kantoren RRP Manegeweg (N2924710587). https://photon.komoot.io
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-olie-europoort-godorf-start.png`, `-venlo.png`, `-eind.png`, `-osmeind.png`.
[8] Wikipedia (de), "Rhein-Main-Rohrleitungstransportgesellschaft" — RMR-productleiding Venlo → Frankfurt, pompstation Köln-Godorf (context, niet getekend). https://de.wikipedia.org/wiki/Rhein-Main-Rohrleitungstransportgesellschaft
[9] Concawe, "Posters: RRP" — alleen gevonden via zoekresultaat (capaciteit 16 en 7 Mt/j), pagina niet leesbaar. https://www.concawe.eu/?p=15689
[10] Routebrieven `olie-wilhelmshaven-koeln` (Godorf/Wesseling, RRP-context, NWO-eind 50.9438, 6.8503) en `olie-corpuschristi-rotterdam`; v1 `data/oil.js` en `design/olie.md` (checklist, geen anker).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-olie-europoort-godorf.json` (16,3 KB, versie 2, lonlat) · **totaal 268,2 km · 823 punten · 3 markers** · functie `bak_olie_europoort_godorf` in `v2/tools/bak_stromen.sh`.
| # | modaliteit | km | punten | stippel |
|---|---|---|---|---|
| a1 | leiding | 175,6 (176 gepubliceerd, -0,2%) | 584 | nee |
| a2 | leiding | 80,3 (OSM) | 237 | nee |
| a3 | leiding | 12,3 (hemelsbreed) | 2 | ja, RRP-slot niet in OSM |
**Markers** (afstand tot lijn): Europoort-station 20 m, Venlo-tankpark 59 m, Godorf Werk Nord 0 m. **Naden:** a1-a2 26 m, a2-a3 6 m (max 0,03 km).
**Recept:** `python v2/tools/maak_leidingbeen_olie_europoort_godorf.py --schrijf` (OSM-API, 12 ways), daarna `bash v2/tools/bak_stromen.sh olie-europoort-godorf`. Geen zee, weg, spoor of vlucht; geen profiel in `maak_stroombeen_weg.py`; geen haven-aanloop.
**Toelichting stippel a3:** hier reikt het net niet; het RRP-slot Köln-Hurth naar Godorf ontbreekt in OSM, dus rechte lijn 12,3 km (hemelsbreed, geen leidingkm). a2+a3 = 92,6 km tegen 103 gepubliceerd (-10%), binnen de indicatie.
**Toets:** `toets_knikken.py` 14 knikken >= 60 graden, 0 omkeringen, 0 terugloop (OSM-geometrie van de leiding zelf, o.a. nabij Neuss/Kaarst, niet aangeraakt); `toets_rechte_benen.py --min-km 5` meldt alleen de a3-stippel (12,3 km, bewust).
**Lessen:** een volledige OSM-leidingstreng is met een eigen maak_leidingbeen-tool in een minuut gestikt (nul naden bij a1); de ontbrekende laatste kilometers zijn een stippel met reden, niet een verzonnen tracé. Eindpunt valt 1,7 km van `olie-wilhelmshaven-koeln` (andere leiding, NWO), niet gedeeld.
