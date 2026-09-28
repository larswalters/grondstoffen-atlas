# Routebrief (licht) · gas — Arzew (Algerije) → Barcelona (Spanje)

**stroom-id:** `gas-arzew-barcelona` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) · **status:** gebakken
**Keten in één zin:** Saharagas van het **Hassi R'Mel-gasveld** loopt via het Algerijnse nationale trunknet naar het
**Arzew LNG-complex** (GL1Z/GL2Z/GL3Z, Sonatrach), wordt daar tot LNG verwerkt en vaart per **LNG-carrier** rechtstreeks
over de westelijke Middellandse Zee (géén zeestraat) naar het Spaanse LNG-net bij Barcelona — de eerste korte
Middellandse-Zee-as van de kaart.
**Welke as van het verhaal:** Algerije levert Spanje nog steeds gas, via twee onafhankelijke routes — de onderzeese
Medgaz-pijp (Hassi R'Mel → Almería, niet Barcelona) én LNG-ladingen vanuit Arzew/Skikda. Deze keten is die tweede,
LNG-route; welke van Spanje's zeven regasterminals het Arzew-volume daadwerkelijk ontvangt is niet gebrond (zie §7).

## 1 · Ketenkaart
```
Hassi R'Mel-gasveld `gas-hassirmel-veld` (Algerije, binnenland)
   ──(b1 leiding · nationaal trunknet, kandidaten GG1/GK3-Borg Chegga/RGZ3/LZ2 · hemelsbreed ~400 km, geen
       leidingkm, aannemelijk: exacte way-keten bake-werk)──►
Arzew LNG-complex `gas-arzew-laad` (GL1Z/GL2Z/GL3Z, Sonatrach)
   ──(b2a zee · haven-aanloop Arzew, stippel, 10,35 km)──►
   ──(b2 zee · westelijke Middellandse Zee, rechtstreeks, géén zeestraat · hemelsbreed ~650 km · MARNET)──►
   ──(b2b zee · haven-aanloop Barcelona, stippel, 5,09 km)──►
Spaans LNG-net bij Barcelona `gas-barcelona-los` (aannemelijk: welke terminal ontvangt, niet gebrond) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-hassirmel-veld` → `gas-arzew-laad` | nationaal trunknet, kandidaten GG1/GK3-Borg Chegga/RGZ3/LZ2 (excl. Krechba-In Salah/GALSI, zie §7) | hemelsbreed ~400 km, geen leidingkm gevonden | OSM-pipeline (way-stitch, bake-werk) | nee — doorgetrokken, aannemelijk (exacte way-keten dit sessie niet stuk voor stuk gevolgd) |
| b2a | B | zee | `gas-arzew-laad` → zeeknoop 9074 (35,85230,-0,13870) | haven-aanloop Arzew | 10,35 [eigen meting] | rechte stippel of `maak_havenaanloop.py` | ja — kade > 5 km van zeeknoop (bakhandleiding §2) |
| b2 | B | zee | zeeknoop 9074 → zeeknoop 3723 (41,31220,2,20940) | westelijke Middellandse Zee, rechtstreeks | hemelsbreed ~650 [ontwerp] | MARNET (knoop → knoop) | nee |
| b2b | B | zee | zeeknoop 3723 → `gas-barcelona-los` | haven-aanloop Barcelona | 5,09 [eigen meting] | rechte stippel of `maak_havenaanloop.py` | ja — kade > 5 km van zeeknoop (bakhandleiding §2) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-hassirmel-veld` | gasveld / kop leiding | Hassi R'Mel-gasveld, Sonatrach | 32.94722, 3.17056 | [3][9] | bron-gelegd (z14 gezien: dicht netwerk van toegangswegen, well pads en een centrale procesinstallatie met twee donkere bekkens (productiewater/faciliteit) — industrieel gasveldterrein, geen bebouwde kom; coördinaat = Wikipedia-geohack, dit sessie zelf satellietgecheckt — vervangt het niet-herbevestigde v1-registerpunt 32.90/3.30 [7]) |
| `gas-arzew-laad` | laadplek / LNG-liquefactie | Arzew LNG-complex (GL1Z/GL2Z/GL3Z, Sonatrach) | 35.8078, -0.2395 | [1][2][6] | bron-gelegd — **letterlijk hergebruikt** uit `v2/design/gas-sitelaag.json` (site-id `w-arzew`, satelliet z16 al gelegd op de bolvormige LNG-tanks aan de kade) |
| `gas-barcelona-los` | losplek / LNG-regasificatie | "Planta de Barcelona" (Enagás), Zona Franca, Barcelona | 41.3405, 2.1615 | [5][6] | bron-gelegd — **letterlijk hergebruikt** uit `v2/design/gas-sitelaag.json` (site-id `w-barcelona`, satelliet z16 al gelegd op het LNG-tankencomplex met eigen havenhoofd) |

## 4 · Via-punten
Niet van toepassing: b2 is een zeebeen zonder corridorkeuze (MARNET routeert knoop→knoop); b1 is een leiding-been
zonder wegcorridor — de exacte OSM-way-keten is bake-werk (§7), geen via-puntkeuze op brief-niveau.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Arzew LNG-complex | Sonatrach | pijpleidinggas → LNG | GL1Z 7,8 + GL2Z 8,4 + GL3Z 4,7 = 20,9 Mtpa × 1,36 ≈ **28,4 bcm/j** (peiljaar 2024/2025; GL4Z/CAMEL 0,9 Mtpa buiten bedrijf sinds 2010) | [1][2][6] |
| Spaans LNG-net (Barcelona als kandidaat-terminal) | Enagás | LNG → hervergast gas naar het Spaanse net | Barcelona indicatief ~13,2 bcm/j regascapaciteit (geen vers 2024/2025-cijfer); Spanje telt daarnaast Cartagena, Huelva, Bilbao, Sagunto, El Musel, Mugardos als regasterminals [5][6] | [5][6] |

## 6 · Stoppunt
De brief stopt bij het Spaanse LNG-net rond Barcelona: geen bron bevestigt welke van Spanje's zeven regasterminals
het Arzew-volume daadwerkelijk ontvangt (zie §7), en er is geen gedocumenteerde downstream-fabriek of -afnemer die
deze specifieke lading met naam verbindt — fase C/D/E vervallen.

## 7 · Open punten
- **Bestemmingsterminal niet cargo-specifiek gebrond.** `gas-barcelona-los` is het enige Algerije-relevante
  sitelaag-anker in Spanje en wordt daarom als geografisch eindpunt aangehouden, maar Spanje heeft zes andere
  regasterminals (Cartagena, Huelva, Bilbao, Sagunto, El Musel, Mugardos) en geen bron in dit sessie koppelt het
  Arzew-volume specifiek aan Barcelona — AIS-scheepsbewegingsdata zou dit vóór het bakken moeten bevestigen
  (haalbaarheidstoets-aanpassing 1).
- **Fase A-corridor is dit sessie NIET stuk voor stuk gevolgd.** Een pyosmium-scan op de lokale Algerije-extract
  (`v2/build-cache/geofabrik/algerije-latest.osm.pbf`) vond 2.477 `man_made=pipeline substance=gas`-ways, waarvan
  76 benoemd. De vier kandidaat-namen uit het ketenontwerp zijn teruggevonden met exacte coördinaten (zie
  bak_aanwijzingen), maar de doorlopende reeks tussen Hassi R'Mel en Arzew bestaat grotendeels uit **onbenoemde**
  ways — dit is bake-werk (topologische component-check, zoals bij `gas-bonny-zeebrugge` b2 gedaan is), niet aangenomen.
- **Twee namen zijn BEWEZEN VERKEERDE CORRIDOR en moeten uitgesloten worden:** `Krechba - In Salah`
  (way 391023450, rond 28,07–28,57 N / 2,14–2,40 O — het In Salah Gas-project, ~500 km ten zuiden van Hassi R'Mel,
  niets met de Arzew-export te maken) en `GALSI` (ways 225282712/379118070/1393655399, rond 36,02–36,88 N /
  6,17–8,07 O — het geannuleerde Algerije-Sardinië-Italië-tracé, ver ten oosten van de Arzew-corridor). Beide dit
  sessie zelf gecontroleerd op coördinaat, niet alleen op naam.
- **`GK3 - Borg Chegga`** (ways 469395884/469395885/485487144, rond 34,42–34,47 N / 4,79–5,89 O) ligt geografisch
  ten OOSTEN van Hassi R'Mel, richting Touggourt/El Oued — niet aantoonbaar op weg naar Arzew (dat ten
  noordwesten ligt). De bake-agent moet de richting verifiëren vóór dit segment wordt meegenomen; mogelijk hoort
  het bij een andere corridor.
- **Geen gepubliceerde leidingkm voor fase A** (hemelsbreed ~400 km) en **geen gepubliceerde routelengte voor
  fase B** (hemelsbreed ~650 km) — beide pas na het bakken bekend; de ±15%-toets geldt daarom als indicatie, niet
  als harde norm.
- **Geen Arzew→Barcelona-specifiek cargovolume gevonden.** Wel bevestigt de haalbaarheidstoets-webcheck dat Spanje
  in 2025 ca. 1,44 Mt Algerijnse LNG ontving en dat Algerije gecommitteerd blijft aan gasleveringscontracten met
  Spanje (Medgaz + TransMed + LNG uit Arzew/Skikda) — een jaartotaal, niet Barcelona-specifiek.
- **Medgaz is bewust niet als pijpleidingas gekozen** (conform het ketenontwerp): die onderzeese leiding
  (Hassi R'Mel → Beni Saf → Almería, 10,5 bcm/j) draagt in OSM slechts een kort naamfragment aan elke kust en
  gaat bovendien naar Almería, niet Barcelona — bevestigd via Wikipedia [4].

## 8 · Bronnen
[1] Wikipedia (EN) — "List of LNG terminals": Arzew GL1Z 7,8 + GL2Z 8,4 + GL3Z 4,7 Mtpa (Sonatrach), GL4Z/CAMEL 0,9 Mtpa gesloten sinds april 2010; Barcelona (Enagás) als operationele regasterminal. https://en.wikipedia.org/wiki/List_of_LNG_terminals
[2] Wikipedia (EN) — "Arzew": coördinaten 35,850°N/-0,317°O (stadscentrum-referentie); industrieel havengebied met LNG-exportraffinage sinds de Algerijnse onafhankelijkheid. https://en.wikipedia.org/wiki/Arzew
[3] Wikipedia (EN) — "Hassi R'Mel gas field": coördinaten 32,94722/3,17056; grootste gasveld van Algerije, 550 km ten zuiden van Algiers, productie sinds 1961, geraamde reserves 2,415 biljoen m³. https://en.wikipedia.org/wiki/Hassi_R%27Mel_gas_field
[4] Wikipedia (EN) — "Medgaz": onderzeese pijpleiding Hassi R'Mel → Beni Saf (547 km onshore) → Perdigal Beach, Almería (210 km offshore), gekoppeld aan de Almería-Albacete-pijpleiding; 8 bcm/j initiële capaciteit; NIET verbonden met Barcelona. https://en.wikipedia.org/wiki/Medgaz
[5] Wikipedia (EN) — "Enagás": eigenaar van regasterminals in Huelva, Barcelona, Cartagena en Gijón (El Musel), plus 50% Bilbao (BBG) en 72,5% Sagunto (Saggas) — bevestigt Spanje's meervoudige LNG-terminalnet. https://en.wikipedia.org/wiki/Enag%C3%A1s
[6] `v2/design/gas-sitelaag.json` — site `w-arzew` (35,8078/-0,2395, bron-gelegd z16, [B12]) en site `w-barcelona` (41,3405/2,1615, bron-gelegd z16, [B28]) — letterlijk hergebruikte ankers.
[7] `data/gas.js` / `design/gas.md` (v1-register) — `gas-algeria` (Hassi R'Mel) 32,90/3,30; `gas-lng-arzew` 35,80/-0,27; `gas-regas-es` (Barcelona/Sines) 41,35/2,15 — checklist-startpunt, dit sessie vervangen door een verse, zelf gecontroleerde Wikipedia-coördinaat voor Hassi R'Mel.
[8] OpenStreetMap (ODbL) via lokale Geofabrik-extract `algerije-latest.osm.pbf` (pyosmium-scan, dit sessie) — 2.477 `man_made=pipeline substance=gas`-ways, waaronder de benoemde segmenten GG1 (ways 224794671/889728478/1155377188/1155377191), GK3-Borg Chegga (ways 469395884/469395885/485487144), RGZ3 (way 1316630656), LZ2 (way 578918608), Krechba-In Salah (way 391023450, uitgesloten) en GALSI (ways 225282712/379118070/1393655399, uitgesloten). https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14) — `v2/build-cache/satcheck/sat-gas-arzew-barcelona-hassirmel.png`.
[10] Lokale zeeknoop-afstandsberekening via `v2/tools/hecht_marnet.py` (MARNET-net `v2/build-cache/marnet-preais`, geen internet nodig) — Arzew 10,35 km tot zeeknoop 9074, Barcelona 5,09 km tot zeeknoop 3723.
[11] Haalbaarheidstoets-webcheck (dit ketenontwerptraject) — Spanje ontving in 2025 ca. 1,44 Mt Algerijnse LNG; Algerije blijft gecommitteerd aan gasleveringscontracten met Spanje (Medgaz + TransMed + LNG-ladingen vanuit Arzew/Skikda).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Recept:** `v2/tools/bak_stromen.sh` → `bak_gas_arzew_barcelona()`. Draaien: `bash v2/tools/bak_stromen.sh gas-arzew-barcelona`.
**Uitvoer:** `v2/data/stroomroute-gas-arzew-barcelona.json` (8,8 KB, contract versie 2, `punt_formaat` lonlat).

| # | modaliteit | km | punten | stippel | toelichting |
|---|---|---|---|---|---|
| 1 | leiding | 7,3 | 2 | ja | gasveld-verzamelnet Hassi R'Mel → trunkleiding — geen OSM-way op het veldterrein |
| 2 | leiding | 496,0 | 288 | nee | Houd El Hamra-trunkleiding Hassi R'Mel → Arzew (aannemelijk: exacte way-keten bake-werk) |
| 3 | leiding | 1,5 | 2 | ja | trunkleiding → Arzew LNG-complex — geen OSM-way op het complexterrein |
| 4 | zee | 11,6 | 21 | ja | haven-aanloop Arzew (`maak_havenaanloop.py` geslaagd) |
| 5 | zee | 700,8 | 81 | nee | LNG-carrier Arzew → Barcelona (westelijke Middellandse Zee, MARNET knoop→knoop) |
| 6 | zee | 5,1 | 2 | ja | haven-aanloop Barcelona (`maak_havenaanloop.py` timeout 300 s → rechte stippel, geen tweede poging) |
| **totaal** | | **1.222,3** | **396** | | **3 markers**, alle exact 0 m van hun lijn |

**Fase A (b1, leiding) — het zwakste punt van de keten, opgelost met een topologische component-graaf.**
Nieuw gereedschap `v2/tools/maak_leidingbeen_gas_hassirmel_arzew.py`: een pyosmium-scan over de lokale
`algerije-latest.osm.pbf` vond 794 `man_made=pipeline substance=gas`-ways (na uitsluiting van de twee bewezen-
verkeerde corridors op way-id: Krechba-In Salah way 391023450, GALSI ways 225282712/379118070/1393655399). De
graaf op gedeelde OSM-node-refs valt uiteen in **502 componenten** — de globaal dichtstbijzijnde vertices bij
elk anker lagen op kleine geïsoleerde stompen (19 resp. 17 vertices) die NIET met elkaar verbonden zijn, dus een
naïeve "snap op de dichtstbijzijnde vertex"-aanpak gaf ten onrechte "geen pad". Zaaien per component (kies de
component die beide ankers samen het dichtst benadert) vond de juiste: **775 vertices, namen "Houd El Hamra"/
"LZ2"**, 7,3 km van Hassi R'Mel en 1,5 km van Arzew. De Dijkstra daarbinnen geeft een doorlopend pad van
**496,0 km** (288 punten, omwegfactor 1,112 tegen de hemelsbrede 446,2 km tussen de exacte ankercoördinaten; de
brief-schatting van ~400 km hemelsbreed was zelf een ruwe aanname — de ±15%-toets gold hier al als indicatie,
geen harde norm, brief §7). **GK3-Borg Chegga (ways 469395884/469395885/485487144) is expliciet gecontroleerd
en ligt NIET op het gevonden pad** — de oostwaartse richting die de brief al vermoedde (§7) is hiermee bevestigd
en het segment is terecht niet meegenomen. Resultaat: b1 is **~98% doorgetrokken**, met twee kleine gestippelde
terreingaten (veldterrein Hassi R'Mel 7,3 km, complexterrein Arzew 1,5 km, geen OSM-way) — ver van de 100%-
stippel-klasse van Bingham Canyon → Garfield (golf 4, afgewezen); dat scenario is hier niet uitgekomen.

**Fase B (b2a/b2/b2b, zee) — twee verplichte haven-aanlopen (LAR-586), één geslaagd, één op de terugval.**
Arzew (10,35 km van MARNET-zeeknoop 9074): `maak_havenaanloop.py` slaagde (cel 0,005° kaal, 11,6 km, 21 punten,
0,80 km over land — geheel bij het kade-uiteinde, wat de korrel van de 1:10M-kustlijn is, geen fout). Barcelona
(5,09 km van zeeknoop 3723): `maak_havenaanloop.py` liep vast op `timeout 300` (exit 124) — geen tweede poging
(bakhandleiding §2) → rechte stippel van 5,1 km. Het hoofdzeebeen (zeeknoop → zeeknoop, 700,8 km) is doorgetrokken
MARNET-geometrie door de westelijke Middellandse Zee; geen gepubliceerde routelengte, dus de ±650 km hemelsbreed
uit het ontwerp blijft de enige referentie (omwegfactor 1,078 — indicatie, geen harde norm).

**Toets (bakhandleiding §5):** alle 6 naden 0,00 km · alle 3 markers exact 0 m van hun lijn · `toets_knikken.py`
geeft 2 knikken ≥60° op het zeebeen (78,7° bij 41,17610/2,31410 en 69,0° bij 36,20000/-0,60000), beide 0°
omkering/terugloop — normale bochten in de bestaande MARNET-geometrie, geen artefact van dit bakwerk ·
`toets_rechte_benen.py --min-km 5` flagt de twee lange stippels (7,3 km en 5,1 km) terecht als "omwegfactor 1,000"
— dat klopt, het zijn bewust rechte schematische gaten, geen gemiste corridor · JSON-contract: `json.load` slaagt,
`versie 2`, `punt_formaat lonlat`, modaliteiten `{leiding, zee}` (beide in de toegestane set), elk been ≥2 punten,
8,8 KB (ruim onder de norm). Geen afwijkingen buiten de norm.

**Lessen voor de volgende leiding-bake:** (1) een globale "dichtstbijzijnde vertex"-snap op een gefragmenteerde
pijpleidinggraaf geeft valse negatieven — snaai per samenhangende component, niet over de hele graaf; (2) een
component-graaf op 502 stukken kan tóch één dominant, bijna-doorlopend segment bevatten dat de brief niet met
naam kende (hier "Houd El Hamra", niet één van de vier ontwerpkandidaten) — de bake-uitkomst overschrijft dan de
ontwerpaanname, met bewijs; (3) een uitgesloten-op-coördinaat-segment (GK3) blijft na het bakken opnieuw
controleerbaar doordat het script expliciet rapporteert of die naam op het gevonden pad ligt.
