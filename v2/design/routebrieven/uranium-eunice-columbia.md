# Routebrief (licht) · Uranium — Urenco USA (Eunice, New Mexico) → Westinghouse Columbia Fuel Fabrication Facility (South Carolina)

**stroom-id:** `uranium-eunice-columbia` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** verrijkt UF6 (30B-cilinder in een UX-30-transportverpakking) van Urenco USA — de enige
commerciële verrijkingsfabriek van de VS, Eunice/Lea County, New Mexico — per **truck** over I-20 oostwaarts
(Odessa/Midland → Fort Worth → Shreveport → Jackson → Birmingham → Atlanta → Augusta) en I-77/I-26 naar de
Westinghouse Columbia Fuel Fabrication Facility, South Carolina — stoppunt (splijtstoffabricage).
**Welke as van het verhaal:** de VS — de niet-Russische verrijking-naar-splijtstof-schakel; de enige binnenlandse
route van Amerikaans verrijkt uranium naar Amerikaanse kernbrandstoffabricage. Urenco USA ~9% wereld-SWU
(≈ omgerekend ~5.850 t U-feed-equivalent/j, WNA-reactorbehoefte 2023/24) [9]; Westinghouse Columbia ~1.400 t HM/j
[9][8]. Geen bron geeft een Eunice→Columbia-specifiek jaartonnage — de bestemmingsrelatie zelf is wél
bron-gelegd: concrete, gedateerde NRC-gerelateerde cilinderzendingen in beide richtingen [4][5].

## 1 · Ketenkaart
```
Urenco USA — verrijking `u-eunice-verrijking` ──(b1 D truck, aannemelijk: corridor niet gepubliceerd ·
I-20 oost (Odessa/Midland → Fort Worth → Shreveport → Jackson → Birmingham → Atlanta → Augusta) →
I-77/I-26 → Columbia · hemelsbreed ~2.065 km, geen wegkm)──►
Westinghouse Columbia Fuel Fabrication Facility `u-columbia-fabricage` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Urenco USA (Eunice) → Westinghouse Columbia Fuel Fabrication Facility | I-20 oost (Odessa/Midland → Fort Worth → Shreveport → Jackson → Birmingham → Atlanta → Augusta) → I-77/I-26 naar Columbia | hemelsbreed ~2.065 km, geen wegkm [1, 2, 7 — NRC/DOT publiceren geen routedetails voor verrijkt-UF6-transport; ±15%-toets geldt als indicatie, niet als norm] | maak_stroombeen_weg (extracts us-new-mexico, us-texas, us-louisiana, us-mississippi, us-alabama, us-georgia, us-south-carolina) | nee — *aannemelijk: enig plausibele doorgaande Oost-West-corridor over deze afstand, niet route-specifiek gebrond* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-eunice-verrijking` | verrijking (kop) | Urenco USA / National Enrichment Facility, Eunice/Lea County, New Mexico | 32.4356, -103.0796 | [1][9] | bron-gelegd (z15 gezien: groot proces-/cascadecomplex met kenmerkende langgerekte hallen, tanks, bufferbekkens en beveiligde omheining, direct naast Waste Control Specialists in "nuclear alley" — het sitelaag-punt `w-urenco-eunice` (32.4667,-103.1833, status "aannemelijk", geen satellietblik) ligt ~5,4 km WNW ervan, op los verspreide olie-/gaswinningserven zonder herkenbaar fabrieksterrein. Deze brief gebruikt de Wikipedia-infobox-coördinaat (National Enrichment Facility, pageid 7403983) i.p.v. het letterlijk hergebruikte sitelaag-punt; zie §7.) |
| `u-columbia-fabricage` | splijtstoffabricage (staart, stoppunt) | Westinghouse Columbia Fuel Fabrication Facility, Hopkins (Lower Richland County), South Carolina | 33.8831, -80.9194 | [8][9] | bron-gelegd (z17 gezien: groot proces-/hallencomplex met parkeerterreinen, tanks en bufferbekkens aan Bluff Road — het sitelaag-punt `w-westinghouse-columbia` (33.8811,-80.9233, status "aannemelijk") ligt ~420 m ZW ervan, bij een kruising/vijver net naast het terrein (de sitelaag noemt dit zelf al: "kruis ligt bij een kruising/vijver dicht bij het terrein maar niet duidelijk op de fabriekshallen zelf"). Deze brief schuift naar het zichtbare hoofdgebouw; zie §7.) |

## 4 · Via-punten (b1 — corridorkeuzes op I-20/I-77/I-26)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Odessa, TX (I-20-oprit) | 31.8314, -102.3432 | dichtstbijzijnde doorgaande I-20-toegang vanaf Eunice/Hobbs — pint de "Odessa/Midland"-knik uit het ketenontwerp |
| b1 | 2 | Fort Worth, TX (I-20 door de DFW-metroplex) | 32.7283, -97.5909 | enige doorgaande I-20-tracé door Dallas–Fort Worth, geen alternatieve hoofdroute |
| b1 | 3 | Shreveport, LA (I-20/I-49-knooppunt) | 32.4593, -93.8277 | staatsgrensoversteek Texas→Louisiana, I-20 kruist hier I-49 |
| b1 | 4 | Jackson, MS (I-20-hoofdknooppunt) | 32.2884, -90.2494 | enige doorgaande I-20-corridor door centraal Mississippi |
| b1 | 5 | Birmingham, AL (I-20/I-59/I-65-knooppunt) | 33.4980, -86.9026 | hier draait de corridor van zuidoost naar oost richting Atlanta |
| b1 | 6 | Atlanta, GA (I-20 doorgaande snelweg) | 33.7547, -84.4662 | pint "Atlanta" uit het ketenontwerp — enige doorgaande Oost-West-as door Georgia |
| b1 | 7 | Augusta, GA (I-20, oversteek Savannah-rivier naar SC) | 33.5047, -82.0557 | laatste hoofdknooppunt vóór de staatsgrens Georgia→South Carolina |
| b1 | 8 | Columbia, SC (I-20/I-77/I-26-knooppunt) | 34.0128, -80.9521 | hier verlaat de route I-20 op I-77/I-26 richting Bluff Road (S-48) naar Hopkins — pint de "I-77/I-26 naar Columbia"-knik uit het ketenontwerp; **correctie op het ketenontwerp**: I-20's eigen Wikipedia-routebeschrijving noemt voor Columbia primair de I-26-afslag bij "Malfunction Junction" (exit 64) — I-77 kruist I-20 wél noordelijk van de stad en is de kortere aansluiting naar Bluff Road/Hopkins in het zuiden, dus deze brief volgt de I-77-route uit het ketenontwerp (zie §7) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Westinghouse Columbia Fuel Fabrication Facility | Westinghouse Electric Company | verrijkt UF6 (30B-cilinder) → PWR/BWR-splijtstofelementen | nameplate ≈ 1.400–1.700 t HM/j, grootste splijtstoffabriek van de VS | [8][9] |

## 6 · Stoppunt
De brief stopt bij de Westinghouse Columbia Fuel Fabrication Facility: dat is het opgedragen keten-eindpunt
(naar_site = stoppunt). Geen bron noemt een specifieke vervolgbestemming (reactor/utility) voor déze zending,
dus fase E vervalt.

## 7 · Open punten
- **De exacte wegcorridor is niet gepubliceerd** (veiligheidsgevoelig transport van verrijkt UF6; NRC-
  vergunningsdocumenten noemen faciliteiten maar geen routes) — de I-20/I-77/I-26-corridor is de enig
  plausibele doorgaande Oost-West-snelwegroute over deze afstand, "aannemelijk: enige logische corridor", niet
  bron-gelegd. Km-veld is daarom "hemelsbreed, geen wegkm" (±15%-toets geldt als indicatie).
- **Columbia→Hopkins (I-77/I-26 vs. I-26/exit-64) is niet individueel gebrond** — I-20's eigen Wikipedia-tekst
  noemt de I-26-afslag bij "Malfunction Junction" als gangbare toegang tot Columbia-centrum; deze brief volgt
  toch de I-77/I-26-aanname uit het ketenontwerp (de fabriek ligt zuidelijk, Hopkins/Lower Richland, en I-77
  sluit noordelijk van Columbia op I-20 aan) — bij het bakken kan de I-26-route een betere snap geven.
- **Modaliteit is aangenomen: truck**, bevestigd via de 30B/UX-30-verpakking (een wegtransport-eenheid); een
  gedeeltelijk spoortransport voor grotere cilinders is niet expliciet uitgesloten — bevestigen bij het bakken.
- **Sitelaag-discrepantie voor de orkestrator (niet zelf gewijzigd):** beide sitelaag-ankers (`w-urenco-eunice`
  32.4667,-103.1833 en `w-westinghouse-columbia` 33.8811,-80.9233, status "aannemelijk") liggen 5,4 km resp.
  0,42 km van de nu satelliet-gelegde fabrieksterreinen. Eigen ankers `u-eunice-verrijking`/`u-columbia-
  fabricage` gebruikt; de sitelaag zelf is niet aangepast (buiten mijn bestanden) — zie §3.
- **Geen actueel Eunice→Columbia-specifiek jaartonnage gevonden** — de bestemmingsrelatie zelf is wél
  bron-gelegd (twee gedateerde cilinderzendingen, 2019 en 2024, zie §8), de volumecijfers zijn faciliteits-
  totalen uit de sitelaag, geen route-specifieke stroom.
- **Overlap:** geen — stroom-id `uranium-eunice-columbia` bestaat nog niet in `v2/data/`, en geen andere
  golf-6-as of bestaande stroom raakt deze corridor (New Mexico/Texas/Louisiana/Mississippi/Alabama/Georgia/
  South Carolina).

## 8 · Bronnen
[1] Wikipedia, "National Enrichment Facility" (pageid 7403983) — "located 5 miles (8.0 km) east of Eunice, New
Mexico"; operator Louisiana Energy Services (LES) / URENCO USA; coördinaat 32.4356,-103.0796.
https://en.wikipedia.org/wiki/National_Enrichment_Facility
[2] Wikipedia, "Eunice, New Mexico" — bevestigt de URENCO USA National Enrichment Facility bij Eunice.
https://en.wikipedia.org/wiki/Eunice,_New_Mexico
[3] Urenco — "Urenco USA authorised to produce up to 10% enriched uranium by NRC" (2025), en de UUSA-
operationspagina: "capable of supplying approximately one-third of U.S. demand for enriched uranium annually".
https://www.urenco.com/global-operations/uusa ·
https://www.urenco.com/news/global/2025/urenco-usa-authorised-to-produce-up-to-10-enriched-uranium-by-nrc
[4] WISE Uranium Project — "Urenco USA uranium enrichment plant (USA) - Current Issues": "On April 5, 2019,
UUSA shipped a full 30B cylinder [...] within a UX-30 shipping package to the Westinghouse Fuel Fabrication
Facility at Columbia South Carolina." https://www.wise-uranium.org/eoples.html
[5] WISE Uranium Project — "Westinghouse Electric Co. Columbia nuclear fuel plant (USA) - Current Issues":
"On February 16, 2024, during a receipt inspection of Six UX-30 overpack (packages) [containing heeled
cylinders], transported from Westinghouse's Columbia Fuel Fabrication Facility to the Urenco USA's facility
[...] at the Urenco USA facility in Eunice, New Mexico" (plus een vergelijkbare retourzending, dec. 2024).
https://www.wise-uranium.org/eopwecc.html
[6] NRC-vergunningsdocument (via het ketenontwerp) — ML2505/ML25051A106.pdf.
https://www.nrc.gov/docs/ML2505/ML25051A106.pdf
[7] Wikipedia, "Interstate 20" — routebeschrijving Reeves County TX → Florence SC via Odessa/Midland/
Abilene/Fort Worth/Shreveport/Jackson/Birmingham/Atlanta/Augusta; bij Columbia "can be reached most directly
by taking I-26 east at exit 64 ('Malfunction Junction')". https://en.wikipedia.org/wiki/Interstate_20
[8] NRC-vergunningsdocument / Westinghouse (via de sitelaag) — Westinghouse Columbia Fuel Fabrication
Facility, Bluff Road, Hopkins/Lower Richland County, coördinaat 33°52'52"N 80°55'24"W (33.8811,-80.9233);
nameplate ≈1.400–1.700 t HM/j.
[9] `v2/design/uranium-sitelaag.json` — bestaande ankers `w-urenco-eunice` (aandeel ~9% wereld-SWU,
≈5.850 t U-feed-equivalent/j) en `w-westinghouse-columbia` (~1.400 t HM/j); hergebruikt voor de
capaciteitscijfers, niet voor de coördinaten zelf (zie §3/§7).
[10] OpenStreetMap / Nominatim (ODbL) — coördinaten van de I-20/I-77/I-26-via-punten in §4 (Odessa, Fort
Worth, Shreveport, Jackson, Birmingham, Atlanta, Augusta, Columbia), live opgevraagd via nominatim.openstreetmap.org.
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16/z17, live) —
`v2/build-cache/satcheck/sat-uranium-eunice-columbia-eunice-nef.png` (Urenco USA / National Enrichment
Facility) en `sat-uranium-eunice-columbia-columbia-adj.png` (Westinghouse Columbia Fuel Fabrication Facility).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**1 been, 2.316,4 km, 15.567 punten, 2 markers.** Eén truckbeen (b1, fase D), doorgetrokken —
geen stippel, geen haven-aanloop, geen leiding, geen luchtbeen, geen gedeeld been.

| # | modaliteit | km | naad met vorige | opmerking |
|---|---|---|---|---|
| b1 | truck | 2.316,4 | 0,00 (eerste been) | Urenco USA/NEF → Odessa → Fort Worth → Shreveport → Jackson → Birmingham → Atlanta → Augusta → Columbia → Westinghouse Columbia FFF (I-20 oost → I-77/I-26) |

**Recept:** `python v2/tools/maak_stroombeen_weg.py --profiel uranium-eunice-columbia-eunice-columbia`
(profiel in `v2/tools/maak_stroombeen_weg.py`, extracts us-new-mexico/us-texas/us-louisiana/
us-mississippi/us-alabama/us-georgia/us-south-carolina, 7/7 bevestigd aanwezig) →
`v2/build-cache/ais/graaf/uranium-eunice-columbia-weg-eunice-columbia.geojson` →
`bash v2/tools/bak_stromen.sh uranium-eunice-columbia` (functie `bak_uranium_eunice_columbia`,
`--been-geojson`, geen routering meer in `hecht_marnet.py` zelf).

**Lengtetoets:** geen gepubliceerde wegkm (brief §2/§7, veiligheidsgevoelig UF6-transport) —
gemeten 2.315,6 km weggeometrie (2.316,4 km met de korte anker-verbindingsstukjes) tegen
hemelsbreed ~2.065 km = **+12,2%**, ruim binnen "indicatie, geen norm" die de brief voorschrijft
voor dit veld (zelfde behandeling als `uranium-smithranch-metropolis`).

**Toelichting per bevinding:**
- **Plant → weg-aanloop 0,66 km** (net over de 0,5 km-vuistregel van de handleiding) — géén
  procesgat: het is het rechte anker-verbindingsstukje van de Urenco USA/NEF-poort naar NM 176/
  Andrews Highway, een reëel bestaande, doorgaande staatsweg 0,66 km verderop (bevestigd op de
  extract: `highway=primary`, `ref=NM 176`). Weg → kade-aanloop bij Westinghouse Columbia: 0,07 km
  (OK), direct op een residential-straat bij de fabriekspoort.
- **"service" uit `eindKlassen` gehaald voor dit profiel** (afwijkend van de default
  residential/service/tertiary/unclassified) — het NEF-terrein draagt een geïsoleerd 11-punts
  `highway=service`-lusje (way/905682611, 0,115 km van het anker) dat in OSM nergens op het
  wegennet aansluit; gemeten met een BFS-componenttelling (component van 11 knopen, terwijl NM 176
  op 0,66 km in de hoofdcomponent van 1.463.845 knopen ligt). Met "service" erin snapte het anker
  op die isolaat en gaf de Dijkstra "geen wegpad tussen punt 0 en 1"; zonder "service" snapt hij op
  NM 176 en routeert de hele keten door. Vastgelegd als kopnoot bij het profiel.
- **2 TERUGLOOP-knikken, klein en bewust niet weggeschoven** (`toets_knikken.py`): 34.07153,
  -80.92587 (R 23 m, bij de I-20/I-77/I-26-knoop Columbia) en 32.45965,-93.82747 (R 2 m, bij het
  I-20/I-49-knooppunt Shreveport) — kleine op-en-neer-bewegingen op een klaverblad-oprit, dezelfde
  klasse als het "aannemelijk een echte kop-maak-junctie"-terugloopje in `uranium-malvesi-
  tricastin` §9. `snoei_keerlussen` (drempel 25 m) heeft al 5 grotere loops (tot 0,70 km)
  weggesneden vóór de toets; deze twee zijn te klein en te dicht bij de doorgaande as om via een
  via-punt te verschuiven zonder de knooppunt-pin te verliezen — geen via-punt bijgeschoven om het
  getal te halen.
- **Bestandsgrootte 319,0 KB** — iets boven de "~300 KB"-vuistregel uit de handleiding (§5.3),
  door de lengte van het been (2.316 km, 15.567 punten op een reëel wegennet met veel knikken over
  9 staten). Laadt en valideert (versie 2, punt_formaat lonlat, modaliteit `truck`, been ≥ 2
  punten); geen actie ondernomen, geen via-punt/simplify-stap toegevoegd die niet in het gereedschap
  bestaat.
- **Geen stippel verwacht en geen stippel nodig**: beide ankers liggen op of vlak bij het
  fabrieksterrein (0,66 en 0,07 km aanloop), ruim onder de ~2 km-drempel voor een last-mile-stippel.

**Markers:** beide op 0,00 km van de lijn (de geometrie begint/eindigt letterlijk op de
anker-coördinaten uit de brief).

**Lessen voor de volgende bak-agent:** een enkel geïsoleerd `service`-lusje vlak bij een fabrieks-
poort kan dichter bij het anker liggen dan de echte doorgaande weg en zo de snap kapen — een
BFS-componenttelling vanaf het ankerpunt is de goedkoopste manier om dat te onderscheiden van een
échte "geen wegpad"-fout (Carretera del Cobre-klasse), zonder de private-toegang-sleutel
(`eindToegangPrivaat`) nodig te hebben.
