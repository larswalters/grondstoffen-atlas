# Routebrief (licht) · kobalt — Huayou Tongxiang (China) → LG-Huayou Gunsan (Zuid-Korea)

**stroom-id:** `kobalt-huayou-gunsan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** kobalttetroxide/-sulfaat van Zhejiang Huayou Cobalt's hoofdraffinage in Tongxiang (Zhejiang) per **truck** naar de containerkade Ningbo Beilun, per **zeeschip** naar Busan, en (nog niet getekend — geen coördinaat) per **truck** naar de LG-Huayou precursor-JV in het Saemangeum-industriegebied bij Gunsan.
**Welke as van het verhaal:** de ontbrekende productfase China-raffinage → Zuid-Korea-precursor — een 1,2 biljoen won JV tussen LG Chem en Zhejiang Huayou Cobalt (aangekondigd april 2023, Saemangeum Industrial Complex, 6공구/blok 6, 50 kt/jaar precursorcapaciteit fase 1 → 100 kt/jaar 2028) [4][5][6]. Jaarvolume: ~10 kt Co/jaar in de v1-checklist (`data/cobalt.js`, flow `co-ref-huayou→co-mkt-lg`, indicatief/nattevingerwerk, geen peiljaar, en dat is een ándere LG-site — Ochang, batterijcellen — niet de nieuwe Gunsan-precursor-JV); een reëel per-zending-volume voor de Gunsan-JV is deze sessie niet gevonden.

## 1 · Ketenkaart
```
Huayou Tongxiang-raffinaderij `co-tongxiang-raffinaderij` ──(b1 truck · G60/G92 Tongxiang–Ningbo · ~150 km)──► Ningbo Beilun-containerkade `co-ningbo-kade` (hergebruikt anker)
   ──(b2a zee · Oost-Chinese Zee → Korea-straat · ~850 km, MARNET)──► zeeknoop 5621 (dichtstbijzijnde MARNET-zeeknoop bij Busan)
   ──(b2b zee-aanloop · ~10,1 km, stippel — LAR-586, kade > 5 km van de zeeknoop)──► Busan New Port `co-busan-newport` ⏹ stoppunt
        ┊ (niet getekend — LG-Huayou-precursorfabriek Gunsan/Saemangeum: geen coördinaat gevonden, zie §7)
   LG-Huayou precursor-JV, Saemangeum Industrial Complex, Gunsan (knoop, §5)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `co-tongxiang-raffinaderij` → `co-ningbo-kade` | G60/G92 Tongxiang–Ningbo (Hangzhou-ringweg-corridor) | ~150 [ontwerp-webcheck; hemelsbreed gemeten 146,6 km deze sessie] | maak_stroombeen_weg (extract `china`) | nee |
| b2a | C | zee | `co-ningbo-kade` → zeeknoop 5621 (Busan) | Oost-Chinese Zee → Korea-straat | ~850 [hemelsbreed 867,2 km deze sessie; ontwerp gaf ~830 MARNET-schatting] | MARNET `--been "zee\|…\|29.9353,121.8695\|<zeeknoop 5621 lat,lon>"` | nee |
| b2b | C | zee (haven-aanloop) | zeeknoop 5621 → `co-busan-newport` | Busan New Port-containerzone | 10,1 [haalbaarheidstoets: `hecht_marnet.marnet_zee`, gemeten] | `maak_havenaanloop.py` (timeout 300; bij "geen pad" terugval rechte stippel) | ja — LAR-586: kade > 5 km van de zeeknoop, ook al snapt de router binnen 25 km |

**Been C (Busan → LG-Huayou-precursorfabriek Gunsan, NIET getekend):** de bron bevestigt het project (1,2 biljoen won JV, Saemangeum-blok 6, 338.000 m²) maar geen enkele geraadpleegde bron (Nominatim, Photon, Overpass ×2 mirrors, Wikipedia-API) geeft een coördinaat voor het perceel zelf — regel "geen coördinaat verzinnen" (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-tongxiang-raffinaderij` | mijn/raffinaderij (kop van b1) | Zhejiang Huayou Cobalt — 镍钴冶炼 (nikkel-kobaltsmelterij), Tongxiang Economic Development Zone fase 2, 梧振东路18号, Jiaxing | 30.6167, 120.5629 | [1][7] | **bron-gelegd** (MEE-emissieregister, vergunning 913300007368873961001P, decimaal én DMS exact overeenkomend; z18 gezien: industriecomplex met opslagtanks, procesgebouwen met leidingwerk en meerdere hallen — consistent met een metallurgisch/chemisch complex) |
| `co-ningbo-kade` | overslag truck → zee | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | `kobalt-tfm-quzhou.md` §3 [8] | bron-gelegd (**hergebruikt anker, letterlijke kopie** — zelfde punt als in kobalt-tfm-quzhou/-morowali-quzhou/-kisanfu-daressalaam, niet opnieuw satelliet-gecheckt; 1,95 km van zijn zeeknoop, geen aanloop nodig) |
| `co-busan-newport` | overslag zee → (onbekend vervolg) | Busan New Port, containerterminal | 35.0731, 128.8338 | haalbaarheidstoets [9] | bron-gelegd (z15 gezien: rijen containerstapels en portaalkranen, schepen aan de kade in de doorgaande containerhaven-geul; 10,12 km van zijn MARNET-zeeknoop, dus haven-aanloop verplicht) |
| — | fabriek (fase D, niet gelegd) | LG-Huayou precursor-JV, Saemangeum Industrial Complex blok 6 (6공구), Gunsan | **niet gevonden** | [4][5][6] | onzeker/open — geen OSM-object, geen Nominatim/Photon-treffer voor het Saemangeum-industrieterrein of blok 6; coördinaat niet verzonnen |

## 4 · Via-punten
Geen via-punten vastgelegd deze sessie: Wikipedia-API en Nominatim/Photon waren het grootste deel van de sessie **429/403 (rate-limited)** op dit gedeelde IP (waarschijnlijk door de gelijktijdige golf-2-agenten) — te weinig budget om 3–8 corridorkeuzepunten op de G60/G92 te bevestigen. Bij het bakken (`maak_stroombeen_weg.py --bron geofabrik`) kan de weg-scan op het `china`-extract zelf via-punten opleveren zonder externe API's; dat gebeurt dan tijdens het bakken, niet in deze brief.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Huayou Tongxiang-raffinaderij | Zhejiang Huayou Cobalt | kobalthydroxide/-erts → kobalttetroxide/-sulfaat | vergunning 913300007368873961001P, geldig 2025-05-26/2030-05-25; geen productiecijfer gebrond | [1][7] |
| LG-Huayou precursor-JV — **knoop, niet gekoppeld** | LG Chem + Zhejiang Huayou Cobalt (50/50, JV aangekondigd april 2023) | kobalt-/nikkelsulfaat → precursor (pCAM) | 1,2 biljoen won; fase 1 50 kt/jaar (target 2026 volgens één bron), fase 2 → 100 kt/jaar 2028; bouw gestart eind 2023, oplevering "eind 2028", commerciële start "begin 2029" volgens kedglobal.com — bronnen lopen uiteen over het opleverjaar | [4][5][6] |

## 6 · Stoppunt
De brief stopt op Busan New Port (`co-busan-newport`): de LG-Huayou-precursorfabriek in Saemangeum/Gunsan is een reëel, bevestigd project, maar (a) geen coördinaat voor het perceel is deze sessie te vinden (§7) en (b) de bouwstatus op de ontwerpdatum (eind 2026) is volgens de enige gedetailleerde bron (kedglobal.com) nog "bouw gestart eind 2023, oplevering eind 2028" — dus vermoedelijk nog een bouwplaats. Zonder coördinaat is er sowieso geen satellietblik mogelijk om het Balama-Vidalia-precedent ("aannemelijk, in aanbouw, volume nul") toe te passen; het been Busan→Gunsan blijft daarom ongetekend en de fabriek staat als losse knoop in §5, net als Huayou Quzhou in `kobalt-tfm-quzhou.md`.

## 7 · Open punten
- **Huayou Tongxiang WÉL gevonden** (correctie op de haalbaarheidstoets, die het endpoint nog als onbereikbaar noteerde): het MEE-emissieregister (`permit.mee.gov.cn/perxxgkinfo/…`) werkte deze sessie wél — POST met `registerentername=华友钴业` + `tempReportKey` + `JSESSIONID`-cookie gaf één treffer (浙江华友钴业股份有限公司, 镍钴冶炼, 嘉兴市/桐乡市), en de detailpagina gaf decimale + DMS-coördinaten die exact overeenkomen (30.6167 N, 120.5629 E). Been C1 (Tongxiang→Ningbo) kan dus wél getekend worden, in tegenstelling tot wat de haalbaarheidstoets als terugvalscenario voorzag.
- **LG-Huayou-precursorfabriek Gunsan: geen coördinaat.** Bevestigd: 새만금산단 6공구 (Saemangeum National Industrial Complex, blok 6), 338.000 m² (~10 ha), Gunsan-si, Jeollabuk-do [4][5]. Niet gevonden ondanks meerdere pogingen: Nominatim (429/403, rate-limited het grootste deel van de sessie), Photon (geen treffer voor het industrieterrein of blok 6), Overpass via twee mirrors (406 op overpass-api.de, timeout op overpass.kumi.systems — zelfde uitkomst als de haalbaarheidstoets). Eerstvolgende zet: een Koreaanse overheidsbron met een kavelkaart (새만금개발청, saemangeum.go.kr) of VWorld/Kakao-geocoding met een API-sleutel.
- **Bouwstatus Gunsan-JV per eind 2026 niet apart geverifieerd deze sessie** — kedglobal.com (april 2023) noemt oplevering eind 2028/commerciële start begin 2029; industrynews.co.kr (eveneens 2023) noemt een optimistischer "fase 1 klaar 2026". Beide bronnen zijn van vóór de bouw; geen van beide is een voortgangsupdate uit 2025/2026. Zonder coördinaat kon dit ook niet met een satellietblik getoetst worden.
- **Via-punten op b1 (G60/G92) ontbreken** — Wikipedia-API en Nominatim/Photon waren het grootste deel van de sessie rate-limited (gedeeld IP, waarschijnlijk door gelijktijdige golf-2-agenten); geen budget meer om dit alsnog op te lossen binnen het webbudget.
- **km b2a is een hemelsbreed/MARNET-indicatie**, geen gepubliceerde route-lengte — de exacte MARNET-km volgt bij het bakken.
- **Zeeknoop 5621** (bij Busan) is uit de haalbaarheidstoets overgenomen (35,0731/128,8338 → 10,12 km); exacte lat/lon van knoop 5621 zelf niet apart opgevraagd deze sessie — de bak-agent haalt die met `hecht_marnet.marnet_zee` zoals in bakhandleiding §2.
- **Jaarvolume Gunsan-JV per zending onbekend** — het enige cijfer (10 kt Co/jaar, `co-ref-huayou→co-mkt-lg`) is uit v1's checklist en betreft een ándere LG-site (Ochang, batterijcellen), niet de nieuwe Gunsan-precursor-JV.

## 8 · Bronnen
[1] MEE-emissievergunningregister (permit.mee.gov.cn/perxxgkinfo, recept `zoek-chinees-adres-recept.md`) — vergunning 913300007368873961001P, 浙江华友钴业股份有限公司, 生产经营场所地址 浙江省嘉兴桐乡市经济开发区二期梧振东路18号, 行业类别 镍钴冶炼, geldig 2025-05-26/2030-05-25, decimaal 120.56289/30.61670 + DMS 120°33'46.40"E/30°37'0.12"N. https://permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action
[2] Wikipedia (EN), "Zhejiang Huayou Cobalt" — bevestigt hoofdraffinage in Tongxiang Economic Development Zone, Zhejiang (niet Quzhou). https://en.wikipedia.org/wiki/Zhejiang_Huayou_Cobalt
[3] Huayou Cobalt, corporate site. https://en.huayou.com/
[4] KED Global, "LG Chem, Huayou Cobalt to build $900m battery material plant in S. Korea" (2023-04-14) — 1,2 biljoen won JV, Saemangeum Industrial Complex Gunsan, 50 kt/jaar fase 1 → 100 kt/jaar 2028, bouw start eind 2023, oplevering eind 2028, commerciële start begin 2029. https://www.kedglobal.com/batteries/newsView/ked202304140020
[5] Industry News (KR), "LG화학-화유코발트, 새만금서 이차전지 소재 '전구체' 생산 공장 건설" (2023) — locatie 새만금산단 6공구, 338.000 m² (~10만 평), investering 1,2 biljoen won t/m 2028. https://www.industrynews.co.kr/news/articleView.html?idxno=49544
[6] Korea Times, "LG Chem to build battery precursor factory in Korea with China's Huayou Cobalt" (2023-04-17). https://www.koreatimes.co.kr/business/companies/20230417/lg-chem-to-build-battery-precursor-factory-in-korea-with-chinas-huayou-cobalt
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15/z18, live) — `v2/build-cache/satcheck/sat-kobalt-huayou-gunsan-tongxiang-raffinaderij.png`, `sat-kobalt-huayou-gunsan-tongxiang-close.png`, `sat-kobalt-huayou-gunsan-busan-newport.png`.
[8] `v2/design/routebrieven/kobalt-tfm-quzhou.md` §3 — hergebruikt anker `co-ningbo-kade` (29.9353, 121.8695).
[9] Haalbaarheidstoets M31-golf2 (kobalt-huayou-gunsan) — `hecht_marnet.marnet_zee`: Busan New Port (35.0731, 128.8338) → zeeknoop 5621 op 10,12 km; Ningbo Beilun (29.9353, 121.8695) → zeeknoop 5849 op 1,95 km.
[10] OpenStreetMap via Nominatim (ODbL) — "새만금 방조제"/"새만금호" (Saemangeum-zeewering/-meer) gevonden, geen object voor het industrieterrein zelf of blok 6; grootste deel van de sessie 429/403 (rate-limited). https://www.openstreetmap.org

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `kobalt-huayou-gunsan`** → `v2/data/stroomroute-kobalt-huayou-gunsan.json` — 3 benen, **1.176,4 km**,
991 punten, 3 markers. truck 192,2 · zee 973,4 + 10,8 (stippel) = 984,2 km. Recept: `bak_stromen.sh` (functie
`bak_kobalt_huayou_gunsan`), profiel `kobalt-huayou-gunsan-tongxiang-ningbo` in `maak_stroombeen_weg.py`.

**b1 (truck, weg-scan `china`-extract, `maak_stroombeen_weg.py --profiel kobalt-huayou-gunsan-tongxiang-ningbo`):**
van de raffinaderij-anker (30,6167/120,5629) naar de Ningbo Beilun-kade (29,9353/121,8695), G60/G92-corridor.
Scanner leverde zelf de corridor (geen via-punten aangeleverd — brief §4/§7). **192,1–192,2 km tegen ~150 km
ontwerp-webcheck (hemelsbreed 146,6 km) = +28,0%, BUITEN de ±15%-norm.** ⚠️ **Bevinding, niet dichtgetrokken**
(bakhandleiding §5): de brief-km was een niet-onafhankelijk-geverifieerde webcheck-schatting, geen gepubliceerde
routelengte; de gemeten omwegfactor over de G60-ringweg rond Hangzhou/Jiaxing is aannemelijk voor een werkelijke
truckcorridor (geen rechte lijn, geen keerlus behalve één triviale 0,02 km). Anker-verbindingen (plant→weg 0,13 km,
weg→kade 0,04 km) beide binnen de norm.

**b2a (zee, MARNET, `--been "zee|...|29.9353,121.8695|35.0485,128.7268"`):** Ningbo-kade snapt op **1,95 km** van
zijn zeeknoop (< 5 km, LAR-586 → geen haven-aanloop nodig aan de Ningbo-kant); zeeknoop 5621 zelf snapt op
0,000 km (dat IS de knoop). Zeeknoop 5621 = 35,0485/128,7268, opgehaald met `hecht_marnet.marnet_zee`
(bakhandleiding §2). Resultaat **973,4 km over 15 MARNET-edges** (106 punten) tegen de indicatieve ~850 km uit de
brief (hemelsbreed 867,2 km deze sessie eerder gemeten) = **+14,5%**, binnen de ±15%-norm. Lengte-invariant:
getekende lijn 973,410 km vs som edge-km 973,400 km = +0,010 km (de naden).

**b2b (zee, haven-aanloop Busan New Port, stippel-geojson, LAR-586-verplicht):** `maak_havenaanloop.py --van
35.0485,128.7268 --naar 35.0731,128.8338` — pad over water gevonden op de eerste getoetste trap (cel 0,02° kaal,
na het proberen van vijf fijnere trappen die alle "geen pad" of een grover resultaat gaven), **10,8 km · 6 punten ·
0,00 km over land**, omwegfactor 1,072 tegen de rechte lijn (10,1 km). Geen terugval nodig — de reden voor de
haven-aanloop is niet dat de router geen pad vindt (Busan snapt ruim binnen de 25 km-norm), maar LAR-586: de kade
ligt 10,12 km van haar zeeknoop (> 5 km), dus zonder aanloop zou het zeebeen 10 km vóór de kade eindigen.

**Toets naden:** b1→b2a **0,00 km** (het wegbeen eindigt letterlijk op de Ningbo-kade-coördinaat, "continuïteit met
de haven-aanloop = 0,000 km" meldde de weg-scan zelf) · b2a→b2b **0,00 km** (beide beginnen/eindigen op zeeknoop
5621, exacte coördinaatgelijkheid). Geen naad boven de norm van 5 km.

**`toets_knikken.py`:** truck-been 20 knikken ≥60° waarvan 1 omkering (176,3°, R~124 m, "scherpe bocht, echt",
v=2,2 — een kopmaak-plek bij Tongxiang, geen terugloop) en 19 spikes (R 2–132 m, typisch voor OSM-stadswegen
rond Jiaxing/Ningbo, geen van alle TERUGLOOP); zee-been 5 knikken ≥60° (alle "krappe bocht", R 4.466–8.070 m,
0 omkeringen — normale MARNET-routebochten in de Oost-Chinese Zee/Korea-straat). **0 TERUGLOOP** over de hele
stroom (de enige klasse die gerepareerd hoort te worden, bakhandleiding §5) → geen actie nodig.
**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — het haven-aanloopbeen (10,8 km,
omwegfactor 1,072) is niet degenererend recht, dus terecht niet gevlagd.

**Contract:** `json.load` slaagt, `versie == 2`, `punt_formaat == "lonlat"`, alle drie modaliteiten in {truck, zee}
⊂ de toegestane set, elk been ≥ 2 punten (6/106/879), bestandsgrootte **20,9 KB** (21.449 bytes) — ruim onder de
~300 KB-norm.

**Gereedschapslessen:**
- De weg-lengtetoets waarschuwt terecht bij een schatting die zelf al als "ontwerp-webcheck, niet onafhankelijk
  geverifieerd" in de brief stond — een webcheck-km is geen gepubliceerde routelengte en de ±15%-marge geldt de
  laatste, niet de eerste.
- `maak_havenaanloop.py` koos hier de grofste geteste trap (cel 0,02° kaal) als winnaar ("minste land midden op de
  lijn, dan totaal, dan kortst"), niet de fijnste — bij een korte open-water-aanloop zonder kustobstakel geeft een
  grover raster soms al 0,00 km land en wint dan op totale lengte.
- Tijdens het bakken meldde `bak_stromen.sh` zelf een shell-syntax-fout ná het schrijven van het json (concurrent
  bewerkte gedeelde `bak_stromen.sh`-tekst door andere golf-2-agenten tegelijk met deze bake-run); `bash -n`
  bevestigde ná afloop dat het bestand syntactisch weer geldig was en het geschreven json was compleet en correct
  — een leesrace tijdens gelijktijdig schrijven aan hetzelfde gedeelde bestand, geen fout in het eigen recept.

**Open (ongewijzigd t.o.v. §7 van de brief):** been C (Busan → LG-Huayou precursor-JV, Saemangeum-blok 6, Gunsan)
blijft ongetekend — geen coördinaat gevonden voor het perceel deze sessie. Via-punten op b1 (G60/G92) ontbreken
nog steeds (Wikipedia/Nominatim/Photon rate-limited); de weg-scan heeft dit zelf ondervangen door de corridor uit
het `china`-extract te halen, dus dit blokkeert het bakken niet, alleen de brief-documentatie van tussenpunten.
