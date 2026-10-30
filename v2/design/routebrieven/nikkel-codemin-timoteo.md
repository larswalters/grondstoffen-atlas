# Routebrief (licht) · Nikkel — Codemin → Aperam Timóteo (Brazilië)

**stroom-id:** `nikkel-codemin-timoteo` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** ferronikkel (FeNi, ~30 % Ni) van de Codemin-fabriek van Anglo American in Niquelândia (Goiás) per **truck** over de Braziliaanse binnenlandse wegen (BR-414 → BR-080 → BR-040 → BR-381) naar de roestvrijstaalfabriek van Aperam South America (ex Acesita) in Timóteo (Minas Gerais) — stoppunt, geen fase D/E.
**Welke as van het verhaal:** de binnenlandse ferronikkel-as van Brazilië: nikkel dat het land niet verlaat. Eén bron voor de afnemer (ANM, over 2004): Codemin verkocht 17.630 t FeNi binnenlands, 76,6 % naar Acesita [1][2] ≈ 13,5 kt FeNi ≈ **4,3 kt Ni per jaar (peiljaar 2004, indicatie)**. Anglo's Braziliaanse FeNi (Barro Alto + Codemin, 39,4 kt Ni in 2024 [4]) gaat tegenwoordig vooral naar de EU [5] — of Aperam nu nog afneemt is niet gebronnen.

## 1 · Ketenkaart
```
Codemin-fabriek `ni-codemin-smelter` (Niquelândia) ──(b1 truck · GO-237 → BR-414 → BR-080 → Brasília-ring
   → BR-040 (Paracatu) → BR-381 oostelijk van BH · hemelsbreed 851 km, geen wegkm)──► Aperam-staalfabriek
   `ni-aperam-timoteo` (Timóteo) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-codemin-smelter` → `ni-aperam-timoteo` | BR-414 / BR-080 / BR-040 / BR-381 (corridor uit OSRM-controle, wegnummers niet gebronnen) | hemelsbreed 851 km, geen wegkm; eigen verwachting 1.200–1.350 km; wegscan 1.201,6 km (OSRM 1.206) — indicatie, geen norm | maak_stroombeen_weg (`wegscan_puur`) | nee |

Beennaam: *truck Codemin → Aperam Timóteo (aannemelijk: één bron, ANM over 2004; vermoedelijk voorloper Acesita)*.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-codemin-smelter` | fabriek (FeNi-smelter) | Codemin, Anglo American, Niquelândia | -14.1570, -48.3413 | [1][2][3][6] | bron-gelegd (z15 gezien: industriecomplex met lange ovenhal en slakopslag ~1 km ten zuiden van de dagbouwput, aan het Serra da Mesa-meer; 0,19 km verschoven van de toetsmarker op de westrand naar de hal) |
| `ni-aperam-timoteo` | afnemer (staalfabriek) | Aperam South America (ex Acesita), Timóteo | -19.5320, -42.6480 | [2][7][8][6] | bron-gelegd (z15 gezien: groot staalfabriekscomplex met lange walshallen tussen Rio Piracicaba en spoorlijn; OSM-toegangsweg "Acesso Aperam" 0,5 km ten noorden). De bron noemt de fabriek, niet de afleverplek |

Niet gebruikt: sitelaag `w-barro-alto` (-15.1100, -48.8000) is alleen een regiocentroïde, geen Codemin-anker; Photon-punt "Codemim" (-14.1446, -48.3405) ligt bij de dagbouwput.

## 4 · Via-punten (b1, alleen waar een corridorkeuze bestaat)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | BR-414 bij de aftakking van GO-237 | -14.4675, -48.4824 | pint de uitgang uit Niquelândia zuidwaarts naar Padre Bernardo (alternatief: oostelijk via de BR-010) |
| b1 | 2 | BR-080 / GO-230 bij Barro Alto | -15.2083, -48.6999 | pint BR-080 naar Brasília; op de weg, niet in het dorp |
| b1 | 3 | BR-080 / BR-251 noordrand Distrito Federal | -15.6200, -48.1988 | houdt de lijn aan de rand van het DF in plaats van door Brasília |
| b1 | 4 | BR-040 zuid van het DF | -16.0757, -47.9856 | op de BR-040 ten zuiden van de Brasília-ring |
| b1 | 5 | BR-040 bij Paracatu | -17.2320, -46.8525 | pint de BR-040 (en niet de BR-251/BR-365) richting Belo Horizonte |
| b1 | 6 | BR-381 oostelijk van Belo Horizonte | -19.8567, -43.8995 | op de BR-381 ten oosten van BH, niet in het centrum; kiest de noord-/oostrand |

Punten komen uit een OSRM-routecontrole (router.project-osrm.org, 2026-10-30): een voorspelling over OSM-wegen, geen bron. Wegscan (`wegscan_puur`, brazilie) geslaagd: 1.201,6 km, snaps ≤ 0,31 km, 10.616 punten, `v2/build-cache/ais/graaf/nikkel-codemin-timoteo-weg-codemin-aperam.geojson`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Codemin, Niquelândia | Anglo American (verkoop aan MMG vastgelopen bij de EU) | laterietertz (eigen mijn + Barro Alto-erts) → FeNi (~30 % Ni) | 2004: 20.326 t FeNi (31,9 % Ni); Anglo Brazilië 39,4 kt Ni in 2024 | [1][4] |
| Aperam South America, Timóteo | Aperam | FeNi + schroot → roestvrij staal | 900 kt staal per jaar (fabriek) | [8] |

## 6 · Stoppunt
De brief stopt bij Aperam Timóteo: de ANM noemt Acesita als grootste binnenlandse afnemer van Codemin-FeNi; geen bron noemt een vervolgzending van het staal (fabrieksproduct).

## 7 · Open punten
- **Afnemer niet actueel gebronnen:** de enige bron (ANM, over 2004) is oud; sinds 2011 is Barro Alto erbij gekomen, Anglo's FeNi gaat nu vooral naar de EU [5]. Of Aperam nu Codemin-FeNi neemt staat in geen bron — vandaar *aannemelijk: één bron*.
- **Vervoerswijze niet gebronnen:** dat het FeNi per truck gaat is een aanname (ANM noemt geen modaliteit); een spoorverbinding is niet onderzocht (de Vitória–Minas-lijn loopt wel langs Timóteo [8]).
- **Wegkm onbekend:** geen gepubliceerde route of afstand; alleen hemelsbreed 851 km. 1.200–1.350 km is eigen schatting.
- **Aperam-aflevering:** poort of terminal binnen de fabriek niet genoemd; anker op het fabrieksterrein.
- **Corridor onbevestigd:** geen bron voor BR-414/BR-080/BR-040/BR-381; alleen OSRM-voorspelling.
- **Verkoop Codemin/Barro Alto aan MMG** per sept 2026 vastgelopen bij de EU [5]; de fabriek draait wel.

## 8 · Bronnen
[1] ANM, Sumário Mineral Brasileiro 2005, Níquel (over 2004): Codemin 17.630 t FeNi binnenlands, Acesita 76,6 %. https://www.gov.br/anm/pt-br/assuntos/economia-mineral/publicacoes/sumario-mineral/sumario-mineral-brasileiro-2005/niquel-2005rev
[2] ANM, Sumário Mineral Brasileiro 2004, Níquel (over 2003): Codemin 85 % binnenlands (MG 79 %), Acesita als afnemer van Votorantim. https://www.gov.br/anm/pt-br/assuntos/economia-mineral/publicacoes/sumario-mineral/sumario-mineral-brasileiro-2004/niquel-2004.pdf
[3] Anglo American, nikkelverkoop Brazilië (Barro Alto en Codemin, Goiás). https://investnews.com.br/negocios/anglo-american-anuncia-venda-de-negocios-de-niquel-no-brasil-por-ate-us500-milhoes/
[4] Engineering News, "MMG to acquire Anglo American's nickel business for $500m" (39,4 kt Ni in 2024). https://www.engineeringnews.co.za/article/mmg-to-acquire-anglo-americans-nickel-business-for-500m-2025-02-18
[5] Poder360, 2025-10-15, Anglo/EU-voorstel: Anglo's FeNi naar de EU. https://www.poder360.com.br/poder-infra/anglo-american-propoe-acordo-a-ue-sobre-venda-de-mina-no-brasil/
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-nikkel-codemin-timoteo-smelter.png`, `sat-nikkel-codemin-timoteo-aperam.png`.
[7] OpenStreetMap/Nominatim (ODbL): "Aperam South America", "Acesso Aperam", Timóteo. https://www.openstreetmap.org
[8] Wikipedia, "Aperam South America" (ex Acesita, Timóteo, 900 kt/j). https://en.wikipedia.org/wiki/Aperam_South_America
[9] OSRM routecontrole 2026-10-30 (voorspelling, geen bron). https://router.project-osrm.org

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
Stroom `nikkel-codemin-timoteo` gebakken via `bash v2/tools/bak_stromen.sh nikkel-codemin-timoteo` (functie `bak_nikkel_codemin_timoteo`, profiel `nikkel-codemin-timoteo-codemin-aperam`), uitvoer `v2/data/stroomroute-nikkel-codemin-timoteo.json` (226,6 KB, 10.616 punten, 1 been, 2 markers, 1.202,0 km).

| # | modaliteit | km gebakken | brief | opmerking |
|---|---|---|---|---|
| b1 | truck, doorgetrokken | 1.202,0 | indicatie: hemelsbreed 851, geen wegkm; verwachting 1.200-1.350; OSRM 1.206 | Codemin -> BR-414 -> BR-080 -> BR-040 (Paracatu) -> BR-381 oostelijk van BH -> Aperam. Snaps 0,00-0,31 km (Codemin 0,31 via OSM-servicewegen, Aperam 0,08). Geen +-15%-norm, wel indicatie: 0,4% van OSRM, binnen de eigen verwachting. |

Naden: n.v.t. (een been). Markers: beide 0,0 km van hun lijn. Geen zee, geen haven-aanloop, geen stippel, geen leiding, geen kopie.
**Recept:** profiel (extract brazilie, refs BR-040 en BR-381, corridorKlassen tertiary/unclassified, venster 40 km, gepubliceerdKm None) met de zes via-punten uit §4 en de twee ankers als eind-via, gescand met `wegscan_puur.py`; geojson (FeatureCollection) als `--been-geojson "truck|..."` in de bake-functie; geen herscan nodig.
**Toelichting stippel/aanloop/vlucht/leiding:** niet van toepassing; beide ankers liggen op het terrein, het wegnet snapt op minder dan 0,4 km.
**Bevindingen:** (1) bestand 227 KB, onder de ~300 KB-richtlijn. (2) toets_knikken: 25 knikken >= 60 gr (spikes < 30 m en enkele krappe bochten in de OSM-geometrie bij de DF-rand), 0 omkeringen, 0 TERUGLOOP. (3) Segmenten via 2 -> 3 (Barro Alto -> DF-noordrand, 106,3 km tegen 70,6 hemelsbreed, factor 1,51) en via 6 -> anker (BR-381 -> Timoteo, factor 1,37) zijn bochtig; het totaal komt overeen met OSRM (1.206 km), dus geen via-punt verplaatst. (4) De open punten uit §7 blijven staan: afnemer alleen gebronnen over 2004, truck is aanname, corridor alleen OSRM-voorspelling, aflevering binnen de fabriek niet genoemd.
**Lessen:** een eenbenige truckketen in een reus-extract (brazilie) is met een vooraf gedraaide wegscan een kwestie van bake-functie + toets; de via-punten uit een OSRM-controle hoeven geen bron te zijn zolang de beennaam het zegt (aannemelijk: een bron).
