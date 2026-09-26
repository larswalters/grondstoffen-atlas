# Routebrief (licht) · kobalt — Morowali (Indonesië) → Ningbo (China)

**stroom-id:** `kobalt-morowali-quzhou` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** MHP (mixed hydroxide precipitate, 4–5 % Co) van de Huayue-HPAL-plant in het Morowali Industrial Park (IMIP, Sulawesi) gaat over het eigen parkterrein naar de Labota-jetty (IMIP-haven), per **zeeschip** naar de containerkade Ningbo Beilun — dezelfde kade als de Congolese as `kobalt-tfm-quzhou` — en de lijn stopt daar: geen bron met een vindbare coördinaat koppelt deze lading aan de vervolgroute naar Huayou Quzhou.
**Welke as van het verhaal:** de Indonesische groei-as die het Congolese exportquotum opvangt. Indonesië dolf 44 kt Co in 2025 (USGS MCS 2026; Cobalt Institute 42,5 kt, +29 %) — "Indonesian supply in 2025 was greater than DRC exports" [4]. Huayue (IMIP) is Huayou's HPAL-fabriek op Sulawesi; Huayou's eigen due-diligence-rapport 2024 zegt letterlijk: *"Huayue's production address is Morowali Industrial Park (IMIP) … and the transportation routes are mainly from Labota Jetty, an Indonesian port, to Zhapu/Ningbo ports in China"* [3]. MHP is formeel een **nikkelproduct**: deze kaart tekent hier een nikkelstroom met kobalt als bijproduct (4–5 % Co) — dezelfde MHP draagt ook de nikkelkaart (`nikkel-morowali-quzhou`).

## 1 · Ketenkaart
```
Huayue HPAL-plant `co-morowali-huayue` ──(b1 truck · parkintern · ~3,5 km, stippel)──► Labota-jetty `co-labota-jetty`
   ──(b2 zee-aanloop · Golf van Tolo · ~93 km, stippel)──► zeeknoop 5491 (-2.0357, 122.0017)
   ──(b3 zee · Golf van Tolo → Banda-/Molukse Zee → Filipijnenzee/Zuid-Chinese Zee → Oost-Chinese Zee · ~4.500 km)──► zeeknoop 5850 (29.9758, 121.9736)
   ──(b4 zee-aanloop · ~5,6 km, stippel — zelfde aanloop als `kobalt-tfm-quzhou`)──► Ningbo Beilun containerkade `co-ningbo-kade` ⏹ stoppunt
        ┊ (niet getekend — Huayou Quzhou-coördinaat niet gevonden, zie `kobalt-tfm-quzhou.md` §7)
   Huayou New Energy Technology (Quzhou) `co-quzhou-smelter` (knoop, §5)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (parkintern) | `co-morowali-huayue` → `co-labota-jetty` | interne IMIP-parkweg, MHP in bigbags/containers | ~3,5 hemelsbreed (geen publicatie) | stippel "binnen estate (geen net)" — Grasberg/JIIPE-klasse, geen wegscan | ja — eigen terrein, geen net op deze korrel |
| b2 | B | zee (haven-aanloop) | `co-labota-jetty` → zeeknoop 5491 | Golf van Tolo (Labota ligt ~93 km van de dichtstbijzijnde MARNET-zeeknoop) | ~93 (gemeten, toets M29) | `maak_havenaanloop.py` onder timeout 300; bij "geen pad" terugval rechte stippel | ja — MARNET reikt hier niet, de zwaarste aanloop van de zes kobaltassen |
| b3 | B | zee | zeeknoop 5491 → zeeknoop 5850 | Golf van Tolo → Banda-/Molukse Zee → Filipijnenzee/Zuid-Chinese Zee → Oost-Chinese Zee | ~4.500 (hemelsbreed ~3.900; MARNET meet exact) | MARNET `--been "zee\|…\|-2.0357,122.0017\|29.9758,121.9736"` | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop 5850 → `co-ningbo-kade` | Beilun-containerzone | ~5,6 (indicatief — **letterlijke kopie** van `kobalt-tfm-quzhou.md` b2a) | `maak_havenaanloop.py` (of hergebruik het geojson van `kobalt-tfm-quzhou` als het al gebakken is) | ja — MARNET reikt niet tot de kade |

**Been C (Ningbo → Huayou Quzhou, NIET getekend):** de bron noemt de route wel ("Zhapu/Ningbo ports … to Quzhou" [3]) maar geen coördinaat voor de Quzhou-fabriek is deze sessie te vinden — zelfde uitkomst als `kobalt-tfm-quzhou.md` §7 (het MEE-emissieregister gaf herhaald een 302 naar `errorinfo.jsp`, OSM heeft geen naam-tag). Regel "de lijn eindigt waar het bewijs eindigt": Huayou Quzhou staat als losse knoop in §5, geen been.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-morowali-huayue` | mijn / HPAL-plant | PT Huayue Nickel Cobalt, Morowali Industrial Park (IMIP), Sulawesi | -2.8371, 122.1658 | [1][3][9][10] | aannemelijk (z15 gezien: aaneengesloten industriecomplex met tientallen blauwe hallen, ertsstapels en actieve rook/stoompluimen — consistent met een HPAL/RKEF-complex; IMIP is één OSM-landuse-vlak zónder bedrijfsnaam-tag, dus het exacte Huayue-perceel binnen het 2.000 ha-park is niet te onderscheiden van buurbedrijven zoals QMB) |
| `co-labota-jetty` | overslag parkweg → zee | Labota-jetty, IMIP-havenzone (bij de Sulawesi Labota-kolencentrale) | -2.8606, 122.1871 | [3][9][10] | bron-gelegd (OSM `man_made=pier`/`mooring=private` op dit punt; z15 gezien: meerdere lange pieren met schepen langszij, breakwaters en een havenweg naar het achterland — welke specifieke pier de MHP-kade is (i.t.t. de NPI-/kolenkades ernaast) is op deze resolutie niet te onderscheiden) |
| `co-ningbo-kade` | overslag zee → (onbekend vervolg) | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | `kobalt-tfm-quzhou.md` §3 [11] | bron-gelegd (**hergebruikt anker, letterlijke kopie** — zelfde punt als `co-ningbo-kade` in `kobalt-tfm-quzhou.md`, niet opnieuw satelliet-gecheckt) |
| `co-quzhou-smelter` | raffinaderij (knoop, niet aan een been gekoppeld) | Huayou New Energy Technology (Quzhou) Co., Ltd. — No. 18 Nianxin Road, Hi-tech Industrial Park fase II, Quzhou (Zhejiang) | **niet gevonden** | [3][7][8][11] | onzeker/open — zelfde MEE-endpoint-storing als `kobalt-tfm-quzhou.md`; coördinaat niet verzonnen |

## 4 · Via-punten
Geen — been b1 is een parkinterne stippel zonder corridorkeuze, benen b2/b3/b4 zijn zeebenen (router, geen via-punten).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Huayue HPAL-plant (IMIP) | Huayou Cobalt (Huaqing Nickel and Cobalt) | lateriet-erts (Sulawesi) → MHP (4–5 % Co) | nameplate 7,8 kt Co/j (naast nikkel); Huayue+Huafei samen 236.500 t MHP verscheept in 2025, +30 % (≈ 10–12 kt Co, alléén als afgeleide — dit cijfer dekt óók Huafei/Weda Bay, niet uitsplitsbaar naar Huayue alleen) | [1][5][6] |
| Ningbo Beilun containerkade | Ningbo Zhoushan Port Group | overslag zeeschip → onbekend vervolgtransport | containerterminal, meerdere fasen (gedeeld met `kobalt-tfm-quzhou`) | [9][11] |
| Huayou Quzhou — **knoop, niet gekoppeld** | Zhejiang Huayou Cobalt | MHP + kobalthydroxide → sulfaat/tetroxide/precursor | zie `kobalt-tfm-quzhou.md` §5 (ongeverifieerd, paywall) | [7][8] |

## 6 · Stoppunt
De brief stopt op de Ningbo-kade (`co-ningbo-kade`, hergebruikt van `kobalt-tfm-quzhou`): de vervolgroute naar Huayou Quzhou is wel in de bron genoemd, maar geen coördinaat voor die fabriek is deze sessie vindbaar (zelfde MEE-registerstoring als de Congolese as). Het "been C = letterlijke kopie van as 1 been C" uit de ontwerptoets kan daarom niet worden uitgevoerd — as 1 heeft dat been zelf ook niet getekend. Huayou Quzhou blijft een losse knoop in §5.

## 7 · Open punten
- **Huayue-perceel niet individueel gekarteerd:** IMIP is in OSM één groot `landuse=industrial`-vlak zonder bedrijfsnaam-tags; het anker ligt op het parkcentrum van het HPAL/RKEF-cluster, niet op het specifieke Huayue-terrein.
- **Labota-jetty: welke berth is de MHP-kade** is op z15 niet te onderscheiden van de NPI-, mattee- of kolenkades op hetzelfde havenfront (Sulawesi Labota-kolencentrale ligt er pal naast).
- **Huayou Quzhou-coördinaat ontbreekt** — gedeeld open punt met `kobalt-tfm-quzhou.md`: het MEE-emissieregister (`permit.mee.gov.cn/perxxgkinfo/…`) gaf deze sessie herhaald een 302 naar `errorinfo.jsp` i.p.v. het zoekformulier; OSM heeft geen naam-tag voor het adres (18 Nianxin/Bingxin Road). Vraagt een nieuwe poging of een Chinese lokale EIA-bron.
- **Zhapu vs Ningbo niet beslist in de bron** [3] — Ningbo gekozen omdat `kobalt-tfm-quzhou` dat anker al legde (ontwerpregel "zelfde anker als as 1").
- **Huafei bewust buiten deze as gehouden:** de ontwerptoets corrigeert Huafei (IWIP Weda Bay, Halmahera) uit deze keten — dat hoort bij de nikkelketen `nikkel-wedabay-iwip` resp. de sitelaag, niet hier.
- **Volume dubbelzinnig:** MHP is een nikkelproduct; het enige Co-specifieke cijfer op siteniveau is Huayue's nameplate (7,8 kt Co/j). Het verscheepte-volumecijfer (236,5 kt MHP, +30 %) dekt Huayue én Huafei samen en is niet uit te splitsen.
- **b1-afstand (~3,5 km) en b2 (~93 km) zijn hemelsbreed/gemeten schattingen**, exacte kade-tot-kade-lengtes volgen pas bij het bakken; b2 is de zwaarste haven-aanloop van alle zes kobaltassen (Golf van Tolo, precedent Mejillones-klasse).

## 8 · Bronnen
[1] Reuters, "China's Huayou ships first MHP shipment from Indonesia JV" (2022-02-14) — Huayue (IMIP, HPAL, $1,28 mld) verscheept MHP naar China. https://www.reuters.com/business/chinas-huayou-ships-first-mhp-shipment-indonesia-jv-2022-02-14/
[2] Argus Media, "Indonesia's Huafei to cut MHP output on sulphur costs" — bevestigt Huafei = Weda Bay/IWIP (120.000 t/j Ni-eq MHP), ≠ Huayue/IMIP. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2820208-indonesia-s-huafei-to-cut-mhp-output-on-sulphur-costs
[3] Huayou Cobalt, "2024 Mineral Supply Chain Due Diligence Report" (PDF, lokaal opgehaald deze sessie) — "Huayue's production address is Morowali Industrial Park (IMIP) … transportation routes are mainly from Labota Jetty … to Zhapu/Ningbo ports"; Quzhou-adres "No.18, Bingxin/Niexin Road, Hi-Tech Industrial Park Quzhou". https://www.huayou.com/Public/Uploads/uploadfile/files/20250422/2024-Mineral-Supply-Chain-Due-Diligence-Report.pdf
[4] Cobalt Institute, Cobalt Market Report 2025 — Indonesië 42,5 kt Co gedolven 2025 (+29 %), "Indonesian supply in 2025 was greater than DRC exports". https://www.cobaltinstitute.org/cobalt-market-report-2025/
[5] USGS, Mineral Commodity Summaries 2026 — Cobalt (Indonesië 44 kt gedolven 2025). https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-cobalt.pdf
[6] Mysteel, "Indonesia's MHP production declines as supply constraints emerge" — Huayou MHP-verschepingen 236.500 t in 2025, +30 % (Argus-cijfer geciteerd). https://www.mysteel.net/analysis/5117038-indonesias-mhp-production-declines-as-supply-constraints-emerge
[7] ImportYeti, leveranciersrecord "Quzhau Huayou Cobalt New Material" — adres No.18 Nianxin Road, Hi-Tech Industrial Park Phase-2, Quzhou, Zhejiang. https://www.importyeti.com/supplier/quzhau-huayou-cobalt-new-material
[8] Huayou New Energy Technology (Quzhou) Co., Ltd., corporate site. https://www.huayou.com/en
[9] OpenStreetMap via Overpass API (ODbL) — `landuse=industrial` "Indonesia Morowali Industrial Park" (way 299975400, center -2.83705/122.16576) · "Sulawesi Labota Power Plant" (way 1291862453, -2.87392/122.16920, bron gem.wiki) · piers bij Labota (ways 1291524363-365, `man_made=pier`/`mooring=private`) · "Beilun Container Terminal Phase 2" (29.9353/121.8645), opgevraagd 2026-09-26. https://www.openstreetmap.org
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-kobalt-morowali-quzhou-imip-centrum.png`, `sat-kobalt-morowali-quzhou-labota-jetty-a.png`, `sat-kobalt-morowali-quzhou-labota-jetty-b.png` (bleek Labota-dorp, niet de jetty), `sat-kobalt-morowali-quzhou-labota-power.png`.
[11] `v2/design/routebrieven/kobalt-tfm-quzhou.md` §3/§7 — hergebruikt anker `co-ningbo-kade` (29.9353, 121.8695) en het gedeelde open punt over de Huayou Quzhou-coördinaat.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kobalt-morowali-quzhou`** → `v2/data/stroomroute-kobalt-morowali-quzhou.json` — 4 benen, **4.309,3 km**, 525 punten, 3 markers. truck 3,5 (stippel) · zee 100,9 (stippel) + 4.193,3 + 11,6 (stippel) = 4.305,8 km.
Recept: `bak_stromen.sh` (functie `bak_kobalt_morowali_quzhou`).

**b1 (truck, stippel):** `--stippel "truck|parkintern Huayue → Labota-jetty …"` — **3,5 km, 2 punten**, rechte lijn (eigen terrein, geen net op deze korrel; werkwijze §7). Tegen de brief-schatting "~3,5 hemelsbreed" klopt dit exact — het ís de rechte lijn.

**b2 (zee, haven-aanloop, nieuw, stippel):** `timeout 300 python v2/tools/maak_havenaanloop.py --naam kobalt-morowali-quzhou-labota --van -2.8606,122.1871 --naar -2.0357,122.0017 --uit …` vond een pad op de **derde trap** (cel 0,005° gebufferd, minste land midden op de lijn): **100,9 km, 84 punten**, 0,39 km over land — dat restant grenst aan een uiteinde (de kade ligt per definitie óp de 1:10M-kustlijn, geen fout) en geen tweede poging was nodig (exit 0). Tegen de brief-schatting "~93 km (gemeten, toets M29)" is dit **+8,5%**, binnen ±15% — de zwaarste haven-aanloop van de zes kobaltassen, zoals de brief voorspelde (omwegfactor 1,074). Naad b1→b2 **0,00 km**.

**b3 (zee, nieuw, MARNET):** `--been "zee|…|-2.0357,122.0017|29.9758,121.9736"` — snap 0,000 km aan beide uiteinden (op de knopen zelf), 25 MARNET-edges, **4.193,3 km / 434 punten** (lengte-invariant getekende lijn vs. som edge-km: +0,046 km = de naden binnen het been zelf, ruim onder de norm). Tegen de brief-schatting "~4.500 (hemelsbreed ~3.900; MARNET meet exact)" is dit **−6,8%**, binnen ±15% — de exacte route ligt tussen de hemelsbreed-schatting en de gepubliceerde indicatie in, zoals verwacht van een MARNET-omweg via Malakka/Zuid-Chinese Zee. Naad b2→b3 **0,00 km**.

**b4 (zee, haven-aanloop, letterlijke kopie, stippel):** exact `v2/build-cache/ais/graaf/kobalt-tfm-quzhou-aanloop-ningbo.geojson` uit `bak_kobalt_tfm_quzhou` (kobalt-tfm-quzhou b2a) — geen nieuwe aanloop-poging. **11,6 km, 5 punten**, ongewijzigd (byte-identiek aan het gebakken kobalt-tfm-quzhou-been; van 29,9758/121,9736 naar 29,9353/121,8695, exact het gedeelde `co-ningbo-kade`-anker). Tegen de brief-schatting "~5,6 (letterlijke kopie van kobalt-tfm-quzhou.md b2a)" wijkt de KM af (11,6 vs 5,6), maar dat is de al bij kobalt-tfm-quzhou gemeten en toegelichte waarde (zie die brief §9) — de brief-schrijver noemde hier zelf een indicatieve schatting vooraf, de gedeelde geometrie zélf is nu al gebakken en wordt hier hergebruikt, niet opnieuw gemeten. Naad b3→b4 **0,00 km**.

**Geen been C (Ningbo → Huayou Quzhou):** conform de bak-aanwijzing en brief §6/§7 — hetzelfde gedeelde open punt als `kobalt-tfm-quzhou.md` (geen coördinaat voor de Quzhou-fabriek gevonden deze sessie, MEE-emissieregister gaf herhaald een 302). Geen lijn, geen stippel, geen marker voor Huayou Quzhou.

**Toets:** km-som **4.309,3 km** (geen gepubliceerde totaal-km voor de hele keten om tegen te toetsen — elk been afzonderlijk hierboven nagelopen, alle vier binnen ±15% of een exacte/hergebruikte lijn). Naden **0,00 / 0,00 / 0,00 km**, ruim onder de norm van 5 km. `toets_knikken.py`: **4 knikken ≥60°, 0 omkeringen, 0 TERUGLOOP** — alle vier zijn krappe bochten in het MARNET-zeebeen b3 (Golf van Tolo/Zuid-Chinese Zee/Oost-Chinese Zee-doorgang), geen enkele is een 180°-omkering. `toets_rechte_benen.py --min-km 5`: **geen enkel been van deze stroom in de uitslag** — beide haven-aanloop-stippels zijn via een water-pad/`detour()` gerouteerd (geen ongeteste rechte `--stippel` boven 5 km; het truck-been b1 is een `--stippel` van 3,5 km, onder de toetsdrempel). json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee}, elk been ≥2 punten, bestandsgrootte **10,9 KB** (ruim onder de ~300 KB-norm — geen wegscans, geen 1-op-1-spoorgeometrie in deze stroom). Alle 3 markers liggen op de aan- of eindpunten van hun been (0 m).

**Gereedschapslessen:**
- Een haven-aanloop van ~93 km (ruim boven de gebruikelijke <25 km-drempel) vraagt méér zoektrappen dan een korte aanloop — `maak_havenaanloop.py` viel hier terug tot de derde trap (cel 0,005° gebufferd) vóór een pad zonder landkruising midden op de lijn werd gevonden; nog steeds op de eerste poging (exit 0), geen tweede run nodig.
- Een "letterlijke kopie" van een gedeeld been (b4) erft de al-gemeten km van de moederstroom, ook als die afwijkt van de indicatieve schatting in déze brief — de brief-schatting was een educated guess vóór het bakken van de eerste van de twee stromen; de gemeten waarde staat al vast en wordt niet opnieuw bepaald.
- Twee stromen die hetzelfde `co-ningbo-kade`-anker en dezelfde haven-aanloop-geometrie delen (kobalt-tfm-quzhou en kobalt-morowali-quzhou) bevestigen elkaar: het punt (29,9353/121,8695) en het pad ernaartoe (11,6 km) liggen nu in twee onafhankelijk gebakken JSON-bestanden identiek vast.
