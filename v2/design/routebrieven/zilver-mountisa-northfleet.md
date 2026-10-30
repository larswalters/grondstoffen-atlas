# Zilver · Mount Isa-loodsmelter → Townsville Berth 3 → Britannia Refined Metals, Northfleet (Verenigd Koninkrijk)

**stroom-id:** `zilver-mountisa-northfleet` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** lood-zilverbullion (blokken van 4,1 t) uit de loodsmelter van Mount Isa Mines (Glencore, Queensland) per **spoor** (Great Northern Railway / Mount Isa-lijn, ~1.000 km) naar Berth 3 van de haven van Townsville, daarna per **zeeschip** naar Britannia Refined Metals (Glencore) in Northfleet aan de Thames, waar het zilver uit het lood wordt gescheiden; stoppunt bij de raffinaderij.
**Welke as van het verhaal:** *Australisch lood-zilver naar de Londense edelmetaalmarkt* (hetzelfde Glencore-systeem als het Britse zilver van Valcambi/Londen): 11,36 Moz Ag in ruw lood = ca. **353 t Ag/j** met 160 kt lood in bullion (peiljaar 2005, bron [3]). Recenter bullioncijfer niet gevonden; indicatie 2025: Mount Isa 3.405 koz Ag in concentraat = ca. 106 t Ag (secundair, concentraat, geen bullion) [10]. BRM zelf: 160 kt lood/j en tot 350 t LBMA-zilver/j [4][5].

## 1 · Ketenkaart
```
Mount Isa-loodsmelter `ag-mountisa-loodsmelter` ──(b1 spoor · Great Northern Railway via Cloncurry, Julia Creek, Hughenden, Charters Towers · 977 km gemeten, "nearly 1,000" gepubliceerd)──►
Townsville Berth 3 `ag-townsville-berth3` ──(b2 zee · MARNET Torres-Indische Oceaan-Suez-Kanaal · ~20.970 km, aannemelijk: één bron)──►
Britannia Refined Metals, Northfleet `ag-brm-northfleet` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Mount Isa-loodsmelter → Townsville Berth 3 | Great Northern Railway (Mount Isa-lijn): Duchess–Cloncurry–Julia Creek–Hughenden–Charters Towers–Townsville | "nearly 1,000" [6]; gemeten 977,3 (router) / 979,2 (json), -2% | toets_spoorroute (BAKE_SUFFIX=-raw, extract `australie`), één run, geen via-punt | nee |
| b2 | B | zee | Townsville Berth 3 → Northfleet (BRM) | niet gebronnen; bron zegt alleen "shipped to Britannia Refined Metals in England" [2] | geen gepubliceerde zeeroute; MARNET meet 20.968 (hemelsbreed ~15.400) | MARNET (kade → kade) | aanloop: nee (snap 2,8 en 1,7 km, beide < 5 km) |

Beennamen: b1 `trein Mount Isa-loodsmelter → Townsville Berth 3 (Great Northern Railway/Mount Isa-lijn, 1-op-1-net)`; b2 `zeeschip Townsville Berth 3 → Northfleet (aannemelijk: één bron)`. Geen b3: het landbeen eindigt op het site-anker, BRM ligt 0,2 km van de rivier.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-mountisa-loodsmelter` | laadplek bullion (kop b1) | Mount Isa Mines-loodsmelter (Glencore) | -20.7249, 139.4833 | OSM building "Lead Smelter" (way 116434830) + "Lead Smelter Stack" (-20.7233, 139.4825) [8] | bron-gelegd (z16 gezien: smelterhallen met schoorsteen en spoorbundel aan de oostrand van het complex, naast de hoofdlijn; spoor snapt op 0,16 km) |
| `ag-townsville-berth3` | losplek spoor / laadplek zee (overgang b1 → b2) | Haven van Townsville, Berth 3 (NSS-kade, "lead bullion … exported through Berth 3") | -19.2480, 146.8362 | Glencore port operations [1]; berth-tabel [7]; OSM-node Berth 3 (-19.2481, 146.8358, in het water) [8], 35 m oostwaarts op de kade gelegd | bron-gelegd (z17 gezien: kadefront met containerstapels en opslagterrein erachter, geen portaalkraan op dit stuk; spoor snapt op 0,07 km) |
| `ag-brm-northfleet` | losplek zee / raffinaderij (staart b2) | Britannia Refined Metals Ltd, Botany Road, Northfleet | 51.4554, 0.3214 | OSM way 675320941 (metal_refinery, works) [8]; adres Botany Road, Northfleet, Gravesend DA11 9BG [5] | aannemelijk (z15 en z17 gezien: groot raffinaderijcomplex met hallen en zonnepanelen aan de zuidoever van de Thames; geen benoemde kade, 0,2 km oostelijk een klein betonnen steigertje/helling dat voor zeeschepen te klein lijkt) |

Hergebruik: Townsville Berth 11 (-19.2441, 146.8358, `ag-townsville-haven`, brief zilver-cannington-townsville) is de South32-concentraatlader [7] en wordt hier NIET gebruikt; het ontwerp noemde hem ten onrechte (zie §7).

## 4 · Via-punten
Geen. De Mount Isa-lijn is de enige spoorverbinding; één directe run (977,3 km, 713 edges, verhouding 1,24 op de grootcirkel 785,6 km, 0 bochten >= 60°) passeert Cloncurry (1,2 km ernaast), Julia Creek (1,0), Hughenden (1,4) en Charters Towers (0,7). Zee: MARNET routeert kade → kade zonder via-punt; de lijn loopt via Torres Strait, Indische Oceaan, Bab-el-Mandeb, Suez en het Kanaal.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mount Isa-loodsmelter | Glencore | loodconcentraat (George Fisher, evt. McArthur River) → lood-zilverbullion (4,1 t-blokken) | 160 kt Pb en 11,36 Moz Ag in bullion (2005); nu lager | [3][9][10] |
| Britannia Refined Metals, Northfleet | Glencore | bullion + recyclingfeed → raffinaderijlood en LBMA-zilver (99) | ~160 kt Pb/j; tot 350 t Ag/j | [4][5] |

## 6 · Stoppunt
De brief stopt bij BRM: dat is de bestemming die de bron noemt ("shipped to Britannia Refined Metals", daarna verkoop op de LME) en de plek waar het zilver van het lood wordt gescheiden; geen bron noemt de afnemer van het zilver, dus fase D/E vervallen.

## 7 · Open punten
- **Berth 3 i.p.v. Berth 11 (afwijking van het ontwerp):** Glencore noemt voor lood-bullion Berth 3 met Northern Stevedoring Services [1]; Berth 11 is de South32-lader [7]. De Berth 3-kade is gelegd op de kade, de tegels tonen containerstapels (NSS is een algemene kade); of de bullion daar in containers of als losse blokken wordt geladen is niet gevonden.
- **Actualiteit:** Glencore-historiepagina (2021, via zoekresultaat, directe fetch 404) en mining-technology (2005) noemen de route spoor + schip naar BRM [2][3]; of dat in 2026 nog rechtstreeks gebeurt is niet bevestigd. Het BRM-rapport 2025 noemt als lood-feed alleen "two other Glencore industrial assets" zonder namen [5].
- **Zeeroute niet gebronnen:** MARNET kiest Suez via de Rode Zee; een bron over Kaap of Suez ontbreekt (km 20.968 is de router, geen gepubliceerd getal).
- **BRM-kade niet bevestigd:** geen bron noemt een Thames-wharf van BRM; het anker is de werkplaats (OSM), MARNET-zeeknoop 1.591 ligt 1,7 km oostwaarts in de rivier. Geen haven-aanloop nodig (< 5 km).
- **Recent volume ontbreekt:** 353 t Ag/j is peiljaar 2005; de smelter draait door (ILZSG feb 2026 volgens de haalbaarheidstoets, niet zelf geopend) maar de bullionhoeveelheid 2025/26 is onbekend.
- **Overlap:** b1 deelt de rails met zilver-cannington-townsville b2 (765 van 977 km) en koper-mountisa-townsville; eigen run omdat het eindpunt (Berth 3) en het beginpunt (loodsmelter 0,5 km noordelijk van de kopersmelter) verschillen; b2 is nieuw.

## 8 · Bronnen
[1] Glencore Australia, Port operations — lood-bullion en kopergecathode via Berth 3 (laden door Northern Stevedoring Services), concentraten via Berth 8. https://glencore.com.au/operations-and-projects/qld-metals/operations/glencore-port-operations
[2] Glencore Australia, "A remarkable 90 years of lead smelting at Mount Isa Mines" (2021): bullion in 4 t-blokken, per spoor naar Townsville, per schip naar BRM, verkoop LME (zoekresultaat; pagina gaf 404 bij fetch). https://www.glencore.com.au/operations-and-projects/qld-metals/resourceful/resourceful-august-2021/a-remarkable-90-years-of-lead-smelting-at-mount-isa-mines
[3] Mining-technology, Mount Isa lead (2005: 160 kt lood in bullion, 11,36 Moz Ag in ruw lood, raffinage in Northfleet UK). https://www.mining-technology.com/projects/mount_isla_lead/
[4] Glencore, "BRM opens new sampling plant" (okt 2025): 160.000 t lood/j, tot 350 t LBMA-zilver/j, Gravesend/Northfleet sinds 1930. https://www.glencore.com/media-and-insights/insights/2025-10-glencores-britannia-refined-metals-opens-new-sampling-plant-to-support-critical-mineral-recovery
[5] Glencore, 2025 BRM Public Responsible Supply Chain Due Diligence Report (adres Botany Road, 350.000 kg zilver/j, feed uit twee Glencore-assets + recycling). https://www.glencore.com/.rest/api/v1/documents/static/d2a91885-2dab-4529-8230-d7d54b0c4484/2025+BRM+Public+Responsible+Supply+Chain+Due+Diligence+Report.pdf
[6] Wikipedia, "Great Northern Railway (Mt Isa line)", "nearly 1,000 kilometres" (overgenomen uit routebrieven/koper-mountisa-townsville.md [3]). https://en.wikipedia.org/wiki/Great_Northern_Railway_(Mt_Isa_line)
[7] Port of Townsville, berth information (Berth 3 NSS common user, Berth 11 South32 concentrates). https://s3-ap-southeast-2.amazonaws.com/os-data-2/port-townsville/documents/berth_information_website_final.pdf
[8] OpenStreetMap (ODbL) via Overpass: Berth 3 node 12099718775, Lead Smelter way 116434830, BRM works way 675320941, piers 5229997/5229998. https://www.openstreetmap.org
[9] Mount Isa Mines Fact Sheet 2020 (producten naar Townsville, bullion 4,1 t). https://minedocs.com/20/Mount_Isa_Mines_Fact_Sheet_2020.pdf
[10] Kadoa, Mount Isa production (2025: 3.405 koz Ag in concentraat; Q1 2026 lood 19,8 kt), secundair. https://www.kadoa.com/mining/mine/mount-isa
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15–z18) — `v2/build-cache/satcheck/sat-zilver-mountisa-northfleet-loodsmelter.png`, `-berth3.png`, `-brm.png`, `-brm-zoom.png`, `-brmkade.png`, `-smelter.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Bestand:** `v2/data/stroomroute-zilver-mountisa-northfleet.json` (71,5 KB, contract versie 2, punt_formaat lonlat) · **recept:** `bak_zilver_mountisa_northfleet()` in `v2/tools/bak_stromen.sh` · **totaal 21.947,5 km, 3.859 punten, 3 markers, 0 stippel.**

| # | modaliteit | km (json) | punten | naad naar vorige | geometrie |
|---|---|---|---|---|---|
| b1 | spoor | 979,2 (router 977,3; "nearly 1,000" [6]: -2%) | 1.698 | — | `spoorroute-zilver-mountisa-northfleet-loodsmelter-berth3.geojson` (toets_spoorroute, BAKE_SUFFIX=-raw, 713 edges, geen via-punt, 0 bochten >= 60 gr) |
| b2 | zee | 20.968,3 (geen gepubliceerd getal) | 2.161 | 2,78 km (Berth 3-snap) | MARNET kade → kade, 125 edges, snaps 2,80 en 1,68 km (< 5 km, geen haven-aanloop) |

**Markers (3):** `ag-mountisa-loodsmelter` 0,16 km van b1; `ag-townsville-berth3` 0,07 km van b1; `ag-brm-northfleet` 1,68 km van het b2-eind (zee-snap naar zeeknoop in de Thames, onder de 5 km-aanloopgrens).

**Toets:** km b1 binnen ±15%; naad 2,78 km (< 5 km); `toets_knikken` 4 knikken >= 60 gr, allemaal op de zeeroute (Noordzee 51,47N 1,47E; Theems-monding 51,45N 0,43E; Kaap St. Vincent 36,80N -9,25W; Torres-straat -10,45 143,02), 0 omkeringen, 0 terugloop; `toets_rechte_benen` geen treffer; json.load, versie 2, lonlat, modaliteiten {spoor, zee}, elk been >= 2 punten.

**Recept:** één spoorrouter-run kop → staart zonder via-punt (de lijn is de enige verbinding; geojson was al gebakken en is hergebruikt, 33,9 KB); één `--been zee` kade → kade. Geen weg, geen leiding, geen vlucht, geen kopie, geen stippel, geen haven-aanloop, geen via-punten.

**Toelichting:** geen stippel in deze keten: het spoor reikt van smelter tot kade (beide snappen < 0,2 km) en de zee-snaps zijn < 5 km. Het zeebeen is "aannemelijk: één bron" (de bestemming BRM staat in een bron, de route niet) — dat staat in de beennaam, de lijn is doorgetrokken. Een wegbeen ontbreekt bewust: de bronnen noemen alleen spoor + schip.

**Lessen / bevindingen:** (1) het b1-spoor deelt 765 van 977 km met zilver-cannington-townsville b2 en vrijwel de hele lijn met koper-mountisa-townsville: bewuste eigen run (ander begin- en eindpunt), geen kopie. (2) Het BRM-anker ligt op de OSM-werkplaats; MARNET eindigt 1,68 km oostwaarts in de Thames: gezien de 5 km-regel geen aanloop, wel een bekend procesgat. (3) De zeeroute (Suez via de Rode Zee, 20.968 km) is de router en niet gebronnen; bij Rode Zee-omleidingen via de Kaap zou de werkelijke afstand groter zijn.
