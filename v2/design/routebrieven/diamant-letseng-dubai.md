# Routebrief (licht) · diamant — Letšeng (Lesotho) → Johannesburg (Zuid-Afrika) → Dubai (VAE)

**stroom-id:** `diamant-letseng-dubai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** ruwe diamant van de Letšeng-mijn (Gem Diamonds + regering Lesotho, 3.100 m — 's werelds
hoogste diamantmijn) gaat per **truck** over de eigen $3,7 mln-bergweg (haarspeldbochten, deels grind) naar de
vrachtterminal van O.R. Tambo (Johannesburg), vliegt als vrachtvlucht (**grootcirkel**) naar Dubai International
Airport en gaat per **truck** naar de DMCC/Almas Tower in Dubai voor handel.
**Welke as van het verhaal:** *het hoogste-$/karaat-been* — Letšeng draait op een klein aantal uitzonderlijke,
zeer grote stenen (type IIa); het jaarvolume in Mct is nauwelijks representatief voor de waarde, en de
gemiddelde $/karaat is de hoogste van alle diamantmijnen ter wereld [1][12].

## 1 · Ketenkaart
```
Letšeng-mijn `dia-letseng-mijn` ──(b1 truck · bergweg Mokhotlong → Johannesburg, $3,7 mln aangelegd ·
   ~450 km, ontwerp/niet apart geverifieerd)──► O.R. Tambo vrachtapron `dia-jnb-cargo`
   ──(b2 lucht · grootcirkel JNB → DXB · 6.432 km, gemeten)──► DXB vrachtterminal `dia-dxb-cargo`
   ──(b3 truck · Al Garhoud → Sheikh Zayed Road → JLT · ~31 km hemelsbreed)──► DMCC / Almas Tower
   `dia-dmcc-almas` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Letšeng-mijn → O.R. Tambo vrachtapron (JNB) | eigen bergweg Mokhotlong → Oxbow/Tlaeeng-Moteng-pas → Butha-Buthe → Caledonspoort → Fouriesburg → Bethlehem → Villiers → JNB | ~450 [ontwerp; GIA noemt alleen Maseru↔mijn 214 km, niet apart geverifieerd op JNB-afstand, zie §7] | maak_stroombeen_weg.py | nee |
| b2 | B | lucht | O.R. Tambo vrachtapron (JNB) → DXB vrachtterminal | vlucht JNB → DXB, grootcirkel | 6.432,4 (gemeten, grootcirkel tussen de twee vrachtterminal-ankers) | maak_luchtbeen.py | nee — doorgetrokken |
| b3 | C | truck | DXB vrachtterminal → DMCC/Almas Tower | Al Garhoud → Sheikh Zayed Road (E11) → Jumeirah Lake Towers | ~31 hemelsbreed (berekend uit ankers); wegafstand naar verwachting 35–40 km | maak_stroombeen_weg.py | nee |

Fase C is toegevoegd op de haalbaarheidstoets: "Ontbrekend laatste been DXB → DMCC" — de keten mag niet
eindigen op de luchthaven zelf.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-letseng-mijn` | mijn / laadplek (vertrekpunt truck) | Letšeng-mijn (Gem Diamonds + regering Lesotho), Mokhotlong, 3.100 m | -29.00028, 28.86194 | [1][11] | bron-gelegd (z15 gezien: put met twee open pits, tailingsdam (blauw/groen bekken) en een gebouwencluster met toegangswegen precies tussen de pits — het mijn-/verwerkingscomplex) |
| `dia-jnb-cargo` | vrachtterminal / overslag truck→lucht | O.R. Tambo vrachtapron (apron Golf/Whiskey), Kempton Park, Johannesburg | -26.14300, 28.22700 | [6][11] | bron-gelegd (z16 gezien: cluster vrachtloodsen met meerdere wide-body vrachttoestellen op het platform ernaast, direct ten zuiden van de passagiersterminal — de omschreven cargo-aprons) |
| `dia-dxb-cargo` | vrachtterminal / overslag lucht→truck | Dubai Cargo Village / DXB Cargo Gateway, Al Garhoud, Dubai | 25.26440, 55.36610 | [8][11] | bron-gelegd (z16 gezien: rij van ~15 langwerpige vrachtloodsen direct grenzend aan het platform, vrachttoestellen nose-in ernaast op de apron ten zuiden — de Dubai Cargo Village-loodsenrij) |
| `dia-dmcc-almas` | handelshub (eindpunt) | DMCC / Almas Tower, Jumeirah Lake Towers, Dubai | 25.06890, 55.14120 | [9][10] | bron-gelegd (z15 gezien: de kenmerkende 68-verdiepingen-toren aan het meer in JLT, exact op het Wikipedia-coördinaat van Almas Tower — huisvest de Dubai Diamond Exchange en duizenden diamanthandelaren) |

## 4 · Via-punten (alleen b1 — de enige landcorridor met een keuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Oxbow (Tlaeeng-/Moteng-pas) | -28.7712, 28.6396 | enige doorgaande bergpas-corridor (A1) van de mijnregio naar het noordwesten, geen alternatieve route [ontwerp; niet satelliet-gelegd] |
| b1 | 2 | Butha-Buthe | -28.7833, 28.2333 | laatste Lesothaanse plaats vóór de grensovergang, corridor buigt hier naar de grens |
| b1 | 3 | Caledonspoort-grensovergang | -28.6949, 28.2338 | de grensovergang Lesotho → Zuid-Afrika op deze corridor (OSM "Caledon's Poort Bridge") |
| b1 | 4 | Fouriesburg (Zuid-Afrika) | -28.6228, 28.2109 | eerste Zuid-Afrikaanse plaats na de grens, corridor buigt noordoostwaarts |
| b1 | 5 | Bethlehem (Zuid-Afrika) | -28.2240, 28.3110 | knooppunt richting de N5/N3, enige zinnige doorgaande route naar Johannesburg |
| b1 | 6 | Villiers (Zuid-Afrika) | -27.0333, 28.6000 | op de N3 tussen Free State en Gauteng, laatste corridorkeuze vóór Johannesburg |

Deze zes punten zijn indicatief (bergpas-/grensroute zonder zinnig alternatief), niet zelf satelliet-gelegd —
alleen de vier ankers in §3 zijn dat.

## 5 · Verwerkingsknopen
*(geen — deze keten kent geen smelter/slijperij. DMCC/Almas Tower is een handels-/certificeringshub, geen
fysieke bewerking; slijpen gebeurt elders (overwegend Surat, buiten deze keten).)*

## 6 · Stoppunt
De brief stopt bij DMCC/Almas Tower in Dubai: dat is het opgegeven eindpunt van de keten (het ketenontwerp
noemt géén vervolgbestemming), en de haalbaarheidstoets voegde alleen het ontbrekende laatste been
(DXB → DMCC) toe, geen fase D — die vervalt.

## 7 · Open punten
- **De 450 km-bergweg-claim (Letšeng → Johannesburg) is niet onafhankelijk geverifieerd** — de
  haalbaarheidstoets noemt dit zelf al expliciet ("bekend, veelgeciteerd feit, niet apart geverifieerd binnen
  budget"). GIA/G&G bevestigt wel de $3,7 mln-bergweg en de afstand Letšeng↔Maseru (214 km, laatste 30 km
  grind met haarspeldbochten) [4], maar niet de exacte km naar Johannesburg specifiek.
- **Gem Diamonds' eigen hoofdverkoopkanaal is Antwerpen, niet Dubai** — gemdiamonds.com noemt Antwerpse
  tenders (Lange Herentalsestraat) als primair afzetkanaal, met klanten in "Belgium, India, Hong Kong,
  Israel, New York and Dubai" [3]. De keuze voor Dubai in dit ontwerp is bewust gemaakt voor
  luchthaven-spreiding binnen deze golf (chain 1/2/5 convergeren al op Antwerpen) op basis van de bredere
  Lesotho-exportbevinding "ships nearly all its high-quality diamonds ... to hubs such as Antwerp and Dubai"
  — niet een Letšeng-specifieke, per-lading gebronde Dubai-route. Antwerpen blijft een gebronde alternatieve
  bestemming.
- **Geen bron voor een tussenlanding op b2** — JNB–DXB wordt op meerdere maatschappijen dagelijks direct
  gevlogen; één directe vlucht aangenomen zoals de bakhandleiding voorschrijft bij het ontbreken van een
  hub-bron.
- **Letseng Airport (FXLT), de mijnstrip zelf, bestaat** (62.53 km hemelsbreed van de mijn, ICAO FXLT) [2] —
  niet gebruikt als vertrekpunt omdat het ketenontwerp expliciet de truckroute naar Johannesburg beschrijft
  ("het hoogste-$/karaat-been, over de eigen bergweg").
- **DXB-vrachtloods niet aan Letšeng-specifieke lading gekoppeld** — het anker `dia-dxb-cargo` staat op een
  algemene rij vrachtloodsen van Dubai Cargo Village (Al Garhoud); welke loods/operator specifiek
  Lesotho-ruw afhandelt is niet gebrond.
- **b3-via: geen corridorkeuze gevonden** — Al Garhoud naar JLT loopt vrijwel geheel over de Sheikh Zayed
  Road (E11), enige zinnige doorgaande corridor binnen Dubai; geen via-punten toegevoegd (been < 40 km,
  regel staat 0–2 via-punten toe bij een stadsbeen).
- **Risico uit het ketenontwerp:** Letšeng's omzet hangt sterk van een klein aantal uitzonderlijke
  grote-stenenvondsten af — het Mct-jaarvolume hieronder zegt weinig over de waarde van deze as.

## 8 · Bronnen
[1] Wikipedia, "Letseng diamond mine" — eigendom Gem Diamonds Ltd. + regering Lesotho, elevatie 3.100 m,
's werelds hoogste diamantmijn, extreem lage graad maar hoogste $/karaat (>$1.894/ct in 2007 tegen wereldgem.
~$81/ct). Coördinaat 29.00028S/28.86194E. https://en.wikipedia.org/wiki/Letseng_diamond_mine
[2] Wikipedia, "Letseng Airport" — mijnvliegveld FXLT, 62.5344S/... (coördinaat: -29.00972, 28.85694),
zeer hoge elevatie (10.084,8 ft), bedient de Letšeng-mijn. https://en.wikipedia.org/wiki/Letseng_Airport
[3] Gem Diamonds, Operations — Letšeng in de Maluti-bergen; analyse bij Baobab Technologies in Antwerpen;
tenders in Antwerpen (juni/sep/dec 2026); klanten in België, India, Hongkong, Israël, New York en Dubai.
https://www.gemdiamonds.com/operations.php
[4] GIA, Gems & Gemology, Fall 2015, "Letšeng's Unique Diamond Proposition" — de mijn ligt ~214 km NO van
Maseru; een weg van 3 miljoen rand ($3,7 mln destijds) werd door de bergen aangelegd, die de mijn verbindt met
zowel Johannesburg als Maseru; route grotendeels verhard, laatste 30 km grind met haarspeldbochten.
https://www.gia.edu/gems-gemology/fall-2015-letseng-unique-diamond-proposition
[5] Haalbaarheidstoets (intern, orkestrator) — bevestigt eigendom Gem Diamonds + regering Lesotho en
3.100 m-hoogte via Wikipedia "Letseng diamond mine" (curl-webcheck), voegt fase C toe (DXB → DMCC).
[6] Wikipedia, "O. R. Tambo International Airport" — cargo-vliegtuigen parkeren op aprons Golf en Whiskey
(ook Delta/Foxtrot om jetbridges vrij te maken); cargo-maatschappijen incl. FedEx, Lufthansa Cargo, Emirates
SkyCargo; nieuw cargoterminal aangekondigd in het 2024-investeringsplan. https://en.wikipedia.org/wiki/O._R._Tambo_International_Airport
[7] Menzies Aviation / Swissport, netwerkpagina's JNB — bevestigen cargo-afhandeling op O.R. Tambo (Menzies
namens SAA Cargo; Swissport met vijf vrachtloodsen), geen exact adres. https://menziesaviation.com/our-network/johannesburg-jnb/ ·
https://www.swissport.com/en/network/africa/south-africa/jnb
[8] Wikipedia, "Dubai International Airport Cargo Gateway" (voorheen Dubai Cargo Village) — vrachtfaciliteit
naast Dubai International Airport in Al Garhoud, eigendom Dubai Airports Company; hoofdmagazijnen in een
bonded area, dnata als afhandelaar, ~2,7 mln ton/jaar capaciteit na de Mega Cargo Terminal (2008).
https://en.wikipedia.org/wiki/Dubai_International_Airport_Cargo_Gateway
[9] Wikipedia, "Dubai Multi Commodities Centre" — DMCC, vrijhandelszone in Jumeirah Lake Towers; Dubai
Diamond Exchange (2004) als facilitator voor diamant-/edelsteenhandel; Almas Tower = hoofdkwartier met
diamanthandelaren en -kluizen. https://en.wikipedia.org/wiki/Dubai_Multi_Commodities_Centre
[10] Wikipedia, "Almas Tower" — coördinaat 25.0689N/55.1412E, DMCC-hoofdkwartier, Jumeirah Lake Towers.
https://en.wikipedia.org/wiki/Almas_Tower
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16, live) —
`v2/build-cache/satcheck/sat-diamant-letseng-dubai-letseng-mijn.png`,
`sat-diamant-letseng-dubai-jnb-cargo-cand3.png`, `sat-diamant-letseng-dubai-dxb-cargo-cand5.png`,
`sat-diamant-letseng-dubai-dmcc-almas.png`.
[12] `v2/design/diamant.md` §3a — dia-letseng: Lesotho, ~1% wereldvolume, ~1 Mct/j, Gem Diamonds, "hoogste
gemiddelde $/karaat ter wereld; grote uitzonderlijke stenen" (intern ontwerpdocument).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `diamant-letseng-dubai`** → `v2/data/stroomroute-diamant-letseng-dubai.json` — 3 benen (truck · lucht ·
truck, fase A → B → C → stoppunt), **6.976,4 km**, 7.298 punten, 4 markers, 148,7 KB. Recept: `bak_stromen.sh`
(functie `bak_diamant_letseng_dubai`); twee nieuwe wegprofielen `diamant-letseng-dubai-letseng-jnb` en
`diamant-letseng-dubai-dxb-dmcc` in `maak_stroombeen_weg.py`.

**b1 (truck, nieuw profiel `diamant-letseng-dubai-letseng-jnb`, extracts `lesotho`+`zuid-afrika`, vensterKm 75,
`corridorKlassen: tertiary/unclassified`):** `maak_stroombeen_weg.py --profiel diamant-letseng-dubai-letseng-jnb
--bron geofabrik` — **523,2 km** getekend (523,1 km lengtetoetswaarde) over de zes via-punten uit de brief
(Oxbow/Tlaeeng-Moteng-pas → Butha-Buthe → Caledonspoort-grens → Fouriesburg → Bethlehem → Villiers), 32 keerlussen
gesnoeid (540,3 → 523,1 km). **Eerste poging faalde** ("geen wegpad tussen punt 0 en 1", Letšeng-mijn → Oxbow,
33 km): de eigen bergwegtoegang bij de mijn draagt in OSM een kleine klasse (`track`) die de scanner zonder
uitbreiding nooit doorlaat. Opgelost met `eindKlassen` incl. `track` + `eindToegangPrivaat: True` binnen de
12 km-eindzone — daarna routeert de hele corridor door, geen stippel nodig (ankerverbindingen 0,04/0,09 km, ruim
binnen 0,5 km).

**⚠️ Lengtetoets BUITEN de ±15%-norm:** 523,1 km tegen de toetswaarde 450 km (ontwerp, brief §2/§7) = **+16,2%**.
Bevinding, geen fout — niet dichtgetrokken: het ontwerpcijfer was zelf al "niet apart geverifieerd" (GIA/G&G
bevestigt alleen de $3,7 mln-bergweg en Letšeng↔Maseru 214 km, niet de km naar Johannesburg specifiek, brief §7);
de zes via-punten zijn indicatief, niet satelliet-gelegd (brief §4), en de gemeten route volgt een reële
bergpas-/grenscorridor zonder alternatief. First mile 3,04 km + last mile 1,54 km over kleine wegklassen, beide
binnen de 12 km-marge.

**b2 (lucht, grootcirkel, JNB → DXB):** `maak_luchtbeen.py --van "O.R. Tambo vrachtapron (JNB)|-26.14300,28.22700"
--naar "DXB vrachtterminal|25.26440,55.36610"` — **6.415,6 km** gemeten grootcirkel (brief noemde 6.432,4 km —
verschil 16,8 km/0,26%, binnen norm; geen aparte km-toets voor een luchtbeen). 258 punten. Doorgetrokken, geen
stippel: een vlucht tussen twee gelegde vrachtterminals is geen gat. Geen tussenlanding gebrond (geen bron noemt
een hub tussen Johannesburg en Dubai) → één directe vlucht, conform §7 van de brief en de bakhandleiding.

**b3 (truck, nieuw profiel `diamant-letseng-dubai-dxb-dmcc`, extract `gcc-staten`, vensterKm 30):**
`maak_stroombeen_weg.py --profiel diamant-letseng-dubai-dxb-dmcc --bron geofabrik` — **37,6 km** geroute (37,6 km
getekend) rechtstreeks tussen de twee ankers, geen via-punten (brief §4/§7: Sheikh Zayed Road/E11 is de enige
zinnige doorgaande corridor binnen Dubai). 20 kleine keerlussen gesnoeid. First mile 1,07 km + last mile 0,32 km
over kleine wegklassen, beide binnen de 12 km-marge. Ankerverbindingen 0,01/0,04 km — geen stippel nodig.

**⚠️ `dia-dxb-cargo` NIET hergebruikt van de zusterbrieven.** Deze brief legde zijn eigen `dia-dxb-cargo`-anker
(25,2644/55,3661, sat_check.py z16, "rij van ~15 langwerpige vrachtloodsen", brief §3) onafhankelijk vast, vóórdat
bleek dat de zusterbrieven diamant-marange-dubai en diamant-mbujimayi-dubai al een `dia-dxb-cargo`-anker gebakken
hadden op 55,3406/25,2575 — een andere kandidaat-loods binnen hetzelfde Dubai Cargo Village-vrachtcomplex, ~2,7 km
verderop. Bewust NIET literal hergebruikt (de twee coördinaten wijken te veel af om zonder nadere toetsing als
"hetzelfde punt" te behandelen): deze bake draait een eigen wegscan met het eigen satelliet-gelegde anker. Gevolg:
er staan nu twee onafhankelijke DXB↔DMCC-truckbenen in de graaf-cache (`diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson`
en `diamant-letseng-dubai-weg-dxb-dmcc.geojson`) voor twee net-verschillende punten in hetzelfde vrachtcomplex —
gemeld voor een latere redactieronde, niet zelf gecorrigeerd (deze agent raakt geen andermans profielen/bestanden).
**Lengtetoets tegen de hemelsbreed-vervangwaarde (31 km) toont +21,3%**, maar dat is geen bevinding: de brief
verwachtte zelf al "wegafstand naar verwachting 35-40 km" (§2), en 37,6 km valt daar middenin.

**Geen zeebeen** (truck + lucht + truck) → geen MARNET, geen haven-aanloop. Fase D/E vervallen (brief §6,
stoppunt DMCC/Almas Tower — handels-/certificeringshub, geen fysieke bewerking; slijpen gebeurt elders, buiten
deze keten).

**Toetsen:** `toets_knikken.py` — b1 40 knikken ≥60° (spikes op kruispunten/grenspassage, straal 2–234 m) en b3
11 knikken ≥60° (spikes op stadskruispunten Al Garhoud/JLT, straal 3–21 m), lucht-been 0 knikken (per constructie
recht); **0 omkeringen ≥150°, 0 terugloop op alle drie de benen** — geen actie nodig. `toets_rechte_benen.py
--min-km 5` — geen melding voor `diamant-letseng-dubai` (lucht-been per constructie overgeslagen; beide truckbenen
zijn geen rechte lijnen). `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `truck`/`lucht`/`truck`
∈ toegestane set, elk been ≥ 2 punten (6.539/258/501), bestandsgrootte 148,7 KB (ruim onder ~300 KB). Naden tussen
de drie benen: **0,000 km** op beide overgangen (b1→b2 op de JNB-vrachtapron, b2→b3 op de DXB-vrachtterminal).
Markers: alle vier op 0,0-0,1 m van hun been (elk anker is tegelijk het routeerpunt/been-uiteinde).

**Toelichting stippels/haven-aanlopen/vluchten:** één vlucht, doorgetrokken (geen stippel, zie b2 hierboven). Geen
zeebeen in deze keten → geen MARNET, geen haven-aanloop. Geen stippel op b1 of b3: beide truckbenen routeren
volledig door na het toevoegen van `eindKlassen`/`eindToegangPrivaat` op b1 (zie hierboven); alle vier
ankerverbindingen zijn triviaal klein (0,01-0,09 km).

**Gereedschapslessen:** `maak_luchtbeen.py` werkte zonder aanpassing. Bij `maak_stroombeen_weg.py` faalde de
eerste poging op b1 volledig ("geen wegpad tussen punt 0 en 1") omdat de mijntoegangsweg in OSM als `track`
gekarteerd staat — dit is dezelfde klasse als eerdere mijn-/raffinaderijtoegangen in dit project (Bathopele,
Rustenburg e.d.): `eindKlassen` moet `track` expliciet bevatten (niet alleen `corridorKlassen`, die volgens de
handleiding `track` sowieso nooit doorlaat) vóórdat een bergpascorridor vanaf een afgelegen mijnsite routeert.
Voor `dia-dxb-cargo` bleek pas ná de eigen satellietlegging dat twee sibling-brieven in dezelfde golf een
net-verschillend punt binnen hetzelfde vrachtcomplex hadden vastgelegd — een les voor de volgende golf: bij een
gedeeld vrachtcomplex (luchthaven, haven) is het de moeite waard om vóór de eigen `sat_check.py`-ronde kort te
zoeken of een zusterbrief in dezelfde golf al een anker op dat complex heeft gelegd.
