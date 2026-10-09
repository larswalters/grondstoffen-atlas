# Routebrief (licht) · goud — Kibali (Haut-Uélé) → Doko → Nairobi (NBO) → OR Tambo (JNB) → Rand Refinery (DR Congo → Zuid-Afrika)

**stroom-id:** `goud-kibali-randrefinery` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken (2026-10-09)
**Keten in één zin:** doré van de Kibali-mijn (Barrick/AngloGold/SOKIMO, Haut-Uélé) per truck over de mijnwegen naar de
Doko-airstrip, per privé-/vrachtvlucht (grootcirkel) naar de vrachtterminal van Nairobi JKIA, per vlucht (grootcirkel)
naar de vrachtterminal van OR Tambo (JNB), en per truck over de R21/N12 naar Rand Refinery in Germiston.
**Welke as van het verhaal:** Midden-Afrika (DRC) → Zuid-Afrika, de doré-as zonder weg- of spoorverbinding. Kibali
≈ **673 koz in 2025 = ≈ 20,9 t Au/j** (100%-basis; 2024 ≈ 687 koz = 21,4 t; koz ÷ 32,15) [4]; Barrick-guidance 2026
600–689 koz [4]. De enige gebronde zending: 539,3 kg (≈ 0,54 t = ± 2,6% van een jaar) in aug-2025 [1]. **Aannemelijk: één bron.**

## 1 · Ketenkaart
```
Kibali-verwerkingscomplex `au-kibali-plant`
  ──(b1 truck · mijnwegen Kibali (OSM unclassified, compacted) · hemelsbreed 3,1 km, geen wegkm)──►
Doko-airstrip, apron W van de baan `au-doko-airstrip` (ICAO FZJB)
  ──(b2 lucht · vlucht FZJB → NBO, grootcirkel, aannemelijk: één bron · 954 km grootcirkel)──►
Nairobi JKIA vrachtterminal/-apron `au-nbo-vracht`
  ──(b3 lucht · vlucht NBO → JNB, grootcirkel, aannemelijk: één bron · 2.911 km grootcirkel)──►
OR Tambo vrachtterminal `au-jnb-vracht` (hergebruikt uit goud-mponeng-londen)
  ──(b4 truck · R21/N12 · 25,7 km, omgekeerde kopie van goud-mponeng-londen b2, aannemelijk)──►
Rand Refinery, Germiston `au-randrefinery` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Kibali-plant → Doko-airstrip | OSM-mijnwegen (unclassified, compacted; rotondes, brug) [10] | hemelsbreed 3,1 km, geen wegkm; OSM-scan 4,5 km (indicatie, ±15% geen norm) | maak_stroombeen_weg (extract congo-drc, `--bron overpass`) | nee (plant-anker ligt 0,26 km van de weg: korte stub in de scan) |
| b2 | A | lucht | Doko FZJB → Nairobi JKIA (NBO) | vlucht FZJB → NBO (grootcirkel; **aannemelijk: één bron — krantenbericht 31-08-2025, vertrekveld niet genoemd**) | 954 grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b3 | B | lucht | Nairobi JKIA → OR Tambo (JNB) | vlucht NBO → JNB (30-08-2025; **aannemelijk: één bron**) | 2.911 grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b4 | C | truck | OR Tambo-vrachtterminal → Rand Refinery | R21/N12 (**aannemelijk: één bron voor de afnemer**) | 25,7 [11] (ontwerp 15 was schatting; hemelsbreed 11,2) | LETTERLIJKE KOPIE van goud-mponeng-londen b2, geojson omgekeerd | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-kibali-plant` | mijn / laadplek (verwerking) | Kibali-verwerkingscomplex (Barrick-operator) | 3.1135, 29.5939 | [2][osm-wiki] | bron-gelegd (z16 gezien: verwerkingscomplex met lange hallen, tanks en leidingwerk, zuidoost van de pits; het Wikipedia-punt 3.1127, 29.5847 ligt 1,0 km W op een haulroad tussen pits en plant, dus verschoven; sitelaag-punt w-kibali 3.0833, 29.5833 ligt 3,6 km ZW en is regiocoördinaat) |
| `au-doko-airstrip` | overslag truck→lucht | Doko-airstrip, gebouwen en apron W van de baan (FZJB) | 3.1414, 29.5903 | [3][osm] | bron-gelegd (z16 gezien: ± 1,9 km baan N-S met rode/lichte verharding, kleine hangars en apron aan de westzijde, via een mijnweg bereikbaar; OSM Watsa Doko 3.1370, 29.5898 = baanmidden 0,5 km ZZW, Wikipedia 3.1444, 29.5917 = 0,4 km NNO) |
| `au-nbo-vracht` | overslag lucht→lucht | Nairobi JKIA vrachtapron/-terminal (Swissport/KQ-cargo) | -1.3361, 36.9139 | [1][8][osm] | bron-gelegd op terreinniveau (z16 gezien: ZW van de passagierterminal een rij vrachtloodsen met een apron vol geparkeerde grote toestellen); welk pand Swissport is niet te onderscheiden: pand **onzeker** |
| `au-jnb-vracht` | overslag lucht→truck | OR Tambo vrachtterminal | -26.1440, 28.2295 | [11] | bron-gelegd (hergebruikt letterlijk uit goud-mponeng-londen.md) |
| `au-randrefinery` | raffinaderij / stoppunt | Rand Refinery, Germiston | -26.2189, 28.1550 | [7][11] | bron-gelegd (hergebruikt letterlijk uit goud-mponeng-londen.md; Wikipedia noemt dezelfde coördinaat) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | mijnweg-knoop ten NW van de plant (OSM way 1152662128) | 3.1192, 29.5910 | pint de westelijke omloop om het complex; de weg Z langs de TSF blijft zo buiten |
| b1 | 2 | rotonde-uitloop (way 580476768) | 3.1246, 29.5874 | zit op de doorgaande haulroad naar het zuiduiteinde van de baan |
| b1 | 3 | haulroad ten Z van de baan (way 1153084863) | 3.1287, 29.5867 | laat de route het zuiduiteinde van de baan nemen en dan de servicestrook N naar de apron |
| b4 | — | geen: de kopie draagt de via-punten van goud-mponeng-londen b2 | — | niet opnieuw routeren |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kibali-verwerkingscomplex | Kibali Goldmines (Barrick 45% / AngloGold 45% / SOKIMO 10%) | erts → doré | plant 7,2 Mt erts/j; ≈ 673 koz Au 2025 | [2][4] |
| Rand Refinery (Germiston) | Rand Refinery (Pty) Ltd | doré → LBMA-baren | niet gebronde capaciteit; neemt regionaal doré af | [7][11] |

## 6 · Stoppunt
Rand Refinery: de brief stopt waar de enige bron stopt (zending afgeleverd aan de raffinaderij). De verdere afzet
(Londen e.d.) is goud-mponeng-londen; fase D/E vervallen.

## 7 · Open punten
- **Dunne evidentie, één krantenbericht** [1]: 539,3 kg goud (+ 29 pakketten zilver) kwam 29-08-2025 op JKIA aan "uit DRC", werd in een warehouse gecontroleerd en naar het Swissport-cargocentrum gebracht, en vloog 30-08 naar Johannesburg. Het bericht noemt Kibali maar plaatst het in "Kinshasa" (Kibali ligt in Haut-Uélé), noemt het vertrekveld en het toestel (privéjet) niet en noemt Rand Refinery alleen in een onduidelijke importeurstring. **Dat Kibali structureel al zijn doré via NBO naar JNB vliegt is niet aangetoond; dit kan één incidentele route zijn.** Daarom "aannemelijk" in b2/b3/b4.
- Waarde-controle: US$ 45,5 mln voor 539,3 kg ≈ US$ 2.620/oz; dat lijkt laag voor een goudprijs in aug-2025 (niet bronnen-gecheckt) — het bericht kan getallen of lading (zilver) door elkaar halen.
- Dat Kibali met vliegtuigen doré afvoert is wel onafhankelijk gebrond: de Doko-luchthaven is uitgebreid om de goudmijn te bedienen [3] en een Mining Weekly-kop (2017) noemt "flying people in and gold bars out" [6] (alleen de kop gezien, artikel geblokkeerd). Welke bestemming (NBO of elders) en welke maatschappij: niet gebronde informatie.
- Rand Refinery als afnemer van DRC-doré: één zoekresultaat (mining.com, door de toets gelezen als kop, artikel niet geopend) [12]; Kibali niet met naam.
- Doko heeft geen IATA-code (ICAO FZJB); de beennaam gebruikt FZJB. Bandekking: Wikipedia zegt asfalt, OSM zegt gravel — geen invloed op de lijn.
- JKIA-vrachtterminal is airside: geen truckbeen aan de NBO-kant (b2 en b3 delen één anker); het toestel kan in werkelijkheid op een andere apron staan.
- Kenia heeft geen Geofabrik-extract: geen blokkade (alleen luchtbenen). Volumes lopen uiteen (Wikipedia 814 koz in 2019 [2], 2025 673 koz [4]): één bron voor 2025.
- Sitelaag-fout (melden, niet gewijzigd): `w-kibali` in goud-sitelaag.json staat op een regiocoördinaat 3,6 km ZW van het complex en op "onzeker": centraal gelijktrekken met `au-kibali-plant`.

## 8 · Bronnen
[1] Kahawa Tungu, 31-08-2025, "Heavy security as 539 kilos of gold is moved from DRC through JKIA to SA": https://kahawatungu.com/heavy-security-as-539-kilos-of-gold-is-moved-from-drc-through-jkia-to-sa/
[2] Wikipedia, "Kibali Gold Mine" (3°06′46″N 29°35′05″E; 814 koz 2019; eigenaren; plant 7,2 Mt/j): https://en.wikipedia.org/wiki/Kibali_Gold_Mine
[3] Wikipedia, "Doko Airport" (ICAO FZJB, 3°08′40″N 29°35′30″E, baan 1.900 m, uitgebreid voor Kibali/Kalimva): https://en.wikipedia.org/wiki/Doko_Airport
[4] Bankable, 10-02-2026, Kibali 2025 ≈ 673.000 oz (2024 ≈ 687.000), guidance 2026 600–689 koz: https://bankable.africa/en/business-climate/1002-2375-gold-prices-lift-kibali-mine-revenue-to-a-record-2-3-billion-in-2025
[5] Ecofin Agency, 11-11-2025, Kibali Q3 2025 191 koz, YTD 498 koz: https://www.ecofinagency.com/news-industry/1111-50329-barrick-s-kibali-mine-in-drc-posts-21-jump-in-q3-gold-output
[6] Mining Weekly, 06-03-2017, "Secret of the Kibali mine – flying people in and gold bars out" (alleen kop): https://www.miningweekly.com/article/secret-of-the-kibali-mine-flying-people-in-and-gold-bars-out-2017-03-06
[7] Wikipedia, "Rand Refinery" (26°13′08″S 28°09′18″E): https://en.wikipedia.org/wiki/Rand_Refinery
[8] Wikipedia, "Jomo Kenyatta International Airport" (364.822 t vracht 2024): https://en.wikipedia.org/wiki/Jomo_Kenyatta_International_Airport
[9] Mining Technology, "Kibali Gold Mine" (814 koz 2019, 807 koz 2018): https://www.mining-technology.com/projects/kibali-gold-mine/
[10] OpenStreetMap (ODbL) via Overpass (overpass.openstreetmap.fr), 2026-10-09: highway-ways rond de plant, o.a. 580945668, 1152662093/94/122/125/127–130, 1153084863/64/66, 580476768, 581556491; reserve-scan: `v2/build-cache/ais/graaf/goud-kibali-randrefinery-weg-plant-doko-scan.geojson`.
[11] `v2/design/routebrieven/goud-mponeng-londen.md` §3/§9 (au-jnb-vracht, au-randrefinery, b2 25,7 km): hergebruikt.
[12] mining.com, "Africa's top gold refiner restarts smelter" (alleen via zoekresultaat in de haalbaarheidstoets: Rand Refinery raffineert doré uit Ghana, DRC, Tanzania): https://www.mining.com
[osm] Photon/Nominatim via de toets: Watsa Doko-aerodrome 3.1369514, 29.5897675 (way 1153084862); JKIA-vrachtkandidaat -1.3361, 36.9139. [osm-wiki] Wikipedia-plantpunt 3.1127, 29.5847 (verschoven, zie §3).
Satellietblik: `v2/build-cache/satcheck/sat-goud-kibali-randrefinery-plant.png`, `-plant16.png`, `-doko.png`, `-dokoN16.png`, `-nbo.png`, `-nbo16.png` (Esri z15/z16, 2026-10-09).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh goud-kibali-randrefinery` → `v2/data/stroomroute-goud-kibali-randrefinery.json` (13,9 KB, versie 2, `lonlat`).
Functie `bak_goud_kibali_randrefinery()`, profiel `goud-kibali-randrefinery-plant-doko`. **3.895,5 km · 4 benen · 615 punten · 5 markers · geen stippel.**

| # | modaliteit | been | km gebakken | km brief | naad naar vorige |
|---|---|---|---|---|---|
| b1 | truck | Kibali-plant → Doko-apron (mijnwegen) | 4,8 | hemelsbreed 3,1, geen wegkm; eigen OSM-scan 4,5 (indicatie) | — |
| b2 | lucht | vlucht FZJB → NBO (grootcirkel, aannemelijk: één bron) | 954,2 | 954,2 (berekend) | 0,000 |
| b3 | lucht | vlucht NBO → JNB (grootcirkel, aannemelijk: één bron) | 2.910,8 | 2.910,8 (berekend) | 0,000 |
| b4 | truck | JNB-vrachtterminal → Rand Refinery (R21/N12, omgekeerde kopie) | 25,7 | 25,7 | 0,000 |

**Markers (volgorde = reisvolgorde, alle 0,0 m van de lijn):** au-kibali-plant 3.1135,29.5939 · au-doko-airstrip 3.1414,29.5903 · au-nbo-vracht -1.3361,36.9139 · au-jnb-vracht -26.1440,28.2295 · au-randrefinery -26.2189,28.1550.

**Toelichting per been**
- **b1 (weg).** Overpass-bron (`--bron overpass`; pyosmium is geblokkeerd). De twee ingebouwde spiegels (overpass-api.de, overpass.kumi.systems) gaven op 2026-10-09 leeg antwoord resp. een 500; `overpass.openstreetmap.fr` werkte met de User-Agent van het tool. Het gedeelde tool is niet aangepast: een wrapper buiten de repo (scratchpad) stuurt alleen de spiegel-URL om naar de fr-spiegel en roept daarna `maak_stroombeen_weg.main()` ongewijzigd aan. De reserve-scan is niet gebruikt. 1.266 ways door het wegfilter, 843 kleine-klasse-ways binnen 12 km mee, 8 keerlussen gesnoeid (alle < 0,05 km). Lijn = 0,26 km stub plant → weg + 4,48 km mijnwegen + 0,06 km weg → apron = **4,8 km getekend**. Lengtetoets: +46% tegen de hemelsbrede 3,1 km; dat is geen norm-overschrijding maar de hemelsbreed-factor (de brief zegt zelf "geen wegkm"), en het sluit aan op mijn eigen scan van 4,5-4,9 km. Geen airside-stippel nodig: de mijnweg eindigt 0,06 km van het apron-anker. `toets_knikken`: 6 knikken, 0 omkeringen; vijf daarvan zijn 1-80 m-spikes op rotondes en één 80° bocht van 111 m straal.
- **b2/b3 (lucht).** `maak_luchtbeen.py`, doorgetrokken, "grootcirkel" in de beennaam, "aannemelijk: één bron" in de beennaam (niet in de lijnstijl). 40 resp. 118 punten. Beide delen één airside-anker op JKIA (`au-nbo-vracht`): geen truckbeen of stippel op de NBO-kant. Geen tussenlanding aangenomen; het krantenbericht noemt het vertrekveld en het toestel niet.
- **b4 (weg).** Letterlijke kopie van `goud-mponeng-londen-weg-randrefinery-jnb.geojson` (381 punten, 25,717 km), alleen de coördinatenlijst omgekeerd (begin 28.2295,-26.144 = JNB, einde 28.155,-26.2189 = Rand Refinery), eigen id/naam, van/naar-velden gewisseld. Geen nieuwe routering. Km-toets niet van toepassing. De 2 omkeringen (168° en 162°, "scherpe bocht, echt") en de spikes bij de terminal zijn identiek aan het brontoets-profiel van goud-mponeng-londen b2.
- **Haven-aanloop, leiding, stippel:** n.v.t. (geen zeebeen, geen leiding, geen net-gat). Fase D/E vervallen (stoppunt Rand Refinery, §6).

**Lessen / open voor centraal**
- De twee ingebouwde Overpass-spiegels in `maak_stroombeen_weg.py::_ways_uit_overpass` zijn op 2026-10-09 onbruikbaar; `overpass.openstreetmap.fr` werkt (met het User-Agent van het tool; zonder UA "only available to white-listed usages"). Aanbeveling: de fr-spiegel toevoegen aan de lijst `spiegels` in dat tool.
- Sitelaag `w-kibali` (3.0833, 29.5833) ligt 3,6 km ZW van `au-kibali-plant` en moet centraal gelijkgetrokken worden; niet door deze bake aangepast.
- Een lengtetoets tegen een hemelsbreed getal (b1) leest als +46% maar is een indicatie; voor een echte wegkm ontbreekt de bron.
- De evidentie blijft één krantenbericht (§7); de lijn is dus doorgetrokken en gemeten, maar de keten "Kibali → NBO → JNB → Rand" is aannemelijk, niet bewezen.
