# Routebrief (licht) · gas — Moomba (Cooper-bekken) → Moomba–Sydney-pijpleiding → Wilton-knoop (Australië)

**stroom-id:** `gas-moomba-wilton` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** Aardgas uit het Cooper-bekken wordt in de Moomba-gasfabriek (Santos, Zuid-Australië) verwerkt en gaat door de 1.298 km lange,
ondergrondse Moomba Sydney Pipeline (DN850, APA, via Young) zuidoostwaarts naar de Wilton-knoop bij Sydney. Een een-been-pijp (reserve-as, Oost-Australische
binnenlandse markt); de tekening stopt op de knoop, waar de verdeelnetten van Sydney, Newcastle, Wollongong en Canberra beginnen.
**Welke as van het verhaal:** *Reserve-as "Oost-Australische binnenlandse gasmarkt"* — gas dat niet als LNG de kust uit gaat maar het binnenland door naar Sydney.
Volume: **capaciteit, geen doorzet.** 152 PJ/j ≈ 4,0 bcm/j (SA-overheid, peiljaar onbekend, snippet [7]); AEMC-nameplate 2024 565 TJ/d voorwaarts ≈ 206 PJ/j ≈ 5,4 bcm/j
(zoekresultaat [6]); GEM 446 TJ/d ≈ 4,3 bcm/j [2]. Omrekening 1 PJ ≈ 26,3 Mm³ is eigen rekenwerk. Een gemeten jaardoorzet is niet gevonden. Gewicht in de gloed: 4,0 bcm/j (capaciteit).
De pijl is de capaciteitsrichting: de leiding is **bi-directioneel** (sinds 2015 kan gas ook van Wilton noordwaarts naar Moomba voor de Gladstone-LNG) [2][1].

## 1 · Ketenkaart
```
Moomba-gasfabriek (Santos), Cooper-bekken `gas-moomba-plant`
  ──(b1 leiding · Moomba Sydney Pipeline DN850, 1 OSM-way, doorgetrokken · 1.298,2 km OSM / 1.299 Wikipedia / 1.300 AEMC-APA)──►
Wilton-knoop, Sydney-regio (APA) `gas-wilton-knoop` — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-moomba-plant` → `gas-wilton-knoop` | Moomba Sydney Pipeline (MSP), OSM way 412224720, man_made=pipeline, substance=gas, usage=transmission, diameter 850, operator APA Group, start 1976, flow=bidirectional, ondergronds; passeert Tibooburra-streek (5,7 km), Young (7,9 km), Marsden (2,9 km), Goulburn-streek (3,8 km) | 1.299 [5/4], 1.300 [1][3]; gemeten OSM **1.298,2** (-0,1% / -0,1%) | vooraf gestikt geojson (FeatureCollection, 411 punten; grootste segment 48,7 km, 27 segmenten > 10 km: dun gekarteerde woestijnstukken, geen gat) | nee |

De 2.081 km (Wikipedia, APGA "2081 km bi-directional") is het hele systeem met laterals (Dalton-Canberra 58 km, Young-Lithgow/Bathurst 245, Young-Wagga 131, Burnt Creek-Griffith 179,
Culcairn-Wagga 88 [1][2]) en de parallelle ethaanleiding: geen maat voor b1. **Niet getekend:** de laterals, de Moomba Sydney Ethane Pipeline (zelfde 40-ft-strook, sinds 2023 buiten bedrijf,
wordt omgebouwd voor 20-25 TJ/d methaan [8][5]; geen eigen geometrie) en het Horsley Park-verlengstuk (OSM-way 1421707510, 50,9 km, optioneel, buiten het ontwerp).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-moomba-plant` | gasfabriek, kop van de leiding | Moomba-gasfabriek (Santos), Cooper-bekken | -28.1157, 140.2062 | [9][4][7] | bron-gelegd (z15+z16 gezien: groot verwerkingscomplex met pijpenstraten en tanks, het kruis ligt op de processtraat; landingsbaan en kamp noordelijk, groot watervlak oostelijk (overstroming, april 2025 of eerder); OSM-begin ligt op de fabriek) |
| `gas-wilton-knoop` | ontvangstpunt / eindknoop | Wilton, eind Moomba Sydney Pipeline (APA/Jemena-knoop, naam station niet bevestigd) | -34.2330, 150.7106 | [9][1] | bron-gelegd (z15+z16 gezien: klein omheind terrein met enkele installaties en gebouwtjes in weiland/bos; vanaf het hek lopen kale leidingstroken oostnoordoost; woonwijken van Wilton ca. 1,5 km westwaarts; OSM-eind ligt op het terrein) |

Hergebruik: geen. Moomba en Wilton staan niet in `gas-sitelaag.json` en niet in een andere brief. Beide ankers zijn het OSM-begin respectievelijk -eind van b1 (0 m van de lijn).
Het Wilton-terrein is geen sitelaag-punt; een bronnaam voor het ontvangststation (Wilton Gas Facility / APA-terminal) is niet gevonden, dus de naam in de tabel is een beschrijving.

## 4 · Via-punten
Niet van toepassing: leiding = één OSM-way, geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Moomba-gasfabriek (Cooper-bekken) | Santos (operator; verwerkt ook gas van Beach en Senex) | ruwgas + condensaat → verkoopgas + vloeistoffen | ontwerp 25,4 Mm³/d ruwgas (902 mmcf), 6.000 kL condensaat/ruwe olie per dag; draait onder maximum sinds SEA Gas | [7][4][12] |
| Moomba Sydney Pipeline | APA Group (Eastern Australian Pipeline Ltd) | verkoopgas Moomba → Wilton (en terug) | 565 TJ/d voorwaarts / 193 TJ/d terug (AEMC 2024), 446 TJ/d (GEM); 152 PJ/j (SA-overheid) | [6][2][7] |
| Wilton-knoop | APA (Marsden-Wilton licht gereguleerd) | leiding → verdeelnetten Sydney/Newcastle/Wollongong/Canberra | niet gevonden | [1][2] |

## 6 · Stoppunt
De tekening stopt op de Wilton-knoop: daarachter splitst het gas over het distributienet (Sydney, Newcastle, Wollongong, Canberra [2]); een afnemer met naam en adres per molecuul is niet te volgen,
dus geen fase D/E. Een bewuste een-been-pijp. Verhaal in één zin: het gas van het Cooper-bekken verlaat de Zuid-Australische woestijn door één 850 mm-pijp en komt na 1.300 km bij Sydney aan.

## 7 · Open punten
- **Geen gemeten jaardoorzet.** Alleen capaciteiten (152 PJ/j, 565 TJ/d, 446 TJ/d) en die schelen per bron en jaar; AEMO Gas Bulletin Board / GSOO niet gelezen.
- **Richting:** de leiding is bi-directioneel (2015) en Queensland-gas (Wallumbilla via de QSN Link, sinds 2008 [5]) stroomt ook in; het Moomba-gas is mogelijk deels vervangen. De pijl is capaciteit, geen netto stroom.
- **Moomba overstroomd april 2025** (productie verlaagd) komt uit het ontwerp/de haalbaarheidstoets (AEMO/AEMC); zelf niet in een bron gelezen.
- **Naam van het Wilton-station** onbekend; het terrein is op z16 herkenbaar maar niet benoemd.
- **Capaciteitsbronnen:** AEMC-register (403 bij ophalen) en SA-overheidspagina (403) alleen via zoekresultaat gelezen.
- **Dunne karteringsdichtheid:** 27 segmenten > 10 km (max 48,7 km) in woestijngebied; geometrie is OSM, niet extra gecontroleerd. De 1.298,2 km komt overeen met de gepubliceerde 1.299-1.300 km.
- **Geen last mile:** Wilton-terrein ligt op het OSM-eind; geen last-mile-been, < 2 km.

## 8 · Bronnen
[1] APGA, "Moomba Sydney Pipeline" — 1300 km bi-directioneel Moomba-Wilton, 2081 km totaal, gebouwd 1976, QSN Link 2008, Marsden-Wilton licht gereguleerd, laterals. https://apga.org.au/moomba-sydney-pipeline
[2] Global Energy Monitor wiki, "Moomba to Sydney Pipeline" — 1300 km, 446 TJ/d, EAPL/APA, 1976, flow omgekeerd 2015, laterals en capaciteiten. https://www.gem.wiki/Moomba_to_Sydney_Pipeline
[3] APA Group, "Moomba Sydney Pipeline and MSEP" — East Coast Gas Grid, 100% APA, eerste bouw 1974/76, conversie MSEP; geen capaciteitscijfer op de pagina. https://apa.com.au/operations-and-projects/gas/gas-transmission/moomba-sydney-pipeline-and-msep
[4] Wikipedia, "Moomba, South Australia" — 1.299 km naar Wilton Sydney, 1976, Santos-operator. https://en.wikipedia.org/wiki/Moomba,_South_Australia
[5] Wikipedia, "Moomba to Sydney Pipeline" — 2.081 km totaal, 1976, APA, parallelle ethaanleiding, 40-ft-strook. https://en.wikipedia.org/wiki/Moomba_to_Sydney_Pipeline
[6] AEMC, Gas pipeline register "NSW: Moomba to Sydney Pipeline (MSP)" — DN850, 1300 km, 565 TJ/d voorwaarts / 193 TJ/d terug (2024), oudere versie 489/120 (inhoud uit zoekresultaat; pagina geeft 403). https://aemc.gov.au/energy-system/gas/gas-pipeline-register/nsw-moomba-sydney-pipeline
[7] Government of South Australia, Energy & Mining, "Petroleum infrastructure" — MSP-capaciteit 152 PJ (139,3 bcf) per jaar; Moomba-fabriek ontwerp 25,4 Mm³/d (zoekresultaat; pagina geeft 403). https://energymining.sa.gov.au/industry/energy-resources/infrastructure-and-energy-markets/infrastructure/petroleum-infrastructure
[8] NSW Government, "Pipeline repurposed to strengthen gas supply", 21 okt 2025 — ethaanleiding sinds 2023 stil, conversie 20-25 TJ/d. https://www.nsw.gov.au/ministerial-releases/pipeline-repurposed-to-strengthen-gas-supply
[9] OpenStreetMap (ODbL), way 412224720 "Moomba Sydney Gas Pipeline" (man_made=pipeline, operator APA Group, diameter 850, layer -1, flow bidirectional), gelezen uit de Geofabrik australie-pbf; stikscript `v2/tools/maak_leidingbeen_gas_moomba_wilton.py`. https://www.openstreetmap.org/way/412224720
[10] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-gas-moomba-wilton-moomba.png`, `-moomba-z16.png`, `-wilton.png`, `-wilton-z16.png`.
[11] Haalbaarheidstoets golf 18 (AEMO/AEMC: bi-directioneel sinds 2015, Moomba-flooding april 2025; OSM-way 1.298,2 km, 411 nodes). Ontwerpinvoer, niet apart gelezen. https://aemc.gov.au/energy-system/gas/gas-pipeline-register/nsw-moomba-sydney-pipeline
[12] Santos, nieuwsberichten "Santos extends gas processing agreements with Beach and Senex" en "Moomba resumes full gas production capacity ahead of schedule" (zoekresultaat). https://www.santos.com/news/santos-extends-gas-processing-agreements-with-beach-and-senex/

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Bestand:** `v2/data/stroomroute-gas-moomba-wilton.json` (versie 2, lonlat, 9,4 KB) · functie `bak_gas_moomba_wilton` in `v2/tools/bak_stromen.sh`.

| # | modaliteit | been | km gemeten | km brief | afwijking | stippel |
|---|---|---|---|---|---|---|
| b1 | leiding | Moomba Sydney Pipeline DN850 (OSM-way 412224720, APA, bi-directioneel, ondergronds) Moomba naar Wilton | 1.298,2 (411 punten) | 1.299 (Wikipedia) / 1.300 (AEMC, APGA) | -0,1% | nee |

Totaal 1.298,2 km, 411 punten, 1 been, 2 markers (Moomba-gasfabriek -28.1157,140.2062 op 6 m van de lijn; Wilton-knoop -34.2330,150.7106 op 6 m). Naad n.v.t. (een been); grootste segment 48,7 km.

**Recept:** `--been-geojson leiding` met het vooraf gestikte `v2/build-cache/ais/graaf/gas-moomba-wilton-leiding-msp.geojson` (FeatureCollection; herhaalbaar met `python v2/tools/maak_leidingbeen_gas_moomba_wilton.py`, 17 s). Geen extract, via-punten, profiel, MARNET-zeebeen, haven-aanloop, stippel, vlucht of gedeeld been; hecht_marnet.py nam de lijn letterlijk over (opnieuw gebakken 12:11).

**Toets:** km binnen 15% van de gepubliceerde 1.299-1.300; markers op de lijn; toets_rechte_benen geen melding; toets_knikken 3 knikken >= 60 graden (spike 127 m bij -34.7247,149.7929; krappe bocht 277 m bij -34.3461,150.5578; spike 131 m bij -34.7235,149.7924), 0 omkeringen, 0 terugloop: kartering van het OSM-tracé zelf, niet aangepast.

**Leiding-toelichting:** doorgetrokken omdat OSM de leiding volledig kent (man_made=pipeline, operator APA, diameter 850, substance gas). 27 segmenten > 10 km zijn dun gekarteerde woestijnstukken, geen gat; de lengte klopt met de gepubliceerde. De pijl is capaciteitsrichting (leiding is bi-directioneel), geen netto stroom. Laterals, ethaanleiding en Horsley Park-verlengstuk niet getekend.

**Lessen:** een vooraf gestikte OSM-leiding is een enkele regel `--been-geojson` (patroon bak_gas_draupner_dunkerque). Centraal nodig: sitelaag voor Moomba en Wilton, register, bundel. Bij het bakken meldde de shell een foutregel `beennaam,: command not found` ver na deze functie: een gelijktijdige edit van een andere agent aan bak_stromen.sh tijdens de run (achteraf `bash -n` ok, regel staat nu in een commentaar); deze stroom is niet geraakt.
