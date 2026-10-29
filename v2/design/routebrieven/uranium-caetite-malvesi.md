# Routebrief (licht) · Uranium · INB Caetité → Salvador → Hamburg → Orano Malvési (Brazilië → Frankrijk)

**stroom-id:** `uranium-caetite-malvesi` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) ·
**status:** gebakken
**Keten in één zin:** Braziliaans yellowcake (U₃O₈ in vaten, 12 containers) gaat per **truck** van de INB-concentratiefabriek bij Caetité (Bahia) over BA-262, BR-116 en BR-324 naar de containerkade van Salvador, per **zeeschip** (MV Sea Bird in de planning van 2012) over de Atlantische Oceaan, het Kanaal en de Noordzee naar Hamburg (C. Steinweg Süd-West), en per **trein** via de Hamburg–Malvési-corridor naar Orano Malvési (Narbonne) — **aannemelijk: één bron, een voorgenomen zending die in 2012 is teruggedraaid** [1].
**Welke as van het verhaal:** *Braziliaanse concentraat naar de Franse conversie.* Nameplate 340 t U/j (WNA) [4]; 2013: 192 t U [4]. Zending 2012: 178 t U₃O₈ in 12 containers (≈ 150 t U) [1]; 2007: 300 t U₃O₈ in 21 carretas (≈ 254 t U) naar Salvador [2]. Geen routevolume; sinds feb 2025 gaat 275 t concentraat contractueel naar Internexco (Rosatom), route niet gepubliceerd [4].

## 1 · Ketenkaart
```
INB-fabriek Caetité `u-caetite-ura` ──(b1 A truck · BA-262 → BR-116 → BR-324 · gepubliceerd 757 km, OSRM 775)──►
  Salvador-containerkade `u-salvador-tecon` ──(b2a zee haven-aanloop 9,4 km, stippel)──► MARNET-zeeknoop 5092 (-12.8761, -38.5291)
  ──(b2b zee · Atlantisch → Kanaal → Noordzee → Elbe · 9.005 km MARNET, getest)──► Hamburg Süd-West `u-hamburg-steinweg`
  ──(b3 C spoor · letterlijke kopie uranium-walvisbay-malvesi · ~1.750 km)──► Orano Malvési `u-malvesi` ── stoppunt
```
**Afwijkingen t.o.v. het ontwerp:** (a) laadanker = de INB-fabriek (-13.8357, -42.2813), niet de groeve Mina Cachoeira: INB noemt Cachoeira als voormalige dagbouw, de mijn in bedrijf heet Engenho [3]; (b) kade = TECON-containerkade (-12.9580, -38.5083) i.p.v. het havengebied-punt; (c) zeeknoop snapt op 9,4 km (ontwerp 9,7): aanloop verplicht; (d) wegnummers uit de bronnen kloppen niet: de router rijdt BA-262 (Caetité–Vitória da Conquista), geen BR-030.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `u-caetite-ura` → `u-salvador-tecon` | BA-569/BA-152 → BA-262 (Brumado) → BR-116 Vitória da Conquista → BR-116 Jequié → Feira de Santana → BR-324 → Salvador — **aannemelijk: bronnen noemen alleen Feira de Santana [1]; de rest is de router-corridor** | 757 (Bahia-overheid 2007, vanaf Caetité-stad) [2]; OSRM-indicatie 775 (OSM, geen onafhankelijke bron) | maak_stroombeen_weg (extract brazilie) | nee |
| b2a | B | zee (haven-aanloop) | `u-salvador-tecon` → zeeknoop 5092 | schematisch, over de Baía de Todos os Santos | 9,4 (MARNET-snap) | rechte stippel (`maak_havenaanloop.py` gaf in de haalbaarheidstoets na 300 s niets, geen tweede poging) | ja — het net reikt niet tot de kade |
| b2b | B | zee | `u-salvador-tecon` → `u-hamburg-steinweg` | Atlantische Oceaan, Kanaal, Noordzee, Elbe; MV Sea Bird [1] | hemelsbreed 8.702; MARNET 9.005 (getest) | MARNET (`--been zee`) | nee — Hamburg snap 4,14 km (< 5 km) |
| b3 | C | spoor (aannemelijk: één bron per stuk) | `u-hamburg-steinweg` → `u-malvesi` | Rollbahn Bohmte–Hamm–Köln–Koblenz–Mosel–Metz–Dijon–Miramas–Narbonne | geen spoorkm gepubliceerd; gemeten ≈ 1.749 (kopie) | **letterlijke kopie** van de 9 spoorbenen van `uranium-walvisbay-malvesi` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-caetite-ura` | laadplek (concentratiefabriek) | INB Unidade de Concentrado de Urânio, Fazenda Cachoeira, Caetité | -13.8357, -42.2813 | [3] (Fazenda Cachoeira, 1.700 ha); positie via haalbaarheidstoets | bron-gelegd (z15 gezien: grote dagbouw West, ernaast verwerkingsterrein met laagbouw, vijvers en drie bassins; kruis staat op het fabrieksterrein) |
| `u-salvador-tecon` | overslag weg → zee | Porto de Salvador, TECON-containerkade | -12.9580, -38.5083 | [1][2] (Porto de Salvador); kade volgens satelliet, terminal niet gebronnd | aannemelijk (z15 gezien: containerstapels, portaalkranen en kade op het havenschiereiland; welke terminal laadt uranium is niet gepubliceerd) |
| `u-hamburg-steinweg` | overslag zee → spoor | C. Steinweg Süd-West-Terminal, Hamburg | 53.5335, 9.9868 | letterlijk uit `uranium-walvisbay-malvesi` §3 [5] | bron-gelegd (daar z15 gezien) |
| `u-malvesi` | conversie, stoppunt | Orano Malvési (Comurhex I), Narbonne | 43.2074, 2.9812 | letterlijk uit `uranium-walvisbay-malvesi` §3 / `w-malvesi` [5] | bron-gelegd (daar z15 gezien) |

## 4 · Via-punten (alleen b1; allemaal OP de doorgaande weg, ver van stadscentra)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | BA-262, westrand Brumado (begin van het 108,8 km-stuk BA-262; ±2 km van het centrum, niet erin) | -14.2089, -41.6522 | corridor Caetité → Vitória da Conquista via BA-262; pint de zuidroute (zonder via-punten kiest de router BA-148/BR-242: 667 km via een andere corridor) |
| b1 | 2 | BR-116 / BA-262-aansluiting zuid van Vitória da Conquista | -14.8296, -40.8305 | bron-corridor "Vitória da Conquista" (ontwerp); omzeilt het stadscentrum via de BR-116-bypass |
| b1 | 3 | BR-116 bij Jequié-zone | -13.8517, -40.1141 | BR-116 noordwaarts i.p.v. de BA-/BR-101-alternatieven; houdt de lijn op de BR-116 tot Feira |
| b1 | 4 | BR-116 / BR-324-aansluiting Feira de Santana | -12.2733, -38.9343 | bron noemt Feira de Santana [1]; punt op de BR-324-oprit, niet in het centrum; pint BR-324 naar Salvador |
Refs (zachte voorkeur): BA-262, BR-116, BR-324. Extract: `brazilie` (Geofabrik). Het eerste/laatste via-punt van het profiel zijn de ankers `u-caetite-ura` en `u-salvador-tecon`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| INB Caetité (URA) | INB | erts → U₃O₈-concentraat | nameplate 340 t U/j; 2013: 192 t U | [3][4] |
| Orano Malvési | Orano | U₃O₈ → UF₄ | nameplate ~15.000 t U/j (indicatief, sitelaag) | [5] |

## 6 · Stoppunt
De brief stopt bij Orano Malvési: dat is het eindpunt van het ontwerp en de vervolgstap UF₄ → Tricastin staat al in `uranium-malvesi-tricastin`. Fase D/E vervallen.

## 7 · Open punten
- **Eén bron voor Hamburg en Malvési:** O Eco (2012) noemt "Hamburgo" en "a usina de Malvési" als bestemming van een voorgenomen zending [1]; de zending is gestopt (Franse voorafmelding van 15 dagen ontbrak) en teruggereden naar Caetité. Er is geen uitgevoerde Hamburg-route gepubliceerd; het spoor Hamburg–Malvési is de corridor van een ándere herkomst (Namibië, activistenbronnen).
- **Actualiteit:** sinds 2025 gaat Caetité-concentraat contractueel naar Internexco/Rosatom [4]; de huidige route is niet gepubliceerd. Peiljaar van de lijn: 2012.
- **Wegnummers staan niet in de bronnen:** alleen Feira de Santana [1] en "757 km, Caetité-stad → Salvador" [2]. BA-262/BR-116/BR-324 komen uit OSRM/OSM; de brief-kilometer is een bedrijfs/overheidsopgave, de lengtetoets is een indicatie.
- **Salvador-kade niet op berth-niveau:** TECON volgens satelliet; welke terminal uranium laadt is onbekend. Aanloop 9,4 km is een rechte stippel (aannemelijk over water; MARNET/1:10M kent de baai niet).
- **Hamburg-snap 4,14 km:** geen aanloop; naad zee→spoor ≈ 4,2 km blijft staan (norm < 5 km).
- **Laadplek:** Mina Cachoeira (groeve, -13.8326, -42.2908) niet als anker gebruikt; Engenho (huidige mijn) niet gelegd.

## 8 · Bronnen
[1] O Eco, "Carga de urânio de Caitité vai e volta pelas estradas da Bahia" (12 juli 2012: 12 containers, 178 t, MV Sea Bird, Hamburgo, Malvési, Feira de Santana, RSB Logistic, teruggedraaid) https://oeco.org.br/noticias/26257-carga-de-uranio-de-caitite-vai-e-volta-pelas-estradas-da-bahia/
[2] Governo da Bahia (SEINFRA), "Longa viagem do urânio baiano" (8 okt 2007: 300 t U₃O₈, 21 carretas, Caetité → Porto de Salvador 757 km, PRF-escorte) https://www.ba.gov.br/infraestrutura/noticia/2024-03/1980/longa-viagem-do-uranio-baiano
[3] INB, Onde estamos: Caetité (Fazenda Cachoeira, 1.700 ha, mijn Cachoeira voormalig, Engenho in bedrijf, concentraat per truck naar Salvador en per schip naar Europa) https://www.inb.gov.br/A-INB/Onde-estamos/Caetite
[4] World Nuclear Association, Brazil (Caetité 340 t U/j, 2013: 192 t U, Internexco-contract feb 2025: 275 t) https://world-nuclear.org/information-library/country-profiles/countries-a-f/brazil
[5] `v2/design/routebrieven/uranium-walvisbay-malvesi.md` (Hamburg Steinweg, Malvési, 9 spoorbenen, aanloop-patroon); `v2/design/uranium-sitelaag.json` `w-malvesi`
[haalbaarheidstoets] Bindend invoerdocument: OSRM 667 km zonder via-punten, 775,6 km met; zeeknoop 5092; MARNET 9.005 km; Hamburg-snap 4,14 km; aanloop maak_havenaanloop timeout 300 s.
[OSRM] router.project-osrm.org, controle 2026-10-29: Caetité-fabriek → Vitória da Conquista → Feira de Santana → TECON = 774,5 km (BA-569, BA-152, BA-262, BR-116, BR-324); refs per stuk uit de stappen.
[sat] Esri World Imagery (`v2/tools/sat_check.py` z15): `v2/build-cache/satcheck/sat-uranium-caetite-malvesi-ura-fabriek.png`, `…-salvador-tecon.png`

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`v2/data/stroomroute-uranium-caetite-malvesi.json` (295,6 KB, versie 2, lonlat) · functie `bak_uranium_caetite_malvesi` in `bak_stromen.sh` · profiel `uranium-caetite-malvesi-ura-salvador` in `maak_stroombeen_weg.py`. 12 benen, 11.535,6 km, 15.394 punten, 4 markers (u-caetite-ura, u-salvador-tecon, u-hamburg-steinweg, u-malvesi).

| # | modaliteit | km | naad | beschrijving |
|---|---|---|---|---|
| 1 | truck | 772,7 | 0 | INB-fabriek Caetité → Salvador TECON (gemeten, 7.925 punten) |
| 2 | zee, stippel | 9,4 | 0 | haven-aanloop Salvador → zeeknoop 5092 (rechte stippel) |
| 3 | zee | 9.004,9 | 0 | Salvador-kade → Hamburg Steinweg (MARNET) |
| 4-12 | spoor | 1.749,6 | 4,17 (zee→spoor) | negen letterlijke kopieën uit uranium-walvisbay-malvesi |

**Recept.** b1: `wegscan_puur.py --profiel uranium-caetite-malvesi-ura-salvador` (extract brazilie, 4 via-punten uit §4, refs BA-262/BR-116/BR-324, gepubliceerdKm 757, **vensterKm 75**). b2a: rechte stippel kade → zeeknoop 5092, geen `maak_havenaanloop`-run (timeout 300 s in de haalbaarheidstoets, geen tweede poging). b2b: MARNET `--been zee` kade → kade. b3: negen `--been-geojson`-regels, letterlijke kopie van de spoorgeojsons van walvisbay-malvesi, geen nieuwe spoorrouter-run.

**Toets.** b1 772,4 km tegen 757 (Bahia 2007) = +2,0%, OSRM 775 = -0,3% (norm ±15%, hier een indicatie: wegnummers komen uit OSRM/OSM). Plant → weg 0,17 km, weg → kade 0,13 km, first mile 6,2 km kleine klassen. Naden: alle 0 behalve zee → spoor 4,17 km (Hamburg-snap, < 5 km, in de brief verwacht). Markers 0,0-0,11 km van hun lijn. `toets_knikken`: truck 12 spikes van enkele meters bij via-punten/ankers (geen omkering), zee één krappe bocht (Atlantisch, R 5,5 km), spoor twee terugloop-knikken bij Narbonne (43.1870, 3.0011), geërfd van de kopie en al bekend in de walvisbay-brief. `toets_rechte_benen`: alleen de bedoelde aanloopstippel (9,4 km). json.load, versie 2, punt_formaat lonlat, modaliteiten {truck, zee, spoor}, elk been ≥ 2 punten.

**Toelichting stippel/aanloop.** Eén stippel, b2a: de TECON-kade ligt 9,4 km van de MARNET-zeeknoop (-12.8761, -38.5291); het net reikt niet tot de kade. Geen luchtbeen, geen leiding.

**Lessen.** (1) Eerste scan met vensterKm 40 gaf 872 km (+15%): BR-116 via Milagres ligt ~52 km west van de rechte lijn tussen via-punt 3 (Jequié) en 4 (Feira), dus buiten het venster; de router nam een omweg van +100 km (359,7 km i.p.v. 259,8). Oplossing: vensterKm 75 (de brief gaf 40-75), geen via-punt bijgeschoven. (2) Bestand 295,6 KB zit net onder de ~300 KB-grens (7.925 weg-punten).

**Afwijkingen t.o.v. het ontwerp.** Geen: het eindpunt is Orano Malvési zoals het id belooft. Open punten blijven die van §7 (één bron, peiljaar 2012, Caetité ontbreekt in `uranium-sitelaag.json`).
