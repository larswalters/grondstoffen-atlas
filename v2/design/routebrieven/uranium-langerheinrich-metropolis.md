# Routebrief (licht) · Uranium · Langer Heinrich → Walvis Bay → Montreal → Metropolis Works (Namibië → VS)

**stroom-id:** `uranium-langerheinrich-metropolis` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** U₃O₈-concentraat (vaten in 20'-containers) van de Langer Heinrich-fabriek (Paladin 75% / CNNC 25%, Erongo) per **truck**
over de mijnweg, C28 en B2 naar de containerterminal van Walvis Bay, per **zeeschip** (CSAL) via de Atlantische Oceaan en de Saint-Laurent naar
Montreal, per **truck** over de grens Lacolle–Champlain en door NY/PA/OH/KY/IL naar de ConverDyn-conversiefabriek Metropolis Works (stoppunt).
**Welke as van het verhaal:** *Zuidelijk halfrond naar de enige Amerikaanse conversiefabriek.* Volume: 691 t U in 2024 (herstart maart 2024, WNA [3]);
FY2025 ca. 3,0 Mlb U₃O₈ ≈ 1.150 t U [5]; de sitelaag rekent ~800 t U/j. Gedocumenteerde zending (peiljaar 2010): 114,3 t U₃O₈ = ~97 t U [1].
Route is van 2010 (NRC); of het in 2024+ nog zo loopt is niet gepubliceerd (§7).

## 1 · Ketenkaart
```
Langer Heinrich-fabriek `u-lh-fabriek` ──(b1 A truck · mijnweg → C28 → B2 · aannemelijk · hemelsbreed 87 km, geen wegkm)──►
  Walvis Bay-kade `u-walvisbay-haven` ──(b2a zee haven-aanloop 12,5 km, stippel)──► MARNET-zeeknoop 8084
  ──(b2b zee · Atlantic → Saint-Laurent · 12.366 km gemeten MARNET)──► Montreal-kade `u-montreal-kade` (onzeker: terminal niet gepubliceerd)
  ──(b3 C truck · A-15 → grens Lacolle–Champlain → NY/OH/KY/IL · hemelsbreed 1.575 km, geen wegkm)──► Metropolis Works `u-metropolis-conversie` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Langer Heinrich-fabriek → Walvis Bay-kade | Langer Heinrich Mine Road → C28 (bij Swakopmund) → MR44/B2 (Dr. Hifikepunye Pohamba Freeway) → C14 — **aannemelijk: weg Namibië niet gepubliceerd** (analogie Rössing/Husab, vaten per container) | hemelsbreed 87 km, geen wegkm (OSRM-indicatie 128 km, OSM [8]) | maak_stroombeen_weg (extract namibie) | nee; mijnweg = `unclassified` |
| b2a | B | zee (haven-aanloop) | Walvis Bay-kade → MARNET-zeeknoop 8084 (-22.8344,14.4759) | schematisch, over de baai | 12,5 [MARNET-snap] | rechte stippel (`maak_havenaanloop.py` gaf in de haalbaarheidstoets na 300 s niets) | ja — het net reikt niet tot de kade |
| b2b | B | zee | Walvis Bay-kade → Montreal-kade | Atlantische Oceaan noordwaarts, Golf/Rivier Saint-Laurent (CSAL, Atlantic Impala, 2010) [1][9] | hemelsbreed 11.656; MARNET-dry-run 12.366,0 [10] | MARNET (`--been zee`) | nee — snap Montreal 3,4 km (< 5 km) |
| b3 | C | truck | Montreal-kade → Metropolis Works | A-15 → grens Lacolle–Champlain (**bron** [1]) → daarna **aannemelijk** US-11/I-81 → I-90 → I-271 → I-71 → I-65 → Western Kentucky Pkwy → I-69/I-24 → US-45 | hemelsbreed 1.575 km, geen wegkm (OSRM-indicatie ~1.900 km, OSM [8]; haalbaarheidstoets mat 1.894,5) | maak_stroombeen_weg (extracts canada, us-new-york, us-pennsylvania, us-ohio, us-kentucky, us-indiana, us-illinois) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-lh-fabriek` | mijn-/verwerkingsfabriek (kop) | Langer Heinrich Uranium (Pty) Ltd, verwerkingsfabriek | -22.8142, 15.3255 | [4][5][sat] | bron-gelegd (z16 gezien: procesfabriek met tanks, verdikkers en hallen, tailingsdam en ertsvelden eromheen). ⚠️ Het sitelaag-punt `w-langerheinrich` (-22.8147, 15.3338) ligt 0,8 km oostelijker bij erts/tailings; deze brief gebruikt het fabrieksanker |
| `u-walvisbay-haven` | overslag landweg → zee, **hergebruikt** | NamPort containerterminal, Walvis Bay | -22.9465, 14.4840 | letterlijk uit `uranium-rossing-walvisbay` §3 | bron-gelegd (z16 in die brief: containerterminal met stapels en kade); ligt 12,5 km van zeeknoop 8084 → aanloop |
| `u-montreal-kade` | overslag zee → weg, **hergebruikt** | Port of Montreal, Viau-zijde | 45.5900, -73.5065 | letterlijk uit `uranium-poti-blindriver` §3 | **onzeker: terminal niet gepubliceerd** (NRC: "Montreal, Quebec"; CSAL is een multipurpose/ro-ro-dienst [9], dus de Viau-containerterminal is niet bevestigd) |
| `u-metropolis-conversie` | conversiefabriek (stoppunt), **hergebruikt** | Honeywell/ConverDyn Metropolis Works, Illinois | 37.1718, -88.7570 | letterlijk uit `uranium-smithranch-metropolis` §3 (= sitelaag `w-metropolis`, centraal gelijkgetrokken) | bron-gelegd (z16 in die brief: ommuurd fabrieksterrein met tanks, 3 km NW van de stad) |

## 4 · Via-punten (alleen b3 heeft een corridorkeuze; b1: C28 is de enige gekarteerde weg tussen mijnweg en kust)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | mijnweg-junctie met de C28 | -22.8559, 15.0340 | de mijnweg (`unclassified`) takt hier af naar de C28; zonder punt vindt de scanner geen wegpad (haalbaarheidstoets) |
| b1 | 2 | C28 bij Swakopmund | -22.7001, 14.5921 | houdt de route op C28 → MR44/B2 naar Walvis Bay i.p.v. een zandspoor langs de kust |
| b3 | 1 | grens Lacolle–Champlain (einde A-15 / begin I-87) | 45.0088, -73.4524 | enige bronvaste punt: NRC noemt de oversteek Lacolle/Champlain [1]; coördinaat Wikipedia [7] |
| b3 | 2 | I-81, Pulaski (NY) | 43.6274, -76.0829 | corridorkeuze US-11/I-81 → Thruway tegenover I-87 → Albany → I-90 (ontwerp noemde I-87, +8% km, niet gepubliceerd) |
| b3 | 3 | I-71 bij Medina (OH), I-71/I-76 | 41.1307, -81.7996 | pint I-71 zuidwaarts via Cleveland-zuid i.p.v. I-77/I-79 |
| b3 | 4 | I-71 bij Wilmington (OH) | 39.4562, -84.0007 | I-71 langs Cincinnati naar de Ohio-oversteek bij Louisville i.p.v. I-70/I-64 |
| b3 | 5 | I-65 bij Shepherdsville (KY), zuid van Louisville | 38.0112, -85.6972 | route om het centrum van Louisville heen (I-264/I-265), niet erdoor |
| b3 | 6 | Western Kentucky Parkway (KY) | 37.3937, -86.7562 | WK Parkway → I-69/I-24 → US-45 tegenover I-64/I-57 via Evansville |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Langer Heinrich | Paladin 75% / CNNC Overseas 25% | erts → U₃O₈ (vaten) | nameplate 2.000 tU/j (stage 3, tot 2018); herstart maart 2024, 691 tU in 2024 | [3][5] |
| Metropolis Works | Honeywell, verkoop via ConverDyn | U₃O₈ → UF₆ | ~15.000 tU/j; enige commerciële VS-conversiefabriek | sitelaag `w-metropolis`; `uranium-smithranch-metropolis` §5 |

## 6 · Stoppunt
De brief stopt bij Metropolis Works: dat is de gedocumenteerde ontvanger (ConverDyn) in de NRC-aanmelding [1]; verder (UF₆ → verrijker) noemt geen bron voor déze lading, dus fase D/E vervallen.

## 7 · Open punten
- **Route is van 2010; de haven wisselt.** Een NRC-aanmelding uit 2007 laat dezelfde lading via Hapag-Lloyd per spoor naar Toronto gaan en bij **Buffalo (NY)** de VS binnenkomen [2]; 2009 en 2012 noemen volgens de zoekresultaten ook Walvis Bay → Montreal en 2011 hetzelfde opzet (Atlantic Nyala, haalbaarheidstoets); die aanmeldingen zijn niet zelf gelezen. Of 2024+ nog via Montreal loopt is niet gepubliceerd.
- **Montreal-terminal niet gepubliceerd** (anker onzeker); geen CSAL-bron noemt een berth [9].
- **Amerikaanse wegroute na Champlain niet gepubliceerd:** de via-punten zijn een aannemelijke keuze (kortste OSM-route, niet bron). I-87 → Albany → I-90 is ~8% langer en niet uitgesloten.
- **Wegkm Namibië en VS niet gepubliceerd**; de ±15%-toets is een indicatie (OSRM draait op dezelfde OSM-bron als de scan, geen onafhankelijke toets).
- **Aanloop Walvis Bay** is een rechte stippel (`maak_havenaanloop.py` hing 300 s); b3 levert ~475 KB op (boven de 300 KB-richtlijn, net als `smithranch-metropolis`).
- **Sitelaag `w-langerheinrich`** staat 0,8 km oost van de fabriek (erts/tailings); niet gewijzigd (buiten mijn bestanden), gemeld voor de orkestrator.
- **Wikipedia noemt CNNC 25% én 49% (2016)** [4]; WNA/Paladin noemen 25% [3][5], die zijn aangehouden. Geen overlap met bestaande stromen; de Saint-Laurent-staart (~1.500 km) ligt wel naast `uranium-poti-blindriver` b1b.

## 8 · Bronnen
[1] NRC, advance notification import shipment RSB Logistic ref. 0810-390, 17-08-2010 (zelf gelezen): 432 vaten / 8 × 20' / 114.271,66 kg U₃O₈, Langer Heinrich → ConverDyn Metropolis, zeil 21-08-2010 Walvis Bay → Montreal (CSA Line, Atlantic Impala), over de weg bij Champlain NY. https://www.nrc.gov/docs/ML1033/ML103370061.pdf
[2] NRC-aanmeldingen 2007 (Buffalo), 2009, 2011, 2012 — alleen via zoekresultaat-samenvatting, niet zelf gelezen. https://www.nrc.gov/docs/ML0719/ML071970367.pdf · https://www.nrc.gov/docs/ML0917/ML091770444.pdf · https://www.nrc.gov/docs/ML1127/ML11272A017.pdf · https://www.nrc.gov/docs/ML1206/ML12069A043.pdf
[3] World Nuclear Association, Namibia: Langer Heinrich 0 tU (2023), 691 tU (2024), herstart maart 2024, CNNC Overseas 25%. http://world-nuclear.org/information-library/country-profiles/countries-g-n/namibia
[4] Wikipedia, "Langer Heinrich Mine": 22°48'52.9"S 15°20'01.7"E (mijn), Paladin/CNNC. https://en.wikipedia.org/wiki/Langer_Heinrich_Mine
[5] Uranium Royalty Corp, Langer Heinrich: ~80 km oost van Walvis Bay, FY2025 ~3 Mlb U₃O₈ geproduceerd, 75/25. https://www.uraniumroyalty.com/portfolio/langer-heinrich/
[6] Agence Ecofin, 23-07-2024: eerste klantzending (319.229 lb) vertrok 12-07-2024 uit Walvis Bay. http://www.ecofinagency.com/mining/2307-45754-nambia-uranium-shipping-from-langer-heinrich-mine-resumes
[7] Wikipedia, "Champlain–St. Bernard de Lacolle Border Crossing": 45.008825, -73.452358, einde A-15 / I-87. https://en.wikipedia.org/wiki/Champlain%E2%80%93St._Bernard_de_Lacolle_Border_Crossing
[8] OSRM-demo (OSM), 2026-10-09: mijn → Walvis Bay 128,3 km via mijnweg/C28/MR44; Montreal → Metropolis ~1.900 km via Champlain; gebruikt voor via-coördinaten, niet als gepubliceerde km.
[9] FreightWaves / PortNews, CSAL-lancering 2008: multipurpose-dienst Montreal–Baltimore–Durban–Richards Bay–Kaapstad–Walvis Bay, Atlantic Impala; geen Montreal-berth genoemd. https://www.freightwaves.com/?p=183643
[10] MARNET dry-run `hecht_marnet.py route` (marnet-preais, 2026-10-09): Walvis Bay-kade → Montreal-kade 12.366,0 km, 1.266 punten, snaps 12,493 km (zeeknoop 8084) en 3,377 km (zeeknoop 6358); uitvoer in scratchpad, niet gebakken.
[11] Wikipedia, "C28 road (Namibia)": Windhoek–Swakopmund 319 km, grotendeels onverhard. https://en.wikipedia.org/wiki/C28_road_(Namibia)
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15+z16): `v2/build-cache/satcheck/sat-uranium-langerheinrich-metropolis-lh-fabriek16.png`, `…-lh-fabriek.png`, `…-lh-mijn.png` (sitelaag-punt).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
Recept: `bash v2/tools/bak_stromen.sh uranium-langerheinrich-metropolis` (functie `bak_uranium_langerheinrich_metropolis`) → `v2/data/stroomroute-uranium-langerheinrich-metropolis.json`, contract versie 2, **14.347,4 km · 28.213 punten · 4 benen · 4 markers · 571,0 KB**. Tussenuitvoer in `v2/build-cache/ais/graaf/uranium-langerheinrich-metropolis-*`.

| # | modaliteit | km gemeten | tegen brief | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 127,7 (636 pt) | OSRM-indicatie 128 (−0,3%); hemelsbreed 87 | 0 | doorgetrokken; snaps 0,02 / 0,28 km |
| b2a | zee | 12,5 (2 pt) | 12,5 MARNET-snap | 0 | **stippel**: haven-aanloop Walvis Bay, rechte lijn |
| b2b | zee | 12.366,0 (1.266 pt) | MARNET-dry-run 12.366,0; hemelsbreed 11.656 | 0 | 62 MARNET-edges, 0 track-edges |
| b3 | truck | 1.841,2 (26.309 pt) | OSRM ~1.900 / 1.894,5 (−3%); hemelsbreed 1.575 | **3,38** | doorgetrokken; snaps 0,21 / 0,03 km |

**Toets.** Geen wegkm gepubliceerd (b1, b3): de ±15%-toets is een indicatie en slaagt tegen de OSRM-waarde (b1 109–147, b3 1.615–2.185 km). Geen naad > 5 km; de enige naad is **3,38 km bij Montreal** (zee eindigt op zeeknoop 6358, truck begint op de kade; < 5 km dus geen aanloop, wel een zichtbaar procesgat). Markers liggen 0 m van hun lijn. `toets_knikken`: 85 knikken ≥ 60° (op weg, waar een lus of klaverblad echt kan zijn; niet nader bekeken), **0 omkeringen en 0 terugloop**; `toets_rechte_benen --min-km 5`: alleen de stippel (haven-aanloop, met reden). Segmentkm tegen hemelsbreed per b3-deel 1,07–1,16 (geen omweg door een via-punt).

**Toelichting stippel.** b2a is een rechte stippel van 12,5 km: de NamPort-kade ligt 12,5 km van MARNET-zeeknoop 8084 (> 5 km). `maak_havenaanloop.py` (timeout 300 s) gaf op 2026-10-09 opnieuw exit 124, geen tweede poging. Montreal ligt 3,4 km van zeeknoop 6358: geen aanloop. Geen vlucht, geen leiding, geen kopie van een bestaande stroom (het Walvis Bay-anker is hergebruikt, niet het been).

**Eindpunt.** Het stroom-id klopt met het werkelijke eindpunt (Metropolis Works).

**Lessen.**
- b1 had `corridorKlassen: [unclassified]` nodig (de mijnweg); `eindToegangPrivaat` voor de terminal. De scan van namibie duurt 7 s.
- b3 draaide met extracts canada (6,4 GB, 492 s), us-new-york, us-pennsylvania, us-ohio, us-kentucky, us-indiana, us-illinois via `wegscan_puur.py` (± 25 min totaal). Het geojson is **638 KB**, het stroombestand **571 KB** (boven de 300 KB-richtlijn, zoals de brief verwachtte).
- De route is van 2010 (NRC) en het VS-deel na Champlain is aannemelijk (I-81 → I-90 → I-71 → I-65 → WK Parkway); I-87 via Albany blijft ongetest.
- Sitelaag `w-langerheinrich` staat nog 0,8 km oost van het fabrieksanker (niet gewijzigd, aan de orkestrator gemeld).
