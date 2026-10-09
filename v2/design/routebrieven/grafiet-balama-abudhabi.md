# Routebrief (licht) · Grafiet · Balama (Mozambique) → Pemba → Khalifa Port (VAE)

**stroom-id:** `grafiet-balama-abudhabi` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet (-100 mesh fines) van de Balama-plant (Syrah) gaat per **truck** over N14/N1 naar de Pemba-kade, per **zeeschip** (haven-aanloop Pemba, MARNET over de Indische Oceaan, Arabische Zee en Hormuz) naar de Golf en via een tweede aanloop naar de containerkade van Khalifa Port, voor de nog te bouwen NextSource-anodefabriek in ICAD (aannemelijk: één bron voor de bestemming; Pemba en Khalifa door geen bron voor deze lading genoemd).
**Welke as van het verhaal:** reserve-voeding van de Golf-anodefabriek: Syrah-fines naast Molo-vlok, voorwaardelijk 7-jarig contract. Volume: **0 kt/j vandaag**; contract min ca. 34 kt, max ca. 68 kt over 7 jaar (ca. 5-10 kt/j), start op zijn vroegst 1 juni 2026 [1][2][3]. Eenheid kt grafiet per jaar, peiljaar plan 2026+.

## 1 · Ketenkaart
```
Balama-plant `gr-balama-plant` ──(b1 truck · N14 → Metoro → N1/EN106, LETTERLIJKE KOPIE grafiet-balama-kendal b1 · 260 km gebakken)──► Pemba-kade `gr-pemba-kade`
  ──(b2 haven-aanloop Pemba, STIPPEL, KOPIE · 58,8 km)──(b3 open water, STIPPEL, KOPIE · 242,4 km)──► zeeknoop 2193 (-12.0, 43.0)
  ──(b4 zee · MARNET, Indische Oceaan → Arabische Zee → Hormuz · 5.294,3 km)──► zeeknoop 8065 (24.5196, 54.3123)
  ──(b5 haven-aanloop Khalifa, STIPPEL, KOPIE · 48,3 km)──► Khalifa Port-containerkade `gr-khalifa-kade` ⏹ stoppunt
  (BAF in ICAD/Mussafah ± 50 km landinwaarts, niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-balama-plant` → `gr-pemba-kade` | N14 (Balama-Metoro) → N1/EN106 → Pemba; LETTERLIJKE KOPIE `grafiet-balama-kendal` b1 | 250-265 gepubliceerd [4]; gebakken 260,2 (kendal) | kopie `$BEEN/grafiet-balama-kendal-weg-balama-pemba.geojson` (`--been-geojson`) | nee |
| b2 | A | zee (aanloop) | `gr-pemba-kade` → (-12.9700, 41.0000) | Pemba-baai → open water oost; KOPIE `grafiet-balama-kendal` b2 | 58,8 over water | kopie `$BEEN/grafiet-balama-kendal-aanloop-pemba.geojson` (`--stippel-geojson`) | ja: MARNET reikt niet (dichtste zeeknoop 2148 ligt 261 km zuid) |
| b3 | A | zee (aanloop-vervolg) | (-12.9700, 41.0000) → zeeknoop 2193 | open water; KOPIE `grafiet-balama-kendal` b3 | 242,4 hemelsbreed (kendal-brief schreef 233, bake mat 242,4) | `--stippel` recht, -12.9700,41.0000 → -12.0000,43.0000 | ja: hier reikt het net niet |
| b4 | B | zee | zeeknoop 2193 → zeeknoop 8065 | MARNET kiest (Hormuz); *aannemelijk: één bron voor de bestemming* | **5.294,3** MARNET (proefrun 2026-10-09, 23 edges, snap 0,000); hemelsbreed 4.242; geen gepubliceerde lengte | `--been "zee\|…\|-12.0000,43.0000\|24.5196,54.3123"` | nee |
| b5 | B | zee (aanloop) | zeeknoop 8065 → `gr-khalifa-kade` | haven-aanloop Khalifa (kade 46,8 km van de knoop, > 25 km: router snapt niet); KOPIE `grafiet-molo-abudhabi` b4 | 48,3 over water (46,8 hemelsbreed) | kopie `$BEEN/grafiet-molo-abudhabi-aanloop-khalifa-rev.geojson` (reisrichting knoop → kade, `--stippel-geojson`) | ja: aanloop |

## 3 · Ankers (één per site en per overslag; alle vier LETTERLIJK hergebruikt)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-balama-plant` | mijn / laadplek | Balama-plant (Syrah/Twigg) | -13.3100, 38.6600 | [4][5] sitelaag `w-balama`, brief `grafiet-balama-kendal` §3 | bron-gelegd, hergebruik (z14 gezien in die brief: procesfabriek met bezinkvijvers en zonnepark) |
| `gr-pemba-kade` | overslag truck → zee | Porto de Pemba, breakbulk-kade | -12.9672, 40.4853 | [4][6] brief `grafiet-balama-kendal` §3 | bron-gelegd, hergebruik (z16 gezien daar: kade met schip langszij, blauwdak-loods, korte steiger; Syrah gebruikt Pemba voor al zijn verscheping). Dat DEZE lading via Pemba gaat staat in geen contractbron: aanname |
| `gr-pemba-baai` | naad aanloop → open-water-stippel (geen site) | Pemba-baai, open water | -12.9700, 41.0000 | [4] einde aanloop uit `grafiet-balama-kendal` | bron-gelegd (rekenpunt, geen site) |
| `gr-khalifa-kade` | losplek (containerkade) | Khalifa Port, container terminal, zuidoostkade | 24.8077, 54.6499 | [7][8] brief `grafiet-molo-abudhabi` §3 | **aannemelijk**, hergebruik (z16 gezien daar: kranenrij en stapels, containerschip langszij; kade bevestigd, haven door geen bron voor deze lading genoemd) |

Zeeknopen (MARNET, hergebruikt): 2193 (-12.0, 43.0) op 293 km van de Pemba-kade (58,8 + 242,4 = 301,2 km gestippeld); 8065 (24.5196, 54.3123) op 46,8 km van `gr-khalifa-kade`.
Satellietbeelden: bestaande `sat-grafiet-balama-kendal-{balama-plant,pemba-kade}.png` en `sat-grafiet-molo-abudhabi-khalifa*.png` in `v2/build-cache/satcheck/`; geen nieuwe opnames, geen nieuw anker.

## 4 · Via-punten
Geen eigen via-punten: b1 is een letterlijke kopie (het bestaande profiel `grafiet-balama-kendal-balama-pemba` gebruikt één via-punt, Metoro T-kruising N14 × N1, -13.1040, 39.8730, dat de keuze oost naar Pemba i.p.v. zuid naar Nacala pint); b2 t/m b5 zijn zee/aanloop.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Balama-plant | Syrah Resources | erts → vlokconcentraat | 67 kt geproduceerd / 55 kt verkocht in 2025; 2026 deels stilgelegd | [5][9] |
| Pemba breakbulk-kade (geen eigen been) | CFM / Grindrod, door Syrah gebruikt | zakken/bulk → schip | overcapaciteit | [6] |
| Battery Anode Facility, ICAD Abu Dhabi (niet gebouwd) | NextSource Materials | vlok (Molo primair, Syrah-fines aanvullend) → gecoat sferisch gezuiverd grafiet | 30 kt/j, fase 1 14 kt/j | [1][7] |

## 6 · Stoppunt
De lijn stopt bij de containerkade van Khalifa Port: de BAF ligt in een bestaande hal in ICAD zonder bekend perceel, dus een fase-D-anker zou een verzonnen coördinaat zijn; Khalifa is een aanname (zie `grafiet-molo-abudhabi` §6). Fase D en E vervallen.

## 7 · Open punten
- **Conditioneel, volume nul:** Syrah mag opzeggen als de voorwaarden (start commerciële productie BAF, kwalificatie van Syrah-grafiet) op 31 dec 2026 niet vervuld zijn, NextSource op 31 dec 2027; levering niet vóór 1 juni 2026 [1][2][3]. De fabriek is niet gebouwd. De weg is echt gemeten, de lading bestaat nog niet.
- **Pemba niet genoemd voor dit contract:** geen contractbron noemt een haven; Pemba is Balama's export-haven (AR2025 [6]) en dus de aanname. Idem Khalifa [8].
- **Overlap met twee andere ketens (bewust):** kop = `grafiet-balama-kendal` (b1-b3), eind = `grafiet-molo-abudhabi` (b5). Nieuw is alleen de zeeleg 2193 → 8065 (5.294,3 km); die valt grotendeels samen met `grafiet-molo-abudhabi` b3 ten noorden van 11 graden zuid. Laag prioriteit, valt visueel deels samen: bewust als reservestreng van een andere afzender (Syrah, niet NextSource-Molo).
- **Hormuz:** sinds 28 feb 2026 grotendeels geblokkeerd, wisselende heropeningen [10]; de lijn is de structurele route, geen waarneming.
- **Balama 2026 deels stilgelegd** (Q2 2026: 2,3 kt gemaakt, productie uitgesteld naar Q3) [9].
- **Weg-km:** b1 is een kopie; 260,2 gebakken tegen 250-265 gepubliceerd, binnen de toets. Afstand Pemba-kade tot zeeknoop 2193 is 301,2 km gestippeld (kendal-brief noemde 293 + 58,8 los).
- **Geen vlucht, geen leiding, geen spoor.**

## 8 · Bronnen
[1] NextSource Materials / Investing News Network, 2 mrt 2026 (binding agreement, min ca. 34 kt, tot 68 kt fines, 7 jaar, voorwaarden, opzegrechten 31 dec 2026 / 2027). https://www.investingnews.com/nextsource-materials-signs-agreement-for-the-supply-of-graphite-fines-as-additional-source-of-feedstock-for-its-battery-anode-facility-in-abu-dhabi/
[2] Club of Mozambique, 4 mrt 2026 (Balama-graphite naar Abu Dhabi, 34.000-68.000 t over zeven jaar, start "next June", daarna Japanse klant). https://clubofmozambique.com/news/mozambique-syrah-resources-to-supply-graphite-to-japan-aim-report/
[3] Engineering News / Mining Weekly, "Syrah secures seven-year Balama offtake with NextSource", 2 mrt 2026 (start niet vóór 1 juni, -100 mesh 94% C, prijs per kwartaal). https://www.engineeringnews.co.za/article/syrah-secures-seven-year-balama-offtake-with-nextsource-2026-03-02
[4] Atlas: `v2/design/routebrieven/grafiet-balama-kendal.md` (b1-b3, ankers Balama-plant, Pemba-kade, Pemba-baai; §9 gebakken).
[5] Atlas: `v2/design/grafiet-sitelaag.json` (`w-balama`).
[6] Syrah Resources, 2025 Annual Report (mrt 2026): Pemba-verscheping, kade, offtake NextSource. https://www.datocms-assets.com/65260/1774572803-syr_2025_annual_report.pdf (via [4] [1]; PDF te groot voor directe fetch)
[7] Atlas: `v2/design/routebrieven/grafiet-molo-abudhabi.md` (b3/b4, anker Khalifa-kade, BAF-kader, bronnen [1][4][5] daarin).
[8] Wikipedia, Khalifa Port (alle containerverkeer Abu Dhabi). https://en.wikipedia.org/wiki/Khalifa_Port
[9] Syrah Resources, kwartaalcijfers 2026 (Q2 2026: 7 kt verkocht, productie uitgesteld naar Q3), via https://kalkinemedia.com/au/news/announcements/syrah-resources-defers-balama-production-to-q3-2026-amid-soft-demand-and-advances-vidalia-anode-facility
[10] Wikipedia, 2026 Strait of Hormuz crisis. https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis
[11] MARNET-proefrun zeeknoop 2193 → 8065 (`hecht_marnet.py route`, 2026-10-09, scratch-uitvoer, geen bundelbestand): 5.294,3 km, 23 edges, 544 punten.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Uitvoer:** `v2/data/stroomroute-grafiet-balama-abudhabi.json` (49,1 KB, versie 2, lonlat) · **5 benen · 5.904,0 km · 2.434 punten · 4 markers** · functie `bak_grafiet_balama_abudhabi` in `v2/tools/bak_stromen.sh`. Geen nieuw profiel, geen extract, geen scan.

| # | modaliteit | km gemeten | tegen brief | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 260,2 | 250-265 (binnen) | - | LETTERLIJKE KOPIE kendal b1, doorgetrokken; hemelsbreed geen wegkm, indicatie |
| b2 | zee, stippel | 58,8 | 58,8 | 0,00 | KOPIE kendal b2, haven-aanloop Pemba, MARNET reikt niet |
| b3 | zee, stippel | 242,4 | 242,4 hemelsbreed | 0,00 | rechte stippel open water naar zeeknoop 2193, hier reikt het net niet |
| b4 | zee | 5.294,3 | 5.294,3 proefrun | 0,00 | MARNET 2193 naar 8065, 23 edges, 544 punten, snap 0,000 beide kanten, doorgetrokken, aannemelijk |
| b5 | zee, stippel | 48,3 | 48,3 | 0,00 | KOPIE molo-abudhabi b4 (omgekeerd, knoop naar kade), haven-aanloop Khalifa |

**Markers (4, alle 0,0 km van de lijn):** `gr-balama-plant` (-13.3100, 38.6600) · `gr-pemba-kade` (-12.9672, 40.4853) · `gr-pemba-baai` (-12.9700, 41.0000) · `gr-khalifa-kade` (24.8077, 54.6499). Alle naden 0,00 km.

**Recept:** b1 `--been-geojson` op `grafiet-balama-kendal-weg-balama-pemba.geojson` · b2 `--stippel-geojson` op `grafiet-balama-kendal-aanloop-pemba.geojson` · b3 `--stippel` -12.9700,41.0000 naar -12.0000,43.0000 · b4 `--been zee` -12.0000,43.0000 naar 24.5196,54.3123 · b5 `--stippel-geojson` op `grafiet-molo-abudhabi-aanloop-khalifa-rev.geojson`. Bake 16 s, geen herberekening van de kopieen.

**Toelichting.**
- **Stippel (b2, b3, b5):** uitsluitend "hier reikt het net niet": Pemba heeft binnen 261 km geen zeeknoop (b2+b3 = 301,2 km), en Khalifa ligt 46,8 km van knoop 8065 (b5). b4 is een gemeten, doorgetrokken zeebeen.
- **Aannemelijk (b4, b5):** doorgetrokken; de onzekerheid (Pemba en Khalifa door geen contractbron genoemd) staat in de beennamen en in deze brief. b4 heeft geen gepubliceerde lengte; hemelsbreed 4.242, MARNET 5.294,3.
- **Volume nul:** contract voorwaardelijk (opzegrecht 31 dec 2026), fabriek niet gebouwd, Balama 2026 deels stilgelegd. De weg is gemeten, de lading nog niet; dat staat in de tekst, niet in de lijnstijl. Hormuz grotendeels geblokkeerd: structurele route.
- **Geen vlucht, geen leiding, geen spoor, geen fase D/E.**
- **toets_knikken:** 8 knikken, 0 omkeringen, 0 terugloop; de spikes zitten in de gekopieerde kade-omgeving van Pemba (OSM-zigzag), de twee bochten op zee zijn routeruitvoer (110 gr bij 24,799N 53,953E, 70 gr bij 22,70N 60,40E). **toets_rechte_benen --min-km 5:** alleen b3 (242,4 km, omwegfactor 1,000) en dat is een stippel met reden.
- **Contract:** versie 2, punt_formaat lonlat, modaliteiten {truck, zee}, elk been >= 2 punten.

**Lessen / aandachtspunten.**
- Volledig kopie-gedreven keten: bakken kost seconden zodra de bronstromen bestaan; controleer de reisrichting van een gekopieerde aanloop (de Khalifa-kopie moet de `-rev`-variant zijn).
- Overlap met `grafiet-balama-kendal` (b1-b3) en `grafiet-molo-abudhabi` (b5) is bewust; alleen 2193 naar 8065 is nieuw en valt deels samen met `grafiet-molo-abudhabi` b3 ten noorden van 11 graden zuid.
