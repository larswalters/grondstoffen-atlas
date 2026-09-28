# Routebrief (licht) · Kobalt · Bou Azzer → Tichka-pas → Guemassa (land)

**stroom-id:** `kobalt-bouazzer-guemassa` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** kobalthoudend erts/concentraat van de ondergrondse Bou Azzer-mijn (CTT, Managem-dochter, Drâa-Tafilalet) per **truck** over de N9 door de Tizi n'Tichka-pas (Hoge Atlas) en via Marrakech naar het CTT Guemassa-hydrometallurgisch complex (vijf eenheden: kobaltkathodes, kopersulfaat, nikkelsulfaat, zinkoxide) — één landbeen, geen zeebeen, zelfde stoppunt-logica als `kobalt-ambatovy-toamasina`.
**Welke as van het verhaal:** *Marokko — de enige mijn ter wereld waar kobalt het hoofdproduct is.* Jaarvolume: **~1 kt Co/jaar** (v1-checklist `data/cobalt.js`, share 1, tier 3, indicatief/niet-peiljaar-specifiek — Managem publiceert productiecijfers per jaarverslag, exact peiljaar 2024/2025 niet in deze ronde bevestigd). Bou Azzer levert "voor het grootste deel" van Guemassa's concentraataanvoer [1][2].

## 1 · Ketenkaart
```
Bou Azzer-mijn `co-bouazzer-mijn` ──(b1 truck · N9/R203 via Ouarzazate, Tizi n'Tichka-pas, Aït Ourir, Marrakech · ~280 km schatting, geen gepubliceerde wegkm)──►
CTT Guemassa-complex `co-guemassa-fabriek` ── stoppunt (fase D/E vervallen — vijf productie-eenheden, geen enkele afnemer per stroom gedocumenteerd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Bou Azzer-mijn → CTT Guemassa-complex | N9 (Ouarzazate–Marrakech, Tizi n'Tichka-pas) → binnenstedelijk Marrakech als "Avenue Guemassa" → terrein | geen gepubliceerde referentie — alleen het gemeten getal (`maak_stroombeen_weg.py` meet de lengte zelf) [8][9] | `maak_stroombeen_weg` | nee |

Geen ±15%-lengtetoets mogelijk bij dit been (geen gepubliceerde wegkm gevonden, conform de haalbaarheidstoets) — het gemeten getal wordt in §9 genoteerd zonder referentiewaarde.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-bouazzer-mijn` | mijn / laadplek (kop) | Mine Bou Azzer (CTT, Managem), Drâa-Tafilalet, ~120 km zuid van Ouarzazate | 30.5184, -6.9134 | OSM/Nominatim, `landuse=quarry` node "Mine Bou Azzer" exact op deze coördinaat [4][10]; Managem zelf: "120 kilometres south of the town of Ouarzazate" [3] | **bron-gelegd** — hergebruikt uit het ketenontwerp + de haalbaarheidstoets ("rechtstreeks hergebruiken, niet opnieuw leggen"); niet opnieuw satellietgelegd deze ronde, conform de bindende aanpassing |
| `co-guemassa-fabriek` | fabriek / losplek (staart) | CTT Guemassa hydrometallurgisch complex (Managem), vijf eenheden: Co-kathodes, CuSO₄, NiSO₄, ZnO | 31.3825, -8.0635 | eigen satellietblik (zie hieronder) + toets-kandidaat "Usine Guemassa" (Photon-bushalte 31.3703, -8.0552) als uitgangspunt [5][10] | **bron-gelegd** (z16/z17, live, zie sat_check-bestanden §8): grote rechthoekige procesgebouwen met opslagtanks (tankfarm), aangrenzende rood-roze en okerkleurige afvalbekkens/tailings-vijvers, brede toegangsweg vanaf het terrein — het beeld verschoven van het Photon-kandidaatpunt (bushalte, geen gebouw) 1,5 km naar noordwest naar de zichtbare industriële bebouwing |

## 4 · Via-punten (b1 — corridorkeuzes op de N9/N8)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ouarzazate — aansluiting mijnweg op de N9 | 30.9170, -6.9170 | hier komt de weg vanaf Bou Azzer op de doorgaande N9 Ouarzazate–Marrakech; enige zinnige noord-corridor vanaf de mijn [6] |
| b1 | 2 | Tizi n'Tichka-pas (2.260 m, Hoge Atlas) | 31.2858, -7.3808 | de N9 heeft hier geen alternatieve route door het gebergte — de pas identificeert de corridor zelf, geen omweg mogelijk [7] |
| b1 | 3 | Aït Ourir — N9 tussen pas en Marrakech | 31.5644, -7.6628 | laatste grotere plaats vóór Marrakech waar de N9 nog een enkelvoudige doorgaande weg is [6] |
| b1 | 4 | Marrakech-zuid, N8/Avenue Guemassa-aftakking | 31.5791, -8.0583 | hier verlaat de corridor de N9-richting Marrakech-centrum en volgt de N8 zuidwaarts, in Marrakech letterlijk "Avenue Guemassa" genaamd — de straatnaam bevestigt de bestemming van de weg [10] |

## 5 · Verwerkingsknopen
Geen tussenknoop: dit is een kop-tot-fabriek-transport (erts/concentraat rijdt rechtstreeks van mijn naar hydrometallurgisch complex, geen overslag onderweg). CTT Guemassa zélf is de enige verwerkingsknoop en tevens het stoppunt (§6).

## 6 · Stoppunt
De brief stopt bij het CTT Guemassa-complex: vijf productie-eenheden zetten het concentraat om in kobaltkathodes, kopersulfaat, nikkelsulfaat en zinkoxide, maar geen bron noemt per product een specifieke afnemer of vervolgbestemming — fase D (met naam benoemde vervolgfabriek) en fase E (eindproduct-afzet) vervallen. Dit is een bewuste, geen omissie: v1's vervolgketen `co-bouazzer` → Umicore Olen (België) bestaat wél in de data (`co-ref-umicore`, zie `data/cobalt.js`), maar is niet per zending gedocumenteerd en wordt hier — net als bij `kobalt-ambatovy-toamasina` — niet doorgetekend.

## 7 · Open punten
- **Geen gepubliceerde wegkilometers voor N9/R203 Ouarzazate–Marrakech gevonden** (conform het ketenontwerp en de haalbaarheidstoets) — geen blocker voor het bakken, wel voor de ±15%-toets: alleen het gemeten getal, geen referentiewaarde.
- **Guemassa-anker verschoven t.o.v. het toets-kandidaatpunt**: Photon's "Usine Guemassa" (bushalte, 31.3703, -8.0552) bleek geen gebouw maar een bushalte-node; het werkelijke procescomplex ligt satelliet-zichtbaar 1,5 km noordwestelijker op 31.3825, -8.0635. Niet onafhankelijk bevestigd met een naam-tag of adres — geen tweede bron voor déze exacte coördinaat, alleen het satellietbeeld zelf.
- **Afstand Guemassa–Marrakech: 37 km, niet ~60 km.** Het ketenontwerp noemde "~60 km van Marrakech"; Glencore's eigen persbericht over de Managem-samenwerking noemt 37 km [2], en de satellietcoördinaat ligt ±28 km hemelsbreed / ~37 km wegafstand zuid van het centrum van Marrakech — consistent met elkaar, niet met de 60 km uit het ontwerp.
- **Jaarvolume niet naar peiljaar bevestigd** — alleen het indicatieve v1-cijfer (~1 kt Co/jaar, `data/cobalt.js`); Managem's jaarverslag 2024/2025 is niet geraadpleegd in dit webbudget.
- **Fase D/E vervallen bewust** (zie §6) — v1's Umicore-vervolgketen bestaat, wordt hier niet getekend.
- Corridorklasse/eindtoegang van de N9 niet vooraf getoetst — de toets verwacht geen bijzonderheden ("bekende, goed gekarteerde hoofdweg"), te bevestigen bij het bakken.

## 8 · Bronnen
[1] Managem, "Bou-Azzer mine" — CTT-Bou Azzer, 120 km zuid van Ouarzazate, levert concentraat aan de hydrometallurgische fabrieken van Guemassa. https://www.managemgroup.com/en/bou-azzer-mine
[2] Glencore, persbericht — "Glencore and Managem set up partnership for Moroccan production of cobalt from recycled battery materials": CTT Hydrometallurgical Refinery te Guemssa, 37 km van Marrakech; vijfjarige tolling-overeenkomst ~1.200 t gerecycled kobalt/jaar (aparte stroom, niet in deze keten getekend). https://www.glencore.com/media-and-insights/news/glencore-and-managem-set-up-partnership
[3] Institute of Developing Economies (IDE-JETRO), Managem-bedrijfsprofiel — bevestigt "120 kilometres south of the town of Ouarzazate" voor Bou Azzer. https://www.ide.go.jp/English/Data/Africa_file/Company/morocco05.html
[4] Managem, "Cobalt" — CTT Guemassa: vijf operationele eenheden, kobaltkathodes/kopersulfaat/nikkelsulfaat/zinkoxide. https://www.managemgroup.com/en/taxonomy/term/54
[5] Photon (OSM-geocoder) — "Usine Guemassa" bus_stop, 31.370309, -8.0552097; gebruikt als uitgangspunt voor de satellietblik conform de bindende aanpassing.
[6] Wikipedia (EN) — coördinaten Ouarzazate (30.917, -6.917) en Aït Ourir (31.56444, -7.66278), via de MediaWiki-infobox. https://en.wikipedia.org/wiki/Ouarzazate · https://en.wikipedia.org/wiki/A%C3%AFt_Ourir
[7] Wikipedia (EN) — Tizi n'Tichka-pas, 31.28583, -7.38083, onderdeel van "National Route 9", aangelegd 1936, verbindt Marrakech met Ouarzazate door de Hoge Atlas. https://en.wikipedia.org/wiki/Tizi_n%27Tichka
[8] Ketenontwerp (JSON, M31 golf 2) — schatting ~280 km wegafstand Bou Azzer–Guemassa (geen gepubliceerde bron); v1-checklist `data/cobalt.js` (share 1, tier 3, "de enige mijn ter wereld waar kobalt het hoofdproduct is").
[9] Haalbaarheidstoets (JSON, bindend, M31 golf 2) — bevestigt Bou Azzer als exact OSM-object (hergebruiken), wijst het Photon-kandidaatpunt "Usine Guemassa" aan als uitgangspunt voor de brief-fase, en signaleert het ontbreken van gepubliceerde wegkm.
[10] OpenStreetMap (ODbL) via Nominatim/Photon — "Mine Bou Azzer" (`landuse=quarry`, way 224769039, 30.5183831/-6.9133840); "Avenue Guemassa" (meerdere ways in Marrakech, o.a. way 25891424 bij 31.5791/-8.0583, wijk M'hamid); "Guemassa" bus_stop-nodes. https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15–z17, live) — `v2/build-cache/satcheck/sat-kobalt-bouazzer-guemassa-guemassa.png`, `sat-kobalt-bouazzer-guemassa-guemassa-plant.png`, `sat-kobalt-bouazzer-guemassa-plant-close.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `kobalt-bouazzer-guemassa`** → `v2/data/stroomroute-kobalt-bouazzer-guemassa.json` — 1 been,
**311,3 km**, 7.871 punten, 2 markers, 152,8 KB. Recept: `bak_stromen.sh` (functie
`bak_kobalt_bouazzer_guemassa`), profiel `kobalt-bouazzer-guemassa-bouazzer-guemassa` in
`maak_stroombeen_weg.py` (extract `marokko`, `--bron geofabrik`).

**b1 (truck, `maak_stroombeen_weg.py`):** anker Bou Azzer-mijn (-6,9134/30,5184) → via1 Ouarzazate
(-6,9170/30,9170) → via2 Tizi n'Tichka-pas (-7,3808/31,2858) → via3 Aït Ourir (-7,6628/31,5644) → via4
Marrakech-zuid/Avenue Guemassa (-8,0583/31,5791) → anker Guemassa-complex (-8,0635/31,3825), venster
40 km. Per-segment km (kop→via/via→via, uit de scanconsole): Bou Azzer→Ouarzazate 121,1 · Ouarzazate→
Tichka-pas 88,8 · Tichka-pas→Aït Ourir 70,0 · Aït Ourir→Marrakech-zuid 54,2 · Marrakech-zuid→Guemassa
26,9 km = **310,2 km** vóór 161 keerlussen-snoei (361,2 → 310,2 km, dubbel gereden stukken bij o.a. de
haarspeldbochten op de pas). Getekende lijn ná integratie in `hecht_marnet route`: **311,3 km / 7.871
punten**. Alle via-snaps ≤ 0,47 km (ruim binnen de norm); de ankerverbinding "weg → kade" bij Guemassa
snapt op **0,63 km** (> 0,5 km, zie hieronder).

**⚠️ Geen ±15%-lengtetoets mogelijk** (brief §2/§7/§8[8]): geen gepubliceerde wegkilometers voor N9/R203
Ouarzazate–Marrakech gevonden. Het gemeten getal (311,3 km) staat als enige referentie op de kaart; de
ontwerpschatting was ~280 km (311,3 km ligt daar 11% boven, maar dat is geen bindende toets — er is geen
bron om tegen te toetsen, conform de opdracht).

**⚠️ De noord-zuid-omkering bij Marrakech gaf géén rare knik.** Via4 (Marrakech-zuid/Avenue Guemassa,
lat 31,5791) ligt noordelijker dan de fabriek (lat 31,3825); elk been-segment wordt apart geroutet
(kop→via, via→via, ..., via→staart), dus de Dijkstra kon geen lus maken — het laatste segment (26,9 km)
loopt gewoon rechtstreeks zuidwaarts van de N8-aftakking naar het complex. Geen extra via-punt nodig
geweest.

**⚠️ De weg door Marrakech-centrum (Avenue Guemassa) is inhoudelijk correct maar visueel dicht
bebouwd** — de N8 loopt hier als binnenstedelijke straat i.p.v. een ringweg/rocade. Niet gecorrigeerd
(gemeld conform de opdracht): dit is de daadwerkelijke route naar het industrieterrein, geen
scanfout.

**Toets naden:** 1 been, geen naden tussen benen (naad = 0,00 km voor het enige been in de keten).

**`toets_knikken.py`:** 24 knikken ≥60°, **0 omkeringen ≥150°, waarvan 0 TERUGLOOP.** Alle 24 knikken zijn
scherpe bochten met kleine straal (4–45 m) op twee plekken: de haarspeldbochten van de Tizi n'Tichka-pas
(Hoge Atlas, o.a. 31,31850/-7,37851 en omgeving) en enkele krappe bochten rond Aït Ourir en bij de
Guemassa-aftakking (31,63–31,64/-7,99–-8,01). Dit zijn **echte bergwegbochten**, geen router-artefacten
(spike, geen omkering/terugloop) — precies het patroon dat de handleiding op een bergpas verwacht. Geen
enkele hoort gerepareerd te worden.

**`toets_rechte_benen.py --min-km 5`:** geen treffer voor deze stroom (het been is een bochtige bergweg,
geen rechte lijn — dus terecht doorgetrokken en niet gestippeld).

**Contract:** `json.load` slaagt · `versie == 2` · `punt_formaat == "lonlat"` · modaliteit `truck` ∈
{zee, binnenvaart, truck, spoor, leiding} · been heeft 7.871 ≥ 2 punten · bestand 152,8 KB (ruim onder
de ~300 KB-norm). Beide markers liggen op **0,00 km** van de lijn (het zijn de routeerpunten zelf).

**Gereedschapslessen:**
- Geen haven-aanloop nodig (geen zeebeen in deze keten).
- De ankerverbinding "weg → kade" bij Guemassa (0,63 km, licht boven de 0,5 km-norm) komt doordat het
  satellietgelegde fabrieksanker net naast de dichtstbijzijnde OSM-wegvertex ligt — geen via-punt
  bijgeschoven, blijft als bevinding staan (§7 van de brief noemt het Guemassa-anker al als niet
  onafhankelijk tweede-bron-bevestigd).
- Eén tool, één been: dit is de lichtste bake van de golf (geen zee, geen spoor, geen verwerkingsknoop
  onderweg) — bevestigt dat de lichte werkwijze ook voor een puur landbeen zonder overslag volstaat.
