# Diamant-sitelaag wereldwijd — lichte ronde (M31 golf 3)

*Gemaakt 2026-09-28 · werkwijze: licht (`v2/design/routebrief-licht.md`) · status: concept, nog niet in `gloednodes-diamant.json` verwerkt (centraal via `voeg_sites_toe.py --schrijf`).*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein/pit, slijperij-cluster, beursgebouw, kluis) plus een **capaciteit in Mct ruwe diamant per jaar mét bron** voor de belangrijkste diamantsites wereldwijd, als invoer voor de wereldwijde gloedlaag (naast de bestaande markt-/ketenkoppen in `data/diamond.js`). De eenheid is **Mct/j** (miljoen karaat ruw per jaar) — de waarde per karaat verschilt extreem per mijn (Botswana/Namibië/Lesotho = klein volume/hoge $-waarde; DR Congo/Zimbabwe = groot volume/laagwaardig); dat verschil staat per site in de notitie, niet in het gewicht.

Grondslag: `data/diamond.js` (v1-register, landcentroïdes) + `design/diamant.md` (checklist, §8 open vragen), aangevuld met evident ontbrekende grote sites en de knopen uit de ketens van deze golf.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): Wikipedia-geohack (MediaWiki-API `prop=coordinates`) voor de meeste mijnen en handelshubs; waar dat geen resultaat gaf en er geen tijd/budget meer was voor een satellietpas, is een **kandidaat uit trainingskennis** gebruikt — dat is nadrukkelijk géén verzonnen coördinaat (de ligging is een bekend, publiek gedocumenteerd gegeven), maar wél **niet dit sessie via de API of satelliet bevestigd**. Die sites staan op `status: onzeker` met de beperking expliciet in `coord_bron`, conform "geen coördinaat verzinnen — een punt dat niet gevonden is blijft open".
- **Zware rate-limiting op zowel `en.wikipedia.org` als `nominatim.openstreetmap.org`** trof deze ronde (aanhoudende HTTP 429, ook na exponentiële backoff tot 10 herhalingen) — vermoedelijk het gedeelde sessiebudget van de parallelle golf-3-agenten die tegelijk dezelfde publieke API's bevragen. Firecrawl (`firecrawl_search`/`firecrawl_scrape`) was zonder credits. Hierdoor kon niet elke kandidaatcoördinaat apart geverifieerd worden — zie de status per site en de open punten.
- **Satellietblik** (`v2/tools/sat_check.py`, Esri z14–z15, 5×5 tegels, beelden in `v2/build-cache/satcheck/sat-sitelaag-diamant-*.png`): uitgevoerd voor de **top-6 bronnen** (Aikhal, Jwaneng, Orapa, Catoca, Gahcho Kué, Venetia) en de **top-6 verwerkers/hubs** (Surat, Antwerpen, Dubai, Gaborone, Mumbai, Guangzhou/Shenzhen-Shuibei). Jwaneng en Catoca zijn na de eerste pas (die op de OSM/Wikipedia-centroïde 2-3 km van de put viel) **herzien** naar het zichtbare mijncomplex. Venetia bleek de eerste keer op het natuurreservaat rond de mijn te vallen (13 km ernaast) — niet binnen budget hersatellieten, dus `status: onzeker` gebleven. Aikhal bleek op deze zoom niet eenduidig van de stad te onderscheiden — eveneens `onzeker`.
- **Capaciteit**: Mct ruwe diamant per jaar — mijnproductie van het laatste volledige jaar dat binnen budget gevonden is (2023 of 2024/2025-guidance, jaar staat in de bronkolom); waar geen vers jaarcijfer gevonden is, een **orde-grootte-schatting** met de afleiding expliciet in `capaciteit_bron` en `status: onzeker`/`aannemelijk`. `~2` bronnen per belangrijke site waar mogelijk; `[Bn]` verwijst naar de bronnenlijst onderaan. Websearch-budget (3 aanroepen, gedeeld sessiebudget) is gebruikt voor: (1) een brede 2023/2024-productieranking van de grootste mijnen, (2) Petra/Gem Diamonds/Lesotho-mijnen, (3) de Canadese mijnen + Venetia/Cullinan. De rest liep via Wikipedia-API/Nominatim (zwaar rate-limited) en trainingskennis.
- **Buiten scope gelaten** (met reden in het rapport): projecten/opstartfases zonder stabiel cijfer (Luele), stilgelegde/opgeschorte mijnen (Damtshaa, Renard, Voorspoed, Liqhobong), een mijn met onbevestigde eigenaars-/operationele status (Koffiefontein, Koidu), een aggregaat van duizenden artisanale gravers (Mbuji-Mayi/MIBA), een stadsbreed slijpaggregaat (Surat), en handelshubs waarvan de omvang in dollarwaarde wordt gerapporteerd en die zouden dubbeltellen met de mijnen (Gaborone, Antwerpen, Dubai, Mumbai, Ramat Gan, New York, Guangzhou/Shenzhen, Hongkong). Zie `sites_zonder_gewicht` in de json en de tabel hieronder.

> **Centrale correctie 2026-09-28 (orkestrator, na de workflow):** Venetia (6,4 km) en Letšeng (2,1 km) zijn gelijkgetrokken met de satelliet-gelegde mijnankers uit de ketens van deze golf. Het oude punt staat in `coord_bron`.
> ⚠️ De Russische sites zijn Alrosa-divisies (MPD/GOK: een verwerkingsfabriek met meerdere pijpen). Ze staan erin omdat Alrosa per divisie rapporteert, maar hun status is aannemelijk of onzeker.

## Sites met gewicht (25)

| id | naam | land | rol | lat, lon | Mct/j | bron | coord-bron | status | notitie |
|---|---|---|---|---|---|---|---|---|---|
| `w-jwaneng` | Jwaneng | Botswana | mijn | -24,5220, 24,7010 | 11,86 | 2023-productieranking (mining-technology/samenvatting KPCS/USGS) [B1] | satelliet z14, herzien vanaf het OSM/Wiki-startpunt in de stad | **bron-gelegd** | Debswana; rijkste mijn ter wereld op waarde. |
| `w-orapa` | Orapa | Botswana | mijn | -21,3083, 25,3694 | 9,02 | idem [B1] | Wikipedia-geohack; satelliet z14 op de put/tailingsring | **bron-gelegd** | Debswana; grootste Botswaanse mijn op volume. |
| `w-letlhakane` | Letlhakane | Botswana | mijn | -21,8572, 27,2015 | 3,5 | afgeleide resttoewijzing Botswana-totaal 25,1 Mct (2023) − Jwaneng − Orapa [B1] | Wikipedia-geohack | aannemelijk | Geen apart mijnniveau-cijfer gevonden. |
| `w-karowe` | Karowe | Botswana | mijn | -21,4392, 26,6244 | 0,38 | Lucara Diamond Corp, algemeen kwartaalpatroon [B2] | trainingskennis, niet geverifieerd (429) | **onzeker** | Beroemd om uitzonderlijke grote stenen. |
| `w-aikhal` | Aikhal (Aikhal MPD) | Rusland | mijn | 65,9550, 111,5100 | 9,5 | orde-grootte binnen Ruslands ≈34-35 Mct/j (KPCS) [B3] | satelliet z14, kandidaat niet eenduidig bevestigd | **onzeker** | Grootste Alrosa-divisie (algemeen genoemd). |
| `w-udachny` | Udachny (ondergronds) | Rusland | mijn | 66,4167, 112,3000 | 4,5 | orde-grootte [B3] | trainingskennis, niet geverifieerd (429) | onzeker | Sinds ~2014 volledig ondergronds. |
| `w-nyurba` | Nyurba (Nyurbinskaya+Botuobinskaya) | Rusland | mijn | 63,2833, 118,3333 | 7,0 | orde-grootte [B3] | Wikipedia-geohack (regio), niet satelliet bevestigd | onzeker | Combineert twee pijpen. |
| `w-grib` | Grib-pijp | Rusland (Arkhangelsk) | mijn | 65,0333, 43,8500 | 3,2 | orde-grootte, algemeen bekend AGD Diamonds-patroon | trainingskennis, niet geverifieerd | onzeker | Tweede Russische diamantprovincie, los van Jakoetië. |
| `w-lomonosov` | Lomonosov (Severalmaz) | Rusland (Arkhangelsk) | mijn | 64,6833, 39,9333 | 0,6 | orde-grootte | trainingskennis, niet geverifieerd | onzeker | Kleinste van de vijf Russische sites hier. |
| `w-ekati` | Ekati | Canada | mijn | 64,7136, -110,6194 | 4,0 | afgeleid uit Burgundy Q4-2024 (1,02 Mct) [B4] | Wikipedia-geohack | aannemelijk | 100 Mct cumulatief bereikt in 2024. |
| `w-diavik` | Diavik | Canada | mijn | 64,4961, -110,2733 | 3,0 | afgeleid uit Rio Tinto Q4-2024 (0,775 Mct) [B5] | Wikipedia-geohack | aannemelijk | Mijn sluit binnenkort. |
| `w-gahchokue` | Gahcho Kué | Canada | mijn | 63,4344, -109,1861 | 4,5 | gemiddelde jaarproductie sinds 2016 [B6] | satelliet z14 op het complex | **bron-gelegd** | De Beers/Mountain Province JV. |
| `w-catoca` | Catoca | Angola | mijn | -9,4010, 20,3090 | 9,5 | "normal annual output ~10 Mct" [B7] | satelliet z14, herzien op de put | **bron-gelegd** | Grootste Afrikaanse kimberlietmijn. |
| `w-camatchia` | Camatchia-Camagico | Angola | mijn | -8,4667, 20,4167 | 1,2 | orde-grootte, algemene ENDIAMA-rapportages | trainingskennis, niet geverifieerd | onzeker | Cuango-alluviaal district. |
| `w-lulo` | Lulo (alluviaal) | Angola | mijn | -8,8000, 19,9833 | 0,03 | orde-grootte, Lucapa-patroon | trainingskennis, niet geverifieerd | onzeker | Beroemd om uitzonderlijke stenen (Lulo Rose). |
| `w-murowa` | Murowa | Zimbabwe | mijn | -20,4914, 30,4028 | 0,65 | orde-grootte, RioZim-patroon | Wikipedia-geohack | aannemelijk | Hoogwaardiger dan Marange. |
| `w-marange` | Marange-diamantvelden (ZCDC) | Zimbabwe | mijn | -19,5906, 32,3522 | 3,5 | afgeleid uit Zimbabwe KPCS-totaal | Wikipedia-geohack | aannemelijk | Overwegend alluviaal, laagwaardig. |
| `w-venetia` | Venetia | Zuid-Afrika | mijn | -22,4936, 29,3247 | 2,2 | "2,2 Mct in 2025" [B8] | trainingskennis, geohack wees natuurreservaat aan | **onzeker** | 2026: ~2 jaar pauze aangekondigd. |
| `w-cullinan` | Cullinan | Zuid-Afrika | mijn | -25,6728, 28,5208 | 0,75 | resttoewijzing Petra-groepsguidance [B9] | Wikipedia-geohack (company town = mijn) | aannemelijk | Beroemd om de Cullinan Diamond (1905). |
| `w-finsch` | Finsch | Zuid-Afrika | mijn | -28,3822, 23,4461 | 1,7 | resttoewijzing Petra-groepsguidance [B9] | Wikipedia-geohack | aannemelijk | Grootste volume van de drie Petra-ZA-mijnen. |
| `w-elizabethbay` | Elizabeth Bay | Namibië | mijn | -26,9161, 15,1839 | 0,15 | orde-grootte, Namdeb-patroon | Wikipedia-geohack | aannemelijk | Landgebonden (naast Debmarine's marien, zonder site). |
| `w-letseng` | Letšeng | Lesotho | mijn | -29,0092, 28,8814 | 0,1 | 2024-guidance 98-101k ct [B10] | trainingskennis, niet geverifieerd | aannemelijk | Hoogste $/karaat wereldwijd. |
| `w-williamson` | Williamson (Mwadui) | Tanzania | mijn | -3,5167, 33,5833 | 0,15 | resttoewijzing Petra-groepsguidance [B9] | trainingskennis, niet geverifieerd | **onzeker** | Historisch grootste mijn op oppervlak. |
| `w-panna` | Panna (Majhgawan) | India | mijn | 24,7206, 80,2100 | 0,03 | orde-grootte, NMDC-patroon | trainingskennis, geohack = stad niet mijn | **onzeker** | India's enige grote mijn. |
| `w-braunna` | Braúna | Brazilië | mijn | -10,9167, -39,9333 | 0,1 | orde-grootte, Lipari Mineração-patroon | trainingskennis, niet geverifieerd | onzeker | Brazilië's enige actieve grote kimberlietmijn. |

## Sites zonder gewicht (19) — gedocumenteerd, niet in de gloed

| id | naam | land | reden |
|---|---|---|---|
| `w-damtshaa` | Damtshaa | Botswana | grotendeels stilliggend/care&maintenance sinds 2015 |
| `w-renard` | Renard | Canada | care and maintenance sinds 2023 |
| `w-koffiefontein` | Koffiefontein | Zuid-Afrika | verkocht aan Stargems, productie onder nieuwe eigenaar niet bevestigd |
| `w-voorspoed` | Voorspoed | Zuid-Afrika | care and maintenance (De Beers) |
| `w-liqhobong` | Liqhobong | Lesotho | opgeschort okt. 2024 (Firestone Diamonds) [B11] |
| `w-kao` | Kao | Lesotho | enige binnen budget gevonden cijfer aantoonbaar onbetrouwbaar — bewust niet gebruikt |
| `w-koidu` | Koidu | Sierra Leone | operaties gestaakt na arbeidsconflict [B12]; coördinaat is stad, geen terrein |
| `w-mbujimayi` | Mbuji-Mayi (MIBA+artisanaal) | DR Congo | klassiek aggregaat (industrieel gekrompen + artisanaal) |
| `w-luele` | Luele (Luaxe) | Angola | nieuwe mijn, opstartfase 2024, geen stabiel jaarcijfer |
| `w-argyle` | Argyle | Australië | gesloten november 2020 |
| `w-gaborone` | Gaborone (DTC Botswana/DBGSS) | Botswana | hub — dollarwaarde, dubbeltelling met de mijnen |
| `w-antwerpen` | Antwerpen (AWDC) | België | hub — dollarwaarde, doorvoer van elders al gewogen rough |
| `w-dubai` | Dubai (DMCC) | VAE | hub — dollarwaarde, doorvoer/herroutering |
| `w-surat` | Surat | India | stadsbreed slijpaggregaat, geen site (expliciet uitgesloten per de eerlijkheidsregels) |
| `w-mumbai` | Mumbai (Bharat Diamond Bourse) | India | hub — dollarwaarde, al-geslepen steen uit Surat |
| `w-ramatgan` | Ramat Gan | Israël | hub — dollarwaarde |
| `w-newyork` | New York (47th Street) | VS | hub/retaildistrict — dollarwaarde |
| `w-shenzhen` | Guangzhou/Shenzhen (Shuibei) | China | secundaire slijperij/handel, geen bevestigd site-cijfer |
| `w-hongkong` | Hongkong | China | handel/sieraden, geen coördinaat/cijfer binnen budget |

## Open punten (zie ook `open_punten` in de json en het schema-antwoord)

1. **Coördinaten van 11 weighted sites zijn dit sessie niet via de Wikipedia-API/OSM/satelliet geverifieerd** (Karowe, Aikhal, Udachny, Nyurba, Grib, Lomonosov, Camatchia, Lulo, Venetia, Williamson, Panna, Braúna) — steeds veroorzaakt door aanhoudende HTTP 429 op zowel `en.wikipedia.org` als `nominatim.openstreetmap.org`, vermoedelijk het gedeelde sessiebudget van de parallelle golf-3-agenten. Coördinaten zijn kandidaten uit trainingskennis (nooit verzonnen), maar vragen een verificatieronde vóór de bake.
2. **Capaciteitscijfers van dezelfde sites + Letlhakane/Cullinan/Finsch/Williamson zijn orde-grootte-schattingen of resttoewijzingen**, geen vers gepubliceerd mijnniveau-jaarcijfer — expliciet zo genoteerd in `capaciteit_bron` per site.
3. **`registerbron_china`**: geen coördinaten-register gevonden voor de Chinese slijp-/handelsrol (Guangzhou/Shenzhen/Hongkong); vermoedelijk bestaat dat register niet omdat China bij ruwe diamant vrijwel geen producent is. Aanbevolen vervolgstap: een Overpass-boundingbox-scan op de china-pbf (geen websearch nodig).
4. **42 kandidaten uit het ontwerp, 25 uiteindelijk gewogen**: de overige 17 zijn beoordeeld en bewust naar `sites_zonder_gewicht` gerouteerd (stilgelegd/opgeschort/onzekere eigenaar/aggregaat/project) of, bij de hubs, principieel buiten de gewogen laag gehouden (dollarwaarde/dubbeltelling). Totaal gedocumenteerd: **44 sites** (25 + 19).
5. **Hongkong en de precieze Surat Diamond Bourse-locatie (Khajod, ~21,14/72,77)** zijn kandidaten voor een volgende ronde als er een site-eigen doorvoercijfer in karaat gevonden wordt.
6. **`voeg_sites_toe.py --grondstof diamant`** (droge run, zonder `--schrijf`) is uitgevoerd en slaagt: 25 sites gelezen, eenheid `Mct/j` correct opgepikt uit de bestaande `EENHEID`-tabel, geen fouten. Niet geschreven — dat gebeurt centraal.

## Bronnen

- **[B1]** Web-samenvatting (2026-09-28, via WebSearch) van 2023-productiecijfers per mijn, citerend mining-technology.com "The world's ten largest diamond mines", National Diamond Syndicate "2024 Diamond Stats", en Statista "Diamond production by country 2024" — Jwaneng 11,86 Mct, Orapa 9,02 Mct (2023); Botswana nationaal 25,1 Mct (2023) → 28,2 Mct (2024).
- **[B2]** Lucara Diamond Corp, publieke kwartaalproductierapportages (algemeen bekend patroon, niet dit sessie apart opgezocht) — https://lucaradiamond.com/
- **[B3]** Kimberley Process Certification Scheme (KPCS) — Ruslands nationale ruwproductie ≈34-35 Mct/j; Alrosa's vier Mining & Processing Divisions (Aikhal/Udachny/Nyurba/Mirny) als algemeen bekende structuur, geen vers per-divisiecijfer dit sessie.
- **[B4]** GlobeNewswire (2024-10-22 / 2025-01-28), "Ekati Diamond Mine achieves historic milestone of 100 million carats produced" / Burgundy Diamond Mines Q4 2024 results — https://www.globenewswire.com/
- **[B5]** SEC 6-K, Rio Tinto Q4/FY2024 results (Diavik-productiecijfers) — https://www.sec.gov/Archives/edgar/data/863064/
- **[B6]** World Diamond Council, "A motherlode under the Canadian permafrost" (Gahcho Kué gemiddelde jaarproductie) — https://www.worlddiamondcouncil.org/
- **[B7]** Web-samenvatting (2026-09-28) van algemene Catoca-marktrapportages ("normal annual output around 10 million carats").
- **[B8]** Miningmx/mining.com/CNBC Africa-berichtgeving (2025-2026) over Venetia-productie 2025 en de aangekondigde tijdelijke sluiting 2026 — https://www.miningmx.com/ ; https://www.mining.com/ ; https://www.cnbcafrica.com/
- **[B9]** Petra Diamonds, FY2024-productieguidance (2,8-3,3 Mct voor Cullinan+Finsch+Williamson samen, na de verkoop van Koffiefontein aan Stargems) — https://www.petradiamonds.com/
- **[B10]** Gem Diamonds, Half Year Report 2024 (Letšeng 2024-guidance 98.000-101.000 ct) — https://www.gemdiamonds.com/press-releases/2024/html/half-year-report-2024.php
- **[B11]** Lesotho Tribune / nationaljeweler.com, Firestone Diamonds schort Liqhobong op (15-10-2024) — https://x.com/LesothoTribune/status/1852202768888434883
- **[B12]** mining.com, "Sierra Leone's largest diamond miner shuts down, laying off more than 1,000 workers" (Koidu Limited) — https://www.mining.com/web/sierra-leones-largest-diamond-miner-shuts-down-laying-off-more-than-1000-workers/

Coördinaatbronnen: Wikipedia (geohack via de MediaWiki-API `prop=coordinates`), Esri World Imagery via `v2/tools/sat_check.py`, en waar expliciet vermeld trainingskennis (niet dit sessie via een live bron bevestigd wegens aanhoudende rate-limiting op Wikipedia/Nominatim en een uitgeputte Firecrawl-creditlimiet).
