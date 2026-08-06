---
type: recept
datum: 2026-08-04
bijgewerkt: 2026-08-05
status: bewezen op vier adressen (Tianqi Jiangsu · LG-Huayou Wuxi · 江西铜业铜材 Guixi · 贵溪冶炼厂)
---

> [!important] BIJGEWERKT 2026-08-05 — VIER CORRECTIES OP HET MEE-RECEPT
>
> Het recept is opnieuw gebruikt, nu voor de koperketen Guixi (fase D), en leverde twee nieuwe
> ankers op: **江西铜业铜材有限公司 28.33180 / 117.21919** (vergunning 913600007363561816001Q)
> en **贵溪冶炼厂 28.33227 / 117.22545** (vergunning 91360000X12430120H001P). Vier dingen die in
> de vorige versie fout of onvolledig stonden:
>
> 1. **⚠️ HET ENDPOINT IS VERHUISD.** Het pad `xkgg!licenseInformation.action` hieronder is
>    **dood**. Het werkt nu onder `/perxxgkinfo/`:
>    `permit.mee.gov.cn/permitExt/**perxxgkinfo**/syssb/xkgg/xkgg!licenseInformation.action`
>    (register V3.0). Controleer dit pad als eerste als een zoekopdracht niets teruggeeft —
>    een verhuisd endpoint geeft geen foutmelding maar een leeg resultaat, en dat leest als
>    "bedrijf niet gevonden".
>
>    **⚠️ BIJGEWERKT 2026-08-06 — HIJ IS ALWEER VERHUISD, EN NU FAALT HIJ LUID.**
>    `perxxgkinfo` is **een top-level context geworden**, niet langer een segment binnen
>    `permitExt`. Het pad hierboven geeft nu een harde **404**; het werkende pad is
>    **`permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action`**.
>    Dat het ditmaal 404't in plaats van leeg terug te geven is een meevaller, geen regel —
>    de oude variant zónder `perxxgkinfo` geeft nog steeds een **302 naar
>    `/perxxgkinfo/errorinfo.jsp`**, en dat redirect-doel is meteen de goedkoopste manier om
>    de nieuwe contextnaam terug te vinden als hij weer verschuift.
>
>    **En de zoekopdracht heeft twee dingen nodig die hieronder ontbreken:** een
>    **`JSESSIONID`-cookie** (haal de pagina eerst met GET op) én het verborgen veld
>    **`tempReportKey`** uit diezelfde pagina. Zonder die twee geeft de POST een 302 naar
>    `/perxxgkinfo/error.jsp` — opnieuw een lege uitslag die als "niets gevonden" leest.
>    Volledige veldenset: `tempReportKey`, `page.pageNo`, `page.orderBy`, `page.order`,
>    `registerentername`, `xkznum`, `publishtime`. De detailpagina zit achter
>    **`/perxxgkinfo/xkgkAction!xkgk.action?xkgk=getxxgkContent&dataid=<id>`**, met de
>    `dataid` uit de `查看`-kolom van de resultatenrij.
> 2. **Zoek op een DEELSTRING van de bedrijfsnaam, niet op de volledige naam.** Chinese
>    vennootschapsnamen dragen invoegingen die je niet vooraf kent
>    (江铜华东**（浙江）**铜材有限公司), en een exacte match mist die dan. ⚠️ Een deelstring
>    geeft ook **valse treffers van naburige rechtspersonen** — bij Guixi leverde 铜材 zowel
>    江西铜业铜材有限公司 als 江西铜业**集团**铜材有限公司 op, twee ándere bedrijven met
>    dezelfde 行业类别 én dezelfde 法定代表人. **Controleer altijd de USCC, niet de naam.**
> 3. **Het `副本` rendert leeg** (blijft op `loading..` staan) — dat is geen fout van jou. Het
>    **`正本` is wél downloadbaar als PDF** via
>    `xkgg!downloadFile.action?fileType=fbfile`, en die PDF bevat o.a. het `注册地址`. Bij
>    Guixi was dát het stuk dat de adrescorrectie 冶金大道 15号 → **19号** hard maakte.
> 4. **De USCC-controlecijfer-check is te scripten** en scheidt twee bijna gelijke
>    rechtspersonen zonder mensenogen. Het 18e teken is een controlecijfer over de eerste 17,
>    met gewichten **`Wi = 3^i mod 31`** (i = 0…16) en het tekenalfabet
>    `0-9ABCDEFGHJKLMNPQRTUWXY` (zonder I, O, S, V, Z):
>    `C = 31 − (Σ Wi·Vi mod 31)`, en `31` wordt `0`. Een USCC die faalt is verkeerd
>    overgetypt; twee USCC's die slagen maar verschillen zijn **twee bedrijven**. Bijvangst
>    die bij Guixi de doorslag gaf: de **divisiecode** in tekens 3–8 verschilt (360000 =
>    provinciaal geregistreerd, 360681 = 贵溪市) — dat is een goedkoper onderscheid dan welke
>    naamvergelijking ook.
>
> **Nog steeds waar, en opnieuw bevestigd:** het register geeft de coördinaat **decimaal én in
> DMS** (`longitude`/`latitude` naast `opelngd/f/m` + `opelatd/f/m`), en die twee kwamen bij
> beide Guixi-vergunningen exact overeen. En de datumregel hield opnieuw stand: as-is gelezen
> valt het punt op het terrein, GCJ-02→WGS omgerekend 485 m NW ernaast.
>
> ⚠️ **Wat dit recept NIET oplost, en dat is een grens die je vooraf moet kennen:** het register
> geeft **één punt per vergunning** en dat is de vestiging, geen installatielijst. Bij Guixi is
> de kathode-**expeditie** daardoor onvindbaar gebleven, en bij Esri bestaat daar geen z19
> (z19/z20 leveren 2.521 byte placeholder; Wayback-release 64001 is identiek aan live — een
> **zoomplafond**, geen opnamedatum-probleem). Een registerpunt is een *vestiging*, geen *deur*.

# Recept — een Chinees fabrieksadres naar een WGS-84-coordinaat

*Aanleiding: twee fabrieksankers (Tianqi Jiangsu, LG-Huayou Wuxi) blokkeerden de lithiumketen.
Een eerdere zoekronde in het Engels + OSM-naamzoeken vond ze niet, waarna de taak ten onrechte
bij Lars werd neergelegd. Deze ronde vond ze allebei. Dit bestand legt vast HOE, zodat het
volgende Chinese adres geen zoektocht meer is.*

# Verslag — twee Chinese fabriekscoördinaten

## 1. Per fabriek

### Fabriek A — Tianqi Lithium (Jiangsu), 东新路5号, Zhangjiagang → **GEVONDEN**

**Anker (poort): 32.01218 N / 120.45771 E — WGS-84, geen omrekening toegepast.**

Bron: nationaal emissievergunningregister van het Chinese Ministerie van Ecologie en Milieu (permit.mee.gov.cn, vergunning 91320592551155199K001U van 天齐锂业（江苏）有限公司). De coördinaat staat niet in de gedrukte vergunning maar in verborgen HTML-velden van de detailpagina, zowel decimaal als in graden/minuten/seconden — die twee komen exact overeen.

Waarom we het geloven (vier onafhankelijke lijnen):
- Het sociaal kredietnummer op de vergunning (91320592551155199K) matcht het calamiteitenplan dat Tianqi zelf publiceert; dat plan geeft adres 东新路5号 en terrein 96.533,4 m².
- Op Esri z18 valt het punt op het voorterrein/de poort van een chemisch complex aan de zuidzijde van 东新路 (OSM-way 432043510, ~24 m van de as) — precies waar het adres en de Baidu-sub-POI "北门" het voorschrijven.
- Op de Esri-Wayback-opname uit 2014 is de perceelrechthoek nog scherp: ~330 × 310 m ≈ 10,2 ha tegen 9,65 ha geregistreerd. En op diezelfde 2014-opname ligt ten noorden van de weg wél het lintdorp 北荫村 (350 m noord, uit het calamiteitenplan) dat op de huidige beelden gesloopt is. De enige toets die op live beeld faalde, faalde dus op de opnamedatum, niet op de plek.
- Datum expliciet getoetst, niet aangenomen: als je de waarde als GCJ-02 leest en omrekent (32.014053 / 120.453062), land je 485 m NW in kaal geploegd akkerland — geen gebouw, geen hek. De registerwaarde gedraagt zich dus als WGS-84/CGCS2000. Bijvangst: de Baidu-POI (wél GCJ-02) komt ná conversie op 7 m van de registerwaarde uit.

Kanttekeningen, eerlijk:
- Dit punt is de **poort**, niet het terreincentrum. Voor een register-/centroïdeknoop: ~32.0105 / 120.4565 (219 m ZZW, midden van de 2014-perceelrechthoek). Zet in de node-note waarom er twee punten zijn, anders wordt er later één "gecorrigeerd" weggehaald.
- Eén verificatiepass kwam tot "identiteit niet hard bewezen" (op basis van een OSM-node voor buurbedrijf 双狮 die 1,3 km verkeerd staat). Die pass had het 2014-beeld en de USCC-match nog niet; ik weeg één losse OSM-node niet op tegen de reeks samenhangende treffers, maar het is de resterende twijfel.
- **Entiteitscorrectie die de keten raakt:** de "+30 kt LiOH sinds 2025-09-25" hoort níet bij dit terrein maar bij een aparte rechtspersoon (天齐锂业新能源材料（苏州）) op een aparte kavel bij 港华路/渤海路, ~5 km ZO. Die tweede locatie is **NIET gevonden**: de registerwaarde 31.97744/120.49025 valt op bouwland; de GCJ-gecorrigeerde variant (31.97940/120.48574) valt binnen een complex in aanbouw, maar er is een even plausibel greenfield-bouwterrein 300-400 m ZO en geen bewijs welk van de twee het is. Hang het LiOH-volume dus niet aan het 东新路-anker.

### Fabriek B — LG Chem/Huayou-JV 乐友新能源材料（无锡）, 锡梅路167号, Wuxi → **GEVONDEN**

**Anker: 31.523573 N / 120.475895 E — WGS-84, geen omrekening toegepast.**
Poort (zuidzijde, poortgebouw): 31.520786 / 120.474921 (middelmatig vertrouwen).

Bron: officieel EIA-rapport van de gemeente Wuxi (bigdata.wuxi.gov.cn, juli 2026), veld 地理坐标 in DMS: 120°28'33.222" / 31°31'24.863".

Waarom we het geloven: het rapport noemt geen stelsel, maar het datum is met drie onafhankelijke methodes vastgesteld en drie keer hetzelfde uitgekomen. (1) De vier in het rapport beschreven grenzen (kanaal 伯渎港 noord, 锡梅路 zuid, 爱尔集/新鸿路 west, 通锡高速 oost) liggen alleen bij de WGS-84-lezing aan de juiste kant; bij GCJ-02 komt 新鸿路 aan de verkeerde kant te liggen. (2) De coördinaat rauw op Amap's native GCJ-02-raster geplot landt 470 m NW bij de buren; eerst WGS→GCJ omgerekend landt hij exact op het Amap-label 乐友新能源材料. (3) Op Esri (opname 2025-04-03, 0,34 m) valt hij binnen het omheinde terrein; de nagetrokken hekgrens meet 157.854 m² tegen 172.667 m² opgegeven (9%, binnen tekenfout) en het gebouwenpatroon komt 1-op-1 overeen met plattegrond 附图6 uit het rapport.

Voorbehoud: fabriek B is niet door dezelfde aparte verificatieronde gegaan als A — de satelliettoetsing zit ín de zoekronde zelf. Ik acht het bewijs sterk genoeg, maar het is niet dubbel-blind.

## 2. Wat er uitputtend geprobeerd is en wat níet werkte

Voor de nog ontbrekende locatie (Tianqi Suzhou / LiOH-kavel) en in het algemeen:

- **Dood**: Amap POI-API (Alibaba anti-bot), Baidu hoofdzoek-API (captcha — niet omzeild), Tencent (key vereist), tianyancha/qcc/qixin/aiqicha (WAF-captcha + geoblokkade voor niet-Chinese IP's), Global Energy Monitor (leverde een gemeente-centroïde mét vals "WGS 84"-label, 16 km mis — gevaarlijker dan een datumfout omdat geen omrekening hem repareert).
- **OpenStreetMap is voor beide fabrieken leeg.** Geen naam-tag, geen gebouwvlak, in Wuxi zelfs geen enkel object in het blok. De eerdere scan faalde dus niet — er zit een karteringsgat. Zoeken op naam in OSM is voor Chinese industriezones kansloos; OSM is alleen bruikbaar als WGS-84-referentiekader (wegen, kanalen) om een gevonden coördinaat tegen te toetsen.
- **Eerstvolgende zet voor de LiOH-kavel**: haal de exacte ligging van 港华路 en 渤海路 op en leg die twee straten op de stitch — de kruising wijst dan zelf de juiste kavel aan, zonder datum-gok. Daarnaast: een eigen **Tianditu-token** aanvragen (officiële Chinese dienst, CGCS2000 ≈ WGS-84, dus géén datumval) als tweede onafhankelijke bron.
- **Twee infrastructuurblokkades gevonden die breder pijn doen**: `pyosmium` is op deze machine geblokkeerd door applicatiebeleid ("DLL load failed ... geblokkeerd door een beleid voor toepassingsbeheer"), waardoor het hele offline-spoor over de lokale Geofabrik-extracts dicht zit — inclusief bestaande projecttools (`fetch_landnet.py`, `fetch_service_lastmile.py`, `toets_ankers.py`). En er is geen OCR lokaal (geen tesseract/paddleocr), waardoor gescande EIA's pagina-voor-pagina visueel gelezen moesten worden.

## 3. Schaalbaarheid — het antwoord op je eigenlijke vraag

**Dit is grotendeels machinaal te doen, mits je in het Chinees zoekt en de juiste bron als eerste aanslaat.** Het handwerk zit niet in het vinden van de coördinaat, maar in de identiteitscontrole eromheen.

**Zet als eerste in: het nationale emissievergunningregister (permit.mee.gov.cn).** Dat leverde het meest op en is het best automatiseerbaar. Recept: POST op **`/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action`** (⚠️ pad per 2026-08-05; het oude `xkgg!licenseInformation.action` zonder `perxxgkinfo` is dood en geeft geen fout maar een leeg resultaat) met veld `registerentername=<**deelstring** van de Chinese bedrijfsnaam>` → dataid → detailpagina → de verborgen HTML-velden `longitude`/`latitude` plus dezelfde waarde in DMS (`opelngd/f/m`, `opelatd/f/m`). De gedrukte vergunning zelf haal je op via `xkgg!downloadFile.action?fileType=fbfile` — dat levert het **`正本` als PDF** (mét `注册地址`); het **`副本` rendert leeg** en is geen bruikbare route. Voordelen: nationaal dekkend voor elke vergunningplichtige installatie, uniforme veldnamen, interne consistentiecheck (DMS vs decimaal) gratis, en de semantiek is te valideren door dezelfde extractie op bekende zustervestigingen te draaien (dat is hier gedaan met Shehong en Suining — beide raak). Kosten: seconden per bedrijf.

**Automatiseer de identiteitscontrole met het USCC-controlecijfer.** Zoeken op een deelstring levert onvermijdelijk buurbedrijven op (bij Guixi: 江西铜业铜材有限公司 náást 江西铜业**集团**铜材有限公司 — zelfde 行业类别, zelfde 法定代表人, ándere rechtspersoon). De sociaal-kredietcode scheidt ze zonder mensenogen: teken 18 is een controlecijfer over de eerste 17 met gewichten **`Wi = 3^i mod 31`** (i = 0…16) over het alfabet `0-9ABCDEFGHJKLMNPQRTUWXY` (zonder I, O, S, V, Z), `C = 31 − (Σ Wi·Vi mod 31)` met `31 → 0`. Faalt de check, dan is de code verkeerd overgenomen; slagen twee verschillende codes, dan zijn het twee bedrijven. Goedkoop extra signaal in dezelfde string: de **divisiecode** in tekens 3–8 (360000 = provinciaal geregistreerd, 360681 = 贵溪市).

**Tweede keus: lokale EIA/环评-PDF's op gemeentesites** (veld 地理坐标 in DMS). Minder uniform vindbaar, maar rijker: ze bevatten de 四至 (vier begrenzingen: wat ligt er noord/zuid/oost/west) en terreinoppervlak in 亩. Dat is precies de validatieset waarmee je een coördinaat *zonder mensenogen* kunt toetsen.

**De datumvraag is te scripten en is de kern van de automatisering.** Beide registerbronnen bleken WGS-84/CGCS2000 — dus blind omrekenen zou beide punten 430-485 m hebben verpest. De werkende regel: reken alle drie de hypotheses door (as-is, GCJ-02→WGS, BD-09→WGS), meet per hypothese de afstand tot de OSM-geometrie die in de brontekst als buur genoemd wordt, en kies de lezing waarbij álle genoemde buren aan de juiste kant liggen. Bij fabriek B onderscheidde dat de hypotheses hard (GCJ zette 新鸿路 aan de verkeerde kant); bij A idem (GCJ landde in een akker). Vuistregel om vast te leggen: **Chinese overheidsregisters en EIA's staan in CGCS2000 en hoeven níet omgerekend; alleen kaartdiensten (Amap/Baidu/Tencent) wel.** En let op dat de breedtegraad-offset in de Yangtze-delta negatief is — GCJ ligt daar zuidelijker dan WGS, anders dan vaak aangenomen.

**Wat handwerk blijft (en dus je echte kostenpost is):**
1. **Identiteit.** Bij Tianqi bleek het volume over twee rechtspersonen en twee kavels verdeeld te zijn; bij Guixi staan twee gelijknamige 铜材-vennootschappen 1,7 km uit elkaar op dezelfde boulevard, met dezelfde 法定代表人. De USCC-check hierboven doet het grove werk, maar wélk volume bij wélke rechtspersoon hoort kost lezen.
2. **Poort versus terreincentrum.** Registers geven één punt en zeggen niet welk. Voor een last-mile-lijn wil je de poort, voor een wereldknoop het centrum.
3. **⚠️ Vestiging versus deur — en dit is de harde grens van het recept.** Het register geeft **één punt per vergunning**, geen installatielijst. Een *laadplek* binnen een terrein (expeditiehal, productmagazijn, laadperron) komt er dus principieel niet uit. Bij Guixi bleef de kathode-expeditie daardoor onvindbaar, en de satelliet kon het niet overnemen omdat Esri daar **geen z19** heeft (2.521 byte placeholder; Wayback identiek aan live = zoomplafond, geen opnamedatum-probleem). Reken erop dat dit terugkomt: een registerpunt is genoeg voor een aansluiting op een openbare of interne as, niet voor een deur.
4. **De visuele eindcontrole.** Nodig, maar alleen als de geometrische toets géén eenduidige winnaar geeft — niet standaard.

**Verdict:** met de MEE-registerroute + geautomatiseerde datumtoets schat ik dat je voor een Chinees fabrieksadres in de meeste gevallen binnen minuten op straatniveau uitkomt, met een restcategorie (nieuwe entiteiten, gesplitste terreinen, greenfield in aanbouw) die handwerk blijft. Dat is **geen blokkade voor opschalen**, mits je twee dingen eerst regelt: een eigen Tianditu-token als tweede WGS-84-bron, en OCR lokaal (veel EIA's zijn gescand). En schrap OSM-naamzoeken uit de pipeline voor China — dat kost tijd en levert structureel niets.
