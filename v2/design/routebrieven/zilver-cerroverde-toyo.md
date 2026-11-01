# Zilver · Cerro Verde → Matarani → Toyo (Peru → Japan)

**stroom-id:** `zilver-cerroverde-toyo` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** zilver als bijproduct in het koperconcentraat van de Cerro Verde-concentrator (SMCV, Arequipa; Freeport, SMM 16,8 %, Sumitomo Corp 4,2 %): per **truck** over de mijnweg langs de Quebrada San José naar PeruRail-station **La Joya**, per **spoor** (Ferrocarril del Sur) naar Muelle F in Matarani, per **zeeschip** over de Stille Oceaan naar de Seto-binnenzee en via een haven-aanloop naar de eigen ertslosberth van de **Toyo-smelter van SMM** (Saijo/Niihama, Ehime). Daar stopt de brief. **Bestemming Toyo = aannemelijk: één bron** (afgeleid uit het SMM-aandeel, geen afnamebron).
**Welke as van het verhaal:** Peruaans koperconcentraat met zilver naar de smelter van een aandeelhouder in Japan; het nieuwe aan Peru's zilverketens is Japan. **Jaarvolume: niet gepubliceerd.** FCX meldt voor Cerro Verde geen zilverproductie per jaar [2]; wel reserves: levensduurplan **100,2 Moz Ag (ca. 3.116 t, 100%-basis, FCX TRS 2024)** [2], Wikipedia noemt 113,2 Moz [1]. Geen volume of Ag-cijfer aan Toyo toegewezen.

## 1 · Ketenkaart
```
Cerro Verde-concentrator `ag-cerroverde-conc` ──(b1 truck · mijnweg Quebrada San José · OSM-pad 47,0 km)──► La Joya `ag-lajoya-overslag`
──(b2 spoor · Ferrocarril del Sur · 59,2 km)──► spooreinde `ag-matarani-spooreinde` ──(b3 stippel 1,7)──► Muelle F `ag-matarani-kade`
──(b4 stippel haven-aanloop 72,1)──► zeeknoop 489 ──(b5 zee · MARNET · 17.190,4 km, aannemelijk: één bron)──► Niihama-zeeknoop 5746
──(b6 stippel haven-aanloop 23,3)──► Toyo-kade `ag-toyo-kade` ⏹ stoppunt (smelter)
```

## 2 · Benen (alle zes letterlijke kopieën van `koper-cerroverde-toyo`, zelfde bestanden)
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | concentrator → La Joya-station | mijnweg Quebrada San José (OSM way 286975126, secondary; private tertiary als eerste stuk) [3] | **hemelsbreed 36 km, geen wegkm**; privéweg "40 km" [3] (indicatie); gebakken 47,0 | geojson-kopie `koper-cerroverde-toyo-weg-cerroverde-lajoya.geojson` | nee |
| b2 | A | spoor | La Joya → spooreinde Matarani | Ferrocarril del Sur (PeruRail) [4] | ~60 (MINEM, via koper-brief) ; gebakken 59,2 | geojson-kopie `spoorroute-koper-cerroverde-toyo-lajoya-matarani.geojson` | nee |
| b3 | A | spoor | spooreinde → Muelle F | havenspoor/pier niet in het net | 1,7 hemelsbreed | stippel-kopie (-17.0049,-72.0964 → -17.0044,-72.1124) | **ja**: haventerrein, geen net |
| b4 | B | zee | Muelle F → MARNET-zeeknoop 489 (-17.3000,-72.7000) | haven-aanloop Matarani; kade 70,6 km van de knoop (> 5 km) | 72,1 | `aanloop-matarani.geojson` (kopie) | **ja**: MARNET reikt niet |
| b5 | B | zee | zeeknoop 489 → Niihama-zeeknoop 5746 (34.0720,133.0479); **aannemelijk: één bron** | Stille Oceaan, geen kanaal | MARNET 17.190,4 (hemelsbreed 16.865, +1,9 %) | MARNET (`--been zee`, kopie) | nee |
| b6 | B | zee | zeeknoop 5746 → Toyo-kade | haven-aanloop Toyo; kade 21,5 km van de knoop (> 5 km) | 23,3 | `koper-cerroverde-toyo-aanloop-toyo.geojson` (kopie) | **ja**: Seto-binnenzee buiten het net |
Totaal 17.393,7 km (stippel 97,1 km). Geen lucht-, leiding- of binnenvaartbeen; geen nieuwe geometrie.

## 3 · Ankers (alle hergebruikt uit `koper-cerroverde-toyo` §3; elk met een eigen satellietblik z15 op 2026-11-01)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-cerroverde-conc` | mijn / concentrator | Cerro Verde-concentrator (SMCV) | -16.5170, -71.5966 | [2][5] | bron-gelegd (z15 gezien: compact verwerkingscluster met ronde indikkers en gebouwen, ten noorden van de open pit, tailingbekken noordelijk) |
| `ag-lajoya-overslag` | overslag truck → spoor | PeruRail-station La Joya (transfer) | -16.7245, -71.8598 | [3][4] | aannemelijk (z15 gezien: station met langs de doorgaande lijn een emplacement en wissels in de woestijn naast de Panamericana; de concentraattransferbak zelf niet herkend) |
| `ag-matarani-spooreinde` | spooreinde | Matarani, spooreinde | -17.0049, -72.0964 | koper-lasbambas-matarani §3 | bestaand, hergebruikt |
| `ag-matarani-kade` | overslag spoor → zee | Tisur Muelle F, concentraatpier | -17.0044, -72.1124 | [5][6]; koper-lasbambas-matarani §3 | bron-gelegd (z15 gezien: kruis op de kopzijde van de pier met een afgemeerd schip, loodsen en haventerrein erachter) |
| `ag-niihama-zeeknoop` | zee-knoop | MARNET-zeeknoop 5746 | 34.0720, 133.0479 | nikkel-taganito-niihama b3/b4 | bestaand, hergebruikt (knoop, niet de lijn) |
| `ag-toyo-kade` | losplek / smelter | Toyo Smelter & Refinery (SMM), eigen berth | 33.9505, 133.2295 | [7][8] | aannemelijk (z15 gezien: smelterterrein direct aan de kustlijn, kade ervoor, containerterminal westelijk en een kolen/bulkterminal oostelijk; berth tot 30.000 t volgens [7]) |

## 4 · Via-punten
Geen nieuwe: alle benen zijn kopieën. De truckcorridor (b1) ligt vast in het koper-profiel `koper-cerroverde-toyo-cerroverde-lajoya` met drie via-punten op OSM way 286975126: -16.5681,-71.6494 · -16.5958,-71.7226 · -16.6591,-71.7874 (mijnweg, niet via Arequipa of La Joya-dorp). Regio-extracts voor een eventuele herbake: peru (japan-extract niet nodig). Geen herbake nodig.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cerro Verde-concentrator | SMCV (Freeport 55,1 %) | erts → Cu-concentraat met Ag | zilver niet gerapporteerd | [2][5] |
| Toyo Smelter & Refinery | SMM | concentraat → kathode, goud, zilver (granulaat) | zilvercapaciteit niet gepubliceerd | [7] |

## 6 · Stoppunt
Bij de Toyo-kade: de smelter is het einde van de gedocumenteerde keten; zilver verlaat Toyo als edelmetaalproduct (granulaat) zonder genoemde afnemer. Fase D/E vervallen.

## 7 · Open punten
- **Bestemming Toyo niet bevestigd:** alleen het SMM-aandeel in Cerro Verde (16,8 % [5], 21 % in oudere bronnen [1]) en Sumitomo Corp die concentraat aan smelters in en buiten Japan levert [9]. Geen bron koppelt Cerro Verde-lading aan Toyo; Wikipedia noemt geen afnemer. Daarom aannemelijk: één bron, in beennaam b5.
- **Zilver uit Cerro Verde niet gerapporteerd.** FCX noemt silver alleen als bijproduct in het concentraat, door de smelter teruggewonnen [2]; geen jaarcijfer, dus geen volume. Toyo's zilverproductie is niet bevestigd voor deze lading (de SMM-pagina noemt wel zilvergranulaat [7]).
- **Truckbeen = benadering van een privéweg** (gebakken 47,0 km tegen privéweg 40 km, hemelsbreed 36): geen gepubliceerde wegkm, de ±15 %-toets is een indicatie.
- **La Joya-transferbak niet herkend** op z15; exacte plek niet gepubliceerd.
- Volledige dubbeling van de koperstroom (bewust, zoals zilver-collahuasi-tongling); Peru heeft al zes zilverketens, nieuw is Japan.
- Zilver-sitelaag heeft geen Cerro Verde-site: centraal toevoegen (anker `ag-cerroverde-conc`).

## 8 · Bronnen
[1] Wikipedia, Cerro Verde mine, 2026-11-01: 113,2 Moz Ag reserves, geen productiecijfer, geen afnemer; eigenaren 53,5/21/25,5 % (peiljaar 2015) — https://en.wikipedia.org/wiki/Cerro_Verde_mine
[2] Freeport-McMoRan, Technical Report Summary Cerro Verde (FY2024, SEC): zilver "in the concentrate", recovered in the smelter; LOM-plan 100,2 Moz Ag, geen zilverproductie per jaar — https://www.sec.gov/Archives/edgar/data/831259/000083125925000006/a2024trscerroverde-finalxp.pdf
[3] ProActivo, interview Julia Torreblanca (Cerro Verde): privéweg 40 km naar La Joya, daar per trein naar Matarani; OSM way 286975126 (via koper-brief [3][11]) — https://proactivo.com.pe/entrevista-exclusiva-julia-torreblanca-cerro-verde-tiene-la-concentradora-mas-grande-construida-en-una-sola-fase/
[4] PeruRail Cargo, operationeel net (transfercentra Pillones/La Joya) — https://www.perurail.com/cargo/operational-network/
[5] SMM, overseas locations: Cerro Verde SMM 16,8 %, Freeport 55,1 %, Sumitomo Corp 4,2 % — https://www.smm.co.jp/en/corp_info/location/overseas/
[6] MundoMarítimo, 2016-02-15: eerste verscheping Cerro Verde-concentraat op Muelle F, Tisur — https://www.mundomaritimo.cl/noticias/realizaron-primer-embarque-en-muelle-f-del-puerto-peruano-de-matarani
[7] SMM, Toyo Smelter and Refinery: producten koper, goud- en zilvergranulaat; concentraat uit SMM-belangen in Noord-/Zuid-Amerika en Australië; berth tot 30.000 t; Cerro Verde of Peru niet genoemd — https://www.smm.co.jp/en/corp_info/location/domestic/toyo/
[8] OSM landuse 住友金属鉱山 東予工場 (via koper-brief [10], koper-sitelaag `w-toyo`) — v2/design/koper-sitelaag.json
[9] Sumitomo Corporation, copper business: concentraat aan smelters in en buiten Japan — https://www.sumitomocorp.com/en/jp/enrich/contents/global_1028
[10] Routebrief `v2/design/routebrieven/koper-cerroverde-toyo.md` (ankers, benen, bake-toets, OSM-ways) en `v2/data/stroomroute-koper-cerroverde-toyo.json` (geometrie, letterlijk te kopiëren)
[sat] Esri World Imagery via `v2/tools/sat_check.py`, z15, 2026-11-01: `v2/build-cache/satcheck/sat-zilver-cerroverde-toyo-ag-{cerroverde-conc,lajoya,matarani-kade,toyo-kade}.png`

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
Recept: `bash v2/tools/bak_stromen.sh zilver-cerroverde-toyo` (functie `bak_zilver_cerroverde_toyo`, alles letterlijke kopie van `bak_koper_cerroverde_toyo`; geen profiel, extract, vlucht of leiding). Uitvoer `v2/data/stroomroute-zilver-cerroverde-toyo.json`, 59,8 KB, versie 2, punt_formaat lonlat, 6 benen, 2.986 punten, totaal **17.393,7 km**, 4 markers.

| # | modaliteit | km gebakken | brief | stippel |
|---|---|---|---|---|
| b1 | truck | 47,0 (786 pt) | hemelsbreed 36, privéweg 40 (indicatie, geen wegkm) | nee |
| b2 | spoor | 59,2 (343 pt) | ~60 | nee |
| b3 | spoor | 1,7 | 1,7 hemelsbreed | ja: haventerrein |
| b4 | zee | 72,1 | 72,1 | ja: haven-aanloop Matarani |
| b5 | zee | 17.190,4 (1.759 pt) | 17.190,4 | nee (aannemelijk: één bron in de naam) |
| b6 | zee | 23,3 | 23,3 | ja: haven-aanloop Toyo |

Markers: ag-cerroverde-conc, ag-lajoya-overslag (0,035 km van de lijn), ag-matarani-kade, ag-toyo-kade (overige op de lijn). Naden: grootste 0,133 km (La Joya, spoorbegin), de rest 0,000 km.

**Toelichting stippels:** b3 is het havenspoor/pier zonder net; b4 en b6 zijn haven-aanlopen (MARNET reikt niet: Matarani-kade 70,6 km, Toyo-kade 21,5 km van de zeeknoop), beide letterlijk de gedeelde geojson van de koperstroom. Geen vlucht, geen leiding.
**Toets:** `toets_knikken.py`: 9 knikken, 1 omkering (spoor bij La Joya, echte scherpe bocht 162 gr, geen terugloop), 0 terugloop; de spikes in het truckbeen zijn mijnterrein bij de put en erven van de koperstroom. b1 heeft geen echte wegkm: de ±15%-toets is niet toepasbaar, 47,0 tegen 40 privéweg (+17,5 %) blijft een indicatie.
**Lessen:** een volledige kopie van een koperstroom kost één functie en geen scan; `bash v2/tools/bak_stromen.sh` leest het script tijdens het draaien, dus een gelijktijdige edit van een andere agent geeft aan het eind een bash-foutregel (hier 'otcirkel: command not found' op regel 16736) zonder gevolgen voor de uitvoer. Zilver-sitelaag mist Cerro Verde: centraal toevoegen (anker ag-cerroverde-conc).
