# Routebrief (licht) · gas — Hides/Caution Bay (Papoea-Nieuw-Guinea) → Futtsu (Japan)

**stroom-id:** `gas-cautionbay-futtsu` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** Aardgas uit het Hides-gasveld (Southern Highlands) wordt bij Hides geconditioneerd en
via een ~700 km lange, in OSM vrijwel niet gekarteerde pijpleiding (onshore + offshore door de Golf van
Papoea) naar de PNG LNG-plant bij Caution Bay gebracht, verwerkt tot LNG en vaart als LNG-tanker via de
Filipijnenzee naar de Futtsu LNG-terminal (JERA) in Tokiobaai — de eerste as van de atlas in een volledig
nieuwe regio (Papoea-Nieuw-Guinea).
**Welke as van het verhaal:** PNG LNG (ExxonMobil-operator) produceerde in het ontwerpjaar een nameplate van
6,9 Mtpa maar draaide de jaren daarna structureel boven plan (8,3 Mtpa in 2017, 8,5 Mtpa in 2019) [2][7]; de
oorspronkelijke (2010) afnemerscontracten noemen JERA/Tokyo Electric Power Company en Osaka Gas naast Sinopec
en CPC Taiwan [2] — het Japan-aandeel van de huidige lading naar Futtsu specifiek is dit sessie niet los
gebrond (§7), vandaar "aannemelijk: één bron" op het eindpunt.

## 1 · Ketenkaart
```
Hides-gasveld `gas-cbf-hides` (Southern Highlands, PNG)
   ──(b1 leiding · ~700 km onshore+offshore door de Golf van Papoea, stippel)──►
   PNG LNG-plant, Caution Bay `gas-cbf-plant` (ExxonMobil, Central Province)
   ──(b2 zee · Golf van Papoea → Coral Sea/Bismarckzee → Filipijnenzee (Luzon/Taiwan) →
       Oost-Chinese Zee → Tokiobaai · ~5.000+ km, MARNET, haven-aanloop BEIDE uiteinden)──►
   Futtsu LNG-terminal `w-futtsu` (JERA, Tokiobaai) — stoppunt: regasificatie + invoeding
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A/B | leiding | Hides-gasveld → PNG LNG-plant Caution Bay | Hides Gas Conditioning Plant → onshore-tracé → offshore-tracé Golf van Papoea | ~700 (ExxonMobil, "approximately 700-kilometers of onshore and offshore pipeline" [6]; ≈292 km onshore + 407 km offshore volgens onafhankelijke bron [9]) | stippel (rechte lijn) | ja — subsea/onshore trunkline, in de PNG-Geofabrik-extract vrijwel niet gekarteerd (112 `man_made=pipeline`-ways, precies 1 met `substance=gas`, 3 nodes, ongenoemd) [ontwerp/haalbaarheidstoets, bevestigd] |
| b2 | C | zee | PNG LNG-plant Caution Bay → Futtsu-terminal | Golf van Papoea → Coral Sea/Bismarckzee → Filipijnenzee (Luzon/Taiwan) → Oost-Chinese Zee → Tokiobaai | hemelsbreed ~5.026, geen scheepvaart-kilometrage gevonden | MARNET (kade → kade) | nee, maar met **haven-aanloop op BEIDE uiteinden** (§7) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-cbf-hides` | laadplek / gasveld-conditioneringsplant | Hides Gas Conditioning Plant | -6.0050, 142.8100 | [1][3][8] | bron-gelegd (z14 gezien: een ontgonnen terreincluster met gebouwen/opslag en een toegangsweg te midden van regenwoud, exact op de Wikipedia-coördinaat van het Hides-gasveld) |
| `gas-cbf-plant` | overslag leiding→zee / LNG-laadkade | PNG LNG-plant, Caution Bay | -9.3417, 147.0231 | [2][6][8] | bron-gelegd (z15 gezien: het LNG-fabrieksterrein met procestrains, opslagtanks en een steiger aan de kust; het punt zelf valt binnen de omheinde site tussen de procestrains en het kantorencomplex, deels onder wolkendek) |
| `w-futtsu` | losplek zee/leiding, regas-terminal + invoeding (JERA) | Futtsu LNG-terminal (JERA/Tokyo Electric) | 35.3424, 139.8322 | Hergebruikt letterlijk uit `v2/design/gas-sitelaag.json` (id `w-futtsu`) | aannemelijk (coördinaat overgenomen: OSM landuse `富津火力発電所`, benoemd object op hetzelfde complex; geen eigen satellietblik deze ronde — zie sitelaag) |

## 4 · Via-punten
Geen — b1 is een ongekarteerde stippel zonder corridorkeuze (rechte lijn, geen net om op te
snappen); b2 routeert kade → kade over MARNET.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| PNG LNG-plant, Caution Bay | ExxonMobil PNG Limited (operator) / PNG LNG-joint venture | pijpleidinggas (Hides) → LNG | 6,9 Mtpa nameplate-ontwerp, feitelijk 7,4–8,5 Mtpa (2017–2021) ≈ **±8,3 Mtpa ≈ 11,3 bcm/j** (1 Mt LNG ≈ 1,36 bcm) | [2][7] |
| Futtsu LNG-terminal + centrale | JERA/Tokyo Electric | LNG → hervergast pijpleidinggas → Kanto-net/centrale | niet in deze brief gebrond (§7) | sitelaag [w-futtsu] |

## 6 · Stoppunt
De brief stopt bij de Futtsu-terminal (regasificatie + invoeding in het Kanto-gasnet/de JERA-centrale):
Futtsu is een bestaand, letterlijk hergebruikt sitelaag-anker (status *aannemelijk*) en geen bron koppelt een
specifieke PNG LNG-lading aan specifiek Futtsu — wel zijn Japanse nutsbedrijven (voorgangers van JERA) sinds
2010 contractueel afnemer van PNG LNG in het algemeen [2]. Fase D/E (gas vanaf de centrale verder het net in)
vervalt: geen bron benoemt een specifieke fabriek stroomafwaarts.

## 7 · Open punten
- **Geen site-anker voor het exacte pijpleidingtracé (b1).** Het ~700 km-tracé Hides→Caution Bay is subsea
  (offshore door de Golf van Papoea) en grotendeels onshore-bos; de PNG-Geofabrik-extract (53,6 MB) is
  gescand met pyosmium: 112 `man_made=pipeline`-ways totaal, waarvan precies 1 (3 nodes, ongenoemd)
  `substance=gas` draagt [haalbaarheidstoets, bindend]. Stippel is de bevestigde uitkomst — dit ene been
  alleen maakt de keten niet grotendeels-stippel, want de zeeroute (~5.000+ km) is verreweg het grootste
  deel van de totale lengte (vergelijk Bingham Canyon → Garfield, dat wél 100% stippel werd en is afgewezen).
- **Beide zee-uiteinden liggen ver van hun MARNET-zeeknoop (bindend, haalbaarheidstoets, eigen meting met het
  voorgeschreven recept):** Caution Bay **39,3 km** — buiten het normale 25 km max-snap-bereik — en Futtsu
  **12,1 km**. Op BEIDE uiteinden is een haven-aanloop verplicht, ook al snapt Futtsu binnen de 25 km-grens
  (LAR-586: een kade > 5 km van de zeeknoop krijgt sowieso een aanloop). Reken bij Caution Bay op een
  reëel risico op hangen gezien de grote afstand — `maak_havenaanloop.py` met `timeout 300` en een
  rechte-stippel-terugval klaarzetten (bakhandleiding §2, het Hamburg/Ras Laffan-precedent).
- **Futtsu als specifieke bestemming blijft "aannemelijk: één bron".** De 2010-contracten noemen JERA (voor
  Tokyo Electric Power Company) en Osaka Gas als afnemers van PNG LNG in het algemeen [2]; geen bron in deze
  of de vorige onderzoeksronde (webcheck in de haalbaarheidstoets) koppelt een specifieke PNG-lading aan
  specifiek de Futtsu-terminal — maar er is ook geen tegenbewijs. Het Futtsu-anker zelf is letterlijk
  hergebruikt uit de sitelaag (status *aannemelijk* daar al, geen eigen satellietronde deze sessie).
- **Exact Japan-aandeel/cargovolume niet gebrond** — alleen het Qatar/PNG-projecttotaal (§0) is bekend; geen
  bron koppelt een specifiek volume aan deze ene as (zelfde klasse als de andere gas-Japan-brieven).
- **Pijpleidinglengte: twee net iets verschillende bronopgaven.** ExxonMobil's eigen corporate-pagina noemt
  "approximately 700-kilometers of onshore and offshore pipeline" [6]; een onafhankelijke bron geeft
  292 km onshore + 407 km offshore = 699 km [9]. Beide liggen binnen 1% van elkaar en binnen ±15% van de
  ontwerp-indicatie (692 km); geen widerspruch die verder onderzoek vraagt.

## 8 · Bronnen
[1] Wikipedia, "Hides gas field" — coördinaat -6,0050/142,8100 (exact, via Wikidata-coördinaat), ontdekt
    1987 door BP, ontwikkeld door ExxonMobil, productie sinds 1988, bewezen reserves ~7,1 Tcf.
    https://en.wikipedia.org/wiki/Hides_gas_field
[2] Wikipedia, "Natural gas in Papua New Guinea" — pijpleidingroute (450 km onshore tot de monding van de
    Omati-rivier + 407 km offshore naar Caution Bay), 2010-afnemerscontracten (JERA/Tokyo Electric Power
    Company, Osaka Gas, Sinopec, CPC Taiwan), productiecijfers 2017–2021 (6,9 Mtpa nameplate, 8,3–8,5 Mtpa
    feitelijk). https://en.wikipedia.org/wiki/Natural_gas_in_Papua_New_Guinea
[3] Wikidata — coördinaat Hides-gasveld, gebruikt als kruiscontrole op [1].
[4] Wikipedia, "PNG LNG" (doorverwezen naar "Liquid Niugini LNG") — een vroeg, ander
    InterOil-geleid ontwerp voor hetzelfde gasveld; niet het huidige ExxonMobil PNG LNG-project, alleen ter
    context van de projectgeschiedenis. https://en.wikipedia.org/wiki/Liquid_Niugini_LNG
[5] GEM.wiki, "PNG LNG Terminal" — genoemd in het ketenontwerp als bronstartpunt; site laadde deze sessie
    geen doorzoekbare tekst op (JS-gerenderd), niet los geverifieerd. https://www.gem.wiki/PNG_LNG_Terminal
[6] ExxonMobil, corporate operations-pagina Papoea-Nieuw-Guinea — "approximately 700-kilometers of onshore
    and offshore pipeline" Hides → Caution Bay, operator-bevestiging. https://corporate.exxonmobil.com/locations/papua-new-guinea/operations
[7] pnglng.com — projectwebsite ExxonMobil PNG Limited, genoemd in het ketenontwerp als bronstartpunt.
    https://pnglng.com
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15) — `sat-gas-cautionbay-futtsu-hides.png`,
    `sat-gas-cautionbay-futtsu-cautionbay.png`.
[9] Websearch-synthese (ExxonMobil PNG LNG-projectmateriaal, GEM.wiki PNG LNG Pipeline) — 292 km onshore
    (32") + 407 km offshore (36") = 699 km totaal, offshore-tracé ~24 km voorbij Goaribari Island de open
    zee op, dan de Golf van Papoea over naar de landing bij Caution Bay.
[10] `v2/design/gas-sitelaag.json` — anker `w-futtsu` (35,3424/139,8322), letterlijk hergebruikt, status
    aannemelijk; oorspronkelijke bron OSM/Photon `富津火力発電所`.
[11] Geofabrik OSM-extract `papoea-nieuw-guinea-latest.osm.pbf` (53,6 MB) — pyosmium-scan uit het
    haalbaarheidstoets-recept: 112 `man_made=pipeline`-ways, 1 met `substance=gas`.

## 9 · Bakresultaat (2026-09-28, lichte werkwijze, M31 golf 5)

**Totaal: 6.912,6 km · 688 punten · 4 benen · 3 markers.** Recept: `bash v2/tools/bak_stromen.sh
gas-cautionbay-futtsu` (functie `bak_gas_cautionbay_futtsu` in `v2/tools/bak_stromen.sh`, vlak vóór de
ankerregel). Geen profiel in `maak_stroombeen_weg.py` — deze keten heeft geen wegbeen.

| # | modaliteit | km | punten | stippel? | naam |
|---|---|---|---|---|---|
| 1 | leiding | 594,3 | 2 | ja (rechte lijn) | Hides→Caution Bay pijpleiding |
| 2 | zee | 48,2 | 34 | ja (haven-aanloop) | haven-aanloop Caution Bay |
| 3 | zee | 6.255,3 | 640 | nee | LNG-tanker Caution Bay → Futtsu |
| 4 | zee | 14,8 | 12 | ja (haven-aanloop) | haven-aanloop Futtsu |

**b1 (leiding, stippel, kop-staart, GEEN geometrie-bewijs).** Direct `--stippel` (geen geometrie-tool
nodig, precies zoals de bak-aanwijzingen voorschreven): rechte lijn Hides (-6,0050/142,8100) →
Caution Bay-plant (-9,3417/147,0231), 594,3 km. Dit is ~15% korter dan de gepubliceerde ~700 km
(ExxonMobil corporate / 292+407 km-synthese) — verwacht en INHERENT aan een schematische koorde die de
echte offshore-boog door de Golf van Papoea afsnijdt (bakhandleiding §9, "geen geometrie-bewijs, alleen
kop-staart"). `toets_rechte_benen.py` vlagt dit been terecht als 🟠 GROOT (factor 1,000) — bekend en
gedekt door de reden in de beennaam, net als de bestaande uranium-inkai-stippels van vergelijkbare lengte.

**b2/b4 (haven-aanlopen, BEIDE uiteinden, LAR-586).** Zeeknoop bepaald met het `marnet_zee`-recept uit
bakhandleiding §2: Caution Bay → zeeknoop 5906 (-9,60080/147,26620) op 39,3 km (buiten 25 km) · Futtsu →
zeeknoop 9066 (35,23890/139,79280) op 12,1 km (binnen 25 km, boven de 5 km-drempel). Beide
`maak_havenaanloop.py`-aanroepen SLAAGDEN binnen de `timeout 300` — geen terugval op een rechte stippel
nodig:
- Caution Bay: cel 0,01° kaal, 48,2 km · 34 punten · 2,46 km over land (alle bij het kade-uiteinde — een
  kade ligt per definitie óp de 1:10M-kustlijn, geen fout).
- Futtsu: cel 0,01° gebufferd, 14,8 km · 12 punten · 0,90 km over land (idem).
⚠️ **Les voor de volgende bak-agent:** `maak_havenaanloop.py --van <kade> --naar <zeeknoop>` schrijft de
punten in díe volgorde (kade → zeeknoop) — de bake plakt een `--stippel-geojson` letterlijk aan zoals
hij op schijf staat, zonder te reversen op reisvolgorde. Voor de Futtsu-aanloop (laatste been, dus
zeeknoop → kade in reisvolgorde) gaf de eerste poging daardoor een naad van 12,05 km tussen been 3 en 4;
opnieuw gebakken met `--van=<zeeknoop> --naar=<kade>` (dus in reisvolgorde) gaf naad 0,000 km. De
Caution Bay-aanloop had dit probleem niet, omdat die als tweede been (na de leiding, die al op de kade
eindigt) toevallig al in de juiste kade→zeeknoop-richting lag.

**b3 (hoofdzeebeen, MARNET kade→kade tussen de twee zeeknopen).** 6.255,3 km over 27 MARNET-edges, 640
punten, corridor Golf van Papoea → Coral Sea/Bismarckzee → Filipijnenzee (langs Luzon/Taiwan) →
Oost-Chinese Zee → Tokiobaai — geen Kaap-omweg, zoals verwacht. Dit is 24% meer dan de hemelsbrede
~5.026 km uit de brief; geen gepubliceerde scheepvaart-kilometrage om tegen te toetsen (brief §2/§7), dus
géén harde ±15%-toets — het verschil is de normale afwijking tussen grootcirkel en een werkelijke
vaarroute die rond eilanden buigt (zelfde klasse als gas-raslaffan-chiba). `toets_knikken.py`: 4 knikken
≥60° (krappe bochten bij eilandpassages in de Bismarckzee/Salomonszee, tot 116,3°), **0 omkeringen, 0
terugloop** — geen reparatie nodig.

**Toets (bakhandleiding §5).** Naden tussen alle vier de benen: **0,000 km** (na de richtingscorrectie
op b4). Markers: alle drie op **≤0,1 m** van de lijn. `json.load`: versie 2, `punt_formaat` lonlat, beide
modaliteiten (`leiding`, `zee`) in de toegestane set, elk been ≥2 punten, bestand 14,0 KB. Geen naad > 5
km, geen via-punten (geen corridorkeuze in deze keten), geen luchtbeen, geen gedeeld been.

**Lessen voor de volgende bak-agent met een dubbele haven-aanloop:** bouw de aanloop voor het láátste
been altijd met `--van=<zeeknoop> --naar=<kade>` (reisvolgorde), niet automatisch `--van=<kade>
--naar=<zeeknoop>` naar analogie van het eerste-been-patroon — en controleer de naad-tabel uit
bakhandleiding §5 vóórdat je de bake als geslaagd beschouwt.

**Registerregel voor main.js (centraal, na dit rapport):**
`{ sleutel: "cautionbay-futtsu", bestand: "stroomroute-gas-cautionbay-futtsu.json", aan: true }`
