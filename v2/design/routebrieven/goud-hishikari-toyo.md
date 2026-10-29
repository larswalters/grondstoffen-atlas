# Routebrief (licht) · goud — Hishikari-erts → Kajiki → Toyo (Japan)

**stroom-id:** `goud-hishikari-toyo` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) ·
**status:** gebakken
**Keten in één zin:** goudhoudend erts (circa 20 g/t) van de Hishikari-mijn (Sumitomo Metal Mining, Isa, Kagoshima) per truck
naar Kajiki-haven aan de Kinkowan, per ertsschip over zee (Bungo-kanaal, Iyo-nada) naar de Toyo-smelter van SMM (Saijo/Niihama,
Ehime); daar stopt de brief. De lading is erts, geen dore: het goud dient in Toyo als flux in de kopersmelter en komt er als baar uit [1][2].
**Welke as van het verhaal:** Japan binnenlands — de enige commerciele goudmijn van het land naar de eigen smelter. Volume
**circa 4,4 t Au/j** (SMM-plan vanaf 2023, was ~6 t) [5][3]; meer dan 90% van de Japanse mijnproductie [3].

## 1 · Ketenkaart
```
Hishikari-mijn, breek- en sorteerinstallatie `au-hishikari-mijn`
  ──(b1 truck · route 268 → Kyushu-expressway E3 → Hayato → Kajiki · hemelsbreed 31 km, geen wegkm)──►
Kajiki-haven, kade aan de Kinkowan `au-kajiki-kade`
  ──(b2 zee · MARNET Kinkowan → Osumi-straat → Hyuga-kust → Bungo-kanaal → Iyo-nada · 605,1 km gemeten)──►
MARNET-zeeknoop 5746 (Niihama) `au-niihama-zeeknoop`
  ──(b3 zee · haven-aanloop over water · 23,3 km, letterlijke kopie koper-cerroverde-toyo b6, stippel)──►
Toyo-smelter, eigen ertskade `au-toyo-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Hishikari-mijn → Kajiki-kade | lokale weg → Rt 268 → E3 (Kyushu-expressway) → Hayato → Rt 55/467 [7] | **hemelsbreed 31 km, geen wegkm**; OSRM-indicatie 43,7 km, wegtool nog te bakken | maak_stroombeen_weg (extract japan) | nee |
| b2 | B | zee | Kajiki-kade → zeeknoop 5746 | Kinkowan, Osumi-straat, Bungo-kanaal | MARNET gemeten **605,1** (snap 3,6 km op zeeknoop 5780; hemelsbreed 344) [9] | MARNET (`--been zee`) | nee |
| b3 | B | zee | zeeknoop 5746 → Toyo-kade | Seto-binnenzee | **23,3** gemeten; kade 21,5 km van de knoop [8] | letterlijke kopie `koper-cerroverde-toyo-aanloop-toyo.geojson` (koper-cerroverde-toyo b6) | **ja** — MARNET reikt niet |

Naad b1→b2: kade → zeeknoop 5780 3,6 km (onder de 5 km-grens van de bakhandleiding, geen haven-aanloop; wel noemen in de bake-uitvoer).
Geen overlap met andere goudstromen; enige gedeelde been is b3 (kopie van een kopersstroom, zelfde Toyo-kade).

## 3 · Ankers (een per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-hishikari-mijn` | mijn / sorteerinstallatie | Hishikari-mijn (SMM), Isa | 32.0125, 130.6939 | [6][3] | aannemelijk (z15 gezien: gebouwen en ontgraven terrassen op een dalkop in bos, sporen van ontgraving direct N; welk gebouw de breek-/sorteerinstallatie is, niet te onderscheiden) |
| `au-kajiki-kade` | overslag truck → zee | Kajiki-haven, kade van de ertslading | 31.7297, 130.6645 | [1][4] | aannemelijk (z16 gezien: kade met silo's en tanks aan de monding van de Kinkowan-rivier, een pier ten Z; berth van het ertsschip niet bekend; ja.wikipedia geeft het havenpunt 31.7297, 130.6654, 85 m oostelijk) |
| `au-kajiki-zeeknoop` | zee-knoop | MARNET-zeeknoop 5780 | 31.7013, 130.6831 | eigen meting [9] | knoop, niet de lijn; 3,6 km van de kade |
| `au-niihama-zeeknoop` | zee-knoop | MARNET-zeeknoop 5746 | 34.0720, 133.0479 | koper-cerroverde-toyo §3 | bestaand, hergebruikt |
| `au-toyo-kade` | losplek / smelter | Toyo Smelter & Refinery (SMM), eigen ertskade | 33.9505, 133.2295 | [2][8] | bestaand, hergebruikt (aannemelijk; z15/z16 in de koperbrief: smelterterrein aan de kust met een bulkcarrier langs de kade) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Keuze b1: de expressway (E3, snelst, OSRM 43,7 km) tegenover nationale wegen via Rt 504/56/55 (OSRM 45,3 km). Alle punten op de weg (OSRM-snap 0-5 m), niet in Kajiki-stad of Kokubu.
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Rt 268, begin vanaf de mijnweg | 32.0026, 130.6667 | de mijn verlaat het dal via Rt 268 (8 km) naar het zuiden, geen noordelijke omweg |
| b1 | 2 | E3 Kyushu-expressway, oprit | 31.9445, 130.7210 | dwingt de expressway af (27 km) i.p.v. de nationale-wegvariant |
| b1 | 3 | E3 / Hayato Road, einde expressway | 31.7469, 130.6702 | laatste punt op de snelweg; daarna Rt 55 en 467 naar de haven |
Profiel-recept (lon, lat): anker (130.6939, 32.0125) -> (130.6667, 32.0026) -> (130.7210, 31.9445) -> (130.6702, 31.7469) -> anker (130.6645, 31.7297); `extracts ["japan"]`, `refs ["268","E3","55","467"]`, `gepubliceerdKm` ontbreekt, `vensterKm` 40.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Hishikari-mijn | SMM | erts → gesorteerd goud-erts | circa 4,4 t Au/j (plan vanaf 2023) | [5] |
| Toyo Smelter & Refinery | SMM | Cu-concentraat + Hishikari-erts (flux) → kathode, goudbaren | 450 kt Cu/j (kade tot 30.000 t) | [2][8] |

## 6 · Stoppunt
Bij de Toyo-kade: SMM noemt Toyo als vervolg van het Hishikari-erts en de goudbaren die daar vallen; geen bron noemt een afnemer van die baren. Fase D en E vervallen.

## 7 · Open punten
1. **Lading is erts, geen dore.** Het goud gaat als flux in de kopersmelter; het goudvolume van de Toyo-baren is niet gepubliceerd.
2. **Volume:** ontwerp noemde 6 t Au/j (ja.wikipedia, indicatie); SMM-woordvoerder (HLJ maart 2023, via zoekfragment) noemt **4,4 t Au/j vanaf 2023** [5]; een zoekfragment noemt ~3,5 t (FY-verkoopvolume SMM), niet geverifieerd. Ertstonnage onbekend.
3. **Wegbeen geen gepubliceerde wegkm** (hemelsbreed 31 km; OSRM 43,7 km); de corridor (E3 of nationale wegen) is niet gebronnen: ja.wikipedia zegt alleen dat het erts per truck naar de haven gaat [4]. Een ±15%-toets is indicatief.
4. **Kajiki-berth** onbekend: de haven heeft een kade voor schepen tot circa 5.000 t en overslag van bouwmaterialen [4]; de plek van de ertslading is niet gepubliceerd.
5. **Sitelaag** kent Hishikari en Toyo niet voor goud; centraal toevoegen (koper kent Toyo als `w-toyo`, 33.9493, 133.2305).
6. Het Hishikari-anker is site-niveau; de breekinstallatie staat ergens op het dalterrein.

## 8 · Bronnen
[1] SMM, Hishikari Mine — sortering aan de oppervlakte, erts geladen op een ertsschip bij Kajiki Port in Kinkowan, naar Toyo; ~20 g/t — https://www.smm.co.jp/en/corp_info/location/domestic/hishikari/
[2] SMM, Toyo Smelter & Refinery — Hishikari-erts als flux, eigen berth tot 30.000 t, goudbaren — https://www.smm.co.jp/en/corp_info/location/domestic/toyo/
[3] ja.wikipedia 菱刈鉱山 — 6 t/j (oud), >90% van de Japanse productie, erts naar Toyo — https://ja.wikipedia.org/wiki/菱刈鉱山
[4] ja.wikipedia 加治木港 — havenpunt 31.7297, 130.6654; kade circa 5.000 t; Hishikari-erts per truck naar de haven en naar Niihama — https://ja.wikipedia.org/wiki/加治木港
[5] Government of Japan, Highlighting Japan maart 2023 — SMM: van 6 naar 4,4 t Au/j vanaf 2023 (via zoekfragment; pagina 403) — https://www.gov-online.go.jp/pdf/hlj/20230301/hlj202303_18-19_A_World-leading_Gold_Mine_in_Modern_Japan.pdf
[6] en.wikipedia Hishikari mine — coordinaat 32.0125, 130.6939 — https://en.wikipedia.org/wiki/Hishikari_mine
[7] OSRM (router.project-osrm.org), 2026-10-29 — Hishikari → Kajiki 43,7 km (Rt 268 → E3), alternatief 45,3 km; snaps 0-25 m
[8] v2/design/routebrieven/koper-cerroverde-toyo.md — Toyo-kade, zeeknoop 5746, aanloop b6 (23,3 km)
[9] MARNET (build-cache/marnet-preais), eigen meting 2026-10-29 — Kajiki → knoop 5746: 605,1 km, snap 3,6 km; Toyo-kade 21,5 km van knoop 5746
[10] Mining Weekly 2022 — "circa 6 t/j" (via zoekfragment; pagina 403) — https://www.miningweekly.com/article/hishikari-mine-japan-2022-04-22
Satellietblik (Esri live, 2026-10-29, `v2/build-cache/satcheck/`): `sat-goud-hishikari-toyo-au-hishikari.png` (z15) · `sat-goud-hishikari-toyo-au-kajiki-kade.png` (z16) · `sat-goud-hishikari-toyo-au-kajiki-pier.png` (z15).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh goud-hishikari-toyo` -> `v2/data/stroomroute-goud-hishikari-toyo.json` (22,2 KB, versie 2, lonlat, 3 benen, 1.048 punten, 3 markers, totaal 672,2 km).

| # | modaliteit | km (bake) | naad | stippel | brief | toets |
|---|---|---|---|---|---|---|
| b1 | truck | 43,8 | 0 | nee | hemelsbreed 31 km, OSRM-indicatie 43,7 | indicatie: +0,2% t.o.v. OSRM; geen echte wegkm, dus geen norm |
| b2 | zee | 605,1 | 3,61 km (kade -> zeeknoop 5780) | nee | 605,1 gemeten | exact; naad < 5 km, geen aanloop |
| b3 | zee | 23,3 | 0 | ja, MARNET reikt niet | 23,3 | letterlijke kopie |

Markers (alle 0,0 km van hun lijn): Hishikari-mijn (32.0125, 130.6939) · Kajiki-haven, ertskade (31.7297, 130.6645) · Toyo-kade (33.9505, 133.2295). De zeeknopen 5780 en 5746 zijn knopen, geen markers.

**Recept.** b1: profiel `goud-hishikari-toyo-hishikari-kajiki` in `maak_stroombeen_weg.py` (extract `japan`, refs 268/E3/55/467, vensterKm 40, `gepubliceerdKm` None, vijf via-punten uit §4 incl. beide ankers), gescand met `wegscan_puur.py` (617 s, weg-slot + reus-slot); snaps van alle via-punten 0,00-0,03 km, plant -> weg 0,02 km, weg -> kade 0,03 km; first mile 3,21 km over kleine klassen. b2: `--been zee` 31.7297,130.6645 -> 34.0720,133.0479. b3: `--stippel-geojson` met `koper-cerroverde-toyo-aanloop-toyo.geojson`, letterlijke kopie van koper-cerroverde-toyo b6 (FeatureCollection, 37 punten, van knoop 5746 tot Toyo-kade).

**Toelichting.**
- **Stippel:** alleen b3, de haven-aanloop Toyo over de Seto-binnenzee (MARNET reikt niet; kade 21,5 km van de knoop). Geen eigen verbinding zonder net.
- **Geen aanloop Kajiki:** de kade snapt op 3,6 km van zeeknoop 5780 (onder de 5 km-grens); de naad b1 -> b2 van 3,61 km is een procesgat en blijft staan.
- **Geen luchtbeen, geen leiding.** Fase D/E vervallen; Toyo is het stoppunt.
- **Aannemelijk:** de corridor van b1 (E3 of nationale wegen) is niet gebronnen en staat als 'aannemelijk' in de beennaam; de lijn is doorgetrokken.

**Bevindingen.**
1. `toets_knikken`: truck 11 knikken, 1 omkering (168 graden, 8 m radius) precies op het mijnanker (32.01249, 130.69407) = de aansluiting plant -> weg; verder spikes met radius 4-46 m bij de via-punten (Rt 268-begin, E3-oprit, Hayato-einde) en het Kajiki-anker, dus afrit- en aansluitgeometrie op 10-m-schaal. Geen terugloop. Zee: drie krappe bochten (Bungo-kanaal 33.75, 131.90; Osumi-straat 30.93, 130.62; Iyo-nada 34.17, 132.94) van 85-122 graden met 4,6-6,0 km radius, normale MARNET-vorm.
2. `toets_rechte_benen --min-km 5`: geen regel voor deze stroom.
3. De ±15%-toets voor b1 is een indicatie tegen OSRM (OSM-afgeleid, dus geen onafhankelijke controle).
4. Open uit §7 blijven: erts, geen doré; volume 4,4 t Au/j onbevestigd; Kajiki-berth onbekend; Hishikari en Toyo ontbreken in de sitelaag voor goud (centraal).

**Lessen.** (1) Een reus-extract (Japan, 2,4 GB) kostte 617 s wegscan plus lange wachttijd op een reus-slot; plan de scan als eerste. (2) Een gedeelde aanloop (Toyo) als letterlijke kopie werkt zonder extra gereedschap: het geojson is al een FeatureCollection.
