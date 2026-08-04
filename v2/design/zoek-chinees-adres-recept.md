---
type: recept
datum: 2026-08-04
status: bewezen op twee adressen
---

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

**Zet als eerste in: het nationale emissievergunningregister (permit.mee.gov.cn).** Dat leverde het meest op en is het best automatiseerbaar. Recept: POST op `xkgg!licenseInformation.action` met veld `registerentername=<Chinese bedrijfsnaam>` → dataid → detailpagina → de verborgen HTML-velden `longitude`/`latitude` plus dezelfde waarde in DMS (`opelngd/f/m`, `opelatd/f/m`). Voordelen: nationaal dekkend voor elke vergunningplichtige installatie, uniforme veldnamen, interne consistentiecheck (DMS vs decimaal) gratis, en de semantiek is te valideren door dezelfde extractie op bekende zustervestigingen te draaien (dat is hier gedaan met Shehong en Suining — beide raak). Kosten: seconden per bedrijf.

**Tweede keus: lokale EIA/环评-PDF's op gemeentesites** (veld 地理坐标 in DMS). Minder uniform vindbaar, maar rijker: ze bevatten de 四至 (vier begrenzingen: wat ligt er noord/zuid/oost/west) en terreinoppervlak in 亩. Dat is precies de validatieset waarmee je een coördinaat *zonder mensenogen* kunt toetsen.

**De datumvraag is te scripten en is de kern van de automatisering.** Beide registerbronnen bleken WGS-84/CGCS2000 — dus blind omrekenen zou beide punten 430-485 m hebben verpest. De werkende regel: reken alle drie de hypotheses door (as-is, GCJ-02→WGS, BD-09→WGS), meet per hypothese de afstand tot de OSM-geometrie die in de brontekst als buur genoemd wordt, en kies de lezing waarbij álle genoemde buren aan de juiste kant liggen. Bij fabriek B onderscheidde dat de hypotheses hard (GCJ zette 新鸿路 aan de verkeerde kant); bij A idem (GCJ landde in een akker). Vuistregel om vast te leggen: **Chinese overheidsregisters en EIA's staan in CGCS2000 en hoeven níet omgerekend; alleen kaartdiensten (Amap/Baidu/Tencent) wel.** En let op dat de breedtegraad-offset in de Yangtze-delta negatief is — GCJ ligt daar zuidelijker dan WGS, anders dan vaak aangenomen.

**Wat handwerk blijft (en dus je echte kostenpost is):**
1. **Identiteit.** Bij Tianqi bleek het volume over twee rechtspersonen en twee kavels verdeeld te zijn. Geen algoritme haalt dat eruit; dat kost lezen.
2. **Poort versus terreincentrum.** Registers geven één punt en zeggen niet welk. Voor een last-mile-lijn wil je de poort, voor een wereldknoop het centrum.
3. **De visuele eindcontrole.** Nodig, maar alleen als de geometrische toets géén eenduidige winnaar geeft — niet standaard.

**Verdict:** met de MEE-registerroute + geautomatiseerde datumtoets schat ik dat je voor een Chinees fabrieksadres in de meeste gevallen binnen minuten op straatniveau uitkomt, met een restcategorie (nieuwe entiteiten, gesplitste terreinen, greenfield in aanbouw) die handwerk blijft. Dat is **geen blokkade voor opschalen**, mits je twee dingen eerst regelt: een eigen Tianditu-token als tweede WGS-84-bron, en OCR lokaal (veel EIA's zijn gescand). En schrap OSM-naamzoeken uit de pipeline voor China — dat kost tijd en levert structureel niets.
