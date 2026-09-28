# Routebrief (licht) · Goud — Van → Via → Naar (land)

**stroom-id:** `goud-olimpiada-dubai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** goud(doré/baar) van Polyus' Olimpiada-mijn (Severo-Jenisejsk-district, Krasnojarsk kraj) per **truck** naar de Krastsvetmet-raffinaderij in Krasnojarsk, per **truck** naar de vrachtterminal van Krasnojarsk (KJA), per **vrachtvlucht** (grootcirkel) naar de vrachtterminal van Dubai (DXB), per **truck** naar de DMCC-vrijzone/handelshub in Dubai — de post-2022 "Hormuz-bypass" van Russisch goud om de westerse LBMA-schorsing heen.
**Welke as van het verhaal:** *Rusland-na-2022* — sinds de LBMA de Russische raffinaderijen in maart 2022 schorste, verkoopt Krastsvetmet (Ruslands grootste/op-één-na-grootste edelmetaalraffinaderij [2][11]) zijn goud via directe vrachtvluchten naar Dubai; UAE werd Ruslands belangrijkste goudafzetmarkt (2022: 75,7 t / $4,3 mrd, tegen 1,3 t in 2021 [11]). Olimpiada produceert ≈1,3–1,4 Moz (≈40–44 t Au) per jaar [Polyus-jaarverslag]; Rusland totaal ≈310–330 t Au-mijnproductie/jaar (USGS MCS 2025).

## 1 · Ketenkaart
```
Olimpiada-mijn `au-olimpiada-mijn` ──(b1 truck · regionale weg Severo-Jenisejsk → Jenisejsk/Lesosibirsk → Bolsjaja Moerta → Krasnojarsk · ≈550 km)──►
  Krastsvetmet-raffinaderij `au-krastsvetmet` (Krasnojarsk)
  ──(b2 truck · stadsrand Krasnojarsk · ≈30 km)──►
  KJA-vrachtterminal `au-kja-cargo`
  ──(b3 lucht · vlucht KJA → DXB, grootcirkel, aannemelijk: bron uit 2022 · ≈5.150 km)──►
  DXB-vrachtterminal `au-dxb-cargo`
  ──(b4 truck · Sheikh Zayed Rd via Trade Centre → Mall of the Emirates · ≈20 km)──►
  DMCC-vrijzone `au-dmcc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Olimpiada-mijn → Krastsvetmet-raffinaderij | regionale weg Severo-Jenisejsk → Jenisejsk/Lesosibirsk → Bolsjaja Moerta → Krasnojarsk (P409) | ≈550 [ontwerp] | maak_stroombeen_weg | nee |
| b2 | A | truck | Krastsvetmet-raffinaderij → KJA-vrachtterminal | stadsrand Krasnojarsk (P409/ringweg noordwaarts naar Jemeljanovo) | ≈30 [ontwerp] | maak_stroombeen_weg | nee |
| b3 | B | lucht | KJA-vrachtterminal → DXB-vrachtterminal | vlucht KJA → DXB (vrachtvlucht, grootcirkel, **aannemelijk: bron uit 2022, sanctieroute kan gewijzigd zijn**) | ≈5.150 [ontwerp; grootcirkel bij het bakken exact] | maak_luchtbeen | nee — doorgetrokken (bakhandleiding §2) |
| b4 | C | truck | DXB-vrachtterminal → DMCC-vrijzone | Sheikh Zayed Rd via Trade Centre-rotonde → Mall of the Emirates (Interchange 4) | ≈20 [ontwerp] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-olimpiada-mijn` | mijn / vertrekpunt | Olimpiada-mijn (Polyus), open groeve + mill | 59.8650, 92.9156 | [3][13] | bron-gelegd (z15 gezien: open dagbouwput met concentrische mijnbanken, waterplas op de putbodem, toegangswegen en een industrieel gebouwencluster net buiten de put) |
| `au-krastsvetmet` | raffinaderij | Krastsvetmet OJSC, Transportny proezd, Leninsky district, Krasnojarsk | 56.0160, 92.9998 | [4][13] | bron-gelegd (z15 gezien: industrieel complex met meerdere grote rechthoekige fabrieksgebouwen langs de spoorlijn en de Jenisej, kantine-adres van Krastsvetmet op dit perceel) |
| `au-kja-cargo` | vrachtterminal (luchtanker) | Krasnojarsk (Jemeljanovo/KJA) — vracht-/general aviation-apron | 56.1837, 92.4630 | [5][13] | bron-gelegd (z16 gezien: verhard platform met meerdere geparkeerde grote vierschroefs/widebody-vliegtuigen naast loodsen/hangaars en een brandstoftankpark, ten noordwesten van de hoofdterminal; exacte Lufthansa-Cargo-loods niet apart te onderscheiden — zie §7) |
| `au-dxb-cargo` | vrachtterminal (luchtanker) | Dubai International Airport (DXB) — Emirates SkyCargo-gebouw | 25.2560, 55.3434 | [6][13] | bron-gelegd (z16 gezien: groot vrachtgebouw direct aan een platform met tientallen geparkeerde widebody-vrachttoestellen, OSM-naam "الإمارات للشحن الجوي" (Emirates SkyCargo) op het gebouw) |
| `au-dmcc` | handelshub / vrijzone (stoppunt) | DMCC (Dubai Multi Commodities Centre), Jumeirah Lake Towers | 25.0709, 55.1387 | [8][13] | bron-gelegd (z15 gezien: dichte cluster hoogbouw/torens langs Sheikh Zayed Road rond het Almas Tower-gebied, matcht de OSM-grens van de DMCC special economic zone) |

## 4 · Via-punten (landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Severo-Jenisejsk (districtshoofdplaats) | 60.3747, 93.0330 | de mijnweg loopt eerst noordwaarts naar de districtshoofdplaats vóór het regionale wegennet zuidwaarts begint [9] |
| b1 | 2 | Jenisejsk / Lesosibirsk (Jenisej-oversteek) | 58.4667, 92.1333 | hier steekt de corridor de Jenisej over en begint de doorgaande P409 naar Krasnojarsk [10] |
| b1 | 3 | Bolsjaja Moerta | 56.9093, 93.1393 | vaste tussenstop op de P409 Jenisejsk–Krasnojarsk-corridor, laatste herkenbare keuzepunt vóór de stadsrand [10] |
| b4 | 1 | Trade Centre-rotonde (begin Sheikh Zayed Rd) | 25.2276, 55.2888 | hier begint de doorgaande Sheikh Zayed Road-corridor vanuit de DXB-omgeving [8] |
| b4 | 2 | Mall of the Emirates (Interchange 4) | 25.1180, 55.2004 | vast punt op de doorgaande Sheikh Zayed Road, laatste herkenbare keuze vóór de afslag naar JLT/DMCC [8] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Krastsvetmet-raffinaderij | OJSC Krastsvetmet | mijndoré/erts → LBMA-vormige goud-/zilver-/platinabaren | Ruslands grootste/op-één-na-grootste edelmetaalraffinaderij (bronnen lopen uiteen, §7) | [2][11] |

## 6 · Stoppunt
De brief stopt in de DMCC-vrijzone in Dubai: dit is de aangewezen naar-site van het ketenontwerp (handelshub waar het goud "wit" wordt, v1-registratie `au-hub-dubai`) — geen bron noemt een specifiek raffinage- of smeltbedrijf bínnen DMCC voor déze as, dus fase D (een met naam genoemde vervolgfabriek) vervalt.

## 7 · Open punten
- **Haalbaarheidstoets bindend, nog niet volledig ingelost:** de kernbron voor de vlucht KJA→DXB is het Reuters-onderzoek uit 2022; een WebSearch (binnen het webbudget) bevestigt dat de UAE structureel Ruslands belangrijkste goudafzetmarkt bleef na 2022 [11], maar geen bron bevestigt specifiek voor 2025/2026 dat Krastsvetmet-goud nog altijd via KJA vliegt. De beennaam van b3 draagt daarom de kwalificatie "(aannemelijk: bron uit 2022, sanctieroute kan gewijzigd zijn)" conform de bindende aanpassing.
- **KJA-vrachtterminal is een gedeeld platform** (general aviation + vracht + Volga-Dnepr-hub) — de exacte Lufthansa Cargo-loods (historisch de op-één-na-grootste vrachthub van die maatschappij [webcheck]) is op z16 niet apart te onderscheiden van andere hangaars op hetzelfde platform.
- **b1-corridor (Severo-Jenisejsk-omweg noordwaarts vóór de zuidwaartse doorreis)** is afgeleid uit nederzettingsgeografie (de mijn ligt zuidelijker dan de districtshoofdplaats), niet uit een gepubliceerde routebeschrijving — aannemelijk.
- **Krastsvetmets rang** ("op één na grootste" in het ketenontwerp vs. "grootste" in het WebSearch-resultaat [11]) is niet eenduidig binnen het webbudget opgelost.
- **Geen site-specifiek jaarvolume voor déze as** — alleen Olimpiada-mijnproductie, het nationale Rusland-cijfer en het generieke UAE-importcijfer (§ kop); geen bron koppelt een specifiek tonnage aan de Krastsvetmet→Dubai-vluchtroute zelf.
- **DMCC-anker is het torencomplex/vrijzone-gebied** (Almas Tower-omgeving), geen los aangewezen raffinagegebouw — DMCC is een vrijzone met vele bedrijven.

## 8 · Bronnen
[1] Reuters, special report "Gold worth billions smuggled out of Africa" / "Russian gold flies to Dubai" (2022) — kernbron voor de vluchtroute Rusland→Dubai na de LBMA-schorsing van maart 2022. https://www.reuters.com/investigates/special-report/gold-russia-dubai/
[2] Wikipedia (via zoekindex), "Krastsvetmet" — OJSC Krastsvetmet, Krasnojarsk, Ruslands grootste edelmetaalraffinaderij (platina/goud). https://en.wikipedia.org/wiki/Krastsvetmet
[3] Wikipedia, "Olimpiada mine" — een van de grootste goudmijnen van Rusland/de wereld, Krasnojarsk kraj, coördinaat 59°51′54″N 92°54′56″E (MediaWiki prop=coordinates: 59.8650, 92.9156). https://en.wikipedia.org/wiki/Olimpiada_mine
[4] OpenStreetMap/Nominatim (ODbL) — "Столовая ОАО «Красцветмет»" (Krastsvetmet-kantine), Транспортный проезд 1/1, Leninsky district, Krasnojarsk, 56.01604/92.99978. https://www.openstreetmap.org
[5] Wikipedia, "Krasnoyarsk International Airport" — IATA KJA, ICAO UNKL, coördinaat 56.17167/92.49333 (MediaWiki prop=coordinates); historisch hub Lufthansa Cargo en Volga-Dnepr Airlines. https://en.wikipedia.org/wiki/Krasnoyarsk_International_Airport
[6] Wikipedia, "Dubai International Airport" — IATA DXB, ICAO OMDB, coördinaat 25.25278/55.36444 (MediaWiki prop=coordinates); Emirates SkyCargo-hub. https://en.wikipedia.org/wiki/Dubai_International_Airport
[7] Polyus PJSC, jaarverslag/investor-rapportages — Olimpiada-productie ≈1,3–1,4 Moz (≈40–44 t Au) 2023–2024. https://www.polyus.com/en/investors/results-reports-and-presentations/
[8] OpenStreetMap/Photon (ODbL) — DMCC special economic zone-grens 25.0715/55.1427 en gebouw "مركز دبي للسلع المتعددة" 25.07088/55.13866 (JLT); "مول الإمارات" (Mall of the Emirates) 25.11798/55.20038; "Sheikh Rashid Tower" (Dubai World Trade Centre) 25.22762/55.28879. https://www.openstreetmap.org
[9] OpenStreetMap/Nominatim (ODbL) — "Северо-Енисейский" (Severo-Jenisejsk), districtshoofdplaats, 60.37470/93.03300. https://www.openstreetmap.org
[10] Wikipedia (MediaWiki API prop=coordinates) — Yeniseysk 58.46667/92.13333; Lesosibirsk 58.23583/92.48278; Bolshaya Murta 56.90930/93.13930. https://en.wikipedia.org/wiki/Yeniseysk · https://en.wikipedia.org/wiki/Lesosibirsk · https://en.wikipedia.org/wiki/Bolshaya_Murta
[11] MINING.COM, "Russia becomes UAE's top gold source after being shut out of west" — UAE-import 2022: 75,7 t Russisch goud ($4,3 mrd) tegen 1,3 t in 2021; Rusland/Turkije/China ≈99,8% van de Russische goudexport na februari 2022. https://www.mining.com/web/russia-becomes-uaes-top-gold-source-after-being-shut-out-of-west/
[12] USGS, Mineral Commodity Summaries 2025 — Rusland ≈310–330 t Au-mijnproductie/jaar (ketenontwerp-referentie, niet apart herbevestigd binnen het webbudget).
[13] Esri World Imagery via `v2/tools/sat_check.py` (z13–z16) — `v2/build-cache/satcheck/sat-goud-olimpiada-dubai-olimpiada-mijn.png`, `sat-goud-olimpiada-dubai-krastsvetmet.png`, `sat-goud-olimpiada-dubai-kja-overview.png`, `sat-goud-olimpiada-dubai-kja-terminal.png`, `sat-goud-olimpiada-dubai-kja-apron.png`, `sat-goud-olimpiada-dubai-dxb-cargo.png`, `sat-goud-olimpiada-dubai-dmcc.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `goud-olimpiada-dubai` · **bestand:** `v2/data/stroomroute-goud-olimpiada-dubai.json` (144,0 KB) ·
**recept:** `bak_goud_olimpiada_dubai()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh goud-olimpiada-dubai`).

**4 benen · 5.242,8 km · 7.319 punten · 5 markers**, alle DOORGETROKKEN (geen enkele stippel):

| # | fase | modaliteit | km | naad met vorig been |
|---|---|---|---|---|
| b1 | A | truck | 615,3 | — (start) |
| b2 | A | truck | 45,7 | 0,000 km |
| b3 | B | lucht | 4.548,1 | 0,000 km |
| b4 | C | truck | 33,7 | 0,000 km |

**Luchtbeen (§2 "Lucht" van de bakhandleiding, letterlijk gevolgd):**
- b3 KJA → DXB: `maak_luchtbeen.py`, grootcirkel **4.548,1 km** — lager dan het ontwerpcijfer ≈5.150 km (dat cijfer
  was een grove schatting uit de brief, geen apart gebronde km); een grootcirkel-been heeft per definitie geen
  km-toets. Geen tussenlanding aangenomen (geen bron noemt een hub), dus één directe vlucht conform brief §7.
  De beennaam draagt de bindende kwalificatie "aannemelijk: bron uit 2022, sanctieroute kan gewijzigd zijn"
  (brief §7).
- `toets_rechte_benen.py` slaat het luchtbeen terecht over.

**Stippels:** geen. Alle drie truckbenen zijn gewone openbare wegen (regionale weg P409, stadsring, Sheikh Zayed
Road) boven de "korter dan ~2 km / airside zonder openbare weg"-drempel. Geen haven-aanloop (geen zeebeen in
deze keten).

**Toelichting per truckbeen (haalbaarheidstoets §5/§6 van de bakhandleiding, geen dichtgetrokken bevindingen):**
- b1 (Olimpiada-mijn → Krastsvetmet): profiel `goud-olimpiada-dubai-olimpiada-krastsvetmet` (extract
  rusland-siberie, `corridorKlassen: tertiary/unclassified` nodig — zonder die uitbreiding gaf de scan "geen
  wegpad tussen punt 0 en 1" bij Severo-Jenisejsk). Gebakken **615,3 km** tegen het ontwerpcijfer ≈550 km =
  **+11,8%**, binnen de ±15%-norm (buiten de ±10%-toolwaarschuwing). Alle snaps ≤0,4 km. Dit is en blijft het
  langste/onzekerste been van de keten (brief §7: aannemelijke corridor uit nederzettingsgeografie).
- b2 (Krastsvetmet → KJA-vrachtterminal): profiel `goud-olimpiada-dubai-krastsvetmet-kja` (extract
  rusland-siberie, `corridorKlassen: tertiary/unclassified/residential/service` + `eindKlassen` +
  `eindToegangPrivaat` nodig om een route te vinden). Gebakken **45,7 km** tegen het ontwerpcijfer ≈30 km =
  **+51,9%** — BUITEN de ±15%-norm, een BEVINDING: het ontwerpcijfer was een ruwe schatting van de stadsrand-
  afstand, terwijl de echte P409/ringweg-route over de rivier en om de stad heen loopt. Niet dichtgetrokken;
  de gemeten route volgt de doorgaande, gekarteerde weg.
- b4 (DXB-vrachtterminal → DMCC): profiel `goud-olimpiada-dubai-dxb-dmcc` (extract gcc-staten). Gebakken
  **33,7 km** tegen het ontwerpcijfer ≈20 km = **+67,4%** — eveneens BUITEN de ±15%-norm, een BEVINDING van
  dezelfde soort: de werkelijke Sheikh Zayed Road-corridor via Trade Centre en Mall of the Emirates is
  substantieel langer dan de hemelsbrede schatting in de brief. `trimStaart: True` toegevoegd en herscand —
  geen verandering in het resultaat (de overschiet zat niet op de ankerprojectie).

**Ankers, status ongewijzigd t.o.v. §3:** alle vijf blijven **bron-gelegd** (satellietblik z13–z16, geen
wijziging nodig na het bakken).

**Toets (bakhandleiding §5):**
- Naden tussen alle vier de benen: **0,000 km** (elk been sluit exact aan op het vorige).
- `toets_knikken.py`: 85 knikken ≥60° over de twee lange truckbenen (vrijwel allemaal spikes <30 m straal op
  straatniveau-zigzag, geen reparatie nodig), 4 omkeringen ≥150° waarvan **1 TERUGLOOP** op b4, vlak bij het
  DXB-anker (25.25382, 55.33649, straal 4 m) — een `trimStaart`-poging op dat profiel veranderde de geometrie
  niet (de lus zit niet op de ankerprojectie maar op de terminal-rotonde zelf); te klein en te dicht bij het
  vertrekpunt om als routefout te lezen, gerapporteerd als bevinding.
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag (luchtbeen terecht overgeslagen;
  geen truckbeen heeft omwegfactor 1,000).
- Markers: alle 5 op **0,000 km** van hun lijn (elk marker-anker is het leg-eindpunt zelf).
- `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten ⊂ {truck, lucht}, elk been ≥ 2 punten
  (minimum 183), bestand 144,0 KB (ruim onder ~300 KB).

**Gereedschapslessen:**
- De weg-corridors rond Krasnojarsk (b1, b2) haalden pas een route binnen door achtereenvolgens
  `corridorKlassen` en daarna ook `eindKlassen`/`eindToegangPrivaat` toe te voegen — een default van alleen
  motorway/trunk/primary/secondary dekt de regionale P409 en de stadsring bij Jemeljanovo niet.
- Twee van de drie truckbenen (b2, b4) vielen buiten de ±15%-norm terwijl de brief zelf al aangaf dat de
  km-cijfers "ontwerpcijfers" waren, niet apart gebrond — de bake-lengte is hier zoals bedoeld leidend geworden
  boven de schatting.
- `maak_luchtbeen.py` bleef licht (milliseconden) — geen slot nodig, zoals de werkwijze voorschrijft.
