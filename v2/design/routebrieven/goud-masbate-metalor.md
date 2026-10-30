# Routebrief (licht) · Goud · Masbate → Manila → Zürich → Metalor (Filipijnen → Zwitserland)

**stroom-id:** `goud-masbate-metalor` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** doré (ca 60% Au / 40% Ag) van de Masbate-verwerkingsplant (B2Gold/PGPRC, Aroroy) per truck over
N663/N664/N662 naar het vliegveld van Masbate City (MBT), per binnenlandse vlucht (grootcirkel, aannemelijk) naar de
vrachtterminal van Manila NAIA (MNL), per vrachtvlucht (grootcirkel, aannemelijk) naar de vrachtterminal van Zürich
Airport (ZRH), en per truck over A5/A1 naar de Metalor-raffinaderij in Marin-Epagnier (Neuchâtel).
**Welke as van het verhaal:** Zuidoost-Azië (Filipijnen) → Zwitserland — de B2Gold-doré-as. Volume **6,1 t Au/j**:
196.526 oz in 2025 [1] ÷ 32,15; doré ≈ 10,2 t (60% Au) [1][2]. Afnemer per bron Metalor; het vervoer is nergens beschreven.

## 1 · Ketenkaart
```
Masbate-verwerkingsplant (PGPRC), Aroroy `au-masbate-plant`
  ──(b1 truck · N663 via Aroroy–Baleno → N664/N662 · ~58 km router; 70 km gepubliceerd Masbate City–mijn)──►
Masbate City-vliegveld (MBT) `au-mbt-terminal`
  ──(b2 lucht · vlucht MBT → MNL, grootcirkel, aannemelijk · ~370 km)──►
Manila NAIA vrachtterminal (MNL) `au-mnl-vrachtterminal`
  ──(b3 lucht · vlucht MNL → ZRH, grootcirkel, aannemelijk · ~10.425 km)──►
Zürich Airport vrachtterminal (ZRH) `au-zrh-vrachtterminal` ·· stippel last mile 0,9 km (airside)
  ──(b4 truck · A1/A5 via Biel/Bienne · omgekeerde kopie · ~153 km)──►
Metalor SA, Marin-Epagnier `au-ref-metalor` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Masbate-plant → MBT | N663 (Aroroy–Baleno–Masbate City) → N664 → N662 [5] | wegkm **70** (Masbate City–mijn, NI 43-101 [2]); router ~58 (via Aroroy) resp. 55,0 (mijn-haulroad, toets) — beide buiten ±15%, bevinding | maak_stroombeen_weg (extract filipijnen) | nee (geen last-mile-stippel; snap eindpunt 0,11 km) |
| b2 | B | lucht | MBT → MNL | binnenlandse vlucht; **aannemelijk, geen bron**: lijnvluchten gaan nu alleen vanuit Clark/Cebu [2] | 369,8 grootcirkel [berekend] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | lucht | MNL → ZRH | vrachtvlucht MNL → ZRH; **aannemelijk, geen bron** voor de vlucht | 10.424,9 grootcirkel [berekend] | maak_luchtbeen | nee — doorgetrokken |
| b3s | C | truck | ZRH-platform → openbare weg | airside last mile (patroon goud-loulo-ticino) | 0,9 [bak goud-metalor-istanbul] | `--stippel` | **ja** — hier reikt het net niet |
| b4 | D | truck | ZRH openbare weg → Metalor Marin | A1 → A5 via Biel/Bienne (Solothurn) | 152,6 [kopie]; hemelsbreed 127 | **letterlijke kopie omgekeerd** van goud-metalor-istanbul b1 | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-masbate-plant` | mijn / laadplek | Masbate-verwerkingsplant (PGPRC), Aroroy, naast N663 | 12.4712, 123.3876 | [1][2][sat] | bron-gelegd (z16 gezien: molencomplex met silo's/tanks, proceshallen en sportveld, direct W van de pitterrassen, aan de N663). Toets-punt 12.4745,123.3835 viel op de dorpsrand W van de plant, 0,4 km verschoven |
| `au-mbt-terminal` | overslag / lucht | Masbate City (MBT, RPVJ), W-zijde van de baan | 12.3694, 123.6289 | [3][sat] | **onzeker** (z15/z16 gezien: korte NO–ZW-baan midden in de stad, geen vrachtloods of terminalgebouw te onderscheiden; punt = bebouwde W-rand van de baan, op straat bereikbaar) |
| `au-mnl-vrachtterminal` | overslag / lucht | Manila NAIA International Cargo Terminal | 14.5069, 121.0088 | [6][sat] | bron-gelegd (z16 gezien: groot wit-dakig loodsgebouw met luchtzijde-apron en tankpark, ZO van terminal 1; valt samen met OSM "International Cargo Terminal"; Cargohaus 14.5088,121.0086 ligt 0,2 km N) — airside, geen wegpad |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform | 47.4647, 8.5492 | [7] | bron-gelegd (hergebruik letterlijk uit goud-metalor-istanbul / pgm-springs-zurich) |
| `au-ref-metalor` | raffinaderij / stoppunt | Metalor SA, Marin-Epagnier | 47.0107, 7.0112 | [7][8] | bron-gelegd (hergebruik letterlijk uit goud-metalor-istanbul) |

## 4 · Via-punten (alleen b1; op de doorgaande weg, niet in Aroroy of Baleno zelf)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | N663 N van de plant | 12.4932, 123.3854 | pint de openbare N663 naar Aroroy i.p.v. de mijn-haulroad rond de put (unclassified, 16 km binnen het mijnterrein) |
| b1 | 2 | N663 O van Aroroy | 12.5000, 123.4635 | primary-knoop op de weg Aroroy–Baleno; sluit de haulroad naar Baleno uit |
| b1 | 3 | N663 Z van Baleno | 12.4569, 123.4961 | de enige doorgaande weg naar het zuiden; 1,9 km buiten het centrum |
| b1 | 4 | N663 | 12.4178, 123.5061 | houdt de lijn op de primary i.p.v. een zijweg |
| b1 | 5 | N663 zuidelijke bocht | 12.3198, 123.5536 | de weg buigt ten Z van Masbate City om; direct door het centrum bestaat niet |
| b1 | 6 | N664 | 12.3366, 123.5802 | overgang N663 → N664 → N662, richting het baanuiteinde |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Masbate-plant | PGPRC (B2Gold, 100%); mijn Filminera (B2Gold 40%) | erts → doré 60% Au / 40% Ag | 8,83 Mt erts/j, 2025 [1] | [1][2] |
| Metalor (Marin-Epagnier) | Metalor SA | doré → LBMA-baren | cap. ≈ 650 t/j (v1-register) | [8][v1] |

## 6 · Stoppunt
De brief stopt bij Metalor: fase D (afnemer van de baren) is niet gebrond; fase E vervalt. De Metalor-afnemer zelf staat in beide
B2Gold-documenten [1][2].

## 7 · Open punten
- **BINDEND VERWERKT (haalbaarheidstoets):** wegkm 70 (Masbate City–mijn) tegen router 55,0 (haulroad) / ~58 (via Aroroy): niet
  dichtgetrokken; de 70 km is naar Masbate City, niet vanaf de plant. Beide vluchten aannemelijk, lijn kan korter als ze worden afgewezen.
- **Geen enkele bron beschrijft hoe de doré vertrekt.** De NI 43-101 noemt een CAAP-airstrip met helikopterplatform en charters naar
  Manila (±1 uur) en de AIF een mijnairstrip voor personeel en onderdelen [1][2]; een airstrip NW van de plant is op z14 zichtbaar
  (ca 12.50,123.374), niet gelegd. Ook een kust-aanloop (Port Barrera-causeway, barges) is denkbaar. Gekozen is MBT per toets.
- **MBT-terminal onzeker** (geen vrachtloods); lijnvluchten naar Masbate City komen volgens de NI 43-101 uit Clark of Cebu, niet uit Manila [2].
- **Vlucht MNL → ZRH niet gebrond**; één directe vlucht aangenomen, geen tussenlanding.
- **Via-punten b1** zijn uit de OSM-refs 663/664 gelegd (Geofabrik-extract), niet verder gecontroleerd; de router bepaalt de ligging.
- ZRH-last-mile (47.4647,8.5492 → 47.472087,8.554523) is dezelfde stippel als in goud-metalor-istanbul/-loulo-ticino.
- Fase D/E vervallen: geen bron noemt een vervolg na Metalor.

## 8 · Bronnen
[1] B2Gold, Annual Information Form 2026 (peiljaar 2025): Masbate 196.526 oz; doré 60/40 geëxporteerd naar Metalor; 360 km ZO van Manila; Port Barrera-causeway; plant PGPRC. https://www.sec.gov/Archives/edgar/data/1429937/000110465926026310/tm266740d1_ex99-1.htm
[2] B2Gold, NI 43-101 Masbate Gold Project (nov 2025): 70 km deels verharde weg Masbate City–mijn; vluchten Clark/Cebu; CAAP-airstrip, charters naar Manila; doré naar Metalor (§1.3, §1.18). https://www.sec.gov/Archives/edgar/data/1429937/000110465925108345/tm2529659d1_ex99-1.htm
[3] Wikipedia, "Moises R. Espinosa Airport" (MBT/RPVJ): 12.3694, 123.6292. https://en.wikipedia.org/wiki/Moises_R._Espinosa_Airport
[4] Wikipedia (MediaWiki-API coördinaten): Masbate City 12.3739,123.6247 · Aroroy 12.5125,123.3989 · Baleno 12.4739,123.4982 · Milagros 12.2192,123.5089. https://en.wikipedia.org/wiki/Masbate_City
[5] OpenStreetMap (ODbL), Geofabrik-extract filipijnen: wegen met ref 663/664/662, haalbaarheidstoets-scan `gtoets-masbate`. https://www.openstreetmap.org
[6] OpenStreetMap/Wikipedia, NAIA: International Cargo Terminal 14.5069,121.0088 · Cargohaus 14.5088,121.0086 · luchthavenpunt 14.5083,121.0197. https://en.wikipedia.org/wiki/Ninoy_Aquino_International_Airport
[7] `v2/design/routebrieven/goud-metalor-istanbul.md` (M31 golf 4) en `goud-loulo-ticino.md` (M31 golf 3): ankers ZRH en Metalor, b1 Marin–ZRH, airside-stippel.
[8] Metalor SA, officiële site. https://www.metalor.com/
[v1] `data/goud.js` — au-ref-metalor cap. ≈ 650 t/j.
[toets] Haalbaarheidstoets goud-masbate-metalor (M31 golf 16, bindend): schrijf wegkm 70, router 55,0; ankers MBT/MNL eerst z15.
Satellietblik [sat]: `v2/build-cache/satcheck/sat-goud-masbate-metalor-plant.png`, `-plant15.png`, `-plant16.png`, `-mbt.png`, `-mbt16.png`, `-mnl.png`, `-mnlcargo.png` (Esri z14–z16, 2026-10-30).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
`bash v2/tools/bak_stromen.sh goud-masbate-metalor` → `v2/data/stroomroute-goud-masbate-metalor.json` (113,2 KB, versie 2, lonlat, 5 benen, 5 markers, 5.912 punten, totaal 11.007,2 km). Naden alle 0,000 km; alle markers 0,0 km van de lijn.

| # | modaliteit | km gebakken | km brief | beoordeling |
|---|---|---|---|---|
| b1 | truck (doorgetrokken) | 59,0 (wegtool 58,9) | wegkm 70 (Masbate City-mijn, niet vanaf de plant) | **-15,8%, buiten ±15%: bevinding**, niet dichtgetrokken. Hemelsbreed-indicatie, geen norm: de 70 km meet een ander traject |
| b2 | lucht MBT → MNL (doorgetrokken) | 369,8 | 369,8 berekend | grootcirkel, aannemelijk: geen bron |
| b3 | lucht MNL → ZRH (doorgetrokken) | 10.424,9 | 10.424,9 berekend | grootcirkel, aannemelijk: geen bron |
| b3s | truck stippel | 0,9 | 0,9 | ZRH-platform airside: hier reikt het net niet |
| b4 | truck (doorgetrokken) | 152,6 | 152,6 (kopie) | letterlijke omgekeerde kopie van goud-metalor-istanbul b1, geen tweede scan |

**Recept.** b1: profiel `goud-masbate-metalor-plant-mbt` (extract filipijnen, refs 663/664/662, 6 via-punten uit §4 ongewijzigd, venster 40 km, eindklassen default) via `wegscan_puur.py`; snaps plant 0,02 en MBT 0,03 km, via-snaps 0,00-0,01 km; first mile 0,81 km (service), last mile 0,45 km (residential), 1 keerlus gesnoeid. b2/b3: `maak_luchtbeen.py` (16 resp. 418 punten). b4: `goud-metalor-istanbul-weg-marin-zrh.geojson` met omgekeerde coordinaatvolgorde (begint 47.4721,8.5545, eindigt 47.0107,7.0112; id en naam aangepast, rest van de properties omgedraaid).

**Toelichting per stippel/vlucht.** Stippel b3s: dezelfde airside-last-mile als goud-loulo-ticino en goud-metalor-istanbul (47.4647,8.5492 → 47.472087,8.554523). Beide vluchten zijn doorgetrokken (geen gat); de aanname dat de doré per vlucht via MBT en MNL gaat is aannemelijk, niet gebrond, en staat in de beennamen. Geen haven-aanloop, geen zee, geen fase D/E.

**Lessen.**
- De gepubliceerde 70 km loopt van Masbate City naar de mijn; het bakken meet plant → vliegveld (59 km). Het verschil is een andere definitie, geen routefout; de via-punten bleven staan.
- toets_knikken meldt 22 knikken en 1 terugloop, alle in de gekopieerde Zwitserse b4 (zelfde als goud-metalor-istanbul) of spikes van 4-57 m in b1; geen reparatie nodig.
- MBT-terminal blijft onzeker (geen vrachtloods herkend); alternatief mijnairstrip NW van de plant niet gelegd.
- Alle wegscan-slots waren bezet bij de start: een wachtlus van 20 s per ronde volstond (circa 4 minuten).
