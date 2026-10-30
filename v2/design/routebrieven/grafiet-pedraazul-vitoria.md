# Routebrief (licht) · grafiet — Paca-mijn Pedra Azul → Porto de Praia Mole, Vitória (stoppunt)

**stroom-id:** `grafiet-pedraazul-vitoria` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** vlokgrafiet van de Paca-mijn / Pedra Azul-vestiging van Nacional de Grafite (Minas Gerais) gaat per **truck** over BR-116 naar Teófilo Otoni, oostwaarts via Ataléia en Colatina (ES-080, BR-381), over BR-259 en BR-101 naar de Porto de Praia Mole-terminal in Vitória: hemelsbreed 498 km, geen wegkm. Aannemelijk: één bron voor de mijn, geen bron voor de haven. De brief stopt bij de kade.
**Welke as van het verhaal:** de tweede Braziliaanse mijn van Nacional de Grafite, grootste producent van beneficiated vlokgrafiet in Brazilië. De Pedra Azul-unit leverde 35,2 kt in 2007 van 61,1 kt voor het bedrijf [3]; in 2023 ging 57,2% van de grafiet-CFEM naar Pedra Azul [4]; het bedrijf heeft 70 kt/j capaciteit over drie mijnen (2025/2026) [2]. Eenheid kt grafiet per jaar. Andere mijn en andere corridor dan `grafiet-itapecerica-vitoria` (BR-262), alleen het eindanker is gedeeld.

## 1 · Ketenkaart
```
Paca-mijn Pedra Azul `gr-pedraazul-mijn` ──(b1 truck · LMG-610 → BR-116 (Medina, Teófilo Otoni) → BR-418/BR-342 (Ataléia)
   → ES-080 → BR-381 (Colatina) → BR-259 (João Neiva) → BR-101 (Ibiraçu) · hemelsbreed 498 km, geen wegkm; OSRM-indicatie ~718)──►
   Porto de Praia Mole `gr-praiamole-kade` ⏹ STOPPUNT (geen bron voor haven of afnemer; fase B niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-pedraazul-mijn` → `gr-praiamole-kade` | LMG-610 → BR-116 (Medina–Teófilo Otoni) → BR-418/BR-342 → ES-080 → BR-381 → BR-259 → BR-101 | hemelsbreed 498 km, geen wegkm; OSRM-indicatie 718, haalbaarheidstoets-tool 734 (indicatie, ±15% geen norm) [9][13] | maak_stroombeen_weg, extract `brazilie`, 6 via-punten | nee |

Aannemelijk: één bron voor de mijn [1][2], geen bron voor Praia Mole of een afnemer. Het been wordt gewoon doorgetrokken gemeten; de onzekerheid staat hier en in de beennaam, niet in de lijnstijl. Geen last-mile-stippel: mijn 0,39 km van de weg, kade 0,04 km [13].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-pedraazul-mijn` | mijn (+ beneficiation-unit) | Paca-mijn / Nacional de Grafite, Pedra Azul (Fazenda Baixa Grande, 39970-000) | -15.8804, -41.0732 | [1][2][12] | bron-gelegd (hergebruikt letterlijk uit `grafiet-sitelaag.json` `w-nacgrafite-pedraazul`; z15 gezien: dagbouwpit met lichte bermen, afvalterrassen ten zuiden en gebouwen langs de ontsluitingsweg ~1 km ZO; het kruis ligt aan de pitrand) |
| `gr-praiamole-kade` | exportterminal (stoppunt) | Porto de Praia Mole, Vitória/Serra (ES) | -20.28965, -40.2350 | [12] | bron-gelegd (hergebruikt letterlijk uit `grafiet-itapecerica-vitoria.md` §3; z15 opnieuw gezien: kade-apron met witte loodsen en bulkschepen aan de zuidkade) |

## 4 · Via-punten (b1, corridorkeuzes; uit de bindende haalbaarheidstoets [13], gelegd op de weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | BR-116 bij Medina | -16.3170, -41.4760 | pint de afrit van de mijn (LMG-610/BR-251) op de BR-116 i.p.v. een kustroute via Bahia |
| b1 | 2 | BR-116 bij Pontalete (Catuji), noordelijk van Teófilo Otoni | -17.3518, -41.5314 | pint het blijven op BR-116 tot Teófilo Otoni |
| b1 | 3 | Ataléia (Fazenda Coqueiro, BR-418) | -17.9628, -41.1124 | pint de afslag oostwaarts na Teófilo Otoni i.p.v. BR-116 zuid naar Governador Valadares (ontwerpcorridor, langer) |
| b1 | 4 | Vila Nelita, Água Doce do Norte (ES-080) | -18.4671, -41.0159 | pint de grensoversteek MG → ES en de ES-080 |
| b1 | 5 | São Domingos do Norte (ES) | -19.1211, -40.6233 | pint de nadering van Colatina en BR-381/BR-259 i.p.v. een omweg langs BR-101 noord |
| b1 | 6 | BR-101 bij Ibiraçu (São Benedito) | -19.8285, -40.3688 | pint de afwikkeling over BR-259 naar BR-101 en de laatste 60 km zuidwaarts naar Vitória |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Pedra Azul-unit (Paca-mijn + beneficiation) | Nacional de Grafite Ltda. | ROM grafiet-erts → vlokconcentraat (87,7-94,0% C fixed carbon, bedrijfsbreed) | 35,2 kt (2007, productie van de unit); installatie 30 kt/j volgens ANM-zoekfragment [10]; bedrijf 70 kt/j over drie mijnen (2025/2026) | [2][3][10] |

## 6 · Stoppunt
De brief stopt bij de kade van Praia Mole: geen bron koppelt Nacional de Grafite aan deze haven, aan een scheepvaartlijn of aan een afnemer (ook niet in de ANM-sumários en de bedrijfssite), dus fase B/D is niet getekend; een Bahia-haven (Ilhéus, Salvador) kan dichterbij liggen.

## 7 · Open punten
- **Geen bron voor Praia Mole of Vitória als exporthaven** van Nacional de Grafite; WebSearch (ES, MG, exportroute) vond geen verscheping per haven. Zelfde zwakte als `grafiet-itapecerica-vitoria`; de haven is een aanname.
- **Wegkm niet gepubliceerd**: hemelsbreed 498 km, geen wegkm; OSRM 718 en de tool 734 zijn indicaties, geen bron.
- **Corridor niet gebrond**: de gekozen route (Teófilo Otoni, Ataléia, Colatina, BR-259) volgt OSRM en de toets; de ontwerpcorridor via Governador Valadares is langer en niet gekozen.
- **Productvolume per unit actueel onbekend**: 35,2 kt is peiljaar 2007; 2023 alleen als CFEM-aandeel (57,2% van 56,1 kt landelijk, indicatie ~32 kt, CFEM is waarde-gebaseerd).
- **Functie van de gebouwen bij de Pedra Azul-mijn** (exacte plant) niet gebrond; anker staat op de pitrand uit de sitelaag.
- **Exact berth bij Praia Mole** onbekend; het complex heeft meerdere operators.
- Eerste mijl 7,0 km en laatste mijl 8,4 km over kleine klassen (service/tertiary/unclassified), geen stippel.
- **Geen fase D/E**: geen bron noemt een fabriek of afnemer.

## 8 · Bronnen
[1] Nacional de Grafite, "Units and Head Office" — Pedra Azul (Baixa Grande Farm, 39970-000) als productievestiging. https://www.grafite.com/en/units-and-head-office
[2] BrasilMineral, "Nacional de Grafite" (Maiores Empresas 2026) — mijnen Tejuco Preto, Paca (Pedra Azul), Califórnia; 70 kt grafiet 2025/2026. https://brasilmineral.com.br/maiores/nacionaldegrafite
[3] ANM/DNPM, Sumário Mineral 2008 "Grafita" — 2007: Pedra Azul 35.162 t, Itapecerica 13.741 t, Salto da Divisa 12.153 t, bedrijf 61.056 t. https://www.gov.br/anm/pt-br/assuntos/economia-mineral/publicacoes/sumario-mineral/sumario-mineral-brasileiro-2008/grafita
[4] ANM, Sumário Mineral 2024 (ano base 2023) "Grafita" — CFEM 2023: Pedra Azul 57,2%, Nacional de Grafite 99,1%; productie 56,1 kt. https://www.gov.br/anm/pt-br/assuntos/economia-mineral/publicacoes/sumario-mineral/sumario-mineral-brasileiro-2024/grafita-2024-ano-base-2023.pdf
[5] Wikipedia (pt), "BR-259" — 711,7 km, loopt via Colatina en Governador Valadares, begint op BR-101 bij João Neiva. https://pt.wikipedia.org/wiki/BR-259
[6] Wikipedia (en), "Pedra Azul" — gemeente 16 km ten oosten van de BR-116. https://en.wikipedia.org/wiki/Pedra_Azul
[7] Wikipedia (pt), "Teófilo Otoni" (-17,8578 / -41,505) en "BR-116" (4.713,64 km) en "BR-101". https://pt.wikipedia.org/wiki/Teófilo_Otoni
[8] OpenStreetMap Nominatim (ODbL) — reverse-geocode van de zes via-punten (Medina, Catuji, Ataléia, Água Doce do Norte, São Domingos do Norte, Ibiraçu). https://nominatim.openstreetmap.org
[9] OSRM demo-router (OSM) — route over de via-punten: 718,2 km; wegen LMG-610, BR-116, BR-418/BR-342, ES-080, BR-381, BR-259, BR-101. https://router.project-osrm.org
[10] ANM, Sumário Mineral 2004/2005-zoekresultaten — Nacional de Grafite grootste beneficieerder, planta Pedra Azul 30.000 t/j (alleen als zoekfragment gezien, niet geopend). https://www.gov.br/anm/pt-br/assuntos/economia-mineral/publicacoes/sumario-mineral/sumario-mineral-brasileiro-2005/grafita-2005rev
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15, live): `v2/build-cache/satcheck/sat-grafiet-pedraazul-vitoria-{paca-mijn,praiamole}.png`.
[12] Sitelaag `v2/design/grafiet-sitelaag.json` (`w-nacgrafite-pedraazul`, bron-gelegd) en brief `v2/design/routebrieven/grafiet-itapecerica-vitoria.md` (§3 anker Praia Mole).
[13] Haalbaarheidstoets M31 golf 15 (bindend) + `v2/build-cache/ais/graaf/toets-grafiet-pedraazul-vitoria-weg.geojson` — weg 734,3 km, eerste mijl 7,0 en laatste mijl 8,4 km, via-punten §4.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-grafiet-pedraazul-vitoria.json` (320,0 KB, versie 2, lonlat) · **functie:** `bak_grafiet_pedraazul_vitoria` in `v2/tools/bak_stromen.sh` · **profiel:** `grafiet-pedraazul-vitoria-pedraazul-praiamole` in `v2/tools/maak_stroombeen_weg.py` · **titel:** Grafiet · Paca-mijn Pedra Azul → Porto de Praia Mole, Vitória (Brazilië).

| # | modaliteit | km | punten | naad | stippel | opmerking |
|---|---|---|---|---|---|---|
| b1 | truck | 734,8 | 15.001 | — | nee | gemeten weggeometrie, extract `brazilie`, 6 via-punten; scan 734,3 km tegen 717 (OSRM-indicatie, geen bron): +2,4%, indicatie en geen norm |

Totaal 734,8 km, 1 been, 2 markers (`gr-pedraazul-mijn`, `gr-praiamole-kade`), 0% stippel. Beide markers liggen op de lijn (0,0 km): mijn 0,39 km van de weg, kade 0,04 km.

**Recept:** profiel `grafiet-pedraazul-vitoria-pedraazul-praiamole` (via-punten in (lon,lat): mijn, Medina, Pontalete, Ataléia, Vila Nelita, São Domingos do Norte, Ibiraçu, kade; refs BR-116, BR-418, BR-342, BR-259, BR-101; vensterKm 40; default eindKlassen) → `python v2/tools/wegscan_puur.py --profiel …` (weg-slot en reus-slot, 484 s, 256.105 way-delen) → `v2/build-cache/ais/graaf/grafiet-pedraazul-vitoria-weg-pedraazul-praiamole.geojson` → `bash v2/tools/bak_stromen.sh grafiet-pedraazul-vitoria`.

**Toelichting:** geen stippel, geen haven-aanloop (stoppunt op de kade, geen zee), geen vlucht, geen leiding, geen kopie. Aannemelijk: één bron voor de mijn, geen bron voor Praia Mole; dat staat in de beennaam en in §7, niet in de lijnstijl. Eerste mijl 7,0 km en laatste mijl 8,4 km over kleine klassen (service/tertiary/unclassified), zoals de haalbaarheidstoets al aangaf; 38 keerlussen gesnoeid (734,4 → 734,3 km).

**Toets:** km binnen +2,4% van de OSRM-indicatie (geen echte wegkm, dus indicatie); geen naden (één been); `toets_knikken`: 28 knikken, 1 omkering (164,5 gr op de kade-ankerprojectie, 22 m, echte bocht), 0 terugloop; `toets_rechte_benen`: het been staat er niet in; json: versie 2, lonlat, modaliteit truck, 15.001 punten.

**Bevindingen:** (1) bestand 320,0 KB is iets boven de ~300 KB-richtlijn (een truckbeen van 15.001 punten); centraal noteren, niet herbakken. (2) Het wegtool geeft de eerste/laatste mijl via kleine klassen; geen via-punt bijgeschoven. (3) Open punten uit §7 blijven staan: haven niet gebrond, wegkm niet gepubliceerd, volume per unit alleen indicatie.

**Lessen:** een dubbele scan (reus + weg) op `brazilie` duurt zonder cache ~8 minuten; de tweede run met hetzelfde profiel is meteen klaar. De haalbaarheidstoets (734,3 km) bleek exact reproduceerbaar met het gebakken profiel.
