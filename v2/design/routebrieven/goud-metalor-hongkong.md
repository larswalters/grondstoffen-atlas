# Routebrief (licht) · Goud · Metalor Marin (Zwitserland) → Zürich → Hongkong → Metalor Yuen Long (Hongkong)

**stroom-id:** `goud-metalor-hongkong` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** LBMA-goudbaren van Metalor in Marin-Epagnier (Neuchâtel) per truck naar de vrachtterminal van Zürich
Airport (ZRH, letterlijke kopie van `goud-metalor-istanbul`), per vrachtvlucht (grootcirkel) naar de Cathay-vrachtterminal van
Hongkong (HKG, Chek Lap Kok), en per truck over het Tuen Mun-Chek Lap Kok Link, Tuen Mun Road en Yuen Long Highway naar
Metalor Precious Metals Hong Kong, 61 Fuk Hi Street, Yuen Long Industrial Estate.
**Welke as van het verhaal:** Zwitserland → Hongkong, de Aziatische bullionhub: Hongkong is een vaste top-bestemming van de
Zwitserse goudexport. Zwitserse douane via Reuters/Kitco, 2024: jan 44,6 t, mrt 10,2 t, apr 7,7 t (≈6% van de Zwitserse export
in april) [4][5]. Jaarsom niet gevonden (orde 50–100 t); Metalor-aandeel niet gepubliceerd. **Eenheid t Au/j: niet vast te stellen.**

## 1 · Ketenkaart
```
Metalor, Marin-Epagnier `au-ref-metalor` (hergebruikt uit goud-metalor-istanbul.md)
  ──(b1 truck · A5 Biel/Bienne → Solothurn → A1 · 152,6 km, LETTERLIJKE KOPIE goud-metalor-istanbul b1)──►
Zürich Airport vrachtterminal `au-zrh-vrachtterminal` (hergebruikt; airside, last mile b2 = stippel-kopie, 0,9 km)
  ──(b3 lucht · vlucht ZRH → HKG, grootcirkel, aannemelijk · 9.281 km)──►
Cathay Pacific Cargo Terminal, Chek Lap Kok `au-hkg-vrachtterminal` (hergebruikt anker dia-hkg-cargo)
  ──(b4 truck · Tuen Mun-CLK Link → Tuen Mun Road → Yuen Long Highway · hemelsbreed 20,5 km, geen wegkm; aannemelijk)──►
Metalor Hong Kong, Yuen Long Industrial Estate `au-metalor-hk-yuenlong` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | Metalor Marin → ZRH-vrachtplatform (openbare-wegpunt) | A5 Biel/Bienne → Solothurn → A1 (kopie `goud-metalor-istanbul` b1) | 152,6 [gebakken, zelfde been] | kopie geojson `goud-metalor-istanbul-weg-marin-zrh` | nee |
| b2 | B | truck | ZRH-openbare weg → ZRH-vrachtplatform | airside last mile (kopie `goud-metalor-istanbul`) | 0,9 [gebakken, zelfde stippel] | `--stippel` 47.472087,8.554523 → 47.4647,8.5492 | **ja** — airside/privéterrein, geen net |
| b3 | B | lucht | Zürich (ZRH) → Hongkong (HKG) | vrachtvlucht grootcirkel — **aannemelijk: één bron** (Swiss valuables-vervoerder noemt luchtvracht van goudbaren Zwitserland → Hongkong [6]), geen bron voor déze lading | 9.281,4 [berekend, grootcirkel] | maak_luchtbeen | nee — doorgetrokken |
| b4 | D | truck | HKG-vrachtterminal → Metalor Hong Kong, Yuen Long | Tuen Mun-Chek Lap Kok Link, Tuen Mun Road, Yuen Long Highway (Route 9) | **hemelsbreed 20,5 km, geen wegkm**; OSRM-indicatie 27,2 [9]; wegscan 26,6 (−2% op OSRM, indicatie) | maak_stroombeen_weg (extract china) | nee — doorgetrokken (aannemelijk: vestiging bewezen, zending niet) |

b1+b2 zijn bewuste kopieën (gedeeld been met een bestaande stroom, bakhandleiding §2). Het ontwerp stelde een aparte HKG-airside-
stippel voor; die is overbodig: de wegscan vindt vanaf het Cathay-anker binnen 0,3 km openbare weg (Chun Wan Road).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-ref-metalor` | raffinaderij / laadplek | Metalor SA, Marin-Epagnier | 47.0107, 7.0112 | [1][10] | bron-gelegd — letterlijk hergebruikt uit `goud-metalor-istanbul.md` (z15 daar gezien: industrieel complex aan A5/spoor bij Marin, aan het meer van Neuchâtel) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform | 47.4647, 8.5492 | [10] | bron-gelegd — letterlijk hergebruikt (loodsgebouw + vrachtplatform, O van de hoofdterminal); wegbeen eindigt op 47.472087, 8.554523 |
| `au-hkg-vrachtterminal` | overslag / lucht | Cathay Pacific Cargo Terminal, Chek Lap Kok (HKG) | 22.2975, 113.9247 | [8][10] | bron-gelegd — letterlijk hergebruikt `dia-hkg-cargo` uit `diamant-surat-hongkong.md`; hier z15 opnieuw gezien: vrachtloodsen op het zuidelijke eilandplatform vlak bij Chun Wan Road, wide-body-toestellen op het apron ernaast |
| `au-metalor-hk-yuenlong` | raffinaderij / losplek | Metalor Precious Metals Hong Kong Ltd, 61 Fuk Hi Street, Yuen Long Industrial Estate | 22.4580, 114.0230 | [1][2][3][7] | **aannemelijk** (z15+z17 gezien: dicht industrieblok van Yuen Long Industrial Estate, platte loodsdaken en zonnepanelen, ZW-rand aan Fuk Hi Street; kruis op een groot plat dak; geen naambord leesbaar; adres 61 niet gegeocodeerd — buurnummer 55-57 ligt op 22.4577, 114.0228) |

Adres en naam zijn per bron bewezen (vestigingenlijst [1], LBMA-auditrapport 2024 [3]); of déze vestiging de Wing Fung-fabriek
uit de overname van 2023 is, noemt het persbericht niet [2] — alleen de vestigingenlijst legt het adres.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b4 | 1 | Tuen Mun-CLK Link, tunnelweg (noordoever Lantau) | 22.3140, 113.9593 | pint de route over het Link (westelijk) en sluit de Tsing Ma-corridor (Kowloon) uit |
| b4 | 2 | Tuen Mun Road (Route 9), na de Wong Chu Road-aansluiting | 22.3872, 113.9787 | óp de doorgaande Route 9, niet in het stadscentrum van Tuen Mun |
| b4 | 3 | Yuen Long Highway (Route 9) | 22.4138, 113.9803 | pint de noordelijke hoofdroute naar Yuen Long, niet de Castle Peak Road-omweg |

Punten uit OSRM-stappen (OSM-bron, óp wegvertex) [9]. b1: geen eigen via-punten (kopie van `goud-metalor-istanbul`, waar Bern is
verwijderd). Het ZRH-wegbeen eindigt op de openbare weg.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Metalor Marin | Metalor SA (Tanaka-groep) | doré/schroot → LBMA-baren | cap. ≈ 650 t/j (v1-register) | [1][v1] |
| Metalor Hong Kong, Yuen Long | Metalor Precious Metals Hong Kong Ltd | goud (smelten/evaluatie, vooral goudraffinage, Aziatische klanten) → baren, halffabricaten | niet gepubliceerd | [2][3] |

## 6 · Stoppunt
De brief stopt bij Metalor Hong Kong in Yuen Long: dat is het enige gedocumenteerde Metalor-adres in Hongkong; geen bron volgt
een zending verder naar een afnemer, dus fase E vervalt.

## 7 · Open punten
- **Geen bron dat Marin-baren naar Metalor Hong Kong gaan.** Vestiging bewezen, zending niet; het eindanker is daarom aannemelijk,
  en bij twijfel eindigt de keten bij de HKG-terminal. Een LBMA-raffinaderij in Hongkong ontvangt vooral doré/schroot, dus de
  zending van afgewerkte baren uit Marin is een aanname (intern transfer/voorraadpositie).
- **Of nr 61 de Wing Fung-fabriek is** (overname 31-03-2023) volgt alleen uit de vestigingenlijst; het persbericht noemt geen adres [2].
- **Swiss → Hongkong-aandeel niet geverifieerd:** drie maanden uit eigen lezing (Reuters/Kitco); de overige maanden van 2024 en een
  jaarsom niet bevestigd; zoekresultaten noemden feb 9,8 t, mei 1,6 t en jun 5,0 t, die ik niet zelf heb kunnen openen.
- **Vlucht ZRH → HKG** is niet voor déze lading gebrond: aangenomen als één directe vrachtvlucht (geen tussenlanding gebrond).
  Bron [6] is een vervoerder die haar eigen dienst noemt; [7] noemt alleen vluchten HK–Singapore en een kluis op de luchthaven.
- **b4-lengte:** alleen hemelsbreed 20,5 km en een OSRM-indicatie 27,2 km; het ontwerp (35–45 km) is hoger dan beide. De ±15%-toets
  is een indicatie, geen norm.
- **Adres nr 61 Fuk Hi Street niet gegeocodeerd**; anker op de straat bij de buurpercelen 55-57. Pandniveau onzeker.
- **Fase E vervalt**; geen last-mile-been in Yuen Long (anker ligt aan Fuk Hi Street).

## 8 · Bronnen
[1] Metalor, "Global presence" — Hong Kong: Metalor Precious Metals Hong Kong Ltd, No. 61 Fuk Hi Street, Yuen Long Industrial Estate, Yuen Long, N.T.; Marin: Route des Perveuils 8. https://metalor.com/global-presence/
[2] Metalor, "New Refinery of Metalor in Hong Kong" (31-03-2023) — overname van de raffinaderij van Wing Fung Precious Metals Ltd, naam Metalor Technologies Hong Kong Ltd; geen adres, geen volumes. https://metalor.com/new-refinery-of-metalor-in-hong-kong/
[3] Forvis Mazars / Metalor, LBMA Responsible Gold Guidance compliance report 2024, Metalor Precious Metals Hong Kong Ltd — raffinaderijlocatie No. 61 Fuk Hi Street, Yuen Long Industrial Estate; smelt- en evaluatiediensten voor Aziatische klanten, vooral goudraffinage; LBMA-lid sinds 2008. https://metalor.com/wp-content/uploads/2020/06/Metalor-HK_LBMA-Gold-_Audit-Report_2024_signed_wo.pdf
[4] Reuters via MarketScreener, "Swiss April gold exports fall on lower shipments to China" — Hongkong mrt 2024 10.173 kg, apr 7.710 kg (apr 2023 5.088 kg); totaal apr 123.590 kg (Zwitserse douane). https://www.marketscreener.com/news/latest/Swiss-April-gold-exports-fall-on-lower-shipments-to-China-46899411/
[5] Kitco, "Swiss gold exports hit six-year highs on demand from China and India" (21-02-2024) — Hongkong jan 2024 44,6 t. https://www.kitco.com/news/article/2024-02-21/swiss-gold-exports-hit-six-year-highs-demand-china-and-india
[6] Helveticor (Zwitserse waardevervoerder), "Hong Kong: Swiss precision and local expertise" — luchtvracht van goudbaren Zwitserland → Hongkong als dienst; eigen aanbod, geen volumes. https://helveticor.ch/en/blog/extended-presence-swiss-precision-and-local-expertise-in-hong-kong/
[7] SWI swissinfo.ch, "Investors pull gold from Hong Kong as tensions rise" — goud wordt vaak per vliegtuig verplaatst (HK–Singapore); een grote kluis bij de luchthaven (alleen via zoeksamenvatting gelezen). https://www.swissinfo.ch/eng/business/switzerland-bound_investors-pull-gold-from-hong-kong-as-tensions-rise/45234022
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15, z17, 2026-10-09): `v2/build-cache/satcheck/sat-goud-metalor-hongkong-hkgcargo.png`, `sat-goud-metalor-hongkong-yuenlong.png`, `sat-goud-metalor-hongkong-yuenlong-z17.png`.
[9] OSRM (router.project-osrm.org, OSM-gebaseerd, 2026-10-09) — HKG-cargo → Fuk Hi Street 27,2 km via Chek Lap Kok Road, Tuen Mun-CLK Tunnel Road, Tuen Mun Road/Yuen Long Highway (Route 9), Long Ping Road; stappunten als via-punten; geen publicatie, dezelfde bron als het wegnet.
[10] Bestaande brieven: `goud-metalor-istanbul.md` (b1, ZRH-stippel, ankers `au-ref-metalor`, `au-zrh-vrachtterminal`) en `diamant-surat-hongkong.md` (anker `dia-hkg-cargo`, 22.2975/113.9247).
[osm] OpenStreetMap/Photon (ODbL) — Fuk Hi Street (22.4627/114.0241, Tai Tseng Wai), Yuen Long Textile Co. 55-57 Fuk Hi Street (22.4577/114.0228). https://www.openstreetmap.org
[v1] `data/goud.js` — au-ref-metalor cap. ≈ 650 t/j.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-goud-metalor-hongkong.json` (105,2 KB, contract versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh goud-metalor-hongkong` (functie `bak_goud_metalor_hongkong`; b4 via `wegscan_puur.py --profiel goud-metalor-hongkong-hkg-yuenlong`, extract china, met de pure-Python PBF-wrapper `goud-metalor-hongkong-wegscan-wrapper.py` omdat pyosmium geblokkeerd is; b3 via `maak_luchtbeen.py`; b1+b2 kopie).

| # | modaliteit | km (bake) | punten | toets |
|---|---|---|---|---|
| b1 | truck | 152,6 | 4.256 | letterlijke kopie `goud-metalor-istanbul-weg-marin-zrh.geojson`, gelijk aan de bron (152,6) |
| b2 | truck (stippel) | 0,9 | 2 | kopie van de ZRH-airside-stippel 47.472087,8.554523 naar 47.4647,8.5492 |
| b3 | lucht (doorgetrokken) | 9.281,4 | 373 | grootcirkel ZRH naar HKG, gelijk aan de brief (9.281,4) |
| b4 | truck | 26,6 | 895 | indicatie: OSRM-indicatie 27,2 km = -2%; hemelsbreed 20,5 km (geen wegkm, dus geen norm); alle 4 segmenten snappen ≤ 0,05 km |

Totaal 9.461,5 km · 5.526 punten · 4 markers (alle op 0,0 km van de lijn) · naden b1→b2 / b2→b3 / b3→b4 0,000 km · geen haven-aanloop, geen zeebeen.

- **b4 (wegtool):** segmenten 5,2 / 10,8 / 3,0 / 7,6 km; alle drie via-punten (Tuen Mun-CLK Link, Tuen Mun Road, Yuen Long Highway) hielden, geen enkel verplaatst of geschrapt. Totaal 26,6 km tegen hemelsbreed 20,5 km (factor 1,3): geen omweg. Tuen Mun-centrum en Yuen Long-centrum zijn vermeden. First mile 0,97 km en last mile 0,59 km over kleine klassen (service, tertiary, residential, unclassified), anker-stubs 0,05 en 0,03 km. 22 keerlussen gesnoeid (26,6 naar 26,5 km); de scan duurde 589 s.
- **Stippel (b2):** alleen de ZRH-airside-last-mile (0,9 km), een kopie van `goud-metalor-istanbul`; airside/privéterrein zonder net. Een HKG-airside-stippel is niet nodig: vanaf het Cathay-anker ligt de openbare weg (Chun Wan Road) binnen 0,05 km.
- **Vlucht (b3):** DOORGETROKKEN, beennaam "vlucht ZRH → HKG (vrachtvlucht, grootcirkel, aannemelijk: één bron voor Zwitserland → Hongkong, niet voor déze lading)". Aannemelijkheid zit in de naam en in §7, niet in de lijnstijl. Beide ankers zijn vrachtterminals.
- **Kopie (b1+b2):** letterlijk hetzelfde geojson en dezelfde stippel als `goud-metalor-istanbul`; de beennaam noemt het gedeelde been. De knikken van dat bronbeen (spikes bij 47.01025,7.01143 en 47.45308,8.57235, 32-37 m) zijn niet aangeraakt.
- **Knikken (`toets_knikken.py`):** b4 heeft 9 knikken ≥ 60 graden en 0 omkeringen, allemaal korte OSM-spikes van 4-42 m op de terminalwegen van Chek Lap Kok en bij het eindanker (Fuk Hi Street); b3 heeft er 0. De ene omkering/terugloop in het totaaloverzicht hoort bij een andere stroom. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom.
- **Aannemelijk:** het eindanker (vestiging bewezen, zending niet) en de vlucht (geen bron voor déze lading); zie §7. Zwitserland naar Hongkong: de jaarsom en het Metalor-aandeel zijn onbekend.
- **Lessen:** (1) een pure-Python PBF-wrapper voor `wegscan_puur.py` werkt als pyosmium geblokkeerd is, maar een reus-extract als china kost ruim 9 minuten: draai hem op de achtergrond met een logbestand; (2) bij een luchthavenanker eerst het wegbeen laten scannen: Chek Lap Kok gaf een wegpad van 0,05 km, dus geen airside-stippel; (3) `bak_stromen.sh` is een LF-bestand (0 CR gecontroleerd) en `maak_stroombeen_weg.py` heeft zijn eigen regeleinden.
