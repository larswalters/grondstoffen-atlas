# Routebrief (licht) · kobalt — Van → Via → Naar (land)

**stroom-id:** `kobalt-wedabay-tongxiang` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) · **status:** gebakken
**Keten in één zin:** MHP (mixed hydroxide precipitate, kobalt als bijproduct van nikkel) van de Huafei Nickel Cobalt-HPAL-plant op Weda Bay Industrial Park (IWIP, Halmahera) gaat over het eigen parkterrein naar de IWIP-jetty, per **zeeschip** — via twee haven-aanlopen — naar de containerkade Ningbo Beilun, en per **truck** — letterlijke kopie van de bestaande Tongxiang–Ningbo-weg — naar Huayou's eigen raffinaderij in Tongxiang (Zhejiang); de aanname dat dit specifieke MHP naar de eigen Tongxiang-vestiging gaat (i.p.v. een andere Huayou-site of een derde partij) steunt op eigendom, niet op een gedocumenteerde zending.
**Welke as van het verhaal:** derde Indonesische HPAL-kobaltbron, groepsintern naast Morowali (`kobalt-morowali-quzhou`) en Obi (`kobalt-obi-ganzhou`) — maar met een andere Chinese binnenkomst (Tongxiang i.p.v. Quzhou/Ganzhou) omdat Huafei en Huayou's hoofdraffinage bij dezelfde eigenaar horen. Nameplate 15 kt Co/jaar (Argus Media 2023) [1][2] — sinds **1 mei 2026** staat de helft van de MHP-capaciteit (120 kt Ni-eq/jaar) op *care & maintenance* wegens hoge zwavelkosten (Argus Media 2026) [1]; het 15 kt Co/jaar-cijfer is deze ronde niet onafhankelijk voor de kobaltfractie herbevestigd.

## 1 · Ketenkaart
```
Huafei-HPAL-plant `co-wedabay-huafei` (hergebruikt anker) ──(b1 truck · IWIP-parkterrein · ~5,0 km hemelsbreed, stippel)──►
IWIP-jetty `co-wedabay-jetty` (hergebruikt anker)
  ──(b2 zee-aanloop · Molukse Zee · 131,99 km, gemeten, stippel)──► zeeknoop 9033 (0.0961, 129.1306)
  ──(b3 zee · Molukse Zee → Sulawesizee → Zuid-Chinese Zee → Straat Taiwan → Oost-Chinese Zee · indicatief ~3.700–3.950 km)──► zeeknoop bij Ningbo
  ──(b4 zee-aanloop · 11,6 km, letterlijke kopie kobalt-tfm-quzhou b2a, stippel)──►
Ningbo Beilun-containerkade `co-ningbo-kade` (hergebruikt anker)
  ──(b5 truck · G60/G92 Tongxiang–Ningbo · 192,2 km, letterlijke kopie kobalt-huayou-gunsan b1, aannemelijk: eigendom, geen zending-bevestiging)──►
Huayou Tongxiang-raffinaderij `co-tongxiang-raffinaderij` (hergebruikt anker) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-wedabay-huafei` → `co-wedabay-jetty` | eigen IWIP-parkterrein, zelfde soort korte verbinding als `kobalt-morowali-quzhou` b1 | 4,96 hemelsbreed (berekend deze sessie; geen publicatie) | stippel "binnen estate (geen net)" — geen wegscan | ja — eigen terrein, geen net op deze korrel |
| b2 | B | zee (haven-aanloop) | `co-wedabay-jetty` → zeeknoop 9033 (0.0961, 129.1306) | Molukse Zee — kade ligt 131,99 km van de dichtstbijzijnde MARNET-zeeknoop (gemeten met `hecht_marnet.marnet_zee`, bevestigt de haalbaarheidstoets exact) | 131,99 (gemeten) | `maak_havenaanloop.py` onder timeout 300; "geen pad" → **direct** terugval rechte stippel, geen tweede poging (bakhandleiding §2) | ja — MARNET reikt hier niet; ruim boven de gebruikelijke <25 km-drempel, orde Mejillones (136 km) |
| b3 | B | zee | zeeknoop 9033 → zeeknoop bij Ningbo (29.9758, 121.9736, hergebruikt uit `kobalt-morowali-quzhou`/`kobalt-tfm-quzhou`) | Molukse Zee → Sulawesizee → Zuid-Chinese Zee → Straat Taiwan → Oost-Chinese Zee | indicatief ~3.700–3.950 (hemelsbreed 3.407,8 km deze sessie berekend; omwegfactor 1,07–1,16 naar analogie van `kobalt-morowali-quzhou` b3 [1,075] en `kobalt-obi-ganzhou` b2 [1,069] — **lager dan het ontwerp-cijfer ~4.400 km**, want de hemelsbrede afstand hier is ruim korter dan de Morowali-corridor) | MARNET `--been "zee\|…\|0.0961,129.1306\|29.9758,121.9736"` | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop bij Ningbo → `co-ningbo-kade` | Beilun-containerzone | 11,6 (**letterlijke kopie**, al gebakken in `bak_kobalt_tfm_quzhou`) | `--stippel-geojson` met exact `kobalt-tfm-quzhou-aanloop-ningbo.geojson` — géén nieuwe `maak_havenaanloop.py`-run | ja — MARNET reikt niet tot de kade (bestaand) |
| b5 | C | truck | `co-ningbo-kade` → `co-tongxiang-raffinaderij` | G60/G92 Tongxiang–Ningbo (Hangzhou-ringweg-corridor) | 192,2 (**letterlijke kopie**, al gebakken in `bak_kobalt_huayou_gunsan`/`bak_kobalt_murrinmurrin_kwinana`) | `--been-geojson` met exact `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson` (al de omgekeerde richting) — geen nieuwe wegscan | nee — doorgetrokken; "aannemelijk: eigendom, geen zending-bevestiging" staat in de beennaam, niet in de lijnstijl |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-wedabay-huafei` | mijn/HPAL-plant (relabeling van `ni-iwip-rkef`) | Huafei Nickel Cobalt HPAL, IWIP-ore-yard/industriecluster, Halmahera | 0.4970, 127.9670 | `nikkel-wedabay-iwip.md` §3 [3][8] | bron-gelegd (**hergebruikt anker, letterlijke kopie** — daar al z15/z16 gezien: industriehallen + ertsopslag op het punt waar de RKEF/Huafei-clusterweg de vlakte bereikt; niet opnieuw satelliet-gecheckt deze ronde) |
| `co-wedabay-jetty` | overslag parkweg → zee (relabeling van `ni-iwip-jetty`) | IWIP-havenbekken (jetty), binnen de golfbreker | 0.4745, 128.0055 | `nikkel-wedabay-iwip.md` §3 [3][8] | bron-gelegd (**hergebruikt anker** — daar al z16 gezien: golfbreker met afgemeerde zeeschepen + kolenopslag; welke berth specifiek MHP laadt is niet te onderscheiden, zelfde beperking als bij de moederbrief) |
| `co-ningbo-kade` | overslag zee → truck | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | `kobalt-tfm-quzhou.md` §3 [4] | bron-gelegd (hergebruikt anker, letterlijke kopie, niet opnieuw satelliet-gecheckt — vierde stroom die dit punt gebruikt) |
| `co-tongxiang-raffinaderij` | raffinaderij / losplek ⏹ stoppunt | Zhejiang Huayou Cobalt — nikkel-kobaltsmelterij, Tongxiang Economic Development Zone fase 2 | 30.6167, 120.5629 | `kobalt-huayou-gunsan.md` §3 [5] | bron-gelegd (hergebruikt anker — MEE-emissieregister, vergunning 913300007368873961001P, decimaal én DMS exact overeenkomend; **zie §7 voor een tegenstrijdige notitie in de kobalt-sitelaag**) |

## 4 · Via-punten
Geen nieuwe: b1 is een parkinterne stippel zonder corridorkeuze, b2/b3/b4 zijn zeebenen (router/aanloop, geen via-punten), en b5 is een letterlijke kopie waarvan de eigen via-punten al in `kobalt-huayou-gunsan.md` §4 staan (G60/G92, geen externe via-punten gevonden die sessie — de weg-scan leverde de corridor zelf).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Huafei-HPAL-plant (IWIP) | Huayou / Tsingshan / EVE Energy-JV | lateriet-erts → MHP (Co als bijproduct) | nameplate 120 kt Ni + 15 kt Co/jaar (2023); sinds 1 mei 2026 ~50 % op *care & maintenance* (zwavelkosten, herstel gepland eind 2026) | [1][2][6] |
| Huayou Tongxiang-raffinaderij | Zhejiang Huayou Cobalt | nikkel-/kobalttussenproduct → kobalttetroxide/-sulfaat (batterijchemicaliën) | vergunning 913300007368873961001P; geen productiecijfer gebrond (zie `kobalt-huayou-gunsan.md` §5) | [5] |

## 6 · Stoppunt
De brief eindigt bij de Huayou Tongxiang-raffinaderij (`co-tongxiang-raffinaderij`, hergebruikt anker): geen bron van deze sessie koppelt Huafei's MHP met naam-en-toenaam aan déze vestiging — de aanname steunt uitsluitend op eigendom (Huayou bezit zowel de Huafei-HPAL bij Weda Bay als Tongxiang). Blijkt bij het bakken dat de aanname niet houdbaar is, dan vervalt been b5 en stopt de keten op de Ningbo-kade, exact zoals `kobalt-morowali-quzhou`/`kobalt-obi-ganzhou` al doen op hun eigen Chinese kade.

## 7 · Open punten
- **Centrale aanname niet gebrond op zendingsniveau:** geen bron noemt dat Huafei's MHP naar Tongxiang gaat i.p.v. een andere Huayou-vestiging (Quzhou, coördinaat dit seizoen niet gevonden — zie `kobalt-tfm-quzhou.md` §7) of een derde partij; alleen eigendom pint deze route.
- **b1 gecorrigeerd:** ontwerp gaf "~3 km hemelsbreed"; eigen berekening op de twee hergebruikte ankers geeft **4,96 km** — geen coördinaat gewijzigd, alleen de afstandsschatting.
- **b2 BINDEND gecorrigeerd (haalbaarheidstoets):** ontwerp gaf "~90–100 km"; gemeten met `hecht_marnet.marnet_zee` (deze sessie onafhankelijk herhaald, identieke uitkomst) is de afstand **131,99 km** tot zeeknoop 9033 — reëel risico op timeout (300 s) of "geen pad" bij het bakken; bij falen **direct** de rechte stippel, geen tweede poging.
- **b3 is een indicatieve schatting** (hemelsbreed + analogie-omwegfactor), geen gepubliceerde routelengte; exacte MARNET-km volgt bij het bakken.
- **Productiestatus Weda Bay/Huafei onzeker:** care & maintenance sinds 1 mei 2026 (gecorrigeerd t.o.v. het ontwerp: "sinds april 2026"), 120 kt Ni-eq/jaar-capaciteit op de helft; het 15 kt Co/jaar-cijfer (nameplate) is deze ronde niet onafhankelijk voor de kobaltfractie herbevestigd.
- **Tegenstrijdigheid in de kobalt-sitelaag (niet zelf gewijzigd — melding):** `kobalt-sitelaag.json` §"china_capaciteiten_niet_toegepast" stelt dat het v1-registerpunt "Tongxiang" (30.63, 120.56) Huayou's hoofdkantoor/campus is, **niet** de kobaltraffinaderij — terwijl `kobalt-huayou-gunsan.md`/`kobalt-murrinmurrin-kwinana.md` op vrijwel dezelfde coördinaat (30.6167, 120.5629) een MEE-emissievergunning voor "nikkel-kobaltsmelterij" vonden. Beide bronnen kunnen correct zijn (kantoor/campus én smelterij op hetzelfde bedrijfsterrein) — verdient een centrale check, niet in deze brief opgelost.
- **Jaarvolume voor déze specifieke as** (Weda Bay-aandeel van de 15 kt Co/jaar-nameplate, ná de care & maintenance-korting) niet apart gepubliceerd.

## 8 · Bronnen
[1] Argus Media, "Indonesia's Huafei to cut MHP output on sulphur costs" (2026) — bevestigt (haalbaarheidstoets-webcheck): per 1 mei 2026 helft van de 120 kt Ni-eq/jaar MHP-capaciteit op care & maintenance, zwavelkosten cfr Indonesië +84% (26 feb–23 apr 2026), herstel gepland eind 2026 via eigen zwavelproductie. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2820208-indonesia-s-huafei-to-cut-mhp-output-on-sulphur-costs
[2] Argus Media, "Huayou, Vale commit to Indonesian Huali MHP project" — herkomst/eigendom Huafei/Huayou-JV op Weda Bay. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2483610-huayou-vale-commit-to-indonesian-huali-mhp-project
[3] `v2/design/routebrieven/nikkel-wedabay-iwip.md` §3/§8 — hergebruikte ankers `ni-iwip-rkef` (→ `co-wedabay-huafei`) en `ni-iwip-jetty` (→ `co-wedabay-jetty`), incl. satellietblik.
[4] `v2/design/routebrieven/kobalt-tfm-quzhou.md` §3/§9 — hergebruikt anker `co-ningbo-kade` en de gebakken haven-aanloop-geometrie `kobalt-tfm-quzhou-aanloop-ningbo.geojson` (11,6 km).
[5] `v2/design/routebrieven/kobalt-huayou-gunsan.md` §3/§5/§8 — hergebruikt anker `co-tongxiang-raffinaderij` (MEE-emissieregister, vergunning 913300007368873961001P) en de gebakken weg-geometrie `kobalt-huayou-gunsan-weg-tongxiang-ningbo.geojson` (192,2 km).
[6] `v2/design/kobalt-sitelaag.json`, anker `w-huafei-wedabay` — nameplate 120 kt Ni + 15 kt Co/jaar (2023, in bedrijf sinds juli 2023); status niet bijgewerkt met de 2026-care & maintenance (zie §7).
[7] `data/cobalt.js` (v1-register) — flows `co-weda` (mijn, Weda Bay/IWIP) en `co-ref-huayou` (Tongxiang/Quzhou, Huayou) als checklist-startpunt.
[8] Wikipedia (EN), "Zhejiang Huayou Cobalt" — bevestigt eigendom Huafei-HPAL (Weda Bay) en de Tongxiang-hoofdraffinage onder dezelfde groep. https://en.wikipedia.org/wiki/Zhejiang_Huayou_Cobalt
[9] Haalbaarheidstoets M31-golf6 (kobalt-wedabay-tongxiang) + eigen herhaling deze sessie — `hecht_marnet.marnet_zee`: IWIP-jetty (0.4745, 128.0055) → zeeknoop 9033 (0.0961, 129.1306) op 131,99 km, onafhankelijk twee keer identiek gemeten.
[10] `v2/design/routebrieven/kobalt-morowali-quzhou.md` §2/§9 en `kobalt-obi-ganzhou.md` §2/§9 — precedent voor de omwegfactor-analogie in been b3 en voor het patroon "stoppunt op de Chinese kade als de vervolgroute niet zendingsniveau is gebrond".

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Status: gebakken.** `bash v2/tools/bak_stromen.sh kobalt-wedabay-tongxiang` →
`v2/data/stroomroute-kobalt-wedabay-tongxiang.json` (28,8 KB) — **4.116,0 km · 1.388
punten · 4 markers**, 5 benen, 0 naden > 0,00 km.

| # | fase | modaliteit | km gebakken | km (brief) | stippel? | recept |
|---|---|---|---|---|---|---|
| b1 | A | truck | 4,96 (rechte lijn, 2 punten) | 4,96 hemelsbreed | ja — binnen estate | `--stippel` |
| b2 | B | zee (haven-aanloop) | 142,3 (114 punten) | 131,99 (haalbaarheidstoets, rechte afstand tot de zeeknoop) | ja — MARNET reikt niet | `maak_havenaanloop.py`, 1e trap geslaagd (cel 0,005° gebufferd), omwegfactor 1,078, 0,36 km "over land" uitsluitend op de kade-korrel (geen echte kruising) |
| b3 | B | zee | 3.764,9 (388 punten) | indicatief 3.700–3.950 | nee | MARNET `--been`, geen ±15%-toets (geen publicatie) |
| b4 | B | zee (haven-aanloop) | 11,6 (5 punten) | 11,6 (letterlijke kopie) | ja — MARNET reikt niet tot de kade | letterlijke kopie `kobalt-tfm-quzhou-aanloop-ningbo.geojson`, geen nieuwe run |
| b5 | C | truck | 192,2 (879 punten) | 192,2 (letterlijke kopie) | nee — doorgetrokken | letterlijke kopie `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson`, geen nieuwe wegscan |

**Toets (bakhandleiding §5):**
- Naden tussen opeenvolgende benen: **0,00 km** op alle vier de overgangen (geen
  enkele > 5 km).
- Markers: alle vier op **0,0–0,0001 km** van hun been (anker = routeerpunt op elk
  van de vier punten).
- `toets_knikken.py`: 24 knikken ≥ 60°, waarvan **1 omkering ≥ 150° op b5** (bocht
  bij 30,77832/120,91876, "scherp, echt", 0 terugloop) — deze zit al in het
  gekopieerde `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson` en is dus
  geen eigen bevinding van deze bake (andermans bestand, niet aangeraakt).
  b3 (zeebeen) heeft 4 knikken maar 0 omkeringen ≥ 150° — normale zeeroute-bochten.
- `toets_rechte_benen.py --min-km 5`: b1 (5,0 km, verhouding 1,008) staat op de
  lijst als **verwacht** — het is een gestippelde rechte lijn "geen net op deze
  korrel", precies zoals de norm dat toelaat (· = gestippeld, geen claim).
- `json.load`: `versie 2`, `punt_formaat lonlat`, alle modaliteiten in
  {zee, truck}, elk been ≥ 2 punten, bestand 28,8 KB — allemaal binnen de norm.

**Stippel-/aanloop-toelichting:**
- b1: parkinterne stippel, analoog aan `kobalt-morowali-quzhou` b1 — geen wegscan
  binnen het IWIP-terrein.
- b2: de zwaarste haven-aanloop van deze keten. `maak_havenaanloop.py` onder
  `timeout 300` in het zwaar-slot slaagde meteen op de eerste trap (cel 0,005°
  gebufferd) — geen terugval nodig, geen tweede poging gedaan.
- b4: letterlijke kopie van de al gebakken `kobalt-tfm-quzhou`-aanloop
  (co-ningbo-kade is exact hetzelfde punt in beide stromen).
- b5: letterlijke kopie, omgekeerde richting van `kobalt-huayou-gunsan` b1 (via
  `kobalt-murrinmurrin-kwinana`'s eigen omkering) — dit been draagt de
  "aannemelijk: eigendom, geen zending-bevestiging"-aanname uit de brief in de
  beennaam, niet in de lijnstijl. Getekend (niet vervallen), want de brief laat
  b5 expliciet open zonder een weerlegging te vinden.

**Lessen / open punten die overgaan naar het rapport:**
- Alle vijf coördinaten zijn hergebruikte ankers (nikkel-wedabay-iwip,
  kobalt-tfm-quzhou, kobalt-huayou-gunsan) — geen nieuwe satellietblik nodig
  deze ronde, conform de bak-aanwijzing.
- Geen profiel in `maak_stroombeen_weg.py` nodig: beide truck-benen zijn stippel
  resp. letterlijke geojson-kopie.
- Registerregel voor `main.js` (centraal, niet door deze bake gedaan):
  `{ sleutel: "wedabay-tongxiang", bestand: "stroomroute-kobalt-wedabay-tongxiang.json", aan: true }`.
