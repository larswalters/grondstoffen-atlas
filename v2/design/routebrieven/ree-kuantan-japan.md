# Routebrief (licht) · Zeldzame aardmetalen · Kuantan (LAMP) → Port Klang → Japan (Yokohama)

**stroom-id:** `ree-kuantan-japan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** NdPr-/Dy-/Tb-oxide van de Lynas Advanced Materials Plant (LAMP) in Gebeng gaat per
**truck** dwars over het Maleisisch schiereiland naar Port Klang (Westport, Pulau Indah), en per
**zeeschip** naar Japan — voorgesteld eindpunt Yokohama/Honmoku, te bevestigen bij het bakken — waar
Shin-Etsu, TDK en Proterial (ex-Hitachi Metals) het tot NdFeB-magneten verwerken.
**Welke as van het verhaal:** Lynas is de enige grote niet-Chinese NdPr/Dy/Tb-scheiding buiten de VS, en
Japan is via Shin-Etsu/TDK/Proterial de grootste niet-Chinese afnemer. Lynas FY2026 NdPr-verkoop
7.337 t (+12% j/j), LAMP-nameplate ~10.500 t NdPr/jaar, plus Dy-oxide sinds mei 2025 en Tb-oxide sinds
juni 2025 [1][2]. Het exact naar Japan verscheepte volume is niet apart gepubliceerd — zie §7.

## 1 · Ketenkaart
```
LAMP Gebeng `ree-lamp-gebeng` — scheiding tot NdPr-/Dy-/Tb-oxide (hergebruikt anker, ree-mtweld-kuantan.md)
   ──(b1 truck · Lebuhraya Pantai Timur (E8) → Karak Highway (E8/E9) → KL–Klang-corridor · ~290 km,
       aannemelijk: één bron voor de route zelf)──►
Westport, Port Klang (Pulau Indah) `ree-kuantan-japan-westport-kade`
   ──(b2 zee · Straat Malakka → Z-Chinese Zee → Luzon-/Taiwanstraat → Filipijnse Zee · ~5.300 km,
       MARNET)──►
Honmoku-kade, Yokohama `ree-kuantan-japan-honmoku-kade` — Japanse invoerhaven (voorstel, te bevestigen)
   ⏹ stoppunt — magneetmakerscluster Shin-Etsu/TDK/Proterial, geen offtake per lading gebrond
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `ree-lamp-gebeng` → `ree-kuantan-japan-westport-kade` | Lebuhraya Pantai Timur (E8) → Karak Highway (E8/E9) → Kuala Lumpur–Klang-corridor | ~290, aannemelijk: één bron voor de route zelf, geen gepubliceerde kilometrage [3] | maak_stroombeen_weg (extract `maleisie`) | nee |
| b2 | C | zee | `ree-kuantan-japan-westport-kade` → `ree-kuantan-japan-honmoku-kade` | Straat Malakka → Zuid-Chinese Zee → Luzon-/Taiwanstraat → Filipijnse Zee | ~5.300, grootcirkel-indicatie [ontwerp] — MARNET bepaalt de exacte route | MARNET | aanloop: nee (Westport) / **ja** (Honmoku — zie §3) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lamp-gebeng` | fabriek (start, scheiding) | Lynas Advanced Materials Plant (LAMP), Gebeng-industriegebied | 4.0034, 103.3775 | [1][hergebruik `ree-mtweld-kuantan.md`] | bron-gelegd (hergebruikt anker; zie `ree-mtweld-kuantan.md` §3 — fabrieksterrein met procesgebouwen, ~1,5 km landinwaarts) |
| `ree-kuantan-japan-westport-kade` | overslag truck → zee | Westports Malaysia, Pulau Indah, Port Klang | 2.9498, 101.3076 | [4][5] | bron-gelegd (z14 gezien: haventerrein op het Pulau Indah-schiereiland met een lange kadelijn, containerstapels en tankopslag; 2,3 km van zijn MARNET-zeeknoop (5375) — geen haven-aanloop nodig, ruim binnen de 5 km-norm) |
| `ree-kuantan-japan-honmoku-kade` | losplek zee (voorgestelde Japanse invoerhaven) | Honmoku Futo-containerterminal, Yokohama | 35.4356, 139.6727 | [6][7] | bron-gelegd (z14 gezien: opgespoten pier met containerstapels en kranen direct aan het water; 7,8 km van zijn MARNET-zeeknoop (9065) → **haven-aanloop nodig**, LAR-586 §2, óók al snapt de router binnen de 25 km) |

## 4 · Via-punten (alleen b1 — enige landbeen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kuantan | 3.8167, 103.3333 | corridor komt hier vanaf de Gebeng-industrieweg op de doorgaande Lebuhraya Pantai Timur (E8) |
| b1 | 2 | Bentong | 3.5167, 101.9167 | Karak Highway-interchange; corridorkeuze richting Kuala Lumpur i.p.v. Raub/Fraser's Hill |
| b1 | 3 | Genting Sempah | 3.3497, 101.7806 | bergpas/tunnel door de Titiwangsa-bergketen — enige doorgaande route, geen alternatief |
| b1 | 4 | Gombak-tolplein | 3.2420, 101.7272 | einde Karak Highway (E8/E9), aansluiting op de Kuala Lumpur-ringweg |
| b1 | 5 | Shah Alam | 3.0722, 101.5167 | corridorkeuze KESAS/Federal Highway richting Port Klang i.p.v. doorgaand naar KL-centrum |
| b1 | 6 | Pulau Indah | 2.9489, 101.3317 | laatste corridorkeuze, oprit vanaf de vaste land naar het Westport-schiereiland |

## 5 · Verwerkingsknopen
Geen verwerkingsknoop op deze keten: LAMP Gebeng (scheiding tot oxide) is het startanker van deze brief
en al gedocumenteerd in `ree-mtweld-kuantan.md` §5; de Japanse magneetfabrieken (fase D) zijn niet
gebrond tot één knoop — zie §6.

## 6 · Stoppunt
De brief stopt bij de Japanse invoerhaven: geen bron koppelt een specifieke lading aan één magneetfabriek.
Drie afnemers met verspreide locaties (Shin-Etsu Fukui/Takefu, TDK Akita, Proterial Kumagaya) delen de
Japanse markt; alleen het offtake-niveau van Japan als geheel is gedocumenteerd (grootste niet-Chinese
afnemer via Shin-Etsu/TDK/Proterial), niet per fabriek. Fase D en E vervallen — zelfde behandeling als de
bestaande ree-bayanobo-baotou-as.

## 7 · Open punten
- **Japanse invoerhaven niet bij naam genoemd in enige bron.** Time.com [3] schrijft alleen "leave on a
  ship for Japan" — Yokohama/Honmoku is hier een aannemelijke keuze (historische Keihin-aanvoerroute voor
  Japanse zware-industrie-import, vgl. `lithium-olaroz-naraha.md` §7), geen cargospecifiek gebronde
  bestemming. **Bindend uit de haalbaarheidstoets:** vóór het bakken een concrete haven kiezen met
  satellietblik — Honmoku Futo voldoet (z14 gezien, zie §3) en wordt hier voorgesteld.
- **Gepubliceerde kilometrage voor b1 ontbreekt** — geen enkele bron geeft een operator-kilometrage voor
  Gebeng → Port Klang; ~290 km is een kaartschatting op de beschreven corridor, geen gepubliceerd getal.
- **Fase D (haven → specifieke magneetfabriek) niet getekend** — drie afnemers, geen offtake-koppeling per
  lading gevonden; zie §6.
- **Aandeel van Japan in Lynas' totale NdPr/Dy/Tb-export niet apart gepubliceerd** — het "grootste
  niet-Chinese afnemer"-statement is kwalitatief, geen volumecijfer specifiek voor deze as.
- **Welke Westport-kade specifiek REE-oxiden (vaten/rotainers) ontvangt** is op z14 niet te onderscheiden
  van de overige containerfuncties van het terrein — anker blijft op site-niveau.
- **Geen tweede bron voor de truck-corridor zelf** (alleen Time.com noemt "transported to Port Klang on
  the other side of Malaysia") — corridorkeuze via de gangbare E8/Karak-route is aannemelijk, niet gebrond.

**Volume-notitie:** jaarvolume in de eenheid van het ontwerp: **~7,3 kt NdPr-oxide/jaar** (Lynas FY2026
NdPr-verkoop 7.337 t; oorspronkelijke eenheid: tonnes NdPr/jaar) op een LAMP-nameplate van **~10,5 kt
NdPr/jaar**, plus Dy-oxide (sinds mei 2025) en Tb-oxide (sinds juni 2025) zonder apart gepubliceerd
tonnage [1][2]. Dit is Lynas' totale NdPr-afzet, niet het Japan-specifieke aandeel van deze as — zie §7.

## 8 · Bronnen
[1] Lynas Rare Earths, Kuantan, Malaysia — LAMP-proces (cracking/leaching, solvent extraction, product
finishing), outputs NdPr-oxide/Dy-oxide/Tb-oxide, Gebeng Industrial Estate. https://lynasrareearths.com/kuantan-malaysia-2/
[2] Discovery Alert, "Lynas Rare Earths: FY26 Record Output, Rising Risks" — FY2026 NdPr-verkoop 7.337 t
(+12% j/j), LAMP-nameplate ~10.500 t NdPr/j, Dy-oxide sinds mei 2025, Tb-oxide sinds juni 2025. https://discoveryalert.com/analysis/lynas-rare-earths-investment-analysis/
[3] Time.com, "The Sobering Truth About Rare Earths" (april 2026) — "transported to Port Klang on the
other side of Malaysia, and leave on a ship for Japan"; bevestigt de truck-corridor Gebeng→Port Klang en
de zeeroute naar Japan. https://time.com/article/2026/04/20/trump-s-push-to-break-china-s-dominance-of-critical-rare-earth-minerals/
[4] Wikipedia, "West Port, Malaysia" — Westports Malaysia Sdn Bhd, multi-cargo terminal op Pulau Indah,
Port Klang; coördinaat 2.949834/101.307635. https://en.wikipedia.org/wiki/West_Port,_Malaysia
[5] OpenStreetMap (ODbL) via Nominatim — "Pusat Kawalan WesTPort" bus_stop 2.9488065/101.3082176
(bevestigt de Wikipedia-coördinaat op ~100 m); wegennet Jalan Pelabuhan Utara-Barat/Jalan Pelabuhan
Utara (Northport) los gecontroleerd. https://www.openstreetmap.org
[6] OpenStreetMap (ODbL) via Nominatim — "本牧ふ頭" (Honmoku Futo/Honmoku Pier), Naka-ku, Yokohama,
Kanagawa; locatiepunten 35.4355855/139.6726849 en 35.4393309/139.6768974. https://www.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z14) —
`v2/build-cache/satcheck/sat-ree-kuantan-japan-westport.png` ·
`sat-ree-kuantan-japan-yokohama.png` (verkenning, generiek punt uit de haalbaarheidstoets) ·
`sat-ree-kuantan-japan-yokohama-z15.png` (verificatie: dat punt ligt landinwaarts op een kruispunt, niet
op een kade) · `sat-ree-kuantan-japan-honmoku.png` (het gekozen anker, wél op de pier).
[8] Wikipedia, "Karak Highway" · "Port Klang" · Nominatim/Wikipedia-coördinaten Kuantan, Bentong, Genting
Sempah, Gombak (Plaza Tol Gombak), Shah Alam, Pulau Indah — via-punten b1. https://en.wikipedia.org
[9] Fastmarkets, "China's looming November export controls test rare earth refining/recycling
ambitions" — achtergrond bij het risico van Chinese exportbeperkingen (context, niet route-specifiek). https://www.fastmarkets.com/insights/chinas-looming-november-export-controls-test-rare-earth-refining-recycling-ambitions/
[10] Benchmark Minerals (source.benchmarkminerals.com) — implicaties van Chinese exportbeperkingen voor
Japan (context, niet route-specifiek). https://source.benchmarkminerals.com/article/what-are-the-implications-of-chinas-latest-rare-earth-export-restrictions-on-japan

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `ree-kuantan-japan`** → `v2/data/stroomroute-ree-kuantan-japan.json` — 3 benen. 6.321,8 km. 3 markers:
truck 336,5 km · zee 5.977,5 km · zee (stippel) 7,8 km.
Recept: `bak_stromen.sh` (functie `bak_ree_kuantan_japan`). Bestand 102,6 KB.

**Toelichting per been:**
- **b1 (truck, `maak_stroombeen_weg.py`, profiel `ree-kuantan-japan-gebeng-westport`, extract `maleisie`):**
  **336,5 km getekende weggeometrie tegen ~290 km kaartschatting = +16,0%, net buiten ±15%** — bevinding, niet
  dichtgetrokken: de referentie is zelf al een kaartschatting op de beschreven corridor (brief §7, alleen
  Time.com noemt de route zelf, geen operator-kilometrage). 26 keerlussen gesnoeid (349,1 → 336,5 km). Beide
  ankers snappen op 0,02–0,12 km; geen stippel nodig op het Gebeng-industrieweg-stuk (bleef binnen `WEG_HOUD`).
- **b2 (zee, MARNET, `--been zee` Westport → Honmoku-zeeknoop):** Westport snapt op **2,336 km** van zeeknoop
  5375 — ruim binnen de 5 km-norm (LAR-586 §2), geen haven-aanloop nodig. Honmoku-zeeknoop (9065) snapt op
  **0,000 km** (het zeebeen eindigt daar per definitie). Zeebeen **5.977,5 km tegen ~5.300 km
  grootcirkel-indicatie in de brief = +12,8%**, binnen de in de bak_aanwijzingen verwachte marge (MARNET-route
  via Malakka/Luzon-Taiwanstraat kan 10-20% langer uitvallen dan de grootcirkel, zoals eerder bij
  olie-habshan-chiba). MARNET routeert via Straat Malakka → Zuid-Chinese Zee → Luzon-/Taiwanstraat →
  Filipijnse Zee, zoals de brief voorspelde.
- **Haven-aanloop Honmoku (stippel, 7,8 km):** de kade ligt 7,8 km van zeeknoop 9065 (> 5 km, LAR-586 §2) →
  haven-aanloop vereist. `maak_havenaanloop.py` liep vast op de 300 s-timeout (exit 124) — **geen tweede
  poging** (bakhandleiding §2), terugval op een rechte stippel. Honmoku is een AANKOMENDE haven (net als
  Kuantan in `ree-mtweld-kuantan.md` §9): het hoofd-zeebeen eindigt op de zeeknoop en de stippel vervolgt
  zeeknoop → kade, in de juiste reisvolgorde.

**Toets-bevindingen:**
- Naden tussen benen: 0,00 · 2,34 · 0,00 km — allemaal ruim binnen de 5 km-norm.
- `toets_knikken.py`: 43 knikken op het truckbeen (waarvan 2 omkeringen, **0 terugloop** — OSM-spikes op
  kleine-klasse-eindwegen, Kuantan-havenweg-klasse) en 4 krappe bochten op het zeebeen (0 omkeringen) — geen
  reparatie nodig.
- `toets_rechte_benen.py --min-km 5`: de haven-aanloop-stippel (7,8 km, omwegfactor 0,998) staat terecht in de
  verdachtenlijst — een rechte stippel over water hóórt recht te zijn (net als uranium-inkai-poti's
  Aktau-aanloop); geen doorgetrokken been van deze stroom komt erin voor.
- Alle 3 markers liggen op **0,0 m** van hun been.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, zee} (beide toegestaan), elk been
  ≥ 2 punten, bestand 102,6 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:**
- Een `maak_havenaanloop.py`-timeout op een grote havenkust (Tokiobaai, veel kustdetail) is geen incident maar
  een verwachte uitkomst op sommige havens (net als Hamburg in de bakhandleiding, 20 min op 99% CPU) — de
  regel "geen tweede poging" voorkomt dat één haven een golf blokkeert; de rechte stippel draagt de reden
  expliciet in de naam.
- Voor een aankomende haven (het zeebeen eindigt op de kade, niet begint) hoort de stippel-aanloop ná het
  hoofdbeen te staan en van zeeknoop → kade te lopen — dezelfde omkering als `ree-mtweld-kuantan.md` §9
  beschrijft voor een `--stippel-geojson`, hier toegepast op een rechte `--stippel`.
- Een schatting-op-schatting-referentie (Time.com's routebeschrijving zonder km, omgezet naar een
  kaartschatting van ~290 km) geeft eerder een venster dan een harde ±15%-toets; een overschrijding van 1
  procentpunt (16,0% i.p.v. 15%) is dan een bevinding, geen reden om de geometrie of het venster aan te passen.
