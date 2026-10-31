# Routebrief (licht) · PGM — Ngezi → Platinum Highway → Selous (Zimbabwe)

**stroom-id:** `pgm-ngezi-selous` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat van het **Ngezi-complex** (Zimplats, Mhondoro-Ngezi, Great Dyke) per **truck** over de
**Ngezi-Selous Road ("Platinum Highway")** naar de **Selous-rotonde op de A5** en vandaag naar de **Zimplats Selous Metallurgical Complex
(SMC)**, waar het in de boogoven tot matte wordt gesmolten; één landbeen, geen zee, geen luchtbeen, geen fase D/E (het vervolg naar Springs
staat in `pgm-zimplats-springs`).
**Welke as van het verhaal:** de mijnkant van de Zimbabwaanse matte-keten: waar het concentraat vandaan komt voordat het de grens over gaat.
Volume: **bovengrens 20,1 t 6E/j** = 646.000 oz 6E in matte FY2024 voor héél Zimplats (÷ 32,15; mix 6E = Pt+Pd+Rh+Au+Ru+Ir) [1]; het
aandeel van Ngezi-concentraat daarin is niet gepubliceerd.

## 1 · Ketenkaart
```
Ngezi-complex `pgm-ngezi-concentrator` ──(b1 truck · Ngezi-Selous Road / Platinum Highway → A5-rotonde Selous → SMC-ontsluiting ·
  gemeten 73,8 km, gepubliceerd 77–78 [2][4], aannemelijk: één bron voor de modaliteit)──► Zimplats SMC `pgm-zimplats-smc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-ngezi-concentrator` → `pgm-zimplats-smc` | Ngezi-Selous Road (Platinum Highway) → aansluiting A5 bij de Selous-rotonde → servicewegen naar SMC; aannemelijk: één bron (historisch, niet per lading) | 77–78 [2], 77 [1], 80 [5]; proefmeting 73,8 (−4,2%) | maak_stroombeen_weg (extract zimbabwe) | nee |

Geen zee-, spoor-, binnenvaart-, leiding- of luchtbeen; geen fase B/C/D/E. Waarom de proefmeting onder de 77–78 km ligt: de bronnen meten vanaf
de mijn bij de put (`-18.6658, 30.3564`, 3,7 km zuidelijker); dezelfde route vanaf de put gaf in de haalbaarheidstoets 77,2 km.

## 3 · Ankers (één per site; SMC letterlijk hergebruikt)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-ngezi-concentrator` | mijn-/concentratorcomplex (laadplek) | Zimplats Ngezi-complex, Mhondoro-Ngezi (concentrator niet bij naam of coördinaat gevonden) | -18.6335, 30.3498 | [3][4][8], eigen z16-blik | aannemelijk (z16 gezien: transportband uit het noorden naar een gekoepelde voorraadopslag en een gebouwencomplex, direct langs de doorgaande weg; of dit de concentrator is volgt uit de ligging, niet uit een bron) |
| `pgm-zimplats-smc` | smelter (concentrator + boogoven + converter) | Zimplats Selous Metallurgical Complex — letterlijk uit `pgm-zimplats-springs.md` | -18.0328, 30.4334 | [1][2][9] | bron-gelegd (z15 opnieuw bekeken: smelter-/procesgebouwen met rookpluim, vijfhoekige tailingsdam oost, blauwgroene vijvers, zonnepark west) |
Niet als anker gebruikt: de Ngezi-put (Wikipedia en OSM, `-18.6658, 30.3564`): z15 toont daar steenstort met rehabilitatiebeplanting en een
waterhoudende put, 0,59 km van de weg; ruim 3,5 km ten zuiden van het complex. Bron voor de beeldbestanden: [10].

## 4 · Via-punten (landbeen; één doorgaande weg, dus weinig keuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ngezi-Selous Road, midden | -18.3299, 30.4027 | op de weg gemeten (snap 0,00 km); pint de Platinum Highway boven een omweg via Chegutu/A5 |
| b1 | 2 | Selous-rotonde (A5, "Halfway") | -18.0795, 30.4276 | Wikipedia 18°04'46"S 30°25'39"E = -18.0794, 30.4275 [2]; hier takt de weg van de A5 af naar SMC (snap 0,01 km) |
Geofabrik-regio: `zimbabwe`. Profielwaarden (lon, lat): anker Ngezi (30.3498, -18.6335) · midden (30.4027, -18.3299) · rotonde (30.4276, -18.0795) ·
SMC (30.4334, -18.0328). Proefrun (zonder profiel in de repo): 37,6 + 30,6 + 5,5 km, snaps 0,00–0,21 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ngezi-concentrator(s) | Zimplats (87% Implats) | erts van de Ngezi-mijnen → concentraat; drie Ngezi-fabrieken genoemd (derde plant) | niet per fabriek gepubliceerd | [5][6][8] |
| SMC | Zimplats | concentraat Ngezi + SMC → matte (boogoven, converter); matte naar IRS Springs | 646.000 oz 6E in matte FY2024 (611.000 FY2023) | [1] |

## 6 · Stoppunt
Bij de SMC-poort: de factsheet laat concentraat van Ngezi en SMC samenkomen in de SMC-boogoven; het vervolg (matte naar Springs) is
`pgm-zimplats-springs`, dus deze brief houdt op bij het smelterterrein en tekent geen fase D/E.

## 7 · Open punten
- **Modaliteit niet per lading gebrond:** de bronnen over truck zijn historisch: erts per 100 t-roadtrain 77 km naar Selous [4], na de tweede
  Ngezi-concentrator (2009) "half the output" per negen trucks over 80 km [5]. Een actuele bron die concentraat vandaag per truck zegt ontbreekt.
- **Concentrator niet gevonden bij naam of coördinaat:** het anker is het complex dat bij de weg ligt (§3); een tweede kandidaat of de derde
  plant kan elders in het Ngezi-terrein liggen.
- **Aandeel Ngezi in het volume:** 20,1 t 6E/j is de bovengrens (alle Zimplats-matte); ook SMC heeft een eigen concentrator [6][7].
- **Km-bron:** 77 [1][2] en 78 [2] zijn de weglengte van de mijn tot Selous, 80 [5] is afgerond; geen wegkm van complex tot SMC-poort.
- **Sitelaag:** `w-zimplats-ngezi` (-18.35, 30.08) ligt 42,5 km van dit anker en 46 km van de put: centraal gelijktrekken op
  `-18.6335, 30.3498` (niet door de bak-agent).
- **Factsheet [1] niet zelf geopend** (PDF 13 MB, te groot voor de fetch-tool): alleen via de zoekresultaat-samenvatting (SMC 77 km noord, matte naar
  Springs, 646 koz FY2024).

## 8 · Bronnen
[1] Implats, Zimplats Fact Sheet 2025 (matte naar Springs onder life-of-mine-akkoord; 646.000 oz 6E FY2024; SMC 77 km ten noorden van de
ondergrondse mijnen; via zoekresultaat), https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-zimplats.pdf
[2] Wikipedia, "A5 road (Zimbabwe)", sectie Ngezi-Selous Road (77 km; 78 km tussen mijn en SMC; gebouwd 2001; rotonde 18°04'46"S 30°25'39"E),
https://en.wikipedia.org/wiki/A5_road_(Zimbabwe)
[3] Wikipedia, "Ngezi mine" (coördinaat -18.6658, 30.3564; ~200.000 oz Pt/j), https://en.wikipedia.org/wiki/Ngezi_mine
[4] Mining Technology, "Hartley Platinum Mine, Zimbabwe" (Ngezi-dagbouw, 100 t roadtrains 77 km naar SMC; Ngezi-concentrator 1,5 Mtpa 2009),
https://www.mining-technology.com/projects/hartley/
[5] Business Excellence, "Zimplats: Ngezi Mine" (ca. 2009; tweede concentrator, half the output 80 km, negen trucks, 100 t-trucks),
https://bus-ex.com/index.php/article/zimplats-ngezi-mine-0
[6] Financial Gazette, "Zimplats expansion projects on course", 2024-02-08 (concentrators bij Ngezi en SMC; paywall),
https://fingaz.co.zw/2024/02/08/zimplats-expansion-projects-on-course/amp/
[7] Zimplats Quarterly Report q/e 30 sep 2025 (mill relines "at two concentrator plants"; 158.716 oz 6E in concentraat Q1 FY2026),
https://www.zimplats.com/data/2025/10/Zimplats-Quarterly-Report-Year-End.pdf
[8] Zimplats vacature "Plant Metallurgist" ("Ngezi Concentrator Third Plant"), https://zimplats.com/?p=7158
[9] `v2/design/routebrieven/pgm-zimplats-springs.md` en `pgm-zimplats-rustenburg.md` (SMC-anker, bron-gelegd)
[10] Esri World Imagery: `v2/build-cache/satcheck/sat-pgm-ngezi-selous-ngezi-put.png`, `…-ngezi-cluster.png` (z15), `…-ngezi-plant.png` (z16),
`…-smc.png` (z15); wegproef: `v2/build-cache/ais/graaf/pgm-ngezi-selous-weg-ngezi-smc.geojson` (vervangbaar door de bak-agent)
[11] `v2/design/pgm-sitelaag.json` (`w-zimplats-ngezi`, niet satelliet-bevestigd)

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-pgm-ngezi-selous.json` (10,9 KB, versie 2, lonlat, 492 punten, 2 markers); functie `bak_pgm_ngezi_selous` in
`v2/tools/bak_stromen.sh`; profiel `pgm-ngezi-selous-ngezi-smc` in `v2/tools/maak_stroombeen_weg.py`; tussenuitvoer
`v2/build-cache/ais/graaf/pgm-ngezi-selous-weg-ngezi-smc.geojson`.

| # | modaliteit | been | km gebakken | km gepubliceerd | afwijking | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | Ngezi-complex → SMC (Ngezi-Selous Road / Platinum Highway → A5-rotonde Selous) | 74,0 (gemeten 73,8 + 0,2 ankerverbinding) | 77 (77-78 [2], 80 [5]) | -3,9% | nee |

Totaal 74,0 km; één been, dus geen naden. Markers: 2 (`pgm-ngezi-concentrator` aannemelijk, `pgm-zimplats-smc` bron-gelegd en letterlijk hergebruikt),
beide 0,0 km van de lijn.

**Recept:** `wegscan_puur.py --profiel pgm-ngezi-selous-ngezi-smc` (extract zimbabwe, geen refs, 4 punten: anker, midden, rotonde, SMC); snaps 0,00-0,21 km;
eerste mijl 0,51 km (service), laatste mijl 5,43 km (service, unclassified) tot het SMC-anker. Geen stippel, haven-aanloop, kopie, vlucht of leiding.

**Toets:** ±15% gehaald (de 77-78 km zijn gemeten vanaf de put, 3,7 km zuidelijker dan het complex-anker, dus het verschil is verklaard). `toets_knikken`: twee
knikken (91° en 61°) in de eerste 50 m binnen het complex, geen omkeringen; `toets_rechte_benen`: geen rechte benen. Truck blijft aannemelijk (één, historische
bron per modaliteit; staat in de beennaam, de lijn is doorgetrokken).

**Lessen / open voor centraal:** (1) registreren als `pgm-ns` (bezette sleutels geen botsing); (2) sitelaag `w-zimplats-ngezi` ligt 42,5 km van het anker: centraal
gelijktrekken op -18.6335, 30.3498; (3) de Ngezi-concentrator is niet bij naam gevonden, anker is het complex langs de weg; (4) Bash-gereedschap eet een backslash
aan het eind van een regel in een heredoc/python-string: schrijf regelvervolgen met chr(92) of controleer de functie na de edit.
