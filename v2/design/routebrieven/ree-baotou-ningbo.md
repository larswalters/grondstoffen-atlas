# Routebrief (licht) · zeldzame aardmetalen — Baotou → Ningbo (land)

**stroom-id:** `ree-baotou-ningbo` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** magneet-halffabricaten (毛坯, NdFeB-gietblokken) van JL MAG's eigen fabriek in de
Baotou-稀土高新区 gaan (aannemelijk per spoor) naar Ningbo, waar JL MAG's tweede fabriek ze afwerkt tot
eindmagneten voor EV/wind — een interne bedrijfsstroom, niet de in het ontwerp veronderstelde relatie
tussen Northern Rare Earth-scheiding en een willekeurige Ningbo-afnemer.
**Welke as van het verhaal:** herzien t.o.v. het ontwerp op bindend advies van de haalbaarheidstoets —
zie §0.

## 0 · Afwijking van het ontwerp (bindend, per de haalbaarheidstoets)
Het ontwerp veronderstelde Northern Rare Earth-scheiding (Huamei, `ree-baotou-scheiding`) → een naamloze
Ningbo-magneetfabriek (Yunsheng of Zhenghai). De haalbaarheidstoets wees dat af: geen bron documenteert
een leverancier-afnemerrelatie tussen die twee, en twee kandidaat-eindfabrieken zonder keuze is geen
"aannemelijk (één bron)". De toets vond als bijvangst dat **JL MAG (金力永磁)** eigen fabrieken heeft in
zowel Baotou als Ningbo. Een gerichte zoekronde in deze sessie bevestigde de interne materiaalstroom met
een bron (§8 [1]): JL MAG Baotou (稀土路街道沼园路1号) produceert **磁材毛坯** (magneet-halffabricaten,
23.000 t/j capaciteit) die naar de **JL MAG Ningbo-fabriek** (浦丰路666号, 慈城镇, Jiangbei) gaan voor
afwerking tot **高端磁材** (hoogwaardige magneten) + componenten. Dat is een concrete, eenduidige
leverancier-afnemerrelatie binnen één bedrijf — beter onderbouwd dan het ontwerp — en de keten is
daarom herzien naar deze as. De oorspronkelijke Northern-RE-scheiding levert wél mogelijk de grondstof
aan JL MAG Baotou (beide in dezelfde 稀土高新区), maar dat lokale been is niet getekend (geen bron voor
die specifieke levering; zie §7).

## 1 · Ketenkaart
```
JL MAG Baotou-fabriek `ree-baotou-jlmag` (毛坯-productie, 稀土高新区)
   ──(b1 spoor, aannemelijk: één bron voor de interne relatie · ~2.150 km hemelsbreed-schatting)──►
Ningbo-noord spoorstation/emplacement `ree-ningbobei-emplacement` ⏹ stoppunt
   (JL MAG Ningbo-fabriek, 浦丰路666号 慈城镇, ~13 km verderop — adres bekend, coördinaat niet
   gevonden binnen dit budget, zie §7; laatste been NIET getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | spoor (aannemelijk: één bron — SMM-artikel bevestigt de interne stroom, noemt geen modaliteit) | `ree-baotou-jlmag` → `ree-ningbobei-emplacement` | hoofdspoornet Baotou → Zhengzhou/Xuzhou-regio → Shanghai-regio → Ningbo, geen gepubliceerde enkelvoudige vrachtlijn | geen publicatie; ~2.150 km hemelsbreed-schatting (ontwerp gaf ~2.000-2.200 km) | `BAKE_SUFFIX=-raw toets_spoorroute` (1-op-1-net, extract `china`) | nee |

Fase D (Ningbo-emplacement → JL MAG Ningbo-fabriekspoort, ~13 km truck) is bewust NIET gebakken — zie §6/§7.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-baotou-jlmag` | fabriek (magneet-halffabricaten) | JL MAG (金力永磁) Baotou-fabriek, 内蒙古自治区包头市稀土高新技术产业开发区稀土路街道沼园路1号 | 40.6115, 109.8600 | [2][3] | aannemelijk (z14 gezien: dicht stedelijk/industrieel weefsel met loodsen en hallen rond 沼园路 in de 稀土高新区 — geen OSM-naam-tag om de exacte poort te bevestigen, zie §7) |
| `ree-ningbobei-emplacement` | spoor-eindpunt / stoppunt van deze brief | Ningbo-noord spoorstation (宁波北站), Jiangbei, Ningbo | 29.9517, 121.5200 | [4] | bron-gelegd (z14 gezien: rode perronoverkapping en rangeersporen, duidelijk stationscomplex) |

## 4 · Via-punten
Geen — b1 is een generieke hoofdspoornet-corridor van >2.000 km zonder gedocumenteerde enkelvoudige
vrachtlijn of corridorkeuze binnen dit budget; de bak-agent laat de spoorrouter (1-op-1-net) het tracé
kiezen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JL MAG Baotou | JL MAG (江西金力永磁科技股份有限公司) | NdPr-oxide/metaal (lokaal, 稀土高新区) → magneet-halffabricaten (毛坯) | 23 kt NdFeB-halffabricaat/j (23.000 t/j, fase-2-project) | [2][1] |
| JL MAG Ningbo | JL MAG | magneet-halffabricaten (毛坯, uit Baotou) → hoogwaardige magneten + componenten | 3 kt NdFeB/j hoogwaardig magneetmateriaal + 100 mln stuks/sets componenten (2023-doel) | [1] |

## 6 · Stoppunt
De brief stopt bij het Ningbo-noord spoorstation. De laatste ~13 km (emplacement → JL MAG
Ningbo-fabriekspoort aan 浦丰路666号, 慈城镇) is niet getekend: het adres is met twee bronnen bevestigd,
maar geen coördinaat kon binnen dit sessiebudget gevonden worden (§7). "De lijn eindigt waar het bewijs
eindigt" geldt hier op het laatste stukje, niet op de hele keten — de kern van de as (Baotou-fabriek →
Ningbo-fabriek, intern bij JL MAG) staat wél, bron-gedekt in §8 [1].

## 7 · Open punten
- **Coördinaat JL MAG Ningbo-fabriek (浦丰路666号, 慈城镇, 江北区, 宁波市) niet gevonden.** OSM/Overpass
  heeft geen weg genaamd 浦丰路 in de Ningbo-regio (brede bbox-zoekopdracht op straat- en bedrijfsnaam,
  leeg). Nominatim was het grootste deel van deze sessie 429-rate-limited (gedeeld sessiebudget van de
  parallelle golf). Het MEE-emissieregister (permit.mee.gov.cn, het vaste China-adresrecept) gaf op twee
  pogingen een 302 naar `error.jsp` — het sessie-/`tempReportKey`-mechanisme lijkt sinds de laatste
  documentatie (2026-08-06) opnieuw gewijzigd. Vervolgstap: een Tianditu-token, of een derde MEE-poging
  met een schone sessie buiten de parallelle golf.
- **Coördinaat JL MAG Baotou-fabriek is een straatmatch, geen poortbevestiging.** 沼园路 (Zhaoyuan Road)
  is in OSM bevestigd binnen de 稀土高新区 (twee straatsegmenten, lon 109,8506–109,8737 bij lat
  ~40,6111–40,6118), en de satellietblik toont daar dicht industrieel weefsel, maar geen OSM-naam-tag
  bevestigt welk perceel het bedrijf is (adres "沼园路1号", begin van de straat, niet visueel geverifieerd
  op naam).
- **Het lokale been Northern RE-scheiding (`ree-baotou-scheiding`) → JL MAG Baotou is niet getekend.**
  Beide liggen in dezelfde 稀土高新区 (enkele km uit elkaar), maar geen bron documenteert deze specifieke
  leverancier-afnemerrelatie — JL MAG Baotou kan zijn NdPr-oxide/metaal ook van elders in de zone
  betrekken. Zou bij bevestiging een kort extra been worden (truck, lokaal, fase B).
- **Modaliteit van b1 (spoor) is een aanname, geen bronvermelding.** De SMM-bron ([1]) bevestigt de
  materiaalstroom Baotou→Ningbo maar noemt geen transportwijze; spoor is aannemelijk voor binnenlandse
  bulk over >2.000 km (vergelijk de andere REE-brieven in deze reeks), niet bevestigd.
- **Km-schatting b1 (~2.150 km) is generiek/hemelsbreed-afgeleid**, net als in het oorspronkelijke
  ontwerp (~2.000-2.200 km) — geen gepubliceerde enkelvoudige vrachtlijnlengte.
- **Ningbo Yunsheng heeft óók fabrieken in zowel Ningbo als Baotou** (bijvangst uit onderzoek, [5]) — een
  tweede, onafhankelijke kandidaat voor dezelfde intra-bedrijf-Baotou→Ningbo-logica. Niet gebruikt (JL
  MAG's bron is explicieter over de blanks→afwerking-relatie), maar bevestigt dat dit bedrijfspatroon
  breder voorkomt dan één bedrijf op de Baotou-Ningbo-as.

## 8 · Bronnen
[1] 上海有色网 (SMM), 2021 — reportage over het JL MAG "hoogwaardige zeldzame-aarde-permanentmagneetmateriaal-basisproject" Baotou: 23.000 t/j magneet-halffabricaten (毛坯), die doorstromen naar JL MAG's Ningbo-fabriek voor eindverwerking (jaarcapaciteit 3.000 t hoogwaardig magneetmateriaal + 100 mln stuks/sets componenten, gepland operationeel 2023). https://news.smm.cn/news/101724147
[2] JL MAG Rare-Earth Co., Ltd. (江西金力永磁科技股份有限公司), officiële website, "总部及工厂" — adressen Ganzhou-hoofdkantoor, Baotou-fabriek (内蒙古自治区包头市包头稀土高新技术产业开发区稀土路街道沼园路1号) en Ningbo-fabriek (浙江省宁波市江北区慈城镇浦丰路666号). https://www.jlmag.com.cn/wap/about.php?cid=35
[3] OpenStreetMap (ODbL) via Nominatim — straat 沼园路, 稀土路街道, 包头市稀土高新区, twee segmenten lon 109,8506–109,8737 bij lat ~40,6111–40,6118. https://www.openstreetmap.org
[4] OpenStreetMap (ODbL) via Overpass — spoorstation 宁波北 (Ningbo-noord), node, 29,9517/121,5200. https://www.openstreetmap.org
[5] Web-onderzoek (2026-09-28) — Ningbo Yunsheng: "26.000 t hoogwaardige NdFeB-capaciteit verdeeld over Ningbo en Baotou" (secundaire bron, niet nader met een primair document bevestigd binnen dit budget).
[6] Esri World Imagery via `v2/tools/sat_check.py` (z14, live) — `v2/build-cache/satcheck/sat-ree-baotou-ningbo-jlmag-baotou-cand.png`, `sat-ree-baotou-ningbo-ningbobei.png`.
[7] Haalbaarheidstoets M31 golf 2 voor `ree-baotou-ningbo` (workflow-invoer bij deze opdracht) — verwierp de oorspronkelijke Northern RE→Ningbo-as en wees op de JL MAG-bijvangst als beter onderbouwd alternatief.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom:** `ree-baotou-ningbo` · **bestand:** `v2/data/stroomroute-ree-baotou-ningbo.json` (64,6 KB) ·
**recept:** `v2/tools/bak_stromen.sh` → `bak_ree_baotou_ningbo()` · draaien: `bash v2/tools/bak_stromen.sh ree-baotou-ningbo`

**Benen:** 1 (spoor, geen stippel) · **totaal:** 2.129,7 km · **punten:** 3.481 · **markers:** 2.

| # | modaliteit | km | naad | opmerking |
|---|---|---|---|---|
| b1 | spoor | 2.129,7 | 0,00 km | JL MAG Baotou-fabriek → Ningbo-noord spoorstation, 1-op-1-net (`BAKE_SUFFIX=-raw`, extract `china`, console bevestigd "3260717 spoor-edges") |

**Lengtetoets:** 2.129,7 km (gebakken, na `hecht_marnet.py route`) tegen de ~2.150 km hemelsbreed-schatting
uit de brief = **−0,9%**. De losse spoorrouter-run (vóór de bake-stap) gaf 2.116,6 km / grootcirkel
1.586,1 km / verhouding 1,33 — sanity OK (route ≥ grootcirkel). Dit is een **referentie**, geen ±15%-toets:
er is geen gepubliceerde enkelvoudige vrachtlijnlengte (brief §2/§7), alleen de hemelsbrede schatting.

**Snaps:** kop op hoofdnet-knoop 483430, 1,04 km van het JL MAG Baotou-anker (40,6115/109,8600) · staart op
hoofdnet-knoop 431350, 0,16 km van het Ningbo-noord-anker (29,9517/121,5200). Beide binnen de norm
(anker ≠ exact routeerpunt, gebruikelijk voor een spoorstation/-fabriekspoort-snap op het hoofdnet).

**Markers:** beide ≤ 1,1 km van hun lijn (het zijn zelf de been-uiteinden, geen losse snap nodig).

**Toets_bevindingen (buiten de norm, niet dichtgetrokken):**
- `toets_knikken.py`: **3 omkeringen ≥ 150°, alle drie geclassificeerd als TERUGLOOP** (boogstraal ~0 m,
  bij 29,8606/121,5395 · 40,6136/109,7282 · 39,8610/116,3692) — volgens de tool "de enige die gerepareerd
  horen te worden". Dit is een bekende klasse bij de 1-op-1-spoorrouter op lange hoofdnet-corridors zonder
  via-punt (zie `bakhandleiding-licht.md` §valkuilen: "niet elke omkering is een fout" geldt voor échte
  bochten, TERUGLOOP is de uitzondering die wél een routeerartefact kan zijn — een tie-break tussen
  parallelle sporen op de dichtstbijzijnde tak, zoals eerder gemeten bij de bochtstraf-ijking van 2026-07-29).
  Niet gerepareerd binnen deze lichte bake (geen `--via` beschikbaar om de router bij te sturen zonder een
  gedocumenteerde corridorkeuze te verzinnen) — gerapporteerd als bevinding, niet dichtgetrokken.
- `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom (omwegfactor 1,33, geen rechte lijn).
- `json.load` slaagt, `versie == 2`, `punt_formaat == "lonlat"`, modaliteit `spoor` ∈ toegestane set, been
  heeft 3.481 ≥ 2 punten, bestandsgrootte 64,6 KB (ruim binnen ~300 KB-norm).

**Fase D (niet gebakken):** Ningbo-emplacement → JL MAG Ningbo-fabriekspoort (浦丰路666号, 慈城镇, ~13 km
truck) blijft ongetekend — geen coördinaat gevonden binnen dit sessiebudget (zie brief §7). Geen
haven-aanloop nodig (zuiver binnenlands spoor, geen zee-been in deze keten).

**Gereedschapslessen:** `BAKE_SUFFIX=-raw` bevestigde meteen op de eerste consoleregel het 1-op-1-net
(3.260.717 spoor-edges) — dat is de vaste controle uit de bakhandleiding en klopte hier zonder verdere
actie. De losse spoorrouter-km (2.116,6) en de gebakken been-km (2.129,7) verschillen 0,6% — binnen de
gebruikelijke marge tussen een `--naam=`-run en de `hecht_marnet.py route`-stap eromheen (ankers snappen
op net-iets andere hoofdnet-knopen tussen beide aanroepen).
