# Routebrief · koper (concentraat) — Collahuasi → Tongling (China)

*Vierde routebrief volgens `../routebrief-werkwijze.md`, aangescherpt formaat (2026-07-28).
Keten: **slurryleiding** (Collahuasi → Puerto Patache, 192,4 km — als enige leiding van de
atlas mét gekarteerd tracé) → **zee** (Patache → Yangtze-monding, router) → **binnenvaart**
(Yangtze-monding → Tongling, ~550 rivier-km) → **oostgeul + kade** van de TNMG-smelter.*

*Toets-doel: het Yangtze-been als **stedenlijst op rivier-kilometrering**, zodat een
verkeerde arm of een overgeslagen stad meetbaar wordt. Let op de bekende nuance: veel
concentraat voor de Yangtze-smelters lost in werkelijkheid al **stroomafwaarts** bij
Zhangjiagang of Jiangyin en gaat daarvandaan verder — die punten staan daarom als
referentie in de brief.*

---

## Kernfeiten die de vorm van de keten bepalen

1. **De leiding ís gekarteerd** — anders dan bij Escondida. Het tracé Collahuasi→Patache
   is uit **14 OSM-ways met `substance=slurry`** gestikt tot 1.363 punten en meet
   **192,4 km tegen ±200 gepubliceerd (−3,8%)** [P1]. **7 van die 14 ways dragen tegelijk
   `highway=track` + `surface=dirt`**: de pijp ligt begraven onder zijn eigen
   onderhoudsweg — dat is meteen de beste onafhankelijke bevestiging dat het tracé klopt,
   want die zandweg is op de satelliet zichtbaar.
2. **De leiding eindigt niet bij de pier maar bij de indikkers.** Collahuasi's eigen
   materiaal geeft de keten ná de leiding: *espesadores → planta de molibdeno → planta de
   filtro → stockpile → embarque* [P2]. Er zitten dus **vier verwerkingsstappen** tussen
   het eind van de leiding en het schip; die horen niet in één punt samengeperst.
3. **Patache is Collahuasi's eigen terminal**, niet de haven Antofagasta waar
   `data/copper.js` de stroom heen stuurt (120 km noordelijker).
4. **Tongling ligt aan de oostgeul, niet aan de hoofdgeul.** De kade van de nieuwe
   TNMG-kopersmelter ligt op de oostelijke arm om het eiland; het schip komt van
   benedenstrooms, gaat bij de noordpunt de oostgeul in en zakt naar de kade. Die geul is
   in 2026-07-24 handmatig satelliet-gelegd omdat OSM hem alleen als onvolledig watervlak
   kent — zie `data/vaarwegen-handmatig.geojson` [T1].

## Been 1 · slurryleiding — Collahuasi → Puerto Patache (192,4 km, eigen verbinding)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Kop van de slurryleiding (pompstation Collahuasi)** — 1,9 km van Rajo Ujina, 2,3 km van het mijncomplex | laadplek | -20.97783, -68.64395 | [P1] | bevestigd |
| 2 | — | Rajo Ujina / Rajo Rosario — de putten zelf; erts gaat naar de molen, niet de pijp in | referentie (niet aan lijn) | — | [P1] | bevestigd |
| 3 | 0–192 | Het tracé daalt van ~4.400 m naar zeeniveau; 7 van de 14 ways dragen `highway=track` + `surface=dirt` = de onderhoudsweg bovenop de pijp | passage | — | [P1] | bevestigd |
| 4 | ~191,7 | **Einde van de OSM-kartering** — 736 m vóór het terminalvlak | referentie | — | [P1] | bevestigd |
| 5 | ~192,4 | **Espesadores (indikkers) Patache** — hier mondt de leiding uit | overslag | *nog te leggen (z18)* | [P2] | **onzeker** |
| 6 | — | planta de molibdeno → planta de filtro → stockpile | passage (terreinproces) | — | [P2] | aannemelijk |
| 7 | — | **Terminalgebouwen + wal-einde van de laadsteiger** | overslag | -20.80503, -70.19773 | [P1] + satelliet z16 | **satelliet-gelegd** |
| 8 | — | **Kop van de laadsteiger — ligplaats bulkcarrier** ⟵ **DIT IS SINDS 2026-07-28 HET ANKER** `cu-patache-kade` (286 m verplaatst vanaf punt 7, de walkant; goedkeuring Lars, doorgevoerd) | laadplek zee | -20.8027, -70.1989 | satelliet z16 | **satelliet-gelegd** |
| 9 | — | Tweede, noordelijker pier bij Patache (aparte terminal, o.a. de kolencentrale) hoort NIET bij deze stroom | referentie (niet aan lijn) | ~-20.7985, -70.1955 | satelliet z16 | aannemelijk |

**Opmerkingen been 1.** ⚠️ **Openstaand punt, nu scherper te formuleren.** Het punt
`cu-patache-kade` doet op dit moment twee dingen tegelijk — eind van de leiding én begin
van het zeebeen — terwijl dat twee plekken zijn met vier verwerkingsstappen ertussen. De
satelliet-check bevestigt dat het huidige anker op de **wal** ligt: de ligplaats waar het
schip afmeert ligt ~280 m NW, aan de kop van de steiger. De **espesadores** staan niet in
OSM (binnen 1,8 km kent de kaart vijf objecten, geen tank) en zijn op z16 niet met
zekerheid aan te wijzen → een z18-pass met Lars' oog erbij, of één coördinaat van hem.
Tot dan blijft punt 5 **onzeker** en tekent de kaart de leiding tot het terminalvlak.

## Been 2 · zee — Puerto Patache → Yangtze-monding

Kade→kade + sanity-ankers; de zeerouter doet de rest (werkwijze §6).

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **Patache — kop laadsteiger** (vertrek) | laadplek | -20.8027, -70.1989 | satelliet z16 | **satelliet-gelegd** |
| 2 | Open Stille Oceaan, noordelijke lane richting Oost-Azië | passage | — | [Z1] | aannemelijk |
| 3 | **Yangtze-monding / 吴淞口** — rivier-km 0, overgang zee → binnenwater | overslag (modus-wissel) | 31.39, 121.51 | [Y1] | bevestigd |

**Negatieve ankers been 2.** Géén Panamakanaal · géén Kaap Hoorn · **niet via de haven
Antofagasta** (120 km noordelijker; Patache is de eigen terminal) · en **niet via
Yangshan**: dat is de containerhaven op eilanden vóór de kust, tientallen km van de
riviermond — concentraat voor de Yangtze-smelters komt daar niet binnen [T2].
Meetlat: de atlas mat de hele keten Collahuasi→Tongling op **19.406 km** met 2 overslagen.

## Been 3 · binnenvaart — Yangtze-monding → Tongling (~550 rivier-km)

**Brief-gestuurd** (werkwijze §6). km = officiële vaarweg-kilometrering vanaf de monding;
waar bronnen een bereik geven staat het bereik.

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **吴淞口 / Yangtze-monding** | vaarweg-overgang | 31.39, 121.51 | [Y1] | bevestigd |
| 2 | ~30 | Baoshan / Luojing — de Baogang-bulkpier aan de Yangtze (aanlandingsalternatief) | referentie (niet aan lijn) | 31.42704, 121.47618 | [T2] | bevestigd |
| 3 | ~92–110 | **南通 (Nantong)** — vanaf hier stroomafwaarts is de geul geschikt voor 50.000-tonners | passage | 32.02, 120.86 | [Y1] | bevestigd |
| 4 | ~130 | **张家港 (Zhangjiagang)** — grote concentraat-loshaven; véél Andes-concentraat lost hier | referentie (niet aan lijn) | 31.97, 120.55 | [Y2] | aannemelijk |
| 5 | ~154–178 | **江阴 (Jiangyin)** — idem: bekende loshaven voor concentraat | referentie (niet aan lijn) | 31.92, 120.28 | [Y1][Y2] | bevestigd |
| 6 | ~200–240 | **镇江 (Zhenjiang)** | passage | 32.19, 119.43 | [Y1] | bevestigd |
| 7 | ~330–370 | **南京 (Nanjing)** — bovengrens voor zeeschepen; de Nanjing Yangtze-brug (1968, ~24 m) is het fysieke mechanisme | sluis/kering (hoogtebeperking) | 32.06, 118.74 | [Y1][Y3] | bevestigd |
| 8 | ~390–399 | **马鞍山 (Ma'anshan)** | passage | 31.70, 118.48 | [Y1] | bevestigd |
| 9 | ~440–449 | **芜湖 (Wuhu)** | passage | 31.33, 118.37 | [Y1] | bevestigd |
| 10 | ~547–552 | **铜陵 (Tongling)** — vaarwegkilometrering van de stad | passage | 30.94, 117.81 | [Y1] | bevestigd |
| 11 | — | **Noordpunt van het eiland — invaart oostgeul** (zuid-junctie 117,7373/30,9102 en noord-junctie 117,7696/31,1091 zijn de gedeelde knopen) | vaarweg-overgang | 117.7696, 31.1091 | [T1] | bevestigd |
| 12 | — | **Kade TNMG-kopersmelter Tongling** — losplek | losplek (keten-eind) | 117.7718, 30.98656 | [T1] + satelliet (2026-07-24, go Lars) | **satelliet-gelegd** |
| 13 | — | Oude, gesloten smelter (117,756/30,918) en het eerdere foute terrein (117,773/30,939) | referentie (niet aan lijn) | — | [T1] | bevestigd |

**Negatieve ankers been 3.** **Géén sluizen** op de benedenloop — de Yangtze is vrij
stromend tot ver boven Tongling · **niet via de west-arm om het Tongling-eiland**: die is
in de bake weggeknipt met `knipWayId` omdat de doorgaande vaart de oostgeul neemt [T1] ·
**niet boven Nanjing met een zeeschip** (bruggenhoogte) — vanaf de monding tot de smelter
is dit één binnenvaartbeen na de overslag · en de lijn hoort **Wuhu vóór Tongling** te
raken; omgekeerde volgorde = fout gekozen arm.

## Been 4 · last mile

Er is er bij deze stroom **geen**: de kade van de smelter ligt aan de rivier en het schip
lost direct op het terrein. Dat is de uitzondering die de regel bevestigt — bij grafiet
(1 km truck) en bij Guixi (aansluitspoor) is de last mile er wél, hier valt hij weg.
Aan de mijnkant is de "last mile" de leiding zelf, been 1.

## Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | `cu-patache-kade` doet leiding-eind én zeebeen-begin | één punt op de wal | **splitsen**: espesadores (leiding-eind, nog te leggen) · terminal · **-20.8027 / -70.1989** (ligplaats, zeebeen) | [P2] + satelliet |
| 2 | flow `cu-collahuasi → cu-ref-tongling`, `via: [cu-port-antofagasta, cu-port-shanghai]` | via Antofagasta + Shanghai | via **Patache** en de **Yangtze-monding**; Yangshan is een containerhaven en hoort er niet in | [T2] |
| 3 | Yangtze-been zonder tussenpunten | vrij geroutet | **via-punt→via-punt** langs de stedenlijst hierboven | werkwijze §5 |
| 4 | Zhangjiagang / Jiangyin | niet in de data | opnemen als **referentie**: reëel alternatief losstation voor dit concentraat | [Y2] |

## Wat de kaart moet tekenen (voorstel)

1. **Leidingbeen** (doorgetrokken — het tracé is gekarteerd, anders dan bij Escondida):
   pompstation -20,97783/-68,64395 → terminalvlak Patache. Laatste 736 m gestippeld
   (kartering houdt daar op).
2. **Zeebeen**: ligplaats Patache → Yangtze-monding.
3. **Binnenvaartbeen**: monding → Nantong → Jiangyin → Zhenjiang → Nanjing → Ma'anshan →
   Wuhu → Tongling, dan de **oostgeul** naar de kade.
4. **Geen last mile** — de kade ís het eindpunt.
5. Zhangjiagang/Jiangyin als **referentiemarkers**, niet aan de lijn.

## Bronnen

**Leiding/Patache [P..]:** P1 OpenStreetMap (ODbL) via `fetch_pijpleidingen.py` — 14 ways
`substance=slurry`, 1.363 punten, 192,4 km tegen ±200 gepubliceerd; kartering stopt 736 m
vóór het terminalvlak · P2 Collahuasi bedrijfsmateriaal: espesadores → planta de molibdeno
→ planta de filtro → stockpile → embarque · + eigen satelliet-overlay Esri z16, 2026-07-28.

**Zee [Z..]:** Z1 atlas-meting Collahuasi→Tongling 19.406 km / 2 overslagen (M26.1).

**Yangtze [Y..]:** Y1 *长江干线航道列表* (wikipedia) + NDRC *长江干线过江通道布局规划
2020-2035* — hoofdvaarweg 2.838 km, kilometrering vanaf de monding, klasse per traject
(南通–浏河口 50.000 t; 南京 10.000 t) · Y2 loshavens Zhangjiagang/Jiangyin voor
concentraat (projectnotitie M26.1) · Y3 Nanjing Yangtze-brug 1968, doorvaarthoogte ~24 m
(LAR-514-onderzoek).

**Tongling [T..]:** T1 `data/vaarwegen-handmatig.geojson` + `tools/maak_tongling_oostgeul.py`
(18 punten, satelliet-gelegd Esri z14, go van Lars 2026-07-24, `?v=077`) · T2
`aansluitingen.json` — Baogang-pier Luojing, en de vaststelling dat Yangshan een
containerhaven op eilanden is.
