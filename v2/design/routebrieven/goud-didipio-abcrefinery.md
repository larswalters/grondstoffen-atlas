# Routebrief (licht) · Goud — Didipio → Manila → Sydney → ABC Refinery (Filipijnen → Australië)

**stroom-id:** `goud-didipio-abcrefinery` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** goud-doré van de Didipio-mijn en -verwerkingsplant (OceanaGold Philippines, Kasibu, Luzon) per truck over
Aritao en de Maharlika Highway (Dalton Pass, Cabanatuan-bypass, Jose Abad Santos Avenue, NLEX, Skyway) naar de internationale
vrachtterminal van Manila NAIA (MNL), per vrachtvlucht (grootcirkel, aannemelijk) naar de vrachtterminal van Sydney Airport (SYD) en per
truck over Airport Drive en de Princes Highway naar ABC Refinery in Marrickville (NSW).
**Welke as van het verhaal:** Filipijnen → Australië — tweede Filipijnse speler en tweede Australische raffinaderij (naast Perth Mint).
Volume **tot 2,82 t Au/j**: Didipio 2025 = 90,7 koz ÷ 32,15 [2], goud in doré én concentraat; het doré-aandeel is niet gepubliceerd
(30,54% van het doré ging in 2025 naar de centrale bank BSP [1]; concentraat gaat via Poro Point naar Transamine [1]).

## 1 · Ketenkaart
```
Didipio-mijn en -plant (OceanaGold), Kasibu `au-didipio-plant`
  ──(b1 truck · Kasibu → Aritao → Maharlika Hwy (Dalton Pass, Cabanatuan-bypass) → NLEX → Skyway · 372 wegkm [1]; OSRM 330)──►
Manila NAIA vrachtterminal (MNL) `au-mnl-vrachtterminal` (hergebruikt uit goud-masbate-metalor)
  ──(b2 lucht · vlucht MNL → SYD, grootcirkel, aannemelijk · ~6.261 km)──►
Sydney Airport vrachtterminal (SYD), Mascot `au-syd-vrachtterminal`  ·· stippel last mile airside (~0,1 km)
  ──(b3 truck · Link Road → Airport Drive → Princes Hwy → Marrickville Rd · hemelsbreed 2,2 km, OSRM 6,3)──►
ABC Refinery, Meeks Road, Marrickville `au-ref-abc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Didipio-plant → MNL-vrachtterminal | Didipio–Kasibu-weg → Aritao–Quirino Road → Maharlika Hwy (N1) → Felipe Vergara Hwy (Cabanatuan-bypass) → Jose Abad Santos Ave (N3) → NLEX (E1) → Skyway (E2) | wegkm **372** Didipio → Port of Manila (hoofdroute via Cabarroguis–Cordon) [1]; OSRM 330,3 over de Kasibu-route; hemelsbreed 208,9 | maak_stroombeen_weg (extract filipijnen) | nee; kop en staart ≤ 0,1 km van de weg |
| b2 | B | lucht | MNL → SYD | vrachtvlucht MNL → SYD (grootcirkel); **aannemelijk, geen bron** (TR: alleen "pre-agreed transportation arrangement") [1] | 6.261,3 grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b2s | B/C | truck | SYD-platform → Link Road | airside last mile (patroon goud-pamp-shanghai) | ~0,1 [berekend, OSRM nearest 99 m] | `--stippel` | **ja**, hier reikt het net niet |
| b3 | C | truck | Link Road (SYD) → ABC Marrickville | Link Rd → New Link Rd → Airport Dr → Marsh St → Flora St → West Botany St → Princes Hwy A36 → Railway Rd → Marrickville Rd → Meeks Rd | **hemelsbreed 2,2 km, geen wegkm**; OSRM 6,3 km (indicatie, geen norm) | maak_stroombeen_weg (extract australie) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-didipio-plant` | mijn / laadplek | Didipio-mijn en -verwerkingsplant, toegangsweg bij het dorp Didipio | 16.3351, 121.4581 | [1][4][5][sat] | **aannemelijk** (z15/z16 gezien: punt valt in de dorpskern Didipio aan de weg, 0,5–0,7 km NNO van de pitrand; plantgebouwen met tanks, pit en TSF liggen 0,3–1,5 km ZW; geen plantgebouw op het punt zelf). Pit volgens Wikipedia 16.3248, 121.4503 |
| `au-mnl-vrachtterminal` | overslag / lucht | Manila NAIA International Cargo Terminal | 14.5069, 121.0088 | [6][sat] | bron-gelegd (hergebruik letterlijk uit goud-masbate-metalor; z16 hier opnieuw gezien: wit loodsgebouw met tankpark ten O, apron ten Z; OSRM: NAIA Road op 66 m) |
| `au-syd-vrachtterminal` | overslag / lucht | Sydney Airport vrachtloods, W-rand, aan de Link Road | -33.9307, 151.1668 | [7][sat] | bron-gelegd (haalbaarheidstoets z16; hier z15/z16 gezien: langgerekt loodsgebouw met toestellen aan de apron-zijde, Link Road 0,1 km W); welk exploitantpand het is staat niet vast |
| `au-ref-abc` | raffinaderij / stoppunt | ABC Refinery (Pallion), Meeks Road, Marrickville | -33.9115, 151.1620 | [3][8][9][sat] | **aannemelijk** (z15/z16 gezien: industrieblok met pakhuizen, ca 150 m ten W van het spoor Sydenham–Marrickville; punt ligt op Meeks Road (OSM, 2 m), het gebouw is niet herkend; abcrefinery.com geeft geen straatadres) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; op de weg, niet in een stad)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | weg naar Kasibu, 2 km ONO van het centrum | 16.3326, 121.3068 | pint de zuidelijke toegang (TR: secundaire route via Kasibu) i.p.v. de noordelijke hoofdroute via Cabarroguis–Cordon [1] |
| b1 | 2 | Aritao–Quirino Road | 16.2855, 121.1826 | houdt de lijn op de weg naar Aritao, niet naar Bambang (TR noemt Bambang als alternatieve aansluiting) |
| b1 | 3 | Maharlika-junctie Aritao | 16.2988, 121.0384 | bindend uit de haalbaarheidstoets: hier komt de Kasibu-weg op de Maharlika Hwy |
| b1 | 4 | Maharlika Hwy, Dalton Pass | 16.1280, 120.9342 | de enige passage naar het zuiden; TR noemt de Dalton Pass als moeilijkste stuk [1] |
| b1 | 5 | Felipe Vergara Hwy (Cabanatuan-bypass) | 15.4783, 120.9269 | houdt de lijn op de bypass, niet door het centrum van Cabanatuan |
| b1 | 6 | Jose Abad Santos Ave (N3), Gapan–Pampanga | 15.2835, 120.8793 | corridorkeuze: via Pampanga naar de NLEX, niet via Tarlac en de SCTEX |
| b1 | 7 | NLEX (E1) | 14.9785, 120.7569 | zet de lijn op de snelweg naar Metro Manila |
| b1 | 8 | Skyway (E2) | 14.6365, 121.0086 | de Skyway naar NAIA i.p.v. EDSA door de stad |
| b3 | 1 | Airport Drive | -33.9267, 151.1666 | OSRM-route: ontsluit het platform via New Link Road en Airport Drive |
| b3 | 2 | Marsh Street | -33.9339, 151.1615 | route langs de zuidrand van de luchthaven |
| b3 | 3 | Princes Hwy (A36), begin | -33.9337, 151.1527 | de doorgaande weg naar Sydenham |
| b3 | 4 | Railway Rd, Sydenham | -33.9193, 151.1691 | kruising met het spoor naar Marrickville |
Alle punten zijn OSRM-wegvertices (OSM-data) op de gereden route; de snap in `maak_stroombeen_weg` beslist (> 5 km snap = fout gelegd).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Didipio-plant | OceanaGold Philippines (80%, 20% beursgenoteerd) | erts → doré + Cu-Au-concentraat | 1,48 Mt erts ontgonnen 2025; 90,7 koz Au [2] | [1][2] |
| ABC Refinery | Pallion, Marrickville | doré → LBMA-baren (goud en zilver) | niet gevonden | [1][3] |

## 6 · Stoppunt
De brief stopt bij ABC Refinery: het TR beschrijft dat ABC de baren op de metaalrekening van OGPI zet en dat OGPI ze kan terugkopen; een vervolg met naam en adres is niet gebrond, dus geen fase D en E.

## 7 · Open punten
- **Vervoer niet gebronnd.** Het TR zegt alleen "pre-agreed transportation arrangement and location" voor het doré naar ABC [1]; de weg naar Manila en de vlucht MNL → SYD zijn aanname. Cauayan (100 km over de weg, lijnvluchten naar Manila) en een directe vlucht vanaf een ander vliegveld zijn niet uitgesloten [1].
- **Hoofdroute versus gekozen route.** Het TR noemt als hoofdroute voor zwaar vervoer de weg vanuit het noorden via Cabarroguis en Cordon; de Kasibu-route is de secundaire (kleinere trucks) [1]. Gekozen is Kasibu–Aritao (bindende toets, kortste: OSRM 330 tegen 372 wegkm, -11%). Een pantserwagen past op de secundaire route.
- **Wegkm.** 372 km is naar de haven van Manila, niet naar NAIA; hemelsbreed Didipio–MNL is 208,9 km (het ontwerp noemde 270 km: dat is de TR-afstand tot "Manila" als stad).
- **Didipio-anker.** Het bindende punt ligt in het dorp; de plant zelf is op z16 ca 0,3-1,5 km ZW gezien, niet gelegd. Op site-niveau (< 2 km) geen last-mile-been.
- **Doré-aandeel onbekend**: 30,54% van het doré ging in 2025 naar BSP, de rest naar ABC en/of andere kopers [1]; het volume is een bovengrens.
- **ABC-adres.** Pallion-brochure 8 Meeks Road, White Pages en SGP 12 Meeks Road [9]; gebouw niet herkend. Beide liggen op dezelfde straat (< 0,2 km).
- **Sydney-terminal.** Welk pand op de westrand van het platform de vracht doet is op z16 niet vast te stellen; ook niet gevonden is een bron die goud per vlucht naar SYD noemt.
- Niet in de sitelaag: Didipio en ABC Refinery (centraal te beoordelen). Geen fase D/E: geen bron voor een afnemer na ABC.

## 8 · Bronnen
[1] OceanaGold, NI 43-101 Technical Report Didipio Mine (27-3-2026): §19.4.1 ABC Refinery (contract 28-3-2022, verlengd 1-4-2025 voor 3 jaar, "pre-agreed transportation arrangement"), §19.4.2 BSP (min. 25%, 30,54% in 2025), §19.5 Transamine/Poro Point, §5.2 toegang (hoofdroute via Cabarroguis, secundair via Kasibu), §5.4.5 Port of Manila 372 km, Poro Point 356 km. https://www.sec.gov/Archives/edgar/data/1487326/000162828026021651/exhibit9963-40xf.htm
[2] OceanaGold, FY2025 MD&A: Didipio 2025 goud 90,7 koz, koper 13,3 kt, erts 1.482 kt. https://www.sec.gov/Archives/edgar/data/1487326/000162828026021651/oceanagold-ex9911xmdafy202.htm
[3] ABC Refinery (a Pallion Company): Marrickville NSW 2204, enige onafhankelijke LBMA-geaccrediteerde goud- en zilverraffinaderij in Australië; geen straatadres. https://www.abcrefinery.com/
[4] Wikipedia, "Didipio mine": 16.32484, 121.45034 (pit), Kasibu, Nueva Vizcaya. https://en.wikipedia.org/wiki/Didipio_mine
[5] OpenStreetMap (ODbL) via Nominatim: Didipio (village) 16.3351396, 121.4581342. https://nominatim.openstreetmap.org
[6] `v2/design/routebrieven/goud-masbate-metalor.md`: anker `au-mnl-vrachtterminal` (14.5069, 121.0088); Wikipedia/OSM NAIA International Cargo Terminal.
[7] Haalbaarheidstoets goud-didipio-abcrefinery (M31 golf 20, bindend): Sydney-anker Link Road z16, OSRM SYD → ABC 6,3 km; OSRM Didipio → MNL 330 km.
[8] OpenStreetMap (ODbL) via Nominatim: Meeks Road, Marrickville -33.91147, 151.1620; OSRM-route (router.project-osrm.org, 2026-11-01): Didipio → NAIA 330,3 km en Link Road → Meeks Road 6,3 km, stappen en refs (Maharlika Highway 1, Jose Abad Santos Avenue 3, NLEX E1, Skyway E2, Princes Highway A36).
[9] Pallion-brochure (8 Meeks Road), White Pages en SGP (12 Meeks Road): zoals gemeld door de haalbaarheidstoets, zelf niet geopend.
[sat] `v2/build-cache/satcheck/sat-goud-didipio-abcrefinery-plant.png`, `-plant14.png`, `-plant16.png`, `-mnl.png`, `-syd.png`, `-syd16.png`, `-syd-vracht.png`, `-abc.png`, `-abc15.png` (Esri z14–z16, 2026-11-01).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`v2/data/stroomroute-goud-didipio-abcrefinery.json` (192,6 KB, versie 2, lonlat), functie `bak_goud_didipio_abcrefinery` in `v2/tools/bak_stromen.sh`,
profielen `goud-didipio-abcrefinery-plant-mnl` (extract filipijnen) en `goud-didipio-abcrefinery-syd-abc` (extract australie) in `maak_stroombeen_weg.py`.
Totaal 6.604,7 km, 4 benen, 4 markers (alle op 0,0 km van hun lijn). Alle naden 0,00 km.

| # | modaliteit | been | km gebakken | tegen brief | status |
|---|---|---|---|---|---|
| b1 | truck | Didipio-plant → MNL-vrachtterminal (Kasibu → Aritao → Maharlika Hwy → NLEX → Skyway) | 337,0 | 372 wegkm (naar Port of Manila, noordelijke route) = -9,4% | binnen ±15% |
| b2 | lucht | vlucht MNL → SYD (grootcirkel, aannemelijk: geen bron) | 6.261,3 | 6.261,3 berekend | doorgetrokken |
| b2s | truck | SYD-vrachtplatform last mile (airside) | 0,1 | 0,1 berekend | stippel: hier reikt het net niet |
| b3 | truck | Sydney Airport (Link Road) → ABC Refinery, Meeks Road | 6,3 | hemelsbreed 2,2, OSRM 6,3 (indicatie) | gelijk aan OSRM-indicatie |

**Recept.** b1: wegscan_puur op filipijnen (232 s), 10 via-punten uit §4 plus de twee ankers, refs 1/3/E1/E2, venster 40 km; alle via-snaps ≤ 0,01 km, staart 0,07 km, geen last-mile-stippel nodig.
b2: `maak_luchtbeen.py` MNL (14.5069, 121.0088) naar SYD (-33.9307, 151.1668), 252 punten. b2s: rechte `--stippel` van het platform (-33.9307, 151.1668) naar de Link Road (-33.9309, 151.1658) omdat het platform airside ligt (patroon goud-loulo-ticino).
b3: wegscan_puur op australie (238 s), venster 15 km, 4 via-punten, alle snaps ≤ 0,01 km. Geen zee, geen haven-aanloop, geen spoor, geen leiding, geen letterlijke kopie (MNL-anker wel hergebruikt uit goud-masbate-metalor).

**Toelichting.** (1) Vlucht en weg naar Manila zijn aanname: het TR noemt alleen een "pre-agreed transportation arrangement"; "aannemelijk: geen bron" staat in de beennaam, de lijn is doorgetrokken. (2) Het wegbeen b1 volgt bewust de secundaire Kasibu-route, niet de hoofdroute via Cabarroguis die de 372 km beschrijft; de -9,4% is dus een route-verschil, geen meetfout. (3) De stippel b2s is de enige in de keten en betekent alleen: airside, geen openbaar net.

**Bevindingen.** Knikkentoets b1: 1 omkering (167 gr, 28 m straal) bij 14.5522, 121.0105 voor NAIA, een korte ramp/afrit-lus van ca 0,3 km zonder terugloop; verder spikes van enkele meters (kruispunten), geen reparatie nodig. b1 eindigt met een kronkel (Skyway, Taft/NAIA Road) over de laatste 12 km, wegnet-gedrag, niet bijgeschoven. Didipio-anker blijft de dorpskern (plant 0,3-1,5 km ZW niet gelegd). ABC-gebouw en SYD-exploitant onbekend. Didipio en ABC ontbreken in de sitelaag (centraal).

**Lessen.** (a) Bash leest bak_stromen.sh incrementeel: een gelijktijdige edit door een andere agent gaf na de geslaagde bake een `syntax error near unexpected token` op een latere regel, terwijl `bash -n` daarna schoon is; het json stond al geschreven. (b) Een Filipijnse route van ca 340 km over de Maharlika Hwy scant in 4 min zonder extra klassen; wegscan_puur op australie (reus) kost ook 4 min bij 15 km venster. (c) Slot weg/slot1-2 waren bezet, slot3 vrij.

