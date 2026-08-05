---
type: werkorder
datum: 2026-08-05
stroom: koper-escondida-guixi
status: te beoordelen (één redactioneel besluit open — zie de kop van sectie C)
---

# Werkorder — fase D en E van de koperketen Escondida → Guixi

*Uitkomst van de ankerronde van 2026-08-05 (zes zoeklijnen, elk met een eigen weerlegger).
Twee zoeklijnen hielden stand (R1 walsdraadfabriek, R5 Beilun-overslag, R6 bestaand deel);
drie sneuvelden bij de weerlegging (R2 kathode-expeditie, R3 fase-E-bestemming, R4
Guixi-stations) en staan daarom voluit in sectie F — niet stilzwijgend weggelaten.*

# WERKORDER — koper Escondida → Guixi, fase D op de bol

**Project:** `C:\automation\Projects\General\grondstoffen-atlas` · **stroom-id:** `koper-escondida-guixi` · **brief:** `v2\design\routebrieven\koper-escondida-guixi.md` · **datum:** 2026-08-05

**Uitgangspunt, en het is minder dan de opdracht hoopte.** Van de twee fasen die deze ronde
moest deblokkeren komt er **één half binnen**:

* **Fase D is tekenbaar**, maar als een been tussen twee **satelliet-gelegde registerpunten**
  op hetzelfde complex — niet als laadplek → losplek. De kathode-**expeditie** (de kop van
  been 5) is niet gevonden en wordt niet vervangen door een gok.
* **Fase E is NIET tekenbaar.** De enige kandidaat-bestemming (江铜铜箔 Nanchang) is bij de
  weerlegging gebroken op een entiteitsfout: het gedocumenteerde contract gaat over
  **kathode**, niet over walsdraad, en de tegenpartij is een ándere rechtspersoon, 508 km
  oostwaarts in Zhejiang. Het beargumenteerde stoppunt van de brief blijft staan en wordt
  **sterker** onderbouwd dan voorheen.

**⚠️ Het redactionele besluit dat Lars moet nemen staat bovenaan sectie C** en is precies zo
groot als het besluit van 2026-08-04 bij grafiet: tekenen we been 5 met een **substituut-kop**
(het officiële productiepunt van de smelter) terwijl de echte laadplek open staat, of laten we
fase D leeg tot die laadplek gevonden is? De werkorder is geschreven voor "tekenen"; de
"niet tekenen"-variant staat er expliciet naast in **F7**.

**⚠️ Vóór je begint:** de working tree is schoon (`git status` leeg, HEAD `5a08236`). Stage bij
elke commit hieronder **alleen je eigen bestanden** (sectie J van de project-`CLAUDE.md`).

---

## A · Ankerlijst

lat, lon in decimale graden, 5 decimalen, WGS-84. "aansl." = `v2/data/aansluitingen.json`, en die
wordt **gegenereerd** — je bewerkt `v2/tools/maak_aansluitingen.py` (de redactionele lijst is de
bron van waarheid). Kolom **rol** onderscheidt expliciet wat de werkwijze uit elkaar wil houden:
*aansluitpunt/poort* (waar een last-mile-lijn aanhecht) · *routeerpunt* (waar het net begint) ·
*terreinanker* (het zwaartepunt van een werk, voor een registerknoop).

| id | omschrijving | lat, lon | status | rol | landt in |
|---|---|---|---|---|---|
| `cu-guixi-walsdraad` | 江西铜业铜材有限公司 — officieel **productielocatiepunt** uit het nationale emissievergunningregister (913600007363561816001Q, 铜压延加工, 冶金大道 **19**号). Ligt op de zuidberm van de interne hoofdas 闪速大道, op de mond van een noord-zuid inrit | **28.33180, 117.21919** | **satelliet-gelegd** (z18, 0,53 m/px; eigen pass 2026-08-05 `sat-W-synth-walsdraad-registerpunt.png`) | **aansluitpunt op de interne hoofdas** — ⚠️ *géén* poort: op z18 is geen poortgebouw, slagboom of hek-onderbreking te zien, alleen een T-aansluiting van een inrit op de as | aansl. (nieuw, **`modi=[]`** — zie B5) + marker + staart been 5 |
| ↳ routeerpunt | projectie op OSM `way/1462532976` (`highway=service`, geen access-tag) | **28.33188, 117.21919** | gemeten (8 m van het anker, punt-tot-segment) | routeerpunt | bakprofiel + brief |
| `cu-guixi-smelter-register` | 江西铜业股份有限公司贵溪冶炼厂 — registerpunt (91360000X12430120H001P, 铜冶炼, **zelfde adres** 冶金大道 19号). Midden in het pyro-hart: zwavelzuurtanks en bolvormige opslag NW, procesblokken met pijpenbruggen, stoompluim uit de vlamovenstraat, koeltorens en bezinkbekkens zuid | **28.33227, 117.22545** | **satelliet-gelegd** (z18) | **terreinanker / registerknoop** — dient als **substituut-kop** van been 5 (zie C, besluit) | bakprofiel + brief; **geen** eigen aansluiting (`cu-guixi-spoor` is al de aansluiting van deze knoop) |
| ↳ routeerpunt | projectie op dezelfde `way/1462532976` | **28.33188, 117.22545** | gemeten (43 m van het anker) | routeerpunt | bakprofiel + brief |
| `cu-guixi-smelter-eia2017` | Tweede, onafhankelijke officiële coördinaat van hetzelfde terrein: 赣环监字（2017）第S007号 §2.1.1 «地理坐标为东经117.225156，北纬28.329914» | **28.32991, 117.22516** | bevestigd (provinciale overheidsbron, geen eigen pass exact op dit punt) | **referentie** — kruiscontrole op datum én terreingeometrie | alleen brief §9 |
| `cu-guixi-groep-tongcai` | 江西铜业集团铜材有限公司 (USCC 913606817442997892, 冶金大道 **zonder** huisnummer) — een **ándere rechtspersoon** met een eigen ommuurd werk 1.749 m OZO, eigen poortgebouw aan de boulevard, en in de zuidoosthoek een open veld met rijen cilindrische stapels | **28.32956, 117.23688** | **satelliet-gelegd** (z17/z18) | **reëel alternatief (werkwijze §2) + negatief anker been 5, straal 1,0 km** | brief §2/§4 + verklikker in E; géén aansluiting, géén node |
| `cu-beilun-laadspoor` | 北仑港站 — laadsporen van het havenstation (北极星路178号, 10,9 ha, 2 货场 / 10 装卸线, 78万TEU/j, 中铁联合国际集装箱宁波北仑). Het **tweede anker** dat werkwijze §2b bij de overslag Beilun eist | **29.92653, 121.87308** | **satelliet-gelegd** (z19, 0,26 m/px) | **laadplek** (vertrek been spoor) | aansl. (nieuw, `modi=["spoor"]`) + marker |
| ↳ routeerpunt | kopeinde van de sporenbundel = landnet-knoop 326694; **dit is al het beginpunt van het gebakken spoorbeen** | **29.92820, 121.87380** | gemeten (**0,198 km** — eigen meting tegen `landnet.bin`) | routeerpunt | bakprofiel + brief (max snap 0,198 km) |
| `cu-beilun-bandlandpunt` | Landpunt van de transportband vanaf de ertslosberth + overslagtoren; vandaar lopen banden zuidwaarts het bulkveld in | **29.92742, 121.87573** | **satelliet-gelegd** (z18) | **terreinstap** (overslag) | brief + bakrecept; géén eigen aansluiting |
| `cu-beilun-kade` | Losberth met de rode grijper-scheepslossers — **bestaand anker, ongewijzigd**, maar wordt **zee-only** | **29.93640, 121.88300** | satelliet-gelegd (2026-07-28, hercontrole z17 2026-08-05) | losplek zee | aansl. (**`modi` van `["zee","spoor"]` → `["zee"]`**) |
| `cu-guixi-spoor` | Ertslosbundel 贵溪冶炼厂 — **bestaand anker, ongewijzigd** | 28.32710, 117.22600 | satelliet-gelegd (z18/z17) | losplek spoor | aansl. (ongewijzigd) |
| — | **kathode-laadplek / expeditie 贵冶** (kop been 5, §5.5 van de brief) | — | **niet gevonden** | — | niets — blijft **F1** |
| — | **expeditiedeur / laadperron walsdraadfabriek** (kop fase E, §5.8) | — | **niet gevonden** | — | niets — blijft **F2** |
| — | **terreincentrum 铜材公司** (het blok zelf) | — | **aannemelijk, twee tegenstrijdige kandidaten** | — | niets — **F3**; géén aansluiting, géén marker |
| — | fase-E-bestemming (afnemer van het walsdraad) | — | **niet gevonden** | — | niets — **F4/F5** |

**Wat er NIET in staat, en waarom dat een resultaat is.** De brief stelde in §6 rij 7 twee nieuwe
aansluitingen in het vooruitzicht: `cu-guixi-kathode-laad` **en** `cu-guixi-walsdraad`. Alleen de
tweede komt er. De eerste is de kathode-expeditie en die is deze ronde niet gevonden — niet door
gebrek aan zoekwerk (zie F1) maar omdat Esri bij Guixi **geen z19 heeft** (`Map data not yet
available`, door drie agents onafhankelijk gereproduceerd) en geen enkele bron 电解车间 of 成品库
aan een gebouw koppelt.

**Adrescorrectie die de brief raakt (geen coördinaat, wél een bron).** De brief zet de
walsdraadfabriek op 冶金大道 **15**号 [D3]. Het emissievergunningregister geeft voor **beide**
Guixi-vennootschappen het veld `生产经营场所地址` = 冶金大道 **19**号, en de vergunning-PDF
(`xkgg!downloadFile.action?fileType=fbfile`) van 江西铜业铜材有限公司 zet ook het `注册地址` op 19号.
15号 is het **hoofdkantoor-/administratieve adres** van de groep, de beursvennootschap én de
加工事业部 — de collocatie-conclusie van de brief klopt dus, maar de onderbouwing via nummer 15
moet vervangen worden.

---

## B · Reparaties aan het bestaande deel

### B1 — het gat van 2.379 m bij Beilun sluiten (R5, houdbaar)

**Nu:** het zeebeen eindigt op `121.8837, 29.9478` (MARNET-knoop in de geul) en het spoorbeen
begint op `121.8738, 29.9282` (kop van de sporenbundel). Daartussen: **2.379,1 m niets**, en dat
is het grootste gat van alle vijf stromen op één na.

**Wat het is** — eigen nameting bevestigt R5: het is géén fout uiteinde maar **twee tegengestelde
snaps van één aansluiting**. Het anker `cu-beilun-kade` snapt 1.269,4 m NNO de geul in (zeebeen) en
1.271,7 m ZW het spoor op (spoorbeen). ⚠️ Correctie op R5: die twee tellen **niet exact** op tot
2.379 m — de hoek tussen de snaps is 138,8°, niet 180°, dus 1.269,4 + 1.271,7 = 2.541,2 tegen een
gat van 2.379,1 m. Het woord "exact" moet uit de brief.

**Wordt:** drie korte benen ertussen, in reisvolgorde (bak-recept in C2):

| nieuw been | modaliteit | van → naar | km | reden |
|---|---|---|---|---|
| haven-aanloop Beilun | `zee`, **stippel** | 29.94780, 121.88370 → 29.93640, 121.88300 | 1,27 | het MARNET-routeerpunt ligt in de geul, het schip lost aan de berth (spiegelbeeld van de Coloso-aanloop) |
| transportband losberth → landpunt | `leiding`, **stippel** | 29.93640, 121.88300 → 29.92742, 121.87573 | 1,22 | eigen terrein, geen net — de bandtrestle kruist het slik en het havenkanaal |
| ertsveld → laadspoor 北仑港站 | `leiding`, **stippel** | 29.92742, 121.87573 → 29.92653, 121.87308 | 0,27 | eigen terrein, geen net |

**Waarom `leiding` en niet een nieuwe kleur.** `KLEUR` in `v2/src/stroomroute.js` beschrijft `leiding`
letterlijk als *"een EIGEN VERBINDING, geen net … dit been kan per definitie niet herrouteren"* —
dat is exact wat een transportband is (besluit Lars 2026-07-23: door een eigen verbinding gaat één
product tussen twee punten). ⚠️ Wil Lars een eigen bandkleur, dan is dat **één regel** in `KLEUR`;
laat dat een expliciete keuze zijn en geen sluipende hergebruik-verwatering, want de projectregel is
dat twee modaliteiten in één kleur de legenda onwaar maken.

**Uitkomst, gemeten vooraf:** gaten worden `0 · 0 · 0 · 0 · 0 · 0 · 0,198 · 0,541 km`. ⚠️ **R5's
belofte "van 2.379 m naar ~0 m" is fout** en dat heeft de weerlegger nagerekend: er blijft
**198 m** over tussen het laadspoor-anker en het routeerpunt waar het spoorbeen begint. Dat is
géén restfout maar precies `anker ≠ routeerpunt` (werkwijze §2b), het valt binnen de 0,5 km-eis,
en het hoort als **max snap 0,198 km** in het b-blok van de brief.

**⚠️ Wat je NIET moet doen:** de kop van het spoorbeen naar het laadspoor verplaatsen. Het
spoorbeen begint 198 m **noord** van de laadplek en loopt daarna zuidwaarts er langs op 14,1 m —
verplaats je de kop, dan krijg je een overschiet-en-terug-haak, precies de klasse die op
2026-08-05 bij de via-punten is benoemd.

### B2 — de snap-meting die R5 als kopbewijs voerde is blind (niet overnemen)

R5 opent met "de spoor-snap gaat van 1,27 km naar 0,198 km, langs een onafhankelijke weg gemeten".
Eigen nameting tegen `landnet.bin` (444.101 spoorknopen · 1.883 wegknopen):

```
cu-beilun-laadspoor      spoor  knoop 326694 op 0,198 km
cu-beilun-bandlandpunt   spoor  knoop 326694 op 0,205 km
```

Beide punten scoren tegen **dezelfde** grofkorrelige knoop; élk punt binnen ~200 m daarvan scoort
hetzelfde, op de rails of ernaast. Wat de spoor-claim werkelijk draagt is de **4,5 m tot OSM
`way/1491021972`** plus het z19-beeld (vijf parallelle sporen, vier rode rail-mounted
portaalkranen, wagons met containers eronder). Neem díe formulering over in de brief, niet de
snap-winst.

### B3 — de productvraag bij Beilun is een echt conflict, geen detail

Wat op 北仑港站 satelliet-gelegd is, is een **container**emplacement (78万TEU, containerwagons,
rail-mounted portaalkranen), terwijl ladder **L3** van de brief zegt: *concentraat, natte bulk in
open wagons*. Twee onafhankelijke agents zagen hetzelfde beeld. Chinese bron die de
containerlezing steunt: het 鹰潭国际陆港 meldt 海铁联运-班列 vanaf 宁波北仑 met o.a. 铜精矿 in de
lading, en het eerste multimodale importgeval van Jiangxi (2026-06-29, 26 t 再生铜原料) ging
『原箱』 — in de originele container — via 贵溪北站.

**Dit is een vraag aan de brief, niet aan de satelliet.** Beslis hem in §2a vóór fase C herschreven
wordt: containers of bulk. Zolang hij open staat is `cu-beilun-laadspoor` **geografisch waterdicht
en inhoudelijk voorwaardelijk** — dat hoort er in de `noot` bij te staan.

### B4 — het bak-recept vastleggen, en de tweetraps opheffen

`v2/tools/bak_stromen.sh` draagt vandaag alleen `bak_grafiet()` plus de waarschuwing dat de vier
andere recepten ontbreken. R6 heeft het koperrecept gereconstrueerd en **twee keer byte-identiek
nagedraaid** (canonieke sha zonder het veld `gemaakt`). Dat recept gaat mee in C2, uitgebreid met
de nieuwe benen — met drie waarschuwingen die de weerlegger heeft nagemeten:

1. **De tweetraps is niet geometrisch nodig.** `hecht_marnet route` met `--been-geojson` direct op
   `spoorroute-nieuw-beilun-guixi.geojson` levert in **één stap** hetzelfde bestand; alleen de
   sleutel `herkomst` ontbreekt dan. De nieuwe functie is daarom éénstaps, en de **kop van de
   functie in `bak_stromen.sh` is vanaf nu de herkomst**.
2. **⚠️ `vervang_spoorbeen.py` mag hier niet meer gebruikt worden.** Hij matcht op modaliteit, en
   na B1 heeft deze stroom **één** `spoor`-been maar wél meerdere `leiding`-benen; bij de
   eerstvolgende uitbreiding is die val makkelijk gezet. Zet dat als comment in het script.
3. **⚠️ Zet in de kop dat het recept GERECONSTRUEERD is, niet teruggevonden.** De weerlegger heeft
   vier vrijheidsgraden gemeten die alle vier een byte-identiek bestand geven (`--graaf`
   mississippi of rijn · `--spoor-geojson` of `--been-geojson` · `--naar` op het anker of op het
   routeerpunt · één stap of twee). Het bewijs is *"dit commando produceert dat artefact"*, nooit
   *"dit was het commando van 29 juli"*. Zonder die zin leest een reconstructie straks als een
   gearchiveerd recept.
4. **⚠️ Reproduceerbaarheid is begrensd door `v2/.gitignore` regel 3 (`build-cache/`).** `$GRAAF`,
   `$MARNET`, `$NE` en beide geojsons zijn ongetrackt; op een verse clone draait dit recept niet.
   Geldt even hard voor `bak_grafiet` — noteer het één keer in de kop van het bestand.

### B5 — `aansluitingen.json` (via de generator)

Voeg in `v2/tools/maak_aansluitingen.py` toe, en wijzig `cu-beilun-kade`. `plek` is **[lon, lat]**.
Draai eerst **zonder** `--schrijf` en diff: de 25 bestaande aansluitingen moeten op **0,0 m** gelijk
blijven (de `cu-guixi-spoor`-drift van 741 m).

```python
dict(id="cu-beilun-laadspoor", grondstof="copper", fase="erts", rol="laadplek",
     naam="北仑港站 — laadsporen van het havenstation (Ningbo-Zhoushan)",
     plek=[121.87308, 29.92653], modi=["spoor"],
     bron="SATELLIET-GELEGD op Esri World Imagery (z19, 0,26 m/px, 2026-08-05): bundel van "
          "vijf parallelle sporen met VIER rode rail-mounted portaalkranen en wagons met "
          "containers eronder; coördinaat uit zh.wikipedia 北仑港站 (29°55′35,5″N "
          "121°52′23,1″E), 4,5 m van OSM way 1491021972 (ODbL)",
     noot="HET TWEEDE ANKER VAN DE OVERSLAG BEILUN (werkwijze §2b). cu-beilun-kade is de "
          "losberth in het water; dit is het laadspoor. Eén punt kon niet allebei zijn — dat "
          "stond sinds 2026-07-28 als openstaand punt in de brief (§5.1) en is hiermee dicht. "
          "Routeerpunt = het kopeinde van de bundel 29.92820/121.87380 (= landnet-knoop 326694, "
          "en tevens het beginpunt van het gebakken spoorbeen); max snap 0,198 km. "
          "⚠️ DATUMTOETS: as-is 4,5 m van het spoor; gelezen als GCJ-02 en omgerekend "
          "verschuift het punt 485 m NW naar 279,8 m van élk spoor, midden in de "
          "containerstapel. WGS-84 wint eenduidig — zelfde uitslag als Tianqi Jiangsu. "
          "⚠️ PRODUCTCONFLICT, OPEN: dit is een CONTAINERemplacement (78万TEU, beheerd door "
          "中铁联合国际集装箱宁波北仑) terwijl ladder L3 van de brief 'natte bulk in open "
          "wagons' zegt. Geografisch waterdicht, inhoudelijk voorwaardelijk — zie §5."),

dict(id="cu-guixi-walsdraad", grondstof="copper", fase="raffinaat", rol="losplek",
     naam="江西铜业铜材有限公司 — walsdraadfabriek Guixi (冶金大道 19号)",
     plek=[117.21919, 28.33180], modi=[],
     bron="SATELLIET-GELEGD op Esri World Imagery (z18, 0,53 m/px, 2026-08-05). Coördinaat uit "
          "het nationale emissievergunningregister permit.mee.gov.cn V3.0, vergunning "
          "913600007363561816001Q (行业类别 铜压延加工): verborgen velden longitude=117.21919 / "
          "latitude=28.33180 ÉN opelngd 117/13/9.08 + opelatd 28/19/54.48 — decimaal en DMS "
          "komen exact overeen",
     noot="Einde van fase D. Op z18 ligt het punt op de zuidberm van de brede oost-west "
          "interne hoofdas (闪速大道 = de 物流主轴线 uit het officiële terreinplan in "
          "赣环监字（2017）第S007号), op de mond van een noord-zuid inrit; ZW ervan een ommuurd "
          "blok met een meerbeukige sheddak-hal, ZO ervan een blok van vier lange donkere "
          "hallen. "
          "⚠️ MODI IS BEWUST LEEG. Een weg-aanhechting is hier zinloos: het landnet heeft "
          "wereldwijd maar 1.883 wegknopen en de dichtstbijzijnde ligt op 341,1 km "
          "(115.08000/25.92620) — gemeten, niet aangenomen. De interne complexweg zit niet in "
          "het landnet (wél in OSM, zie de bakprofielen). Zelfde rolverdeling als "
          "cu-escondida-laad. ⚠️ BIJVANGST: er ligt wél een landnet-SPOORknoop op 0,156 km "
          "(117.22050/28.33260) — dat is een MEETRESULTAAT, geen bewijs dat de kathode het "
          "spoor op gaat; de modaliteit van de interne overbrenging is niet gedocumenteerd. "
          "⚠️ ADRES: 冶金大道 19号 (productieadres, registerveld 生产经营场所地址), NIET 15号 — "
          "dat is het hoofdkantooradres van groep/beursvennootschap/加工事业部. "
          "⚠️ NEGATIEF ANKER op 1.749 m OZO: 江西铜业集团铜材有限公司 (28.32956/117.23688), een "
          "ANDERE rechtspersoon (USCC 913606817442997892, divisiecode 360681 tegen 360000) met "
          "een eigen werk en een eigen vergunning die 锡及其化合物/总锡 noemt. Verwar de twee "
          "niet: beide dragen 行业类别 铜压延加工 en beide noemen dezelfde 法定代表人 余琪."),
```

En bij `cu-beilun-kade`: **`modi=["zee", "spoor"]` → `modi=["zee"]`**, met in de `noot` één zin
erbij: *"⚠️ 2026-08-05: de spoorkant is een eigen aansluiting geworden (`cu-beilun-laadspoor`,
0,198 km snap) — precies de tweede aansluiting die deze noot in 2026-07-28 aankondigde."*

**Verwachte snaps na `--schrijf`:** `cu-beilun-laadspoor` spoor **0,198 km** · `cu-beilun-kade` zee
1,27 km (spoor verdwijnt) · `cu-guixi-walsdraad` geen enkele modus · de overige 25 ongewijzigd.
Totaal **27 aansluitingen**.

### B6 — `data/copper.js`: alleen de `note`, géén nieuwe node

**Bewust geen nieuwe node**, en dat is gemeten. `cu-ref-jiangxi` staat op `28.30 / 117.20`; de
walsdraadfabriek ligt daar **4,0 km** vandaan. Twee nodes van dezelfde grondstof binnen één
0,25°-cel geven in de v1-render een `degDist: 0`-boog (de M8-les, Baotou/Ganzhou). En het is
bovendien de vastgelegde **rolverdeling**: het register staat op wereldschaal, de aansluiting op
straatniveau (besluit 2026-07-30, `li-greenbushes` / `cu-guixi-spoor`).

Wél de `note` van `cu-ref-jiangxi` aanvullen, zodat het verband niet verdwijnt:

> "… Op hetzelfde terrein (冶金大道 19号) staat de eigen walsdraadfabriek 江西铜业铜材有限公司 —
> 370 kt/j Φ8 mm walsdraad + 120 kt/j getrokken draad uit 贵冶牌-kathode; 615 m van het
> registerpunt van de smelter. Straatniveau: aansluiting `cu-guixi-walsdraad`
> (28.33180/117.21919). ⚠️ Niet te verwarren met 江西铜业集团铜材有限公司, een andere
> rechtspersoon 1,75 km OZO."

⚠️ **Controleer de eenheid vóór je een getal overneemt** (de les van 2026-07-30): `copper.js` rekent
in `kt Cu/jaar (indicatief)`; de 370/120 kt uit [D1] zijn kt **product**, niet kt Cu-inhoud. Ze zijn
voor koper vrijwel gelijk (walsdraad is ≥99,9% Cu) maar schrijf dat op in plaats van het stil te
laten.

### B7 — cache-busting

`stroomroute-koper-escondida-guixi.json` is een browser-asset. In `v2/index.html` regel **7** en
**250**: `?v=106` → `?v=107`. In `v2/src/main.js` regel **257**: `laadStroomroute(VECTOR_R, "104", …)`
→ `"105"`. Dat herlaadt alle vijf stroombestanden (<300 KB elk) — acceptabel, en het is de enige
plek waar de dataversie leeft.

---

## C · Nieuwe benen — de bak-recepten

> ### ⚠️ HET BESLUIT DAT HIERONDER LIGT
>
> Been 5 krijgt als kop **niet** de kathode-expeditie (die is niet gevonden) maar het
> **satelliet-gelegde registerpunt van de smelter**. Daarmee is fase D geen *laadplek → losplek*
> maar een **verwerkingsknoop → aansluitpunt**-been, en dat moet expliciet in de brief én in de
> node-noot staan — precies zoals De Soto in de grafietketen **één** terreinanker kreeg in plaats
> van de twee die §2b eist, en de lijn daar 443 m vóór het terrein eindigt.
>
> **Voor:** beide uiteinden zijn officiële productiepunten uit hetzelfde register, beide zijn
> satelliet-gelegd, en de corridor ertussen heeft een **naam uit een officieel terreinplan**
> (闪速大道 = de 物流主轴线) én een gemeten OSM-geometrie. Zonder dit been levert een ronde met zes
> agents nul zichtbaar resultaat.
> **Tegen:** het kop-punt is een administratief registerpunt in het pyro-hart, niet de plek waar
> kathodebundels de deur uit gaan. Wie de lijn leest als "hier vertrekt de kathode" leest hem fout.
>
> **Als Lars "niet tekenen" kiest:** sla C1 en de laatste `--been-geojson`-regel van C2 over, houd
> §7 punt 5 van de brief zoals hij is, en voer alleen sectie B uit (de Beilun-reparatie staat
> volledig los van dit besluit). Zie **F7**.

### C0 · Waarom het geen stippel wordt — de meting die dat beslist

De opdracht vroeg te kiezen tussen (i) stippel, (ii) een echt wegbeen en (iii) een hand-geplaatste
geojson. **Het is (ii)**, en dat is niet beredeneerd maar gemeten in de lokale extract
`v2/build-cache/geofabrik/china-latest.osm.pbf` (eigen pyosmium-bbox-scan 2026-08-05, 55
highway-ways in het venster) én onafhankelijk in een live Overpass-set:

| OSM-way | klasse | access | lengte | punten | afstand tot smelter-registerpunt | tot walsdraad-registerpunt |
|---|---|---|---|---|---|---|
| **1462532976** | `highway=service` | **geen** | **2.250 m** | 5 | **43 m** | **8 m** |
| 995766131 | `highway=service` | `private` | 785 m | 4 | 2 m | 615 m |
| 1462532977 | `highway=service` | geen | 274 m | 3 | 792 m | 179 m |
| 313248139 / 552438139 | `highway=secondary`, naam **冶金大道** | geen | 3.177 m | — | 1.051 m | 1.663 m |

`way/1462532976` loopt van **117.23626, 28.33184** (de aansluiting op 冶金大道 aan de oostrand) tot
**117.21327, 28.33187** aan de westrand — kaarsrecht oost-west over het hele complex. Dat **is** de
interne hoofdas die het officiële terreinplan als 物流主轴线 tekent, en beide fase-D-registerpunten
liggen erop (8 resp. 43 m, punt-tot-segment).

* **(i) stippel valt af.** Stippel betekent in dit project precies één ding — *hier reikt het net
  niet* (werkwijze §7). Gemeten reikt het tot op **8 meter**. Een stippel zou hier liegen.
* **(iii) hand-geplaatste geojson valt af.** Die is er voor het geval dat OSM de geometrie **niet**
  heeft (de Tongling-oostgeul). Hier heeft OSM hem wél, en een handlijn zou een gemeten bron
  vervangen door een oog.
* **(ii) wegbeen kan, en is offline reproduceerbaar.** `service` staat al in
  `EIND_KLASSEN_DEFAULT`, de way draagt **geen** `access`-tag (dus hij overleeft `WEG_ACCESS_WEG`),
  en `EIND_STRAAL_KM = 12` dekt een been van 0,6 km volledig. De private dienstweg 995766131 valt
  er per constructie uit — precies goed, want die loopt het smelterhart in.

**Verwachte uitkomst, vooraf gemeten over de OSM-geometrie:** been **613 m** over de as, met
aanlopen van **43 m** (kop) en **8 m** (staart) = 664 m deur-tot-deur.

### C1 · profiel `koper-guixi-fase-d` (been 5)

Zet dit in de `PROFIELEN`-dict van `v2/tools/maak_stroombeen_weg.py` (regel ~96), nadrukkelijk niet
in een kopie. Coördinaten daar zijn **(lon, lat)**.

```python
    # ── Routebrief koper-escondida-guixi, fase D (2026-08-05) ─────────────
    # De interne overbrenging van kathode naar de eigen walsdraadfabriek, over
    # de as die het officiële terreinplan (赣环监字（2017）第S007号, fig. 3-1)
    # als 物流主轴线 tekent en die op de tegels 闪速大道 heet.
    # ⚠️ DE KOP IS EEN SUBSTITUUT. Het registerpunt van de smelter is NIET de
    #    kathode-expeditie; die is niet gevonden (brief §5.5). Zodra hij er is,
    #    schuift dit via-punt daarheen en verdwijnt het procesgat van 0,54 km.
    # ⚠️ eindKlassen BEWUST NIET GEZET: de default-tuple bevat `service` al, en
    #    het corridor-id hasht de eindklassen mee — de default ongewijzigd laten
    #    garandeert dat de drie bestaande profielen byte-identiek blijven.
    "koper-guixi-fase-d": {
        "via": [
            ("贵溪冶炼厂 — registerpunt (substituut-kop)", (117.22545, 28.33227)),
            ("江西铜业铜材有限公司 — registerpunt",        (117.21919, 28.33180)),
        ],
        "id": "cu-guixi-fase-d",
        "naam": "kathode 贵冶 → walsdraadfabriek 铜材公司 (闪速大道 / 物流主轴线)",
        "extracts": ["china"],
        "refs": [],
        "gepubliceerdKm": 0.62,
        "bronnoot": "eigen meting 2026-08-05 over OSM way 1462532976 (highway=service, "
                    "2.250 m, geen access-tag, 8 m resp. 43 m van de twee registerpunten); "
                    "geen bron publiceert deze afstand",
        "vensterKm": 3,
        "uit": "stroombeen-guixi-fase-d.geojson",
    },
```

```bash
python v2/tools/maak_stroombeen_weg.py --profiel koper-guixi-fase-d
```

**⚠️ Twee dingen om te lezen in de uitvoer.**
1. De scan draait over de **volledige china-extract (1,5 GB)**, single-worker en in-proces. Reken op
   enkele minuten; een eigen pyosmium-bbox-pass over hetzelfde bestand deed er onder de tien
   minuten over. De cache is gesleuteld op corridor-id + eindklassen + venster, dus dit is eenmalig.
   Loopt hij vast: dat is een **bevinding**, geen aanleiding om alsnog een stippel te tekenen —
   val dan terug op C1-alternatief hieronder.
2. `refs` is leeg. De ref-voorkeur is een zachte factor 3 en er is hier geen wegnummer; dat is
   goed, maar het betekent ook dat een verkeerde afslag niet door een ref wordt afgestraft. De
   verklikkers in sectie E doen dat werk.

**C1-alternatief als de extract-scan onwerkbaar blijkt** (en alléén dan): knip `way/1462532976` uit
de al gemaakte bbox-scan tussen de twee projecties en schrijf dat als
`stroombeen-guixi-fase-d.geojson`. De geometrie komt dan nog steeds **uit OSM** en niet uit een oog
— het verschil is alleen dat het recept een klein eigen script wordt in plaats van een profiel. Leg
dat script dan in `v2/tools/`, niet in een scratchpad (de `toets_corridor.py`-les).

### C2 · de hele stroom herbakken — het complete commando

Er bestaat geen "voeg één been toe". Dit hoort letterlijk in `v2/tools/bak_stromen.sh`, naast
`bak_grafiet()`, met `koper-escondida` in de `case`-regel — en de waarschuwing onderin dat bestand
(regels 76-80) mag dan voor **deze** stroom vervallen; voor `collahuasi-tongling`, `lobito-duisburg`
en `lithium` blijft hij staan.

```bash
# ── koper · Escondida → Puerto Coloso → Beilun → 贵溪 → walsdraadfabriek
# Routebrief: v2/design/routebrieven/koper-escondida-guixi.md (fasen A–D)
# ⚠️ GERECONSTRUEERD 2026-08-05, NIET TERUGGEVONDEN. Dit commando reproduceert
#    de uitvoer; het is niet aantoonbaar het commando van 29 juli. Vier
#    vrijheidsgraden geven een byte-identiek bestand (--graaf mississippi of
#    rijn · --spoor-geojson of --been-geojson · --naar op anker of routeerpunt ·
#    één stap of twee). Het bestand op schijf onderscheidt ze niet.
# ⚠️ ÉÉNSTAPS. Het spoorbeen komt rechtstreeks uit de OSM-1-op-1-route
#    (spoorroute-nieuw-beilun-guixi.geojson, commit 76fd530, straf 100).
#    vervang_spoorbeen.py NIET meer gebruiken: hij matcht op modaliteit.
# ⚠️ FASE E ONTBREEKT EN DAT IS EEN RESULTAAT: er is geen gedocumenteerde
#    afnemer van het walsdraadproduct (werkorder F4/F5).
# ⚠️ De invoerbestanden ($GRAAF/$MARNET/$NE/$BEEN) liggen in build-cache/ en
#    zijn ongetrackt — op een verse clone draait dit niet.
bak_koper_escondida() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel "leiding|slurryleiding Escondida → Coloso — tracé NIET in OSM (0 substance=slurry, geen doorlopende dienstweg)|-24.262,-69.06|-23.759,-70.467" \
    --stippel "leiding|terminalverwerking Coloso (filterfabriek → laadsteiger)|-23.759,-70.467|-23.7569,-70.4652" \
    --stippel "zee|haven-aanloop Coloso (schematisch — MARNET reikt hier niet)|-23.7569,-70.4652|-23.8,-71.3" \
    --been    "zee|zeeschip Coloso → Beilun|-23.8,-71.3|29.9364,121.883" \
    --stippel "zee|haven-aanloop Beilun (MARNET-knoop ligt in de geul, het schip lost aan de berth)|29.9478,121.8837|29.9364,121.883" \
    --stippel "leiding|transportband losberth → landpunt/ertsveld (eigen terrein, geen net)|29.9364,121.883|29.92742,121.87573" \
    --stippel "leiding|ertsveld → laadspoor 北仑港站 (eigen terrein, geen net)|29.92742,121.87573|29.92653,121.87308" \
    --been-geojson "spoor|trein Beilun → Guixi (甬金-vrachtlijn)|$BEEN/spoorroute-nieuw-beilun-guixi.geojson" \
    --been-geojson "truck|kathode 贵冶 → walsdraadfabriek 铜材公司 (闪速大道)|$BEEN/stroombeen-guixi-fase-d.geojson" \
    --marker "Escondida — concentrator/indikkers|-24.26200,-69.06000" \
    --marker "Puerto Coloso — laadsteiger|-23.75690,-70.46520" \
    --marker "Beilun — ertsterminal, losberth|29.93640,121.88300" \
    --marker "北仑港站 — laadspoor|29.92653,121.87308" \
    --marker "Jiangxi Copper Guixi — ertslosbundel|28.32710,117.22600" \
    --marker "江西铜业铜材有限公司 — walsdraadfabriek (kathode-expeditie open)|28.33180,117.21919" \
    --routebrief v2/design/routebrieven/koper-escondida-guixi.md \
    --uit    v2/data/stroomroute-koper-escondida-guixi.json \
    --stroom koper-escondida-guixi \
    --titel  "Koper · Escondida → Guixi (China)"
}
```

**Aandachtspunten die je niet mag verschuiven.**
* `--marnet` wijst naar `build-cache/marnet-preais`, **nooit** naar `v2/data/` (de bol mag het
  waternet niet laden).
* Zodra er één `--marker` staat vervangt die lijst de automatische afleiding volledig — alle **zes**
  moeten erin.
* De volgorde van `--been` / `--stippel` / `--been-geojson` **is** de reisvolgorde (één gedeelde
  lijst). ⚠️ Daarom `--been-geojson` voor het spoorbeen en **niet** `--spoor-geojson`: die vlag zet
  zijn been altijd achteraan en dan komt het fase-D-been vóór de trein te staan.
* `--vermijd` default `northwest` laten staan (reproduceert de zeeroute exact).

**Resultaat: 9 benen · ≈ 19.826,5 km · ≈ 3.230 punten · 6 markers.** Nieuw t.o.v. de huidige 5
benen / 19.823,1 km: +1,27 (aanloop Beilun) +1,22 (band) +0,27 (ertsveld) +0,66 (fase D) km.

---

## D · Wijzigingen in `koper-escondida-guixi.md`

| sectie | wat er moet gebeuren |
|---|---|
| **kop / statusregel** | "fase D–E concept (satellietpass open)" → **"fase D getekend als terreinanker-been (besluit Lars 2026-08-05); fase E blijft beargumenteerd stoppunt"**, met de datum |
| **nieuw blok onder de kop** | *De substituut-kop-notitie*: been 5 loopt van het **registerpunt van de smelter** naar het **registerpunt van de walsdraadfabriek**; de kathode-expeditie is niet gevonden en het gat van 0,54 km tussen been 8 en been 9 **ís** die ontbrekende laadplek. Doorgetrokken, niet gestippeld — het net reikt hier tot op 8 m |
| **§1 ketenkaart** | ASCII-schema bijwerken: 9 benen i.p.v. 6; de Beilun-overslag krijgt drie zichtbare stappen (aanloop → band → laadspoor); been 5 eindigt op de walsdraadfabriek; been 6 blijft **niet getekend** |
| **§2 tabel productvormen** | fase D-rij: "冶金大道 15" → **19**; jaarvolume-noot: 370 kt walsdraad + 120 kt draad zijn kt **product**, niet kt Cu-inhoud |
| **§2a ladder L3** | ⚠️ **conflict opnemen**: het satelliet-gelegde laadspoor is een **container**emplacement (78万TEU), terwijl stap 1 "natte bulk in open wagons" zegt. Beslis containers of bulk vóór fase C herschreven wordt (B3) |
| **§2a ladder L5** | stap 5/6 blijven **open**; erbij: wat er wél is (registerpunt smelter 28.33227/117.22545, satelliet-gelegd) en dat dát de substituut-kop is — geen laadplek |
| **§2a ladder L6** | stap 3: adres **19号** met de registerbron; stap 5/6: **28.33180, 117.21919**, satelliet-gelegd; uitsluiting erbij: **niet** 江西铜业集团铜材有限公司 (1.749 m OZO, andere USCC, tin-signatuur) |
| **§2b overslagregel** | Beilun heeft nu **twee** ankers: `cu-beilun-kade` (losberth, zee) en `cu-beilun-laadspoor` (北仑港站, spoor), met de terreinstap `cu-beilun-bandlandpunt` ertussen. De zin "als dat gaat knellen hoort er een tweede aansluiting te komen" wordt **doorgevoerd** |
| **been 2 (zee)** | routeerpunt/max snap ongewijzigd; erbij: de haven-aanloop van 1,27 km wordt nu **getekend** als stippel mét reden |
| **overslag b2→b3** | rij 3 (*"北仑港站 — laadspoor, coördinaat ontbreekt"*) krijgt zijn coördinaat: **29.92653, 121.87308**, status satelliet-gelegd (z19), routeerpunt 29.92820/121.87380, max snap 0,198 km. ⚠️ De formulering "het gat is exact de som van twee snaps" **niet** overnemen — de hoek is 138,8°, niet 180° (B1) |
| **been 3 (spoor)** | lengte **550,5 → 565,8 km** (+2,78%) mét de attributie: meetlat↔eindproduct +0,8 · bochtstraf/verdichten +5,3 · 10 m-simplify −1,3 · junctie-fix +4,2 · 1-op-1-vervanging +6,3. Tegen de brief-corridor (~556 km) is dat **+1,8%**, niet −1,0% |
| **been 1 (leiding)** | de getekende 153,5 km is de **koorde**; de gepubliceerde ~170 km is de werkelijke leiding (omwegfactor 1,108). Dat verschil staat nergens in de data of het label → één zin in §7 punt 1 |
| **been 5 (fase D)** | volledig herschrijven: modaliteit **weg, doorgetrokken** (niet stippel — het net reikt tot 8 m); lengte **0,61 km over OSM way 1462532976** + aanlopen 43/8 m; corridor bij naam **闪速大道 / 物流主轴线**; kop = substituut (registerpunt smelter), staart = `cu-guixi-walsdraad`; negatief anker 江西铜业集团铜材有限公司 **28.32956, 117.23688** straal 1,0 km |
| **verwerkingsknoop walsdraadfabriek** | anker-id `cu-guixi-walsdraad` invullen; erbij: geen weg-aanhechting (landnet-wegknoop op 341 km), wél een spoorknoop op 0,156 km — meetresultaat, geen bewering |
| **been 6 (fase E)** | stoppunt **blijft**, maar met de nieuwe onderbouwing: het gevonden CSRC-toezichtstuk documenteert een **kathode**-relatie (委托加工-keten JCC-kathode → een van drie 铜材-bedrijven → draad → Nanchang), niet een walsdraad-afzet, en de tegenpartij in de tabel is 江铜华东（浙江）铜材有限公司 in 诸暨/Zhejiang op 508,2 km — niet 上饶. Dat is een **vertakking bij de smelterknoop**, materiaal voor §4, geen fase-E-been |
| **§4 vertakkingen** | rij 3 (22万吨-lijn 上饶) blijft staan maar zónder de "dochter-van-de-walsdraadfabriek"-herclassificatie: die leunde op dezelfde entiteitsverwarring. Nieuwe rij: **江西铜业集团铜材有限公司, Guixi, 28.32956/117.23688** — reëel alternatief, aandeel onbekend |
| **§5 openstaande punten** | **sluiten:** 1 (北仑港站-laadspoor) · 6 (walsdraadfabriek-coördinaat). **Blijft open, scherper geformuleerd:** 5 (kathode-expeditie — nu mét de reden: Esri heeft bij Guixi geen z19) · 7 (modaliteit interne overbrenging) · 8 (expeditie walsdraad) · 9 (aandelen) · 10 vervalt gedeeltelijk. **Toevoegen:** productconflict container-vs-bulk bij Beilun · welk blok op het complex 铜材公司 is (twee tegenstrijdige kandidaten) · been-ids ontbreken in alle gebakken stromen · de 贵溪站/贵溪北站-vraag (F6) |
| **§6 afwerklijst** | rij 7 op **half doorgevoerd** (`cu-guixi-walsdraad` er wél, `cu-guixi-kathode-laad` niet — en waarom); rij 8 op **doorgevoerd voor de note, bewust niet als node** (rolverdeling + degenerate-arc); nieuwe rij: adres 15号 → 19号; nieuwe rij: `cu-beilun-kade` wordt zee-only |
| **§7 wat de kaart tekent** | 9 benen; punt 5 herschrijven (been 5 wordt wél getekend, als terreinanker-been, mét de reden); punt 6 ongewijzigd (fase E niet tekenen); nieuw punt: het procesgat van 0,54 km is bewust en benoemd |
| **§8 checklist** | de regel "elke overslag heeft twee ankers" mag voor Beilun **afgevinkt**; "elke laadplek satelliet-gelegd" blijft **onafgevinkt** zolang de kathode-expeditie ontbreekt |
| **§9 bronnen** | erbij: permit.mee.gov.cn V3.0 (`/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action` — het pad in `zoek-chinees-adres-recept.md` is **dood**) · vergunning-PDF's via `xkgg!downloadFile.action?fileType=fbfile` · 赣环监字（2017）第S007号 (jxcc.com, 67 p.) · zh.wikipedia 北仑港站 · OSM way 1462532976 / 1491021972 (ODbL) · Esri World Imagery z17–z19 |

**Ook bijwerken buiten de brief:** `v2/design/zoek-chinees-adres-recept.md` — het endpoint is
verhuisd naar `/perxxgkinfo/…`, het `副本` rendert leeg maar het **`正本` is downloadbaar als PDF**,
zoek op een **deelstring** van de bedrijfsnaam, en de USCC-controlecijfer-gewichten zijn
`Wi = 3^i mod 31`. En één correctie op de projectbanner: `CLAUDE.md` noemt voor deze stroom nog
"leiding 154 → zee 19.104 → trein 551 = 19.809 km"; op schijf staat 19.823,1 km met trein 565,8.

---

## E · Volgorde en controlepunten

**0 · Nulmeting (vóór je iets aanraakt).**
```bash
python v2/tools/toets_knikken.py > /tmp/knikken-voor.txt
sha256sum v2/data/stroomroute-*.json v2/data/aansluitingen.json \
          v2/build-cache/ais/graaf/stroombeen-*.geojson
python v2/tools/maak_aansluitingen.py     # zonder --schrijf: 25/25 op 0,0 m
```
Vastgelegde stand van **deze** stroom (nagemeten 2026-08-05, moet exact terugkomen):
`5 benen · 19.823,1 km · 3.223 punten · 4 markers`, benen
`leiding 153,5(s) · leiding 0,3(s) · zee 85,1(s) · zee 19.018,4 · spoor 565,8`, gaten
`0 · 0 · 0 · 2.379,1 m`, sha256 `5b5c1301…`. `toets_knikken` totaal: **157 knikken ≥60°, 25
omkeringen ≥150°, 3 terugloop** (alle drie in `stroomroute-pilot`); koper afzonderlijk **5/1/0**,
met de enige omkering op `28.34290, 117.19750` (169,9°, R=20 m, v=1,9 → *echte scherpe bocht*).

**1 · Profiel toevoegen (C1) — en meteen de regressietoets.**
```bash
python v2/tools/maak_stroombeen_weg.py --profiel grafiet-balama-nacala
python v2/tools/maak_stroombeen_weg.py --profiel lithium-greenbushes-bunbury
python v2/tools/maak_stroombeen_weg.py --profiel grafiet-vidalia-lastmile
sha256sum v2/build-cache/ais/graaf/stroombeen-*.geojson    # identiek aan stap 0
```
**Eis: byte-identiek.** Niet identiek = `EIND_KLASSEN_DEFAULT` is toch geraakt (het corridor-id
hasht hem mee) → terug.

**2 · Been 5 bakken (C1) en de uitvoer lezen.** Eisen:
* lengte **0,53–0,71 km** (gepubliceerd 0,62 ± 15%); verwacht 0,61;
* **2–5 punten** (de OSM-way heeft er 5 over 2.250 m — een been met tientallen punten betekent dat
  hij een andere weg pakt);
* `kmAanloopVan` ≤ **0,05** (verwacht 0,043) · `kmAanloopNaar` ≤ **0,02** (verwacht 0,008);
* `snoei_keerlussen` rapporteert **geen** keerpunt.

**3 · Verklikkers op `stroombeen-guixi-fase-d.geojson`, vóór het herbakken.**
* elk punt ligt tussen lat **28.3310 en 28.3325** (de as loopt op 28.3319; noordelijker = de
  private dienstweg of de spoorbundel, zuidelijker = het fabrieksblok);
* elk punt ligt tussen lon **117.2190 en 117.2256** (het been mag de as niet oostwaarts uitlopen);
* de lijn komt **nergens binnen 1,0 km** van `28.32956, 117.23688` (江西铜业集团铜材有限公司 — het
  negatieve anker; gemeten minimum bij een correcte lijn: 1,15 km);
* de lijn komt **nergens binnen 1,5 km** van `28.34611, 117.18917` (贵溪北站, bestaande verbodsstraal
  2 km uit de brief — ⚠️ **niet** verkleinen, zie F6).

**4 · Stroom herbakken (C2)** en het commando in `v2/tools/bak_stromen.sh` zetten. Script en
gebakken json in **één commit** — lopen ze uit elkaar, dan is het de `cu-guixi-spoor`-klasse.

**5 · Meten aan het gebakken eindproduct** (niet aan de meetlat — de fout van 28-07):
* **9 benen**, totaal **19.826 ± 2 km**, ± 3.230 punten, **6 markers**;
* lengte per been: 153,5 · 0,3 · 85,1 · 19.018,4 · **1,27** · **1,22** · **0,27** · 565,8 · **0,61**;
* **gaten:** `0 · 0 · 0 · 0 · 0 · 0 · 0,198 · 0,541 km`. Harde eis: **alle gaten ≤ 0,5 km, met
  precies één benoemde uitzondering** — het **procesgat b8→b9 van 0,54 km** bij de verwerkingsknoop
  贵冶. Dat gat is exact zo groot als het ontbrekende anker (de kathode-expeditie) en hoort in de
  brief **én** in de node-noot. Groeit of verschuift het: er is iets misgegaan. Verdwijnt het: het
  anker is gevonden. Een tweede uitzondering is een **fout**;
* **markers ≤ 0,15 km van de lijn — en meet punt-tot-SEGMENT, niet punt-tot-vertex.** ⚠️ Dit is een
  echte meetfout uit de vorige ronde: de markertabel van R6 mengt beide maten (Guixi staat er als
  16 m terwijl het segment 0,8 m is en de vertex 48,9 m). Verwacht: Escondida 0 · Coloso 0 · Beilun
  losberth 0 · Beilun laadspoor 0 · Guixi ertslosbundel 0,8 m · Guixi walsdraadfabriek ≤ 10 m;
* `python v2/tools/toets_knikken.py` en **diff tegen `/tmp/knikken-voor.txt`** — de vier andere
  stromen moeten **ongewijzigd** zijn (157/25/3 totaal, 3 terugloop alle in `stroomroute-pilot`);
  een nieuwe omkering in de koperstroom is een bevinding, geen ruis. ⚠️ De 150°-drempel is op
  **spoor** geijkt; de nieuwe benen zijn weg en eigen terrein — beoordeel een omkering daar met de
  maat pad ÷ hemelsbreed, niet met de drempel alleen.

**6 · `aansluitingen.json` regenereren** (`--schrijf`). Eisen: **27 aansluitingen**, de 25 bestaande
op **0,0 m** ongewijzigd, `cu-beilun-laadspoor` spoor **0,198 km**, `cu-beilun-kade` alleen nog zee
**1,27 km**, `cu-guixi-walsdraad` zonder modus. ⚠️ Geef `cu-guixi-walsdraad` **geen**
`modi=["weg"]`: gemeten snap **341,1 km** (het landnet heeft wereldwijd 1.883 wegknopen).

**7 · `data/copper.js`** (B6, alleen de `note`) en een schone laadcheck: geen console-fouten.

**8 · `?v=`-bump** (B7) en de brief bijwerken (D). Pas dán pushen; stuur de klikbare Pages-URL mét
het nieuwe `?v=107` mee (telefoon + 10 min cache).

**9 · Wrapup** volgens de Definition of Done — Linear, vault, project-`memory/`. Zet in
`memory/next-actions.md`: (a) de bak-recepten van `collahuasi-tongling`, `lobito-duisburg` en
`lithium` staan nog steeds nergens; (b) **been-ids ontbreken in álle vijf gebakken stromen** terwijl
werkwijze §2 ze eist en `hecht_marnet route` er geen vlag voor heeft; (c) het patroon "been eindigt
op zijn routeerpunt en niet op zijn anker" is niet Beilun-specifiek — gemeten gaten
`collahuasi-tongling 1.818 m` en `lithium-greenbushes-zhangjiagang 4.933 m` wachten op dezelfde
behandeling.

---

## F · Wat NIET af komt

### Bevindingen die de weerlegger NIET houdbaar vond (verplicht hier, niet weggelaten)

**F1 · R2 "kathode-expeditie" — niet houdbaar op de functie-lens.** De bevinding meldde de
expeditie zélf eerlijk als niet-gevonden (Esri geeft bij Guixi geen z19 — z19 en z20 leveren exact
2.521 byte placeholder, door de weerlegger per tegel nagemeten), maar leverde vervolgens wél drie
punten mét een functie in hun naam (`cu-guixi-elektrolyse-s1/s2`, `cu-guixi-walsdraad-terrein`) en
stelde s1/s2 voor als kop van been 5. **Die functie is nergens gesourcet**, en erger: dezelfde bron
wijst juist die plek aan als iets anders — 赣环监字（2017）第S007号 p.11 zet 一车间 (de
**anodeslijk-/edelmetaalwerkplaats**, 回转窑/湿法/金银电解/碳铜废水, producten 粗金粉 · 海绵铂 ·
海绵钯) *"in het noordoosten van het terrein"*, precies waar `cu-guixi-elektrolyse-s1` valt. De
redenering "anodeslijkverwerking staat altijd naast de tankhouse, dus dit ís de tankhouse" draait
het bewijs om: de bron plaatst de **buurman**, en zegt zelf dat het slijk vanuit het 电解车间 naar
一车间 wordt gebracht — wat afstand impliceert. **Geen van R2's punten wordt anker.** Wat er wél uit
overeind blijft (door de weerlegger onafhankelijk nagemeten) en waard is te bewaren als *bron*, niet
als anker: de tekst op p.11 dat het 198,26 ha-terrein intern is verdeeld in 老厂区 · 新厂区 ·
新产业公司 · **铜材公司** · 新材料车间 · 铜达公司 — dát maakt de collocatie hard, en die staat al in
sectie A onder `cu-guixi-walsdraad`.
*Wat het zou oplossen:* een Chinese aanbestedings- of EIA-tekst die 电解车间 of 成品库 aan een
gebouw koppelt, of een **niet-Esri**-beeldbron voor Guixi.

**F2 · R3 "fase-E-bestemming" — niet houdbaar op de bronkracht-lens.** De keten hing op twee
ongeverifieerde gelijkstellingen. (a) *"江铜华东铜材" = de 上饶-fabriek* is **fout**: de prospectus
definieert die naam letterlijk als **江铜华东（浙江）铜材有限公司**, pand
浙江省诸暨市陶朱街道迎宾路2号厂房, **508,2 km** van de uitgever — de deelstring "华东铜材" matcht in
het register alleen de 上饶-vennootschap omdat in de Zhejiang-naam （浙江）tússen 华东 en 铜材 staat.
Daarmee vervalt de hele herclassificatie van kandidaat (b) én de verklaring van de nulwaarde in
2023H1. (b) De **178 km** hoort bij de **smelter** («距离江铜贵溪冶炼厂仅约178公里 … 最近的**阴极铜**
生产商») en heeft bovendien geen onderscheidend vermogen: smelter→Nanchang 131,40 km tegen
walsdraadfabriek→Nanchang 130,60 km. (c) De volumes veroordelen het been: 江西铜业**铜材** — R3's
eigen anker — levert de uitgever alleen 加工服务 van **1,94 / 9,26 / 9,19 / 7,97 万元** per jaar
(0,00–0,01% van de inkoop), terwijl 江西铜业**集团**铜材 ~50× meer doet. **Fase E wordt niet
getekend.** Wat er wél uit meegaat: het adres 19号 (bevestigd door R1) en de vaststelling dat er een
gedocumenteerde **kathode**-vertakking bestaat (een 委托加工-keten) — materiaal voor §4 van de brief,
geen streng-vervolg.
*Wat het zou oplossen:* een recente 关联交易-tabel van 江铜铜箔 of JCC waarin een walsdraad- of
draadstroom **mét productieplaats** staat.

**F3 · R4 "guixi-stations" — niet houdbaar op de geometrie-lens.** De kernboodschap (het
smelterterrein heeft **één** spooraansluiting en die ligt bij 贵溪北, niet bij 贵溪站) is door de
weerlegger onafhankelijk nagemeten en houdt stand — de doorgaande 皖赣 komt buiten de vork nergens
dichter dan 737 m bij een terreinspoor, en de junctie→贵溪北-lengte van **9,024 km** klopt op 0,3%
met de 9 km buurstationsafstand van zh.wikipedia. **Maar het pakket is niet overneembaar:** de
claim dat de 专用铁路 dubbelsporig is (ways 305238912 + 305237836) is meetbaar onjuist (minimale
onderlinge afstand 14,9 m, aan de NW-kant 2.419 m uit elkaar, verschillende eindpunten — het zijn
twee losse enkelsporige aansluitingen, wat de bevinding in haar eigen `watIkZag` ook zegt); het
贵溪站-punt ligt **niet** op de noordrand van de perrongroep maar 36–41 m aan de **zuid**kant tegen
het stationsgebouw; het punt `cu-guixi-zuurladen` berust op een **mislezing** (de "ketelwagens" zijn
onderling scheef staande objecten op kaal terrein met bandensporen ertussen, 65,7 m van het
dichtstbijzijnde spoor); en het voorstel om been 4 te splitsen legt **1,97 km spoor neer dat er niet
is** (b4+b4b = 14,3 km tegen een gemeten kortste pad van 12,374 km). **Geen enkel R4-punt wordt
anker, en de verbodsstraal rond 贵溪北站 blijft op 2 km** — het voorstel om hem naar 1,5 km te
brengen komt uit dezelfde niet-houdbare bevinding.
*Wat het zou oplossen:* dit is fase-C-materiaal en verdient een **eigen ronde** vóór fase C als
afgesloten geldt. Twee losse punten daaruit zijn goedkoop te hertoetsen en de weerlegger bevestigde
ze zelf: (a) de ertslosbundel ligt aan de **zuid**zijde van het complex, niet de noord (§2a L4 stap
5); (b) de rolverdeling "erts binnen via 贵溪站, product uit via 贵溪北" klopt niet — alles gaat over
贵溪北.

### Niet gevonden — geen coördinaat, geen anker, geen lijn

**F4 · De kathode-laadplek / expeditie op het 贵冶-terrein** (§5.5 van de brief). Geprobeerd:
`permit.mee.gov.cn` (geeft één coördinaat per vergunning, geen installatielijst — het `副本` blijft
op `loading..` staan); Chinese zoekopdrachten op 电解车间 / 成品库 / 阴极铜出库 / 装车 / 提货大门 /
厂区平面布置 / 鸟瞰 / 招标 via smm.cn, cnmn.com.cn, jxcc.com, jxgqcg.com, people.cn (veel over de
geautomatiseerde elektrolyselijn, niets met een plek); Esri z19 (bestaat niet bij Guixi); Esri
Wayback-release 64001 (identiek aan live — de opnamedatum-faalmodus is hiermee **uitgesloten**, het
is een zoomplafond). *Wat het zou oplossen:* een niet-Esri-beeldbron op Guixi, óf het
环评/竣工验收-dossier van het 智能化电解车间 (nieuwsbericht news.cn 2026-01-23) met een
厂区平面布置图 mét 四至.

**F5 · De expeditiedeur / het laadperron van de walsdraadfabriek** (§5.8, begin van fase E). Zelfde
oorzaak: 0,53 m/px is de fijnste korrel en een laaddeur ligt daaronder. Er is een **kandidaat** —
het verharde voorterrein langs de noordgevel op ~`28.33169, 117.21834`, met een rij van 8–10
voertuiggrote rechthoeken — maar op deze korrel is niet te zien of het vrachtwagens met coils zijn,
en er is geen laadperron, geen laaddeur en geen coilstapel zichtbaar. **Status onzeker, dus geen
anker, dus niet in sectie A.**

**F6 · Het terreincentrum van 铜材公司 — twee tegenstrijdige kandidaten, dus geen van beide.** R1
mat het blok op `28.33135, 117.21828` (sheddak-hal, ~158 × 90 m); R2 mat het op `28.33135, 117.22020`
(vier lange evenwijdige hallen); de weerlegger van R1 rekende het officiële functieblok uit fig. 3-1
na op ~415 × 210 m met een zwaartepunt rond `28.33125, 117.21996` en concludeerde dat R1's blok
**te klein en te westelijk** is (1,4 ha kan geen twee SCR-lijnen + vier Niehoff-trekbanken dragen).
Mijn eigen z18-pass laat zien waarom de twee elkaar niet vinden: **er liggen twee aangrenzende
blokken** — westelijk een ommuurd blok met een meerbeukige sheddak-hal, oostelijk een blok van vier
lange donkere hallen met een smal hoog dienstgebouw aan de kop — en het registerpunt ligt er
tussenin, op de mond van de inrit. Geen enkel object op het beeld draagt een label. **Daarom wordt
géén blok terreinanker**; het registerpunt is het anker en dat is genoeg voor een been dat op de as
aanhecht. *Wat het zou oplossen:* een EIA, vergunningbijlage of 竣工验收 van 铜材公司 zélf met 四至
of oppervlak.

**F7 · Been 5 zelf, als Lars "niet tekenen" kiest.** Dan blijft §7 punt 5 van de brief staan zoals
hij is, vervallen C1 en de laatste `--been-geojson`-regel van C2, en levert deze ronde uitsluitend
sectie B (de Beilun-reparatie, die volledig los staat) plus de brief- en receptcorrecties. De
ankers uit sectie A blijven in dat geval gewoon geldig en gaan de brief in — ze zijn gemeten, of ze
nu getekend worden of niet.

### Blijft onzeker — gaat als openstaand punt de brief in

**F8 · Het productconflict bij Beilun** (container-emplacement vs. "natte bulk in open wagons").
Twee bandgalerijen uit het bulkveld eindigen op `29.91820, 121.87075` en
`29.91765, 121.87050`, pal aan de oostelijke sporen van de bundel; dat is de enige bulk-kandidaat en
hij blijft **aannemelijk** (geen wagons onder de galerij, geen laadsilo, geen perron zichtbaar). Eén
Wayback-opname mét gondola's eronder maakt er een anker van.

**F9 · De modaliteit van de interne overbrenging** (§5.7). Nergens beschreven. Het been wordt als
`truck` getekend omdat de brief dat als werkaanname noemt en de corridor een weg is — niet omdat er
een bron is. ⚠️ Bijvangst die het níet beslecht: er ligt een landnet-**spoor**knoop op 0,156 km van
de walsdraadfabriek; dat is een meetresultaat, geen bewijs.

**F10 · Been-ids ontbreken in álle vijf gebakken stromen.** Werkwijze §2 eist dat stroomroute-JSON's
en markertabellen naar dezelfde `<stroom-id>-b<n>`-ids verwijzen zodat brief ↔ bol 1:1 koppelbaar is
zonder mensenwerk. Geen enkel gebakken been draagt er een (de sleutels zijn overal
`['modaliteit','naam','stippel','km','punten']`), en `hecht_marnet route` heeft er geen vlag voor.
Ook: **brief-been b4** (last mile 贵溪站 → ertslosbundel) bestaat niet als eigen been in de data,
terwijl §3.4 de last mile juist als eigen been eist. Beide zijn gereedschapswerk en vallen buiten
deze werkorder.

**F11 · Het procesgat van 0,54 km blijft zichtbaar op de bol** tot de kathode-expeditie gevonden is.
Dat is bewust: het gat **ís** het ontbrekende anker. Wie het later dichttrekt met een rechte lijn
haalt precies de klasse fout binnen die dit project bij Waalhaven, Nacala en New Orleans al drie keer
heeft betaald.

**Statuswaarschuwing bij de oplevering:** in de brief mag de walsdraadfabriek **niet** als
"satelliet-gelegde losplek met bekende laaddeur" komen te staan, en de kathode-expeditie mag
**nergens** een coördinaat krijgen. Het is: *"registerpunt satelliet-gelegd, expeditie open"*. Een
anker dat niet satelliet-gelegd is, is geen anker — ook niet onder druk.
