# Routebrief (licht) · goud — Fidelity (Harare) → HRE → DMCC Dubai (VAE)

**stroom-id:** `goud-fidelity-dubai` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** goud(baren) van de staatsraffinaderij Fidelity (Reserve Bank of Zimbabwe, Msasa, Harare) per truck naar de vrachtterminal van Harare (HRE), per vrachtvlucht (grootcirkel, aannemelijk op landniveau) naar de vrachtterminal van Dubai (DXB), en per truck over Sheikh Zayed Road (E11) naar de DMCC-goudzone — het laatste been is een letterlijke kopie van `goud-tarkwa-dubai` b3.
**Welke as van het verhaal:** *Zimbabwe → Dubai, de staatsraffinaderij als bron* — alle Zimbabwaanse mijngoud gaat wettelijk naar Fidelity (enige koper, raffineerder en exporteur) [1][5]. Volume **36,5 t Au/j** (2024, leveringen aan Fidelity: Herald 36,48 t, Business Times 36,8 t; 2023: 30,1 t) [6]. Bronnen over de Dubai-as beschrijven vooral smokkel, niet het formele Fidelity-pad: dat de baren per vlucht naar Dubai gaan is aannemelijk op landniveau, niet per zending gebrond (§7).

## 1 · Ketenkaart
```
Fidelity Gold Refinery, 1 George Drive, Msasa `au-fidelity-refinery`
  ──(b1 truck · George Drive → R5 → Robert Mugabe Rd → Glenara Ave S → Vitalis Zvinavashe Rd → Joshua Nkomo Rd · hemelsbreed 9,1 km, geen wegkm)──►
Harare (HRE) vrachtterminal `au-hre-cargo` (= `dia-hre-cargo`, hergebruikt)
  ──(b2 lucht · vrachtvlucht HRE → DXB, grootcirkel, aannemelijk: landniveau · 5.471,7 km)──►
Dubai Intl (DXB) vrachtterminal `au-air-dxb-cargo` (hergebruikt uit goud-tarkwa-dubai)
  ──(b3 truck · Sheikh Zayed Road (E11) · 38,4 km, LETTERLIJKE KOPIE goud-tarkwa-dubai b3)──►
DMCC-goudzone `au-dmcc-refine` (hergebruikt) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Fidelity (Msasa) → HRE-vrachtterminal | George Drive → R5 (Harare–Mutare Hwy) → Robert Mugabe Rd → Glenara Ave S → Vitalis Zvinavashe Rd → Joshua Nkomo Rd (luchthavenweg) [11] | hemelsbreed 9,1 km, geen wegkm (OSRM-indicatie ~16 km [11]; de ±15%-toets is indicatie, geen norm) | maak_stroombeen_weg | nee (evt. korte last-mile-stippel bij de HRE-poort, zie §7) |
| b2 | B | lucht | HRE-vrachtterminal → DXB-vrachtterminal | vrachtvlucht HRE → DXB, grootcirkel — **aannemelijk: landniveau (Zimbabwe naar VAE 97% edelmetaal, 2,63 mld USD 2024)** [4] | 5.471,7 grootcirkel [berekend] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | DXB-vrachtterminal → DMCC-goudzone | Sheikh Zayed Road (E11), via Trade Centre Roundabout en Mall of the Emirates | 38,4 [gebakken, `goud-tarkwa-dubai` b3] | kopie geojson `goud-tarkwa-dubai-weg-dxb-dmcc.geojson` | nee |

Geen tussenlanding op b2: geen bron noemt een hub (aanname, §7). Geen claim over formele Fidelity-export per vlucht.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-fidelity-refinery` | raffinaderij / start | Fidelity Gold Refinery (FPR), 1 George Drive, Msasa Industrial, Harare | -17.8408, 31.1078 | [1][3] | **aannemelijk** (z16 + z18 gezien: dicht industrieel blok met loodsen aan George Drive, punt ligt op de straat; geen naambord of terreinomheining herkenbaar, dus welk pand Fidelity is niet te zien; adres uit [1], OSM-straat way 28988926 op -17,84083/31,10782 [3]) |
| `au-hre-cargo` | vrachtterminal (truck → lucht) | Robert Gabriel Mugabe Intl (HRE), vrachtloods landzijde, Harare — hergebruikt uit `diamant-marange-dubai.md` (`dia-hre-cargo`) | -17.9218, 31.0946 | [7][8] | bron-gelegd (eigen z18: grote witte loods met parkeer-/laadfront aan de landzijde, direct O ervan een apron met een breedromptoestel; exploitant niet bevestigd) |
| `au-air-dxb-cargo` | vrachtterminal (lucht → truck) | Dubai Intl (DXB), Emirates SkyCargo (Cargo Village) — hergebruikt uit `goud-tarkwa-dubai.md` | 25.2560, 55.3431 | [9] | bron-gelegd (z18 in die brief: dakopschrift Emirates SkyCargo, vrachttoestellen op de tarmac) |
| `au-dmcc-refine` | raffinagezone / eind | DMCC-goudzone, Al Etihad Gold Refinery — hergebruikt uit `goud-tarkwa-dubai.md` | 25.0602, 55.1352 | [9] | bron-gelegd (z18 in die brief; vertegenwoordigt de zone, niet één bedrijf) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Punten zijn wegmanoeuvre-locaties van OSRM/OSM [11] op de doorgaande weg, nergens in het centrum van Harare; de bak-agent controleert de snaps (> 5 km = fout gelegd).
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | R5 Harare–Mutare Highway | -17.8365, 31.1078 | de enige arterie waar het Msasa-blok op uitkomt; pint de oostzijde (niet door de CBD) |
| b1 | 2 | Robert Mugabe Rd / Glenara Ave S | -17.8340, 31.0874 | corridor verlaat de R5 naar het zuidwesten, pint de keuze tegenover een route via het centrum |
| b1 | 3 | Vitalis Zvinavashe Rd | -17.8448, 31.0746 | doorgaande verbindingsweg naar de luchthavenweg |
| b1 | 4 | Joshua Nkomo Rd (rotonde) | -17.8687, 31.0733 | begin van het lange rechte stuk zuidwaarts naar HRE |
| b1 | 5 | Joshua Nkomo Rd, afslag luchthaven | -17.9116, 31.0953 | laatste doorgaande-weg-punt vóór de aansluiting op het vrachtgebied |
b3: via-punten van `goud-tarkwa-dubai` (kopie, geen eigen via-punten).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fidelity Gold Refinery (Msasa) | Reserve Bank of Zimbabwe | doré/mijngoud → baren (400 oz) en fijn goud | oorspronkelijk 50 t/j (1987), LBMA-accreditatie 1989; doorzet 2024 ≈ 36,5 t [1][6] | [1][6] |
| DMCC-goudzone (Dubai) | div. (Al Etihad, Emirates Gold, Kaloti) | baren → herverfijnd/gestempeld goud | zone, geen bedrijfscijfer | `goud-tarkwa-dubai` [9] |

## 6 · Stoppunt
De brief stopt bij de DMCC-goudzone: geen bron koppelt Fidelity-baren aan één raffinaderij of afnemer in Dubai; fase D en E vervallen. Het begin is bewust de raffinaderij (geen mijn): alle Zimbabwaanse mijnen leveren aan Fidelity, geen enkele wordt als aparte stroom getekend.

## 7 · Open punten
- **Formele Fidelity-vlucht niet gebrond.** Bronnen over Zimbabwe → Dubai gaan over smokkel (Al Jazeera 2023, Zimbabwe Gold Mafia: couriers met handbagage, goud in Dubai geraffineerd en gestempeld [2][5]) en een aangehouden koerier op HRE (2020, 6 kg naar Dubai [10]). Dat Fidelity-baren per vrachtvlucht gaan is aannemelijk op landniveau (97% van 2,72 mld USD export naar de VAE in 2024 is edelmetaal/-steen [4]) maar niet per zending of vliegtuig gebrond; het kan ook belly-cargo of een koerier zijn.
- **Fidelity-anker alleen op adres** (1 George Drive, Msasa [1]) en OSM-straat: status aannemelijk, geen naambord op z18; het exacte pand is een open punt.
- **Geen wegkm** voor Msasa → HRE gepubliceerd: alleen hemelsbreed 9,1 km en een OSRM-indicatie (~16 km); gemeten wegkm uit de bake is leidend.
- **HRE-exploitant onbevestigd** (geen naambord); HRE-landzijde kan "geen wegpad" geven (airside-patroon: wegbeen eindigt op de dichtstbijzijnde openbare weg + korte stippel "HRE-vrachtplatform last mile (schematisch — airside/privéterrein)"). `diamant-marange-dubai` routeerde dit anker zonder stippel.
- **Dubai-aandeel van Fidelity niet gepubliceerd**; de waarde 2,63 mld USD ≈ 34 t Au bij ~2.400 USD/oz is mijn eigen indicatieve omrekening (en bevat ook edelstenen), geen bronwaarde. CNRG-schatting van ~3 t/maand illegaal [2] is niet verenigbaar met 36,5 t totaal en niet gebruikt.
- **Overlap:** b2 ligt vrijwel op `diamant-marange-dubai` b2 (andere grondstof, eindpunt 0,3 km verschil); b3 is bewust gedeeld met `goud-tarkwa-dubai`.
- **Bronnen mengen smokkel en formeel:** de ketenkaart tekent het formele pad; sancties (VS/VK 2024 op personen rond de Gold Mafia [2]) beïnvloeden de bewijslast niet.

## 8 · Bronnen
[1] Wikipedia, "Fidelity Printers and Refiners" — RBZ-eigendom, Msasa, 1 George Drive; goudraffinaderij sinds 1987, LBMA 1989. https://en.wikipedia.org/wiki/Fidelity_Printers_and_Refiners
[2] Wikipedia, "Zimbabwe Gold Mafia" — Al Jazeera 2023, Fidelity-betrokkenheid, CNRG ~3 t/maand, sancties 2024. https://en.wikipedia.org/wiki/Zimbabwe_Gold_Mafia
[3] OpenStreetMap (ODbL) via Photon — George Drive, Harare, way 28988926, -17,84083/31,10782. https://photon.komoot.io
[4] Trading Economics (UN Comtrade) — Zimbabwe-export naar de VAE 2024: 2,72 mld USD, waarvan 2,63 mld (96,7%) parels/edelstenen/metalen. https://tradingeconomics.com/zimbabwe/exports/united-arab-emirates
[5] Al Jazeera, 30-03-2023 — "How Zimbabwe uses gold smuggling to evade sanctions": Fidelity, gouden baren per courier naar Dubai. https://www.aljazeera.com/news/2023/3/30/how-zimbabwe-uses-gold-smuggling-to-evade-sanctions-choke
[6] The Herald (Zimbabwe), "Gold sector defies odds, surpasses target" — record 36,48 t in 2024 (2023: 30,1 t); Business Times (36,8 t leveringen aan Fidelity) via allAfrica. https://www.heraldonline.co.zw/gold-sector-defies-odds-surpasses-target-2/ · https://businesstimes.co.zw/gold-soars-to-record-highs/
[7] `v2/design/routebrieven/diamant-marange-dubai.md` — anker `dia-hre-cargo` -17,9218/31,0946, tevens HRE→DXB-grootcirkel 5.471,7 km.
[8] Wikipedia, "Robert Gabriel Mugabe International Airport" (IATA HRE). https://en.wikipedia.org/wiki/Robert_Gabriel_Mugabe_International_Airport
[9] `v2/design/routebrieven/goud-tarkwa-dubai.md` — ankers DXB (25,2560/55,3431) en DMCC (25,0602/55,1352) en b3 (38,4 km, `goud-tarkwa-dubai-weg-dxb-dmcc.geojson`).
[10] Sowetan (Reuters-credit), 26-10-2020 — Zimbabwaanse koerier met 6 kg goud naar Dubai op HRE aangehouden. https://www.sowetan.co.za/news/south-africa/2020-10-26-zimbabwean-mining-boss-headed-for-dubai-with-6kg-gold-in-her-luggage/
[11] OSRM publieke demo (OSM-gebaseerd), route Msasa → HRE, 16,0 km, manoeuvrelocaties als via-punten. https://router.project-osrm.org
[12] Miningmx (Reuters), 29-06-2021 — FPR "sole buyer, refiner and exporter of gold"; Dubai hoofdbestemming van uitgevoerd goud (ICG). https://www.miningmx.com/news/gold/46591-large-gold-producers-in-zimbabwe-permitted-to-export-portion-of-output-directly/
Satellietblik (Esri z16/z18, 2026-10-09): `v2/build-cache/satcheck/sat-goud-fidelity-dubai-fidelity.png`, `…-fidelity-z18.png`, `…-hre-cargo.png`, `…-hre-cargo-z18.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-goud-fidelity-dubai.json` (24,6 KB, contract versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh goud-fidelity-dubai` (functie `bak_goud_fidelity_dubai`; b1 via `wegscan_puur.py --profiel goud-fidelity-dubai-fidelity-hre`, extract zimbabwe; b2 via `maak_luchtbeen.py`; b3 kopie).

| # | modaliteit | km (bake) | punten | toets |
|---|---|---|---|---|
| b1 | truck | 15,2 | 292 | indicatie: OSRM ~16 km = −5%; hemelsbreed 9,1 km (geen wegkm, dus geen norm); alle 6 segmenten snappen ≤ 0,04 km |
| b2 | lucht (doorgetrokken) | 5.471,7 | 220 | grootcirkel, gelijk aan de brief (5.471,7) |
| b3 | truck | 38,4 | 671 | letterlijke kopie `goud-tarkwa-dubai-weg-dxb-dmcc.geojson`, gelijk aan de bron (38,4) |

Totaal 5.525,3 km · 1.183 punten · 4 markers (alle op 0,0 m van de lijn) · naden b1→b2 0,000 / b2→b3 0,000 km · geen stippel, geen haven-aanloop.

- **b1 (wegtool):** profiel `goud-fidelity-dubai-fidelity-hre` direct onder de ankerregel in `maak_stroombeen_weg.py` (venster 20 km, `eindToegangPrivaat`, zonder `corridorKlassen`). Alle via-punten uit §4 hielden; geen enkel verplaatst of geschrapt. Segment-km tegen hemelsbreed: 0,6/0,5 · 2,3/2,1 · 2,1/1,5 · 3,3/2,7 · 5,3/4,9 · 1,5/1,1, dus geen omweg. Anker-stubs 0,02 km (Fidelity) en 0,04 km (HRE).
- **Geen airside-stippel:** de brief (§7) vreesde "geen wegpad" bij het HRE-vrachtplatform. Gemeten: het landzijde-anker `au-hre-cargo` ligt 0,04 km van een openbare servicestraat; het wegbeen sluit er rechtstreeks op aan (eindklassen service/unclassified over de laatste 1,4 km). Daarom geen korte stippel; wie de vrachtloods zelf wil laten eindigen op het apron kan dat later als een losse stippel toevoegen.
- **Lengte:** 15,2 km tegen de OSRM-indicatie ~16 km is −5%; de tool meldt "+68,6% BUITEN ±10%" omdat hij tegen de hemelsbrede 9 km toetst. Dat is het verwachte gedrag voor een hemelsbreed gepubliceerdKm en geen bevinding over de route (brief §2: toets = indicatie).
- **Vlucht (b2):** DOORGETROKKEN, naam "vlucht HRE → DXB (vrachtvlucht, grootcirkel; aannemelijk: landniveau)". Aannemelijkheid zit in de beennaam en §7, niet in de lijnstijl. Beide ankers zijn vrachtterminals (HRE `dia-hre-cargo`, DXB Cargo Village), geen startbaanmidden. Ligt vrijwel op `diamant-marange-dubai` b2 (eindpunt 0,3 km verschil) en dat is bewust.
- **Kopie (b3):** letterlijk hetzelfde geojson als `goud-tarkwa-dubai` b3; de beennaam noemt het gedeelde been. De bijbehorende knikken horen bij dat bronbeen en zijn hier niet aangeraakt.
- **Knikken (`toets_knikken.py`):** b1 heeft 15 knikken ≥ 60° en 1 omkering (172° bij −17,8409/31,1080, 10 m van het anker, afslag George Drive → R5, gemeten pad ÷ hemelsbreed 1,6 = echte scherpe bocht, geen terugloop). Alle andere knikken zijn korte OSM-spikes van 3–130 m op kruispunten. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom (b2 is per constructie recht en wordt overgeslagen).
- **Lessen:** (1) bij een airport-landzijde-anker eerst het wegbeen laten scannen vóór je een airside-stippel inplant: HRE gaf wel een wegpad; (2) `maak_stroombeen_weg.py` is een CRLF-bestand en `bak_stromen.sh` een LF-bestand, dus voeg per bestand met de eigen regeleinden in (LF-controle bak_stromen.sh: 0 CRLF); (3) `/tmp` in Git Bash is niet `/tmp` in Python op Windows, dus schrijf een tussenbestand naar de scratchpad.
