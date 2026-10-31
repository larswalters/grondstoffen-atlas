# Routebrief (licht) · Lithium — Uis → Walvis Bay → Yangtze-monding (Namibië → China)

**stroom-id:** `lithium-uis-yangtze` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** ruw lithiumerts en concentraat van het Uis-gebied (Xinfeng Investments / partner Long Fire, Erongo) gaat per truck over de C36/C35, de C34-kustweg en de B2 naar NamPort Walvis Bay en per schip rond Kaap de Goede Hoop naar China; geen Chinese haven gebronnd, dus het eindpunt is het conventie-anker Yangtze-monding (aannemelijk: één bron).
**Welke as van het verhaal:** *Namibisch lithium naar China, nieuw land en nieuwe haven (Atlantisch Afrika).* Gebeurtenissen, geen jaarproductie, peiljaar 2022-2025: 54.719 t ruw erts naar China volgens havendata (nov 2022) [2]; ca. 19.000 t erts op de Namport-stapel (okt 2023) [3]; 16.000 t concentraat toegestaan voor export (jun 2025) [1]. Indicatie ≈ 1,6 kt LCE bij aangenomen 4% Li2O op 16.000 t concentraat (×2,473; gehalte niet gebronnd, geen jaarcijfer). Episodisch en klein: uitvoerverbod, licentiegeschil, stillegging nov 2024 [1][2][3].
**Afwijkingen van het ontwerp (bindende toets verwerkt):** mijnanker = OSM Uis Tin Mine -21.2408, 14.8787 (status onzeker) i.p.v. het Africamining-punt (-21.424, 15.946 is een Omaruru-centroïde); wegprofiel met via-punten Uis-west, Henties Bay, B2 bij Swakopmund; zeebeen van zeeknoop 8084 naar de MARNET-eindknoop 31.51, 121.4187 plus de 8,6 km overgangsstippel; Kohero/Omaruru-route (395 km) alleen in §7.

## 1 · Ketenkaart
```
Uis-mijnterrein `li-uis-mijn` ──(b1 truck · C36/C35 → Henties Bay → C34 kustweg → B2/MR44 → C14 · hemelsbreed 194, gemeten ~238, geen wegkm)──►
NamPort Walvis Bay `li-walvisbay-kade` ──(b2 haven-aanloop stippel · 12,5)──► MARNET-zeeknoop 8084
  ──(b3 zee · Kaap de Goede Hoop, Indische Oceaan, Malakka · ~15.686 MARNET)──► MARNET-eindknoop 31.51, 121.4187
  ──(b4 overgangsstippel · 8,6)──► Yangtze-monding `li-yangtze-monding` ⏹ stoppunt (Chinese haven niet gebronnd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (ruw erts/concentraat; aannemelijk: één bron voor de route) | `li-uis-mijn` → `li-walvisbay-kade` | C36/C35 uit Uis, Henties Bay, C34 kustweg, B2/MR44 bij Swakopmund, C14 naar de kade | **hemelsbreed 194 km, geen wegkm** (via-puntenketen 218). Deelstuk Henties Bay-Swakopmund 72 km [8]. Eigen OSM-Dijkstra 237,9 (OSRM-indicatie ca. 248; zelfde OSM-net, geen onafhankelijke toets); bron noemt "ca. 220 km" (Africamining [5], afstand Uis-Walvis Bay, geen wegkm). ±15%-toets = indicatie | maak_stroombeen_weg (extract namibie, nieuw profiel) | nee |
| b2 | B | zee (haven-aanloop) | `li-walvisbay-kade` → zeeknoop 8084 (-22.8344, 14.4759) | over de baai | 12,5 (kade ligt 12,5 km van de zeeknoop, > 5 km = aanloop) | **letterlijke kopie** van de aanloopstippel in `bak_uranium_langerheinrich_metropolis` | ja: MARNET reikt niet tot de kade |
| b3 | B | zee (bulkschip/containers, aannemelijk: één bron) | zeeknoop 8084 → MARNET-eindknoop 9654 (31.5100, 121.4187) | Kaap de Goede Hoop, Indische Oceaan, Straat van Malakka (MARNET beslist) | 15.685,8 (eigen MARNET-meting in de toets, snaps 0; geen gepubliceerde lengte) | MARNET (`--been zee`) | nee |
| b4 | B | zee (overgang) | 31.5100, 121.4187 → 31.4512, 121.4769 | MARNET houdt hier op | 8,6 | **letterlijke kopie** van de overgangsstippel in `bak_lithium` (ook in goulamina/bikita/wodgina) | ja: MARNET reikt niet |

Het anker `li-yangtze-monding` ligt 2,7 km voorbij het einde van b4: binnen de naadnorm (5 km), geen eigen been.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-uis-mijn` | mijn / laadplek (proxy) | Uis-mijngebied, OSM-vlak "Uis Tin Mine" (way 213851063) | -21.2408, 14.8787 | [7]; haalbaarheidstoets 2026-10-31 | **onzeker** (z15+z14 zelf gezien: groot pit- en verwerkingscomplex met bermen, witte tailingsvlakten en plant in het noorden; kruis staat op de pitbermen). Dit complex is volgens [6] de tinmijn van Andrada; welk deel Long Fire/Xinfeng bewerkt is niet aan te wijzen: het ministerie plaatst de claims 73409-73418 "west van Uis, ten zuiden van de Brandberg" [3] |
| `li-walvisbay-kade` | overslag truck → zee | NamPort Walvis Bay, containerterminal/havenhoofd | -22.9465, 14.4840 | **hergebruik letterlijk** uit `uranium-langerheinrich-metropolis.md` §3 (`u-walvisbay-haven`) [10] | bron-gelegd (aldaar z16: containerstapels en kade). Welke kade het lithiumerts laadt is niet gebronnd (de stapel lag "at Namport" [3]) |
| `li-yangtze-monding` | aanlanding China (stoppunt) | Yangtze-monding | 31.42704, 121.47618 | **hergebruik** uit `lithium-goulamina-yangtze.md` / `lithium-atacama-antofagasta.md` §3 [11] | aannemelijk (conventie-anker; geen Chinese haven of afnemer gebrond; MARNET-eindknoop 10,7 km ervandaan) |

## 4 · Via-punten (alleen b1; (lat, lon) uit de haalbaarheidstoets, door de bak-agent te snappen)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | uitgang mijnweg op de C36/C35, west van Uis (niet in het dorp) | -21.2301, 14.8546 | pint de westelijke uitgang richting kust i.p.v. de oostelijke Omaruru-weg |
| b1 | 2 | Henties Bay (C35/C34-knoop op de doorgaande weg) | -22.0687, 14.2588 | corridorkeuze: kustroute via Henties Bay i.p.v. B2 via Omaruru/Karibib (ca. 274 km) |
| b1 | 3 | B2/MR44 bij Swakopmund (op de weg, niet in het centrum) | -22.6783, 14.5276 | houdt de C34 → MR44/B2 naar Walvis Bay aan i.p.v. een zandspoor langs de kust |
Refs: C36 C35 C34 B2 (MR44, C14 als zachte voorkeur). Profiel met `eindToegangPrivaat: True` (havenpoort). Extract `namibie`. Last mile: de mijn ligt 2,4 km van het dorp Uis, geen eigen been; het been eindigt op het anker.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Uis (Long Fire-claims / ML243 Kohero) | Xinfeng Investments (licentie ML243 [2]); Long Fire Investments houdt de claims [3] | ruw erts; vergund 16.000 t concentraat (2025) [1] | niet gepubliceerd; geen jaarcijfer | [1][2][3] |
| Namport Walvis Bay | Namport | opslag stapel, scheepslading | stapel ca. 19.000 t (okt 2023) [3] | [3] |

## 6 · Stoppunt
De brief stopt aan de Yangtze-monding: de bronnen noemen alleen China, geen haven, afnemer of fabriek, en geen enkele bron legt dit erts bij een Chinese raffinaderij (fase D vervalt).

## 7 · Open punten
- **Het mijnanker is een proxy.** De OSM-vlakken "Uis Tin Mine" zijn volgens Wikipedia de tinmijn van AfriTin/Andrada [6]; de Long Fire-claims liggen "west van Uis, ten zuiden van de Brandberg" [3] en zijn niet gevonden (geen coördinaat in de bronnen). Het Africamining-punt -21.424, 15.946 is een Omaruru-centroïde [5] en onbruikbaar.
- **Route twijfelachtig.** New Era 2025 ziet trucks "Uis naar Walvis Bay" [1], Namibian Sun 2023 laat Xinfeng-trucks door Omaruru rijden [4] en volgens het Namibian gaat Long Fire-erts naar Kohero (ML243, Omaruru) voor het breken. Die route (Uis, Omaruru, Karibib, Walvis Bay, ca. 395 km) is niet getekend; de Henties Bay-corridor is de gekozen, niet de gebronde route (alleen modus en eindhaven zijn gebrond). Het Namibian-artikel (?p=686691) gaf bij mij 404 en is alleen via de haalbaarheidstoets bekend.
- **Geen wegkm** voor Uis-Walvis Bay: 194 hemelsbreed, 237,9 eigen routering.
- **China zonder haven:** [2] noemt China en Walvis Bay; [1] noemt geen bestemming. Eindpunt = conventie-anker.
- **Volume** alleen als gebeurtenissen; 1,6 kt LCE is mijn indicatie bij aangenomen 4% Li2O (niet gebronnd). Exportverbod en licentiegeschil [2][3]; onderzoek wegens mijnbouw op een exploratielicentie (EPL 8397) loopt [1].
- **Walvis Bay-kade** niet per lading gebrond; de truckroute binnen de haven (poort naar kade) volgt het toegangsprivaat-profiel.

## 8 · Bronnen
[1] New Era, "Xinfeng gets greenlight for lithium exports" (2025-06-24) — 16.000 t concentraat uit Uis, trucks Uis naar Walvis Bay, Long Fire, stillegging nov 2024 (EPL 8397). https://neweralive.na/?p=348624
[2] The Brief, ban on Xinfeng's lithium exports temporarily lifted (2022-11-15) — 54.719 t erts naar China via Walvis Bay, ML243, 80 kiepwagens. https://thebrief.com.na/2022/11/ban-on-xinfeng-s-lithium-exports-to-china-temporarily-lifted/
[3] New Era, "Lithium destined for China lies in harbour" (2023-10-25) — ca. 19.000 t bij Namport, Long Fire-claims 73409-73418 west van Uis. https://neweralive.na/?p=219127
[4] Namibian Sun, "Xinfeng trucks running again" (2023-10-20) — trucks via Omaruru, test in China, 100.000 t aangevraagd. https://namibiansun.com/business/xinfeng-trucks-running-again2023-10-20
[5] Africamining/China Global South, Xinfeng Investments (alleen via zoekresultaat gezien; punt -21.424, 15.946, ca. 220 km noordelijk van Walvis Bay). https://africamining.chinaglobalsouth.com/projects/xinfeng-investments
[6] Wikipedia, Uis mine — tinmijn, AfriTin/Andrada, coordinaat -21.2167, 14.8811. https://en.wikipedia.org/wiki/Uis_mine
[7] OpenStreetMap (ODbL) via Nominatim — way 213851063 "Uis Tin Mine" (-21.2408, 14.8787), dorp Uis node 258869517 (-21.2208, 14.8709). https://nominatim.openstreetmap.org
[8] Wikipedia, Henties Bay — 72 km ten noorden van Swakopmund. https://en.wikipedia.org/wiki/Henties_Bay
[9] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-lithium-uis-yangtze-li-uis-mijn.png` (z15) en `-z14.png`; eerder `sat-toets-lithium-uis-tinmine.png`.
[10] `uranium-langerheinrich-metropolis.md` §3 en `bak_uranium_langerheinrich_metropolis` — kade Walvis Bay en haven-aanloop 12,5 km.
[11] `lithium-goulamina-yangtze.md` §3 en `bak_lithium` in `bak_stromen.sh` — Yangtze-monding, MARNET-eindknoop 31.51, 121.4187 en overgangsstippel 8,6 km.
[12] Haalbaarheidstoets lithium-uis-yangtze (2026-10-31, orkestrator) — eigen test weg 237,9 km, zee 15.685,8 km, snaps 0; Namibian ?p=686691 (Long Fire-erts naar Kohero) en The Namibian-/Mining.com-berichten over het onderzoek (dec 2024) alleen als titel of samenvatting gezien.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`bash v2/tools/bak_stromen.sh lithium-uis-yangtze` → `v2/data/stroomroute-lithium-uis-yangtze.json` (58,6 KB, versie 2, lonlat): **4 benen · 15.944,8 km · 2.983 punten · 3 markers**. Recept: functie `bak_lithium_uis_yangtze` in `v2/tools/bak_stromen.sh`, wegprofiel `lithium-uis-yangtze-uis-walvisbay` in `v2/tools/maak_stroombeen_weg.py` (scan met `wegscan_puur.py`, extract namibie).

| # | modaliteit | km | naad | opmerking |
|---|---|---|---|---|
| b1 | truck | 237,9 (1.370 pt) | 0 | wegtool 236,9 + ankerstubs; tegen brief eigen routering 237,9 (hemelsbreed 194, **geen wegkm** → indicatie, geen norm). Segmenten: Uis-west → Henties Bay 114,4 · → Swakopmund 79,2 (Wikipedia 72 voor Henties Bay-Swakopmund, +10%) · → kade 38,0. Alle via-snaps 0,00 km; geen omweg. Mijn-snap 0,69 km (> 0,5, bevinding: proxy-anker ligt naast de weg), kade 0,28 km |
| b2 | zee (stippel) | 12,5 | 0 | haven-aanloop Walvis Bay, letterlijke kopie uit `bak_uranium_langerheinrich_metropolis` (-22.9465,14.4840 → -22.8344,14.4759, zeeknoop 8084) |
| b3 | zee | 15.685,8 (1.609 pt) | 0 | MARNET, 81 edges, Kaap de Goede Hoop – Indische Oceaan – Malakka; start snap 0 km, eindsnap van het opgegeven punt 13,0 km naar MARNET-eindknoop 31.5100,121.4187 (zelfde patroon als `bak_lithium_bikita_zhangjiagang`); gelijk aan de 15.685,8 uit de haalbaarheidstoets |
| b4 | zee (stippel) | 8,6 | 0 | overgangsstippel, letterlijke kopie uit `bak_lithium` (31.51,121.4187 → 31.4512,121.4769) |

**Markers:** li-uis-mijn 0,0 km van de lijn · li-walvisbay-kade 0,0 km · li-yangtze-monding 2,69 km voorbij het lijneinde (conventie-anker, binnen de naadnorm 5 km, geen eigen been; zelfde afstand als bij de andere lithium-stromen).
**Toetsen:** geen naad > 0,0 km; `toets_knikken` op b1: alleen kleine spikes (OSM-junctiegeometrie, radius 4-18 m; 0 omkeringen, 0 terugloop), b3 3 krappe bochten (Kaap, Oost-Chinese Zee); `toets_rechte_benen --min-km 5`: alleen de twee bedoelde stippels (b2 en b4). Bestand < 300 KB.
**Toelichting stippel:** b2 en b4 = "hier reikt het net niet" (kade 12,5 km van de zeeknoop; MARNET eindigt 8,6 km voor de Yangtze-bulklaag). Geen leiding, spoor, lucht of binnenvaart; fase D/E vervalt (zie §6).
**Lessen:** (1) het wegprofiel had `corridorKlassen ["tertiary","unclassified"]` nodig voor de C34/C35/C36 en `eindToegangPrivaat` voor de havenpoort; (2) de via-punten uit de haalbaarheidstoets snapten op 0,00 km en gaven geen omweg, dus geen verschuiving nodig; (3) het mijnanker blijft een onzekere proxy (§7): de lijn eindigt waar het bewijs eindigt, op het OSM-vlak Uis Tin Mine, niet op de Long Fire-claims.
**Afwijking van het ontwerp:** geen; eindpunt volgt het id (Yangtze-monding, conventie-anker).

