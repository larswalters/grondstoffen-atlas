# Routebrief (licht) · Zeldzame aardmetalen — Chavara → Aluva (India)

**stroom-id:** `ree-chavara-aluva` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) · **status:** gebakken
**Keten in één zin:** monaziet(-houdend mineraalconcentraat) van IREL's kustzand-mineraalscheidingsplant in Chavara
(Kollam-district, Kerala) per **truck** over de NH-66-kustweg en NH-544 naar IREL's Rare Earths Division (RED) in
Aluva/Udyogamandal aan de Periyar-rivier, waar het tot hoogzuivere La/Ce/NdPr/Sm/Gd/Y-verbindingen wordt gescheiden.
**Welke as van het verhaal:** Zuid-Azië-reserve — een korte, zekere binnenlandse IREL-corridor (één land, geen zee/
spoor/tweede overslag) naast as 1 (OSCOM Odisha → RED Aluva); wordt alleen gebakken als as 1 vastloopt, want beide
eindigen op dezelfde naar-site.

## 1 · Ketenkaart
```
Chavara mineraalscheidingsplant `ree-chavara-scheiding` ──(b1 truck · NH-66 → NH-544 · ~124-150 km)──► RED Aluva
    `ree-aluva-red` (Udyogamandal, Periyar-oever) ── stoppunt
```
Geen overslag, geen spoor/zee/leiding: één binnenlands truckbeen, één land. Manavalakurichi (Kanyakumari) staat in
het ontwerp als alternatieve tweede bron maar zit niet in de opgegeven benen-lijst en wordt hier niet getekend.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-chavara-scheiding` → `ree-aluva-red` | NH-66 (Kollam-kustweg, Karunagappally→Kayamkulam→Alappuzha→Cherthala→Aroor) → NH-544 (Edappally→Kalamassery→Aluva) | hemelsbreed 124,3 km, geen wegkm [webcheck; IREL/Wikipedia noemt "ca. 135 km van Kochi" voor Chavara alléén, geen cijfer voor de hele Chavara→Aluva-route — zie §7] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-chavara-scheiding` | mijn/mineraalscheiding (kop) | IREL Chavara Mineral Division (Mannumala-mijnsite) | 8.98583, 76.52485 | [5][8] | bron-gelegd (z15/z17 gezien: kustmijnbouw-terrein — zandwinning op de smalle landtong tussen zee en de Kayamkulam-achterwaterlagune, verharde uitgravingsvlaktes en voertuigsporen; de aansluitende mineraalscheidingsgebouwen met tanks/loodsen liggen ~200 m zuidelijker in beeld) |
| `ree-aluva-red` | raffinaderij (staart) | IREL Rare Earths Division (RED), Udyogamandal/Edayar, Aluva | 10.08133, 76.29761 | [6][8] | bron-gelegd (z15/z17 gezien: industrieel bedrijventerrein met loodsen en kleine opslagtanks direct aan de westoever van de Periyar, tussen de fabrieksstraten van de Edayar-industriezone — komt overeen met "op de Periyar-oever, 12 km van Kochi" [1]; ligt 190 m van het onafhankelijk satellietgelegde `udyogamandal`-punt van de parallelle keten `ree-oscom-aluva` — zie §7) |

## 4 · Via-punten (b1 — corridorkeuze op de doorgaande NH-66/NH-544)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kayamkulam-bypass (NH-66) | 9.17217, 76.51629 | de aangewezen NH-66-bypass om Kayamkulam-centrum heen, geen zijtak [7] |
| b1 | 2 | Alappuzha-bypass (NH-66) | 9.48955, 76.31949 | NH-66-bypass om Alappuzha-centrum heen (OSM-naam "Alappuzha Bypass" op de weg zelf) [7] |
| b1 | 3 | Cherthala (op de Salem–Kochi–Kanyakumari-weg = NH-66) | 9.69120, 76.32572 | pint de doorgaande NH-66-lijn tussen Alappuzha en de Aroor-oversteek [7] |
| b1 | 4 | Kumbalam–Aroor-brug (NH-66) | 9.88509, 76.30852 | de brug waarmee NH-66 de achterwaterarm bij Aroor oversteekt richting Kochi — enige doorgaande oeververbinding hier [7] |
| b1 | 5 | Edappally (knooppunt NH-66 ↔ NH-544) | 10.02549, 76.30798 | hier verlaat de route NH-66 (verder naar Kozhikode) en slaat NH-544 in (voorheen NH-47, richting Aluva) — de enige corridorkeuze op deze rit [1][7] |
| b1 | 6 | Kalamassery (op NH-544, laatste stuk vóór Edayar) | 10.05217, 76.31990 | pint NH-544 vast tussen Edappally en de afslag naar de Udyogamandal/Edayar-industriezone [7] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Chavara Mineral Division | IREL (staats-PSU, DAE) | kustzand → ilmeniet/rutiel/zirkoon/sillimaniet + monaziet (nevenfractie, niet apart gekwantificeerd) | 235.900 t/j ilmeniet + geassocieerde mineralen (géén los monaziet-cijfer) | [1][3] |
| RED Aluva (Udyogamandal) | IREL (staats-PSU, DAE) | monaziet/gemengd REE-chloride → hoogzuivere La/Ce-oxide-carbonaat + NdPr/Sm/Gd/Y-oxide-oxalaat (>99%) + DAE-strategische materialen | ~10.000 t/j REE-houdend mineraal (IREL-bedrijfsbreed ontworpen capaciteit, geen Aluva-specifiek cijfer) | [1] |

## 6 · Stoppunt
De brief stopt bij RED Aluva: het is de eerste IREL-unit (1952) en verwerkt monaziet tot verkoopbare hoogzuivere
REO-verbindingen die naar de VS, VK, Frankrijk, Duitsland, Noorwegen en Japan gaan [1] — maar geen bron noemt een
specifieke magneetfabriek of afnemer voor déze corridor per zending, dus fase D/E vervallen (conform §1: alleen
tekenen als één bron de fabriek noemt).

## 7 · Open punten
- **Geen gepubliceerde wegkm voor Chavara→Aluva** (zoals de haalbaarheidstoets al signaleerde): alleen hemelsbreed
  124,3 km tussen de site-ankers; Wikipedia/IREL noemt "ca. 135 km van Kochi" maar dat is Chavara→Kochi, niet
  Chavara→Aluva. De via-puntensom (rechte segmenten door de 6 punten in §4) is 129,1 km — een indicatie, geen norm.
- **`ree-aluva-red` (10.08133, 76.29761) ligt 190 m** van het onafhankelijk satellietgelegde `udyogamandal`-anker
  van de parallelle keten `ree-oscom-aluva` (10.08300, 76.29800; zelfde naar-site, andere agent, zelfde industriële
  cluster op de Periyar-oever) — aanbevolen dat de orkestrator deze twee bij het bakken/de sitelaag op één
  coördinaat gelijktrekt, zoals bij eerdere golven met site-coördinaten van dezelfde naar-site is gedaan.
- **Manavalakurichi (Kanyakumari)** — de alternatieve/tweede bron uit het ontwerp — is niet getekend: de opgegeven
  benen-lijst bevat alleen Chavara→Aluva; een MK→Aluva-been zou een apart, niet aangevraagd been zijn.
- **Geen los monaziet/REO-jaarvolume voor déze corridor gevonden** binnen het webbudget — alleen Chavara's totale
  mineraalscheidingscapaciteit (235.900 t/j, overwegend ilmeniet/rutiel/zirkoon) en IREL's bedrijfsbrede ontworpen
  REE-mineraalverwerkingscapaciteit (~10.000 t/j); de monaziet-fractie zelf is in geen bron apart gekwantificeerd.
- **Overgang NH-66 → NH-544 bij Edappally** is de gebruikelijke, algemeen beschreven routekeuze (Kochi-omleiding
  naar Aluva) maar niet apart gebrond per een officiële wegenkaart — de bak-agent toetst dit met de echte wegscan.

## 8 · Bronnen
[1] Wikipedia, "IREL (India)" — Production facilities: Rare Earths Division (RED) Aluva ("op de Periyar-oever,
    12 km van Kochi, 15 km van Kochi International Airport"; operationeel sinds 1952; La/Ce/NdPr/Sm/Gd/Y-oxides);
    Chavara Mineral Division (235.900 t/j ilmeniet+geassocieerde mineralen); Manavalakurichi-unit.
    https://en.wikipedia.org/wiki/IREL_(India)
[2] Wikipedia, "Economy of Kollam" — Indian Rare Earths Limited (IREL) als onderdeel van de Kollam-industrie.
    https://en.wikipedia.org/wiki/Economy_of_Kollam
[3] Wikipedia, "Natural resources of India" — "Mining is done at Chavara, Chatrapur, Aluva and Manavalakurichi by
    Indian Rare Earths limited." https://en.wikipedia.org/wiki/Natural_resources_of_India
[4] Wikipedia, "List of government of India establishments in Kerala" — "Indian Rare Earths (Chavara & Aluva)".
    https://en.wikipedia.org/wiki/List_of_government_of_India_establishments_in_Kerala
[5] OpenStreetMap/Nominatim (ODbL) — "Mannumala - IREL Mining Site", landuse=industrial, Chavara/Kollam,
    8.9858331,76.5248516 (uit de haalbaarheidstoets van dit werkorder). https://www.openstreetmap.org
[6] OpenStreetMap/Photon (ODbL) — "Indian Rare Earths Limited", landuse=industrial, Edayar/Paravur, Kerala,
    10.0813324,76.2976116. https://www.openstreetmap.org
[7] OpenStreetMap/Nominatim (ODbL) — wegpunten op de Salem–Kochi–Kanyakumari Road (NH-66)/NH-544: "Alappuzha
    Bypass", "Kayamkulam"-bypass (way "Bypass", Onnamkutty), "Cherthala" (station aan de NH-66), "Kumbalam Aroor
    Bridge" (NH-66-oversteek), "Edappally" en "Kalamassery". https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15/z17) —
    `v2/build-cache/satcheck/sat-ree-chavara-aluva-{chavara,chavara-zoom,aluva,aluva-zoom}.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)
**Eén been, één modaliteit (truck), geen zee/spoor/leiding/binnenvaart/overslag.**

| # | modaliteit | km | punten | stippel? | recept |
|---|---|---|---|---|---|
| b1 | truck | **143,2 km** | 2.775 | nee | `maak_stroombeen_weg.py --profiel ree-chavara-aluva-chavara-aluva` (profiel in `PROFIELEN`, `v2/tools/maak_stroombeen_weg.py`) → `bak_ree_chavara_aluva()` (`v2/tools/bak_stromen.sh`) |

**Totaal 143,2 km · 2.775 punten · 2 markers.** Output: `v2/data/stroomroute-ree-chavara-aluva.json` (51,6 KB).

**KM-toelichting (geen harde toets, brief §2/§7):** hemelsbreed tussen de site-ankers is 124,3 km,
de via-puntensom (rechte segmenten door §4) 129,1 km — beide alleen indicatie. De gemeten wegkm
is **143,2 km**, verhouding **1,15** tegen hemelsbreed (typische wegfactor 1,1–1,3×) — plausibel en
binnen de vooraf ingeschatte bandbreedte (~135–165 km, zie de bak-aanwijzingen). Vijf keerlussen
gesnoeid (146,4 → 143,0 km getekende weggeometrie; 143,2 km inclusief de twee korte
anker-verbindingsstukjes van 0,07 en 0,11 km, plant → weg resp. weg → kade — geen stippel nodig,
beide ruim onder 0,5 km).

**Stippels: geen.** Beide ankers liggen op industrieterrein met normale toegangswegen en snappen
op 0,07 resp. 0,11 km op het wegnet (§bak-aanwijzingen van het werkorder); geen van de twee ligt
> 2 km van het net, dus geen "last mile (geen net op deze korrel)"-stippel.

**Haven-aanloop / vlucht / leiding:** n.v.t. — één binnenlands wegbeen, geen zee-, lucht- of
leidingcomponent.

**Gedeelde benen:** geen — dit been deelt geen geometrie met een bestaande stroom.

**Toets (§5 bakhandleiding-licht.md):** `toets_knikken.py` → 14 knikken ≥ 60° (alle "spike",
0 omkeringen ≥ 150°, 0 terugloop) — normale weg-junctieknikken, geen fout. `toets_rechte_benen.py
--min-km 5` markeert dit been NIET als rechte lijn (echte, gekromde weggeometrie). Contract:
`versie 2`, `punt_formaat lonlat`, modaliteit `truck` ∈ toegestane set, been ≥ 2 punten (2.775),
bestand 51,6 KB. Naad = 0,00 km (enkel been). Markers op 0,0 km resp. 0,0001 km van de lijn
(anker = routeerpunt).

**Lessen / open punten:**
- **`ree-aluva-red` (10,08133/76,29761) ligt 190 m van het onafhankelijk satellietgelegde
  `udyogamandal`-anker van de parallelle keten `ree-oscom-aluva`** (10,08300/76,29800, zelfde
  naar-site, zie `v2/build-cache/satcheck/sat-ree-oscom-aluva-udyogamandal-z16.png`). NIET
  zelf gelijkgetrokken bij het bakken — dat zou andermans brief/anker wijzigen; gemeld aan de
  orkestrator (aanbeveling: één van de twee coördinaten kiezen en in beide brieven/de
  ree-sitelaag gelijktrekken). `ree-oscom-aluva` is nog niet gebakken op het moment van deze bake.
- Deze keten wordt per ontwerp niet gelijktijdig met `ree-oscom-aluva` ingezet (zelfde naar-site) —
  alleen als As1 (OSCOM → Aluva) vastloopt.
- Geen gepubliceerde wegkm gevonden binnen het webbudget (zie §7); de ±15%-toets is hier
  uitgevoerd als indicatie, niet als harde norm, conform de brief zelf.
