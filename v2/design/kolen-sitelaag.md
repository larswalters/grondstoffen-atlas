# Kolen-sitelaag wereldwijd — lichte ronde

*Gemaakt 2026-09-26 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in
`gloednodes-kolen.json` verwerkt (die laag bestaat nog niet — zie `voeg_sites_toe.py`-generalisatie in
`memory/next-actions.md`).*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein/pit, kolenterminal, centrale, cokerij) plus een **capaciteit
in Mt kolen/j mét bron en peiljaar** voor de belangrijkste kolensites wereldwijd — mijnen, exportterminals,
importhubs en een handvol afnemers (centrale/staalfabriek). Grondslag: `data/coal.js` (v1-register, 20
regionale centroïdes zonder site-precisie) aangevuld met evident ontbrekende grote sites uit de Global
Energy Monitor Global Coal Mine Tracker (GCMT) en de bestaande ankers uit `kolen-cerrejon-ruhr.md` /
`aansluitingen.json`. Dit is de invoer voor de wereldwijde gloedlaag van kolen; net als bij koper zijn de
gewichten in de huidige regionale `coal.js`-nodes nattevingerwerk op continentschaal — dit zijn echte
site-gewichten.

**Eenheid: `Mt kolen/j`** (bindend uit het ontwerp `sitelaag-kolen.json`). Anders dan koper (kt metaal-
inhoud) is kolen zelf het verhandelde product tot het verbrand of vercookst wordt, dus geen omrekening
nodig voor mijnen en terminals. Voor centrales en de staalfabriek/cokerij is het gepubliceerde cijfer vaak
**MW** resp. **Mt staal**, niet **Mt kolen** — die vier sites (Tuoketuo, Vindhyachal, Kalinganagar,
Duisburg) dragen daarom een extra veld `eenheid_site` dat vermeldt dat hun Mt-cijfer is **afgeleid**, niet
rechtstreeks gepubliceerd, en dus niet blind bij mijnproductie mag worden opgeteld.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): primair **Global Energy Monitor —
  Global Coal Mine Tracker** (gem.wiki), dat voor kolen het equivalent is van het MEE-emissieregister bij
  koper — elke mijn ≥ 1 Mt/j heeft er een visueel op Google Earth/Planet gelegde coördinaat, eigenaar en
  productiecijfer (CC BY 4.0, bronvermelding verplicht). Voor terminals/centrales: Wikipedia-geohack, GEM-
  havenpagina's, of bedrijfswebsites (Adani, RBCT, Drummond, PWCS/NCIG). **Firecrawl was deze sessie
  uitgeput (credits op)** — alle research liep via `WebSearch`/`WebFetch` op gem.wiki- en Wikipedia-
  pagina's in plaats van via het gebruikelijke Firecrawl-scrapepad; dat werkte, maar leverde per site vaker
  alleen een AI-samenvatting van de infobox dan de ruwe pagina.
- **Satellietblik** (`python v2/tools/sat_check.py`, Esri z13–z14, beelden in `v2/build-cache/satcheck/`
  met prefix `sitelaag-kolen-`) voor de **top-6 mijnen** op capaciteit (North Antelope Rochelle, Gevra, KPC
  Sangatta, Borneo Indobara, Bara Tabang, Kusmunda) en **top-6 verwerkers** — bij kolen bestaan geen
  smelters, dus dit zijn de zes zwaarste **overslagterminals** (Huanghua, Qinhuangdao, Caofeidian,
  Newcastle/Kooragang, Dalrymple Bay, Richards Bay). Ligt het kruis op het terrein/de stockpile/het wingat
  → **bron-gelegd**; anders verschoven naar wat je wél ziet (genoteerd in `coord_bron`) of, als er niets
  bruikbaars in beeld komt, **onzeker** gelaten. Vier van de twaalve satellietpassen troffen doel; vier
  moesten worden verschoven (North Antelope Rochelle, Huanghua, Qinhuangdao gedeeltelijk) en één bleef
  zonder zichtbare mijnactiviteit onder het kruis (Borneo Indobara).
- **Capaciteit**: mijnproductie laatste volledige jaar (2023, 2024 of 2025 — het jaar staat telkens in de
  bronkolom; GEM's Global Coal Mine Tracker publiceert releases met een mix van jaren per mijn), nameplate/
  doorzet voor terminals, en een **afgeleid** kolenequivalent voor de twee centrales en de cokerij/
  staalfabriek waar geen directe Mt-bron bestaat (zie `eenheid_site` in de json). Bronnen: GEM Global Coal
  Mine Tracker, bedrijfsrapportages (Glencore, Peabody, Adaro, Adani, RBCT, Drummond), overheidspublicaties
  (India: PIB/Ministry of Coal, Coal Controller's Organisation; Rusland: TASS), vakpers (sxcoal, Argus,
  Mining Technology, mining.com); ~2 per site, `[Bn]` naar de bronnenlijst onderaan.
- **Buiten scope gelaten** (met reden in het rapport): Zhundong South Surface Mine (China, Xinjiang) — geen
  site-niveau coördinaat gevonden, alleen een county-centroïde (Jimsar, 43,983/89,067), en een county-
  centroïde is geen anker; Pribbenow/La Loma (Drummond, Colombia) — dezelfde eigenaar en spoorlijn als het
  hier wél opgenomen El Descanso, productie ingestort naar 3,86 Mt (2024) tegen 21,7 Mt bij El Descanso,
  dus niet apart geteld om geen twee bijna-identieke Drummond-ankers te leggen; Aktogay/Tavan Tolgoi-
  Energy Resources/UHG (Mongolië) — alleen de ETT-helft van het Tavan Tolgoi-veld is hier genomen, de
  andere concessie (Energy Resources/UHG) is een apart, niet onderzocht blok op hetzelfde veld; Kideco's
  zusterconcessies, Indominco, Dipka's twee buurmijnen Kusmunda-Zuid en Gevra-Zuid, Heilongjiang/
  Shaanxi-mega-mijnen (Yulin, Shenmu) — evident groot maar deze ronde niet onderzocht (tijdgebrek, geen
  aanwijzing dat ze ontbreken buiten volledigheid).

## Sites (41)

| id | naam | land | rol | lat, lon | capaciteit Mt/j | bron | coord-bron | status |
|---|---|---|---|---|---|---|---|---|
| `w-narm` | North Antelope Rochelle | VS (Wyoming) | mijn | -105,283, 43,588 → **43,588, -105,283** | 58,9 | GEM GCMT 2025 [B1]; Peabody [B2] | GEM Table 1, verschoven ~2 km n.a.v. satelliet | aannemelijk |
| `w-blackthunder` | Black Thunder | VS (Wyoming) | mijn | 43,66, -105,30 | 60,5 | GEM GCMT 2023 [B1]; Wikipedia [B3] | GEM/mindat centroïde | aannemelijk |
| `w-gevra` | Gevra OC | India (Chhattisgarh) | mijn | 22,3363, 82,5457 | 55,8 | GEM GCMT 2025 [B1]; PIB/Min. of Coal [B4] | GEM Table 1 | **bron-gelegd** |
| `w-kusmunda` | Kusmunda OC | India (Chhattisgarh) | mijn | 22,3326, 82,6667 | 50,1 | GEM GCMT 2024 [B1]; drishtiias/PIB [B4][B5] | GEM Table 1 | **bron-gelegd** |
| `w-dipka` | Dipka OCP | India (Chhattisgarh) | mijn | 22,3227, 82,5279 | 37,5 | Coal Controller's Org. [B6]; IndianPSU [B7] | midden van gepubliceerde blokgrenzen | aannemelijk |
| `w-kpc-sangatta` | KPC (Sangatta+Bengalon) | Indonesië | mijn | 0,8240, 117,5990 | 55,0 | KPC/Bumi jaarcijfers [B8]; GEM GCMT [B1] | GEM Table 1 | **bron-gelegd** |
| `w-borneo-indobara` | Borneo Indobara | Indonesië | mijn | -3,7002, 115,5598 | 46,0 | Golden Energy Mines [B9]; GEM GCMT [B1] | GEM 'approximate'; satelliet: geen mijn zichtbaar | **onzeker** |
| `w-bara-tabang` | Bara Tabang | Indonesië | mijn | 0,5509, 116,1263 | 50,5 | GEM GCMT 2024 [B1]; Bayan Resources [B10] | GEM Table 1 | **bron-gelegd** |
| `w-tanjung-enim` | Tanjung Enim (PTBA) | Indonesië | mijn | -3,7400, 103,7683 | 41,8 | GEM GCMT [B1]; PTBA [B11] | GEM Table 1 | aannemelijk |
| `w-tutupan` | Tutupan (Adaro) | Indonesië | mijn | -2,2045, 115,5278 | 43,8 | GEM GCMT 2024 [B1]; sxcoal [B12] | GEM Table 1 | aannemelijk |
| `w-kideco` | Pasir (Kideco) | Indonesië | mijn | -1,8909, 115,8716 | 30,7 | Indika Energy [B13]; GEM GCMT [B1] | GEM Table 1 | aannemelijk |
| `w-haerwusu` | Haerwusu | China (Binnen-Mongolië) | mijn | 39,7310, 111,2583 | 35,0 | GEM GCMT 2023 [B1]; Mining Digital/EJAtlas [B14][B15] | GEM Table | aannemelijk |
| `w-heidaigou` | Heidaigou | China (Binnen-Mongolië) | mijn | 39,700, 111,271 | 33,1 | PMC-publicatie [B16]; CSEC [B17] | midden gepubliceerde mijngrenzen | aannemelijk |
| `w-goonyella` | Goonyella Riverside | Australië (Qld) | mijn | -21,759, 147,977 | 17,1 | Wikipedia/BHP [B18]; BHP [B19] | Wikipedia-geohack | aannemelijk |
| `w-peakdowns` | Peak Downs | Australië (Qld) | mijn | -22,2549, 148,1797 | 17,78 | GEM GCMT (aug-2026 release) [B1]; NS Energy/BHP [B20] | GEM Table 1 | aannemelijk |
| `w-mtarthur` | Mount Arthur | Australië (NSW) | mijn | -32,3370, 150,8561 | 22,335 | GEM GCMT 2024 [B1]; BHP [B21] | GEM Table 1 | aannemelijk |
| `w-grootegeluk` | Grootegeluk | Zuid-Afrika (Limpopo) | mijn | -23,6717, 27,5289 | 26,0 | Exxaro [B22]; Wikipedia [B23] | Wikipedia-geohack | aannemelijk |
| `w-cerrejon` | Cerrejón | Colombia | mijn | 11,1207, -72,5596 | 19,2 | Glencore FY2024/2025 [B24]; Argus [B25] | anker `coal-cerrejon-laad` hergebruikt | **bron-gelegd** |
| `w-tavantolgoi` | Tavan Tolgoi (ETT) | Mongolië | mijn | 43,625, 105,474 | 28,64 | Erdenes TT 2024 [B26][B27] | Wikipedia-geohack | aannemelijk |
| `w-taldinsky` | Taldinsky (+ -Zapadny) | Rusland (Kuzbass) | mijn | 54,1943, 87,1387 | 9,1 | GEM GCMT (deelblok) [B1]; mediaberichten [B28] | GEM Table 1 (één van drie secties) | **onzeker** |
| `w-elga` | Elga (Elginskiy) | Rusland (Jakoetië) | mijn | 56,1994, 130,6358 | 28,6 | TASS 2024/2025 [B29][B30] | Wikipedia-geohack | aannemelijk |
| `w-bogatyr` | Bogatyr | Kazachstan | mijn | 51,6555, 75,4336 | 32,53 | GEM GCMT 2024 [B1]; Times of Central Asia [B31] | GEM Table 1 | aannemelijk |
| `w-eldescanso` | El Descanso (Drummond) | Colombia | mijn | 9,7051, -73,5232 | 21,7 | GEM GCMT 2024 [B1] | GEM Table 1 | aannemelijk |
| `w-elkview` | Elkview | Canada (BC) | mijn | 49,7522, -114,8772 | 9,0 | Wood Mackenzie/media [B32]; Glencore/Teck [B33] | Wikipedia-geohack | aannemelijk |
| `w-qinhuangdao` | Qinhuangdao | China | exportterminal (binnenlands) | 39,945, 119,688 | 200,0 | Wikipedia [B34]; Wood Mackenzie [B35] | verschoven n.a.v. satelliet naar zichtbare stockyards | aannemelijk |
| `w-huanghua` | Huanghua | China | exportterminal (binnenlands) | 38,345, 117,775 | 214,4 | Mysteel 2024 [B36]; CSEC [B37] | verschoven n.a.v. satelliet naar zichtbare stockpiles | aannemelijk |
| `w-caofeidian` | Caofeidian | China | exportterminal (binnenlands) | 38,9333, 118,5333 | 150,0 | GEM Caofeidian Coal Terminal [B38]; steelorbis [B39] | Chinese kaartbronnen; satelliet: <500 m van kade | **bron-gelegd** |
| `w-ganqimaodu` | Ganqimaodu | China/Mongolië-grens | grensovergang (landhub) | 42,4017, 107,5667 | 45,0 | sxcoal 2024/2025 [B40]; Mining Insight [B41] | Wikidata/kaartbronnen | aannemelijk |
| `w-newcastle` | Newcastle (PWCS Kooragang) | Australië (NSW) | exportterminal | -32,8772, 151,7732 | 120,0 | PWCS [B42]; NCIG Sustainability Report [B43] | GEO-coördinaat | **bron-gelegd** |
| `w-dalrymplebay` | Hay Point / Dalrymple Bay | Australië (Qld) | exportterminal | -21,2848, 149,2837 | 85,0 | Dalrymple Bay Infrastructure [B44]; GEM [B45] | GEO-coördinaat | **bron-gelegd** |
| `w-richardsbay` | Richards Bay (RBCT) | Zuid-Afrika | exportterminal | -28,818, 32,052 | 91,0 | RBCT/mining.com [B46]; miningweekly [B47] | Wikipedia-geohack | **bron-gelegd** |
| `w-tanjungbara` | Tanjung Bara (KPC) | Indonesië | exportterminal | 0,5860, 117,7037 | 38,1 | media [B48]; KPC [B49] | GEM/Wikipedia-geohack | aannemelijk |
| `w-mundra` | Mundra — West Basin | India (Gujarat) | importterminal | 22,7385, 69,7061 | 60,0 | Adani Ports [B50][B51] | algemene havencoördinaat, niet West Basin-specifiek | **onzeker** |
| `w-dhamra` | Dhamra | India (Odisha) | importterminal | 20,8233, 86,9628 | 60,0 | Adani Ports [B52]; constructionworld [B53] | Wikipedia-geohack | aannemelijk |
| `w-puerto-drummond` | Puerto Drummond | Colombia | exportterminal | 11,95, -74,3812 | 60,0 | Drummond Ltd [B54]; GEM [B55] | UNIS-coördinaat | aannemelijk |
| `w-rotterdam` | Rotterdam — EMO | Nederland | importterminal | 51,9411, 4,0535 | 60,0 | HES/EMO [B56]; Port of Rotterdam [B57] | anker `coal-rotterdam-kade` hergebruikt | **bron-gelegd** |
| `w-vostochny` | Vostochny | Rusland | exportterminal | 42,7625, 133,0514 | 58,0 | portnews.ru [B58]; GEM [B1] | mediaberichten | aannemelijk |
| `w-tuoketuo` | Tuoketuo (Datang Togtoh) | China (Binnen-Mongolië) | centrale | 40,1969, 111,3644 | 11,7 (afgeleid) | afgeleid uit MW/TWh [B59]; GEM/power-technology [B60] | Wikipedia-geohack | aannemelijk |
| `w-vindhyachal` | Vindhyachal (NTPC) | India (Madhya Pradesh) | centrale | 24,0972, 82,6736 | 17,1 (fase I-III) | NTPC/CERC [B61]; GEM/power-technology [B62] | Wikipedia-geohack | aannemelijk |
| `w-kalinganagar` | Tata Steel Kalinganagar | India (Odisha) | staalfabriek | 20,9458, 86,1292 | 2,1 (cokeskool) | Mysteel/Hellenic Shipping [B63]; Tata Group [B64] | Wikipedia-geohack | aannemelijk |
| `w-duisburg` | Duisburg — Schwelgern | Duitsland | cokerij | 51,5132, 6,7235 | 3,5 (afgeleid) | afgeleid uit cokescapaciteit [B65]; brief kolen-cerrejon-ruhr [B66] | anker `coal-duisburg-kade` hergebruikt | **bron-gelegd** |

*(Coördinaatkolom toont lat, lon zoals in de json; bij `w-narm` staat de oorspronkelijke GEM-waarde en de
na-satelliet verschoven waarde ter vergelijking.)*

## Satellietbevindingen (top-6 mijnen + top-6 terminals)

- **North Antelope Rochelle** (VS): GEM's Table-1-coördinaat (43,56667/-105,28333) ligt ~2 km zuidelijk van
  de zichtbare wingaten/haldes op Esri z14. Verschoven naar de zuidrand van het noordelijke bekken
  (43,588/-105,283) — nog steeds niet midden op een bank, dus status blijft **aannemelijk**, niet
  bron-gelegd.
- **Gevra OC** (India): kruis ligt op de rand van het wingat, terrasvormige excavatie rondom duidelijk
  zichtbaar. **Bron-gelegd.**
- **Kusmunda OC** (India): kruis in de wingatrand, pitmeren en terrassen aan weerszijden, overslagterrein
  direct noordelijk. **Bron-gelegd.**
- **KPC Sangatta** (Indonesië): kruis op een smalle landtong tussen twee pitmeren, midden in het
  KPC-mijncomplex — bewolking rondom maar de directe omgeving is scherp. **Bron-gelegd.**
- **Borneo Indobara** (Indonesië): kruis ligt in dicht regenwoud zonder mijnactiviteit direct eronder; op
  2-4 km liggen wél ontginningen zichtbaar, passend bij de 24.100 ha grote concessie. GEM markeert deze
  coördinaat zelf als *"(approximate)"* — dat is nu bevestigd. **Onzeker**, coördinaat niet verschoven
  (geen eenduidig alternatief zichtbaar binnen het beeld).
- **Bara Tabang** (Indonesië): kruis op de rand van het wingat, processing-plant met rookpluim direct
  zuidelijk. **Bron-gelegd.**
- **Huanghua** (China): geen enkele gepubliceerde coördinaat wees naar land — een eerste poging
  (38,60/117,85) viel middenin de Bohai-zee. Een tweede (Baidu-afgeleide) poging op 38,3333/117,8833 viel
  in het vaarwater, ~600 m van de kade met duidelijk zichtbare donkere kolenstockpiles. Verschoven naar
  38,345/117,775, op de rand van die stockpiles. **Aannemelijk** (verschoven, niet exact op de kade zelf).
- **Qinhuangdao** (China): eerste poging (havencentroïde) trof een kleine jachthaven, geen kolen zichtbaar.
  Verschoven ~4 km NO naar een duidelijk zichtbaar rechthoekig rooster van donkere kolenstockyards.
  **Aannemelijk** (verschoven, niet millimeter-precies op één stapel).
- **Caofeidian** (China): kruis ligt net in het water, direct naast rijen donkere stockpiles en een
  kolenkade — binnen ~500 m van de terminal. **Bron-gelegd.**
- **Newcastle — Kooragang (PWCS)** (Australië): kruis midden op de lange evenwijdige kolenstockpiles,
  shiploaders aan de kade duidelijk zichtbaar. **Bron-gelegd.**
- **Dalrymple Bay / Hay Point** (Australië): kruis midden op de stockyard, twee lange laadsteigers met
  shiploaders de baai in. **Bron-gelegd.**
- **Richards Bay (RBCT)** (Zuid-Afrika): kruis midden op de grote donkere kolenstockpile, spoorbundel en
  kade direct zichtbaar. **Bron-gelegd.**

Van de twaalf sat-passes: **7 bron-gelegd**, **4 aannemelijk (verschoven)**, **1 onzeker**.

## Capaciteiten voor China-registersites

Niet van toepassing deze ronde. Anders dan bij koper is voor de Chinese kolensites in deze lijst géén
apart MEE-registerrecept gebruikt — GEM's Global Coal Mine Tracker geeft voor elke Chinese mega-mijn al
een zelfstandige, visueel gelegde coördinaat + productiecijfer, dus er is geen aparte
`china_capaciteiten`-korting nodig zoals bij koper (waar smelter-onderdelen alleen via het
vergunningregister traceerbaar waren). Wordt in een latere ronde een echte Chinese registerlaag voor kolen
gebouwd (GEM's rapport *"China's Coal Conundrum"*, 81 mega-mijnen ≥ 10 Mt/j), dan hoort die als aparte
sectie hier bij.

## Buiten scope

| kandidaat | reden |
|---|---|
| Zhundong South Surface Mine (Wucaiwan No. 3, Xinjiang, China) | Geen site-niveau coördinaat gevonden — alleen een county-centroïde (Jimsar, 43,983/89,067) uit Wikipedia. Een county-centroïde is geen anker (vaste regel). Wél in de kandidatenlijst van het ontwerp genoemd (~40 Mt/j) — blijft open voor een volgende ronde met een gerichte OSM/Baidu-zoekactie. |
| Pribbenow / La Loma (Drummond, Colombia) | Zelfde eigenaar en dezelfde 193 km-spoorlijn naar Puerto Drummond als het wél opgenomen El Descanso; productie ingestort naar 3,86 Mt (2024) tegen 21,7 Mt bij El Descanso. Twee bijna-identieke Drummond-ankers op 6 km van elkaar voegen weinig toe aan een lichte ronde — El Descanso draagt de as. |
| Energy Resources/UHG-concessie (Tavan Tolgoi, Mongolië) | Alleen de Erdenes-Tavan-Tolgoi-helft van het veld is hier genomen; de andere, eveneens grote concessie is een apart mijnbouwbedrijf op hetzelfde veld en is deze ronde niet onderzocht. |
| Kideco-zusterconcessies, Indominco, Gevra-Zuid/Kusmunda-Zuid, Heilongjiang/Shaanxi-mega-mijnen (Yulin, Shenmu) | Evident groot genoeg om mee te tellen, maar binnen de tijdbox van deze lichte ronde niet onderzocht — geen aanwijzing dat de lijst zonder hen structureel scheef is, wel dat hij niet uitputtend is. |
| Firecrawl-gebaseerd onderzoek (satellietstitching via de gebruikelijke scrape-tool) | Firecrawl-credits waren deze sessie uitgeput; alle research liep via `WebSearch`/`WebFetch`. Werkte, maar leverde vaker een samengevatte infobox dan de ruwe brontabel — waar dat tot een zwakkere bron leidde staat het expliciet in `coord_bron`/`capaciteit_bron`. |

## Open punten

- **Drie sites met status `onzeker`**: Borneo Indobara (satelliet toont geen mijn onder het kruis),
  Taldinsky (coördinaat dekt met zekerheid maar één van drie secties, cijfers tussen bronnen lopen sterk
  uiteen), Mundra West Basin (coördinaat is de algemene havenlocatie, niet het specifieke terminalblok).
  Deze drie horen bij de eerstvolgende scherpere ronde als eerste aan de beurt.
- **Vier sites dragen een afgeleid, niet rechtstreeks gepubliceerd Mt-cijfer** (Tuoketuo, Vindhyachal,
  Kalinganagar, Duisburg) — zie `eenheid_site` in de json. Bij het bakken van de gloedlaag moeten deze vier
  ofwel apart gewogen worden, ofwel bewust licht meetellen; ze zijn geen mijnproductie.
- **Geen Chinese registerlaag gebouwd** (zie boven) — bij een latere, zwaardere ronde is GEM's
  *"China's Coal Conundrum"*-rapport (81 mega-mijnen) de aangewezen bron, net zoals het MEE-register bij
  koper.
- **`voeg_sites_toe.py` is hard-coded op koper** (`SITELAAG=design/koper-sitelaag.json`,
  `GLOED=data/gloednodes-koper.json`) — dit bestand kan pas in de gloedlaag landen nadat het centrale
  voorwerk uit de M29-oordeelsnotitie is gedaan (`--grondstof`/`--sitelaag`-parameter + laadpad in
  `main.js` + genormaliseerd gewicht per grondstof, want Mt kolen/j is 10-100× kt Cu/j). Dat gebeurt
  centraal — dit rapport levert alleen de brondata.
- **Geen enkele Russische of Kazachse mijn is satelliet-gelegd** deze ronde (Taldinsky, Elga, Bogatyr) —
  alle drie op basis van gepubliceerde coördinaten zonder eigen visuele check.

## Bronnen

- **[B1]** Global Energy Monitor, Global Coal Mine Tracker (GCMT) — gem.wiki, diverse mijnpagina's,
  releases 2023-2026 (CC BY 4.0) — https://www.gem.wiki/Global_Coal_Mine_Tracker
- **[B2]** Peabody Energy, North Antelope Rochelle Mine — https://www.peabodyenergy.com/Operations/U-S-Mining/Powder-River-Basin-Mining/North-Antelope-Rochelle-Mine
- **[B3]** Wikipedia, 'Black Thunder Coal Mine' — https://en.wikipedia.org/wiki/Black_Thunder_Coal_Mine
- **[B4]** PIB/Ministry of Coal (juli 2024), 'Atmanirbhar Bharat: Two of the World's Five Largest Coal Mines Now in India' — https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2034007
- **[B5]** drishtiias, 'Gevra and Kusmunda Among World's Largest Coal Mines' — https://www.drishtiias.com/daily-updates/daily-news-analysis/gevra-and-kusmunda-among-world-s-largest-coal-mines
- **[B6]** Coal Controller's Organisation, 'Dipka OCP SECL' — https://coalcontroller.gov.in/dipka-ocp-secl
- **[B7]** IndianPSU, 'SECL's Dipka OCP: Record Coal Production' — https://indianpsu.com/secl-dipka-ocp-record-coal-production-60-mtpa/
- **[B8]** PT Kaltim Prima Coal / Bumi Resources, jaarcijfers 2024 — https://bumiresources.com/en/about-us/subsidiaries/detail/kaltim-prima-coal
- **[B9]** Golden Energy Mines, 'Coal Mining in Indonesia' (Borneo Indobara-cijfers) — https://www.goldenenergymines.com/2025/10/24/coal-mining-in-indonesia-opportunities-challenges-and-the-future/
- **[B10]** Bayan Resources, 'Tabang/Pakar Mine' — https://www.bayan.com.sg/tabang-pakar-mine
- **[B11]** PT Bukit Asam (Persero) — https://www.indonesia-investments.com/business/indonesian-companies/tambang-batubara-bukit-asam/item233
- **[B12]** sxcoal, 'Adaro aims for 67 Mt coal production in 2024' — https://en.sxcoal.com/news/detail/1764474024411443202
- **[B13]** Indika Energy, Energy-divisie (Kideco-cijfers 2024) — https://www.indikaenergy.co.id/business/energy/
- **[B14]** Mining Digital, 'Haerwusu (China)' — https://miningdigital.com/top10/haerwusu-china
- **[B15]** EJAtlas, 'Haerwusu coal mine, Inner Mongolia' — https://ejatlas.org/conflict/haerwusu-coal-mine-inner-mongolia-china
- **[B16]** PMC/wetenschappelijke publicatie, 'Evolution of Landscape Patterns... Heidaigou Mining Area' — https://pmc.ncbi.nlm.nih.gov/articles/PMC10001789/
- **[B17]** CSEC/Zhunneng Group, Heidaigou industrieel erfgoed — http://www.csec.com/zgshwwEn/jtyw/202412/03d24c3f2c7e4cd68da62a6625721737.shtml
- **[B18]** Wikipedia, 'Goonyella Riverside Mine' — https://en.wikipedia.org/wiki/Goonyella_Riverside_Mine
- **[B19]** BHP, 'Goonyella Riverside' — https://www.bhp.com/what-we-do/global-locations/australia/queensland/goonyella-riverside
- **[B20]** NS Energy, 'Peak Downs Coal Mine' — https://www.nsenergybusiness.com/projects/peak-downs-coal-mine-queensland/
- **[B21]** BHP, 'Mt Arthur, New South Wales' — https://www.bhp.com/what-we-do/global-locations/australia/nsw-mt-arthur-coal-mine-hunter-valley
- **[B22]** Exxaro, Operations — https://www.exxaro.com/operations/
- **[B23]** Wikipedia, 'Grootegeluk Coal Mine' — https://en.wikipedia.org/wiki/Grootegeluk_Coal_Mine
- **[B24]** Glencore, Full Year 2024/2025 Production Reports — https://www.glencore.com/media-and-insights/news/full-year-2025-production-report
- **[B25]** Argus Media, 'Cerrejón to cut coal production by 5mn-10mn t in 2025' — https://www.argusmedia.com/en/news-and-insights/latest-market-news/2671317-cerrejon-to-cut-coal-production-by-5mn-10mn-t-in-2025
- **[B26]** Erdenes Tavan Tolgoi JSC, 2024-productiecijfers — https://projects.gbreports.com/mongolia-mining-2024/erdenes-tavan-tolgoi-interview
- **[B27]** Erdenes Tavan Tolgoi, reserve-update sept 2024 — https://mongoliainc.com/key-commodities/coal/
- **[B28]** The Coal Hub, 'KRU company buys 100% of Taldinsky-Zapadny open-pit mine' — https://thecoalhub.com/kru-company-buys-100-of-taldinsky-zapadny-open-pit-mine.html
- **[B29]** TASS, "Yakutia's Elga field to produce about 30 million tons of coal" — https://tass.com/economy/1960451
- **[B30]** TASS, 'Elga produces 18 mln tons of coal in 1H 2025' — https://tass.com/economy/2011317
- **[B31]** Times of Central Asia, "Kazakhstan's Largest Coal Mine to Increase Production from 2026" — https://timesca.com/kazakhstans-largest-coal-mine-to-increase-production-from-2026/
- **[B32]** Wood Mackenzie, 'Elkview coal mine Report' — https://www.woodmac.com/reports/coal-elkview-coal-mine-16475301/
- **[B33]** Wikipedia, 'Elkview coal mine' (Teck/Glencore-overdracht juli 2024) — https://en.wikipedia.org/wiki/Elkview_coal_mine
- **[B34]** Wikipedia, 'Port of Qinhuangdao' — https://en.wikipedia.org/wiki/Qinhuangdao_Port
- **[B35]** Wood Mackenzie, "China's Qinhuangdao port halves daily coal throughput" — https://www.woodmac.com/reports/coal-chinas-qinhuangdao-port-halves-daily-coal-throughput-29153
- **[B36]** Mysteel, 'CNH Energy Huanghua port's 2024 coal throughput exceeds 200 mln t' — https://www.mysteel.net/news/5070620-cnh-energy-huanghua-ports-2024-coal-throughput-exceeds-200-mln-t
- **[B37]** CSEC, Company Profile (Huanghua-havenexploitant) — http://www.csec.com/zgshwwEn/gsjj/gsjjList.shtml
- **[B38]** Global Energy Monitor, 'Caofeidian Coal Terminal' — https://www.gem.wiki/Caofeidian_Coal_Terminal
- **[B39]** steelorbis, 'Annual iron ore handling capacity of Caofeidian Port to reach 100 million mt' — https://www.steelorbis.com/steel-news/latest-news/annual-iron-ore-handling-capacity-of-caofeidian-port-to-reach-100-million-mt-682291.htm
- **[B40]** sxcoal, "China's Ganqimaodu imports 11.85 Mt of coal as of May 6" (2025) — https://en.sxcoal.com/news/detail/1914939225133400065
- **[B41]** Mining Insight (Mongolië), 'Ganqimaodu border: China imported 12.09 million tonnes coal from Mongolia' — https://en.mininginsight.mn/index.php?newsid=243
- **[B42]** Port Waratah Coal Services — https://pwcs.com.au/what-we-do/kooragang-coal-terminal/
- **[B43]** NCIG, Sustainability Report 2024 — https://ncig.com.au/wp-content/uploads/2024/10/NCIG-Sustainability-Report-2024.pdf
- **[B44]** Dalrymple Bay Infrastructure, Terminal Overview — https://dbinfrastructure.com.au/dalrymple-bay-terminal/terminal-overview/
- **[B45]** Global Energy Monitor, 'Dalrymple Bay Coal Terminal' — https://www.gem.wiki/Dalrymple_Bay_Coal_Terminal
- **[B46]** mining.com, "S.Africa's Richards Bay exports up 10% in 2024" — https://www.mining.com/web/s-africas-richards-bay-exports-up-10-in-2024-amid-rail-improvement/
- **[B47]** Mining Weekly, 'Richards Bay Coal Terminal 2024 exports extend beyond 52-million tons' — https://www.miningweekly.com/article/richards-bay-coal-terminal-2024-exports-extend-beyond-52-million-tons-2025-01-24
- **[B48]** SeaRates/dredgepoint, Tanjung Bara Coal Terminal — https://dredgepoint.org/dredging-database/ports/tanjung-bara-coal-terminal
- **[B49]** PT Kaltim Prima Coal, Operations — https://www.kpc.co.id/what-we-do/operations/
- **[B50]** Adani Ports, 'Mundra Port' — https://www.adaniports.com/ports-and-terminals/mundra-port
- **[B51]** Adani Enterprises, Operational Performance — Ports 2025/26 — https://www.adaniports.com/digital-reports/ports/2026/operational-performance-ports.html
- **[B52]** Adani Ports, 'Dhamra Port' — https://www.adaniports.com/ports-and-terminals/dhamra-port
- **[B53]** Construction World, 'Odisha Handles Record 187,000 Tonnes Coking Coal at Dhamra Port' — https://www.constructionworld.in/transport-infrastructure/ports-and-shipping/odisha-handles-record-187-000-tonnes-coking-coal-at-dhamra-port/76564
- **[B54]** Drummond Ltd, 'Puerto Drummond' — https://drummondltd.com/en/our-operations/the-port/puerto-drummond/
- **[B55]** Global Energy Monitor, 'Puerto Drummond coal port' — https://www.gem.wiki/Puerto_Drummond_coal_port
- **[B56]** HES International, 'EMO Dry Bulk terminal — Rotterdam' — https://www.hesinternational.eu/emo
- **[B57]** Port of Rotterdam, 'Coal' — https://www.portofrotterdam.com/en/logistics/cargo/dry-bulk/coal
- **[B58]** portnews.ru, 'Vostochny Port to increase its throughput capacity to 70 million tonnes' — https://en.portnews.ru/news/324814/
- **[B59]** Wikipedia, 'Tuoketuo Power Station' (33,317 TWh/jaar) — https://en.wikipedia.org/wiki/Tuoketuo_Power_Station
- **[B60]** power-technology, 'Power plant profile: Tuoketuo Power Plant, China' — https://www.power-technology.com/data-insights/power-plant-profile-tuoketuo-power-plant-china/
- **[B61]** NTPC/CERC, Vindhyachal O&M-gegevens — https://cercind.gov.in/2018/draft_reg/O&M_data/Generation%20Data/NTPC/Vindhyachal.pdf
- **[B62]** power-technology, 'Power plant profile: Vindhyachal Super Thermal Power Station, India' — https://www.power-technology.com/data-insights/power-plant-profile-vindhyachal-super-thermal-power-station-india/
- **[B63]** Hellenic Shipping News, "Tata Steel's new coke plant unlikely to spur Indian met coal demand in 2024" — https://www.hellenicshippingnews.com/tata-steels-new-coke-plant-unlikely-to-spur-indian-met-coal-demand-in-2024/
- **[B64]** Tata Group, 'India's Largest Blast Furnace Commissioned' (Kalinganagar) — https://www.tata.com/newsroom/business/tata-steel-kalinganagar-india-largest-blast-furnace
- **[B65]** thyssenkrupp Industrial Solutions, 'The new Schwelgern coke plant' — https://ucpcdn.thyssenkrupp.com/_legacy/UCPthyssenkruppBAIS/assets.files/products___services/coke_plants/tkis_schwelgern_coke_plant.pdf
- **[B66]** `v2/design/routebrieven/kolen-cerrejon-ruhr.md` (interne brief, Schwelgern-kade totaal erts+kolen ±23 Mt/j)

Coördinaatbronnen: Global Energy Monitor Global Coal Mine Tracker (CC BY 4.0), Wikipedia (geohack via de
MediaWiki-API `prop=coordinates`), Wikidata, bedrijfswebsites/-rapportages, Chinese kaartbronnen (Baidu)
voor Huanghua/Caofeidian; Esri World Imagery via `v2/tools/sat_check.py` voor de twaalf satellietchecks.

## Openstaande werkwijze-notitie

Deze ronde week op één punt af van de koper-sitelaag-werkwijze: **Firecrawl (`firecrawl_scrape`/
`firecrawl_search`) had geen credits meer** aan het begin van de sessie. Alle coördinaat- en
capaciteitsresearch liep in plaats daarvan via `WebSearch` en `WebFetch` rechtstreeks op gem.wiki- en
Wikipedia-pagina's. Dat gaf bruikbare resultaten, maar de tool vat de infobox samen in plaats van de ruwe
tabel te tonen — bij een paar sites (Zhundong, Mundra West Basin) leverde dat geen bruikbare coördinaat op
waar een directe scrape dat mogelijk wel had gedaan. Wie deze laag verdiept, kan die twee het eerst
opnieuw proberen zodra Firecrawl weer credits heeft.
