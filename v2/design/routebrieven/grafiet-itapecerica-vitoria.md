# Routebrief (licht) · grafiet — Itapecerica → Porto de Praia Mole, Vitória (stoppunt)

**stroom-id:** `grafiet-itapecerica-vitoria` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** vlokgrafiet van de Itapecerica-vestiging van Nacional de Grafite (mijn Tejuco Preto + concentratie, Minas Gerais) gaat per **truck** over de BR-262 (~570 km via-keten, hemelsbreed 510 km) naar de Porto de Praia Mole-terminal in Vitória (Espírito Santo) — Brazilië's grootste onbelichte vlokproducent, de eerste Zuid-Amerikaanse as van de atlas voor deze grondstof. De brief stopt bewust bij de kade: geen bron koppelt Nacional de Grafite specifiek aan deze haven of aan een buitenlandse afnemer.
**Welke as van het verhaal:** Nacional de Grafite (opgericht 1939, hoofdkantoor/hoofdvestiging Itapecerica-MG) heeft drie mijnen in Minas Gerais — Tejuco Preto (Itapecerica), Paca (Pedra Azul), Califórnia (Salto da Divisa) — met samen 70 kt/j grafietcapaciteit (peiljaar 2025/2026), "verkocht op vijf continenten, direct of via distributeurs" [1][6]. Vitória is de dichtstbijzijnde grote exporthaven vanuit Itapecerica over de klassieke mijnbouw-exportcorridor BR-262, maar geen bron bevestigt deze route of bestemming per lading — de zwakste onderbouwing van de drie prioritaire M31-assen.

## 1 · Ketenkaart
```
Itapecerica-vestiging `gr-itapecerica-plant` ──(b1 truck · BR-262 (via lokale weg → Nova Serrana → Belo Horizonte
   → São Domingos do Prata → Manhuaçu → Domingos Martins → Viana) · ~570 km, schatting)──►
   Porto de Praia Mole `gr-praiamole-kade` ⏹ STOPPUNT (afnemer/bestemming niet gedocumenteerd — fase B niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-itapecerica-plant` → `gr-praiamole-kade` | lokale ontsluiting (MG-164-omgeving) → BR-262 (de gangbare mijnbouw-exportcorridor Minas Gerais → Espírito Santo) | ~570 (ontwerpschatting: som van de via-keten hemelsbreed; hemelsbreed plant→kade 510,5 km; geen gepubliceerde wegkilometrage gevonden) | maak_stroombeen_weg, extract `brazilie`, ref BR-262 | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-itapecerica-plant` | mijn + concentratie (Tejuco Preto-vestiging) | Nacional de Grafite, Itapecerica-vestiging (MG-164 km 4, Água Limpa, 35550-000) | -20.4420, -45.1300 | [1][8][9] | bron-gelegd (z18 gezien: fabrieksgebouwen, tanks/verdikkers, een gekromde aarden dam die op een slibbekken lijkt, opslagloodsen en een klein privévliegveld ("Aeródromo Nacional Grafite I") vlakbij — **verlegd van de wegas** (-20,4500/-45,1247 uit het ontwerp, ~950 m zuidelijker, lag in bos) **naar het echte terreincomplex**, conform de haalbaarheidstoets) |
| `gr-praiamole-kade` | exportterminal (stoppunt) | Porto de Praia Mole, Vitória/Serra (ES) | -20.28965, -40.23500 | [4][7][9] | bron-gelegd (z16 gezien: bulkterminalcomplex — ertsopslag, pelletfabriek, loodsen en kranen, met bulkschepen aan de zuidelijke kade direct bevestigd; welk exact sítio/berth grafiet zou laden is niet per lading gebrond, zie §7) |

## 4 · Via-punten (b1 — corridorkeuzes op de doorgaande BR-262)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Nova Serrana (aansluiting lokale weg × BR-262) | -19.8758, -44.9842 | pint waar de lokale ontsluiting vanaf Itapecerica de doorgaande BR-262-corridor bereikt |
| b1 | 2 | Belo Horizonte (BR-262 door de metropoolregio) | -19.9272, -43.4848 | pint de doorgaande BR-262 door/rond de hoofdstad i.p.v. een noordelijke omweg |
| b1 | 3 | São Domingos do Prata (BR-262, Rio Doce-regio) | -19.8671, -42.9658 | pint de oostwaartse corridor door het Rio Doce-dal (parallel aan de EFVM-spoorlijn) |
| b1 | 4 | Manhuaçu (BR-262, grote kruising) | -20.2574, -42.0341 | pint de doorgaande BR-262 i.p.v. een afslag naar Governador Valadares (BR-116) |
| b1 | 5 | Domingos Martins (BR-262, bergpas MG→ES) | -20.3733, -41.0591 | pint de vaste grensoversteek Minas Gerais → Espírito Santo op BR-262 |
| b1 | 6 | Viana (BR-262, nadering Vitória-metropool) | -20.3894, -40.4949 | pint de laatste aftakking naar de havenwegen van Vitória i.p.v. verder zuidwaarts |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Itapecerica-vestiging (Mina Tejuco Preto + concentratie) | Nacional de Grafite Ltda. | ROM grafieterts → grafietconcentraat (vlok, meerdere korrelgroottes) | onderdeel van 70 kt/j totale capaciteit over de drie mijnen (Tejuco Preto/Itapecerica, Paca/Pedra Azul, Califórnia/Salto da Divisa) samen; Itapecerica's eigen aandeel niet apart gepubliceerd | [1][6][9] |

## 6 · Stoppunt
De brief stopt bij de kade van Porto de Praia Mole: geen bron koppelt Nacional de Grafite specifiek aan deze haven of aan een met naam genoemde buitenlandse afnemer. Vitória is de dichtstbijzijnde grote exportterminal vanuit Itapecerica, geen bevestigde route — fase B (zee) is daarom bewust niet getekend.

## 7 · Open punten
- **Geen bron koppelt Nacional de Grafite aan Porto de Praia Mole of aan een buitenlandse afnemer** — geen gepubliceerd exportvolume of -bestemming per haven; geen Wikipedia-pagina voor het bedrijf of de Itapecerica-vestiging gevonden (Wikipedia-API leeg). Dit is en blijft de zwakste schakel van de drie prioritaire M31-assen, exact zoals het ontwerp en de haalbaarheidstoets al inschatten.
- **Truck-km niet gepubliceerd**: §2/b1 is een ontwerpschatting (som van de via-keten, ~570 km) tegen een hemelsbrede afstand van 510,5 km; wordt bij het bakken vervangen door de gemeten weggeometrie.
- **Exacte berth/sítio bij Praia Mole onbekend**: het complex omvat meerdere operators (ertsopslag, pelletfabriek, bulkkades); welk deel eventueel grafiet zou verladen is niet gedocumenteerd.
- **Itapecerica's eigen productieaandeel** (van de 70 kt/j over drie mijnen) is niet apart gepubliceerd.
- **Geen fase D/E**: geen bron noemt een fabriek die dit vlokgrafiet ontvangt — vervalt per de lichte werkwijze.

## 8 · Bronnen
[1] Nacional de Grafite, "Units and Head Office" — adres Itapecerica: Highway MG 164, No number, Km 04, Água Limpa, 35550-000, Itapecerica-MG. https://www.grafite.com/en/units-and-head-office
[2] Nacional de Grafite, "A Nacional de Grafite" — R&D-centrum in Itapecerica-MG; producten verkocht op vijf continenten, direct of via distributeurs. https://www.grafite.com/en/a-nacional-de-grafite
[3] Nacional de Grafite, officiële site (overzicht). https://www.grafite.com
[4] BrasilMineral, "Nacional de Grafite" (Maiores Empresas do Setor Mineral 2026) — opgericht 1939, hoofdvestiging Itapecerica/MG, productiecapaciteit 2025/2026 70 mil t grafite over de mijnen Tejuco Preto (Itapecerica), Paca (Pedra Azul) en Califórnia (Salto da Divisa). https://brasilmineral.com.br/maiores/nacionaldegrafite
[5] Econodata, bedrijfsdossier Nacional de Grafite Ltda. (CNPJ 21.228.861/0001-00). https://www.econodata.com.br/consulta-empresa/21228861000100-NACIONAL-DE-GRAFITE-LTDA
[6] Wikipedia (en), "BR-262 (Brazil highway)" — oost-westcorridor Vitória (ES) ↔ Corumbá (MS), via Betim/Nova Serrana (MG); duplicatie Viana(ES)-grens MG. https://en.wikipedia.org/wiki/BR-262_(Brazil_highway)
[7] Wikipedia (en), "List of ports and harbours of the Atlantic Ocean" — Praia Mole vermeld als haven, Espírito Santo, Brazilië. https://en.wikipedia.org/wiki/List_of_ports_and_harbours_of_the_Atlantic_Ocean
[8] OpenStreetMap/Nominatim + Photon (ODbL) — reverse-geocode bevestigt adres/postcode 35550-000 op MG-164 (ontwerp-coördinaat); "Aeródromo Nacional Grafite I" (Neolândia, Itapecerica, 35550-000) als onafhankelijke OSM-bevestiging van een Nacional de Grafite-vestiging in dit gebied; via-puntnamen (Nova Serrana, Belo Horizonte, São Domingos do Prata, Manhuaçu, Domingos Martins, Viana). https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (z13–z18, live): `v2/build-cache/satcheck/sat-grafiet-itapecerica-vitoria-{wide,airfield,roadaxis,plant-close,praiamole}.png`.
[10] Overpass API (OSM/ODbL) — way's met `ref=BR-262` bevestigen het tracé (Rodovia Senador Eliseu Resende / Rodovia Federal Deputado Aloízio Santos / Avenida Mário Gurgel bij Vitória) en de haalbaarheidstoets-coördinaat van Porto de Praia Mole (-20.2896455, -40.2350039) als bestaand industrieterrein/haven.
[11] Haalbaarheidstoets M31 golf 2 (bindend): Itapecerica-anker lag bij reverse-geocode exact op de wegas van MG-164, niet aantoonbaar op het fabrieksterrein — in deze brief verlegd naar het satelliet-gelegde terreincomplex (zie §3); fase B blijft bewust ongetekend.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom:** `grafiet-itapecerica-vitoria` · **bestand:** `v2/data/stroomroute-grafiet-itapecerica-vitoria.json` (328,1 KB) ·
**recept:** `bak_grafiet_itapecerica_vitoria()` in `v2/tools/bak_stromen.sh` · **profiel:**
`grafiet-itapecerica-vitoria-itapecerica-praiamole` in `v2/tools/maak_stroombeen_weg.py`.

**Benen:** één been, truck, kade→kade doorgetrokken (geen zee, geen fase B — zoals §6 al vastlegde).

| # | modaliteit | km | naad | stippel | van → naar |
|---|---|---|---|---|---|
| b1 | truck | 751,6 km | 0,00 km (eerste been) | nee | Itapecerica-vestiging → Porto de Praia Mole (BR-262) |

**Markers (2):** `gr-itapecerica-plant` (-20,4420 / -45,1300, laadplek, been-start) ·
`gr-praiamole-kade` (-20,28965 / -40,23500, exportterminal, been-eind, stoppunt — geen overslag naar een volgend been).

**Toets:**
- Lengte: gemeten weggeometrie **751,6 km** tegen de ontwerpschatting van ~570 km (som via-keten) = **+31,9%**,
  ruim buiten de standaard ±15%-norm. Zoals de bak-aanwijzing voorschreef is dit coulanter behandeld — er is geen
  gepubliceerde bronkm, alleen een corridor-redenering — en de afwijking blijft staan als **bevinding**, niet
  dichtgetrokken door een via-punt te verschuiven. De hemelsbrede plant→kade-afstand is 510,5 km; de omwegfactor
  van de gemeten lijn (751,6/510,5 ≈ 1,47) is normaal voor een 570 km-corridor door een metropoolregio (Belo
  Horizonte) en een bergpas (Domingos Martins).
- Naden: geen (één been).
- Knikken (`toets_knikken.py`): 36 knikken ≥60°, waarvan 1 omkering (164,5°, R 22 m, bij de Praia Mole-kade —
  havenweg-kopmaak) en **0 terugloop** — de enige klasse die reparatie zou vragen.
- Rechte benen (`toets_rechte_benen.py --min-km 5`): geen treffer voor deze stroom — geen been met omwegfactor
  1,000 dat alsnog een stippel zou moeten zijn.
- Anker-verbindingsstukjes: plant → weg 0,03 km [OK] · weg → kade 0,04 km [OK] — beide ruim binnen de norm, dus
  **geen last-mile-stippel** nodig.
- Bestandsvorm: `versie 2` · `punt_formaat lonlat` · modaliteit `truck` (geldig) · been ≥2 punten (15.389) ·
  328,1 KB.

**Toelichting stippels/haven-aanloop:** geen — dit is een puur landbeen zonder zee, geen haven-aanloop van
toepassing.

**Gereedschapslessen:**
- De ontwerpschatting (~570 km, som van de via-keten hemelsbreed) bleek een aanzienlijke onderschatting van de
  echte weggeometrie (751,6 km) — via-keten-sommen van hemelsbrede segmenten onderschatten systematisch de
  werkelijke wegafstand door een metropoolregio en een bergpas, en dat verschil hoort als bevinding in de brief
  te blijven staan, niet als lengtetoets-fout te worden behandeld.
- `eindklassen` (residential/service/tertiary/unclassified) pakten zowel de first mile bij de plant (0,45 km) als
  de last mile bij het havencomplex (4,87 km, service-klasse rond de Praia Mole-terminal) probleemloos op zonder
  `eindToegangPrivaat`-vlag — geen privéterrein-toegang zoals bij Phillips 66/Codelco-achtige profielen.
- 126 keerlussen gesnoeid (787,3 → 751,5 km) door `snoei_keerlussen`, waaronder een lus van 21,55 km bij
  São Domingos do Prata en 13,89 km bij Nova Serrana — normale dubbelgereden OSM-stukken op een lange
  nationale-wegcorridor, geen teken van een verkeerde wegklasse-keuze.

**Open punten (ongewijzigd t.o.v. §7):** geen bron koppelt Nacional de Grafite aan Porto de Praia Mole of aan een
buitenlandse afnemer; truck-km was niet gepubliceerd (nu vervangen door de gemeten 751,6 km); het exacte
berth/sítio bij Praia Mole blijft onbekend; Itapecerica's eigen productieaandeel (van de 70 kt/j over drie mijnen)
is niet apart bekend — behandeld als sites-zonder-gewicht voor een latere sitelaag-toevoeging, niet aan dit ene
punt toegekend. Geen fase D/E (vervalt per de lichte werkwijze).
