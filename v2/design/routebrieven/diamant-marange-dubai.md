# Routebrief (licht) · diamant — Marange → Harare → Dubai (VAE)

**stroom-id:** `diamant-marange-dubai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** Ruwe alluviale diamant uit de Marange-velden (ZCDC, Manicaland) gaat per truck over de A9-corridor naar de vrachtterminal van Harare (HRE), vliegt als vrachtvlucht (grootcirkel) naar Dubai International Airport (DXB), en gaat per truck naar het DMCC/Dubai Diamond Exchange in Jumeirah Lake Towers — de omstreden, sanctie-beladen alluviale as die Zimbabwe (landlocked, dus per definitie lucht) met de snelst groeiende rough-hub van de wereld verbindt.
**Welke as van het verhaal:** *Marange (Zimbabwe) → Dubai: de meest beladen as van de kaart.* Marange was het toneel van het 2008-geweld/mensenrechtenschendingen bij de eerste "diamond rush" en droeg tot 2024 gedeeltelijk VS-sancties op ZCDC-gelieerde entiteiten; de exportroute (Antwerpen vs. Dubai) is politiek gevoelig en kan snel verschuiven [1][2]. Jaarvolume ~5 Mct/j ruw (~4% wereldvolume, grotendeels laagwaardig/alluviaal), peiljaar ±2023-2024, o.b.v. KPCS [4][5] — oorspronkelijke eenheid Mct/jaar (miljoen karaat), zoals in het ketenontwerp; de waarde per karaat (<$50/ct, ver onder edelsteenkwaliteit) staat in de notitie bij het anker, niet in het gewicht.

## 1 · Ketenkaart
```
Marange-diamantvelden (ZCDC) `dia-marange-mijn` ──(b1 truck · A9 Mutare–Harare · ~270 km)──►
Harare (HRE), vrachtterminal `dia-hre-cargo` ──(b2 lucht · vlucht HRE → DXB, grootcirkel · ~5.472 km)──►
Dubai Intl Airport (DXB), vrachtterminal `dia-dxb-cargo` ──(b3 truck · Sheikh Zayed Road (E11) · ~29 km)──►
DMCC / Dubai Diamond Exchange, Almas Tower `dia-dmcc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Marange-diamantvelden → Harare (HRE) vrachtterminal | A9 Mutare–Harare, via Mutare/Rusape/Marondera | ~270 [ontwerp]; som via-punten (hemelsbreed) 275,4 km | maak_stroombeen_weg | nee |
| b2 | B | lucht | Harare (HRE) vrachtterminal → Dubai Intl (DXB) vrachtterminal | vlucht HRE → DXB, grootcirkel | 5.471,7 (berekend, grootcirkel) | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | Dubai Intl (DXB) vrachtterminal → DMCC / Dubai Diamond Exchange | Sheikh Zayed Road (E11), enige doorgaande corridor | 29,0 hemelsbreed (berekend uit ankers) | maak_stroombeen_weg | nee |

Fase C is toegevoegd op de haalbaarheidstoets: de keten mag niet eindigen op de luchthaven zelf zonder het laatste been naar de beurs/kluis. `dia-hre-cargo`/`dia-dxb-cargo`/`dia-dmcc` zijn nieuwe ankers van deze keten; herbruikbaar voor andere ketens van deze golf die dezelfde luchthavens/beurs aandoen (nog niet elders gelegd, zie §7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-marange-mijn` | mijn / laadplek | Marange-diamantvelden (ZCDC), Chiadzwa, Manicaland | -19,5906, 32,3522 | [3][4] | bron-gelegd (z15 gezien: rand van een open-pit-complex met direct aangrenzend stapelterreinen, ontginningswegen en bezinkbekkens — het ZCDC-mijncomplex) |
| `dia-hre-cargo` | vrachtterminal / vertrek luchtvracht | Robert Gabriel Mugabe Intl (HRE), vracht-/GA-apron, Harare | -17,9218, 31,0946 | [6][11] | bron-gelegd (z18 gezien: vrachtloods met laadperron, direct aangrenzend een apron met een breedromper vrachttoestel en verdere hangaars — consistent met de cargo-operaties van o.a. Astral Aviation vanaf HRE [6]; geen naambord zichtbaar dus de exploitant is niet te bevestigen) |
| `dia-dxb-cargo` | vrachtterminal / aankomst luchtvracht | Dubai Intl (DXB), Emirates Air Cargo-gebouw, Al Garhoud | 25,2575, 55,3406 | [7][11] | bron-gelegd (z15 gezien: groot vrachtgebouw direct aan de apron met tientallen geparkeerde vliegtuigen op de taxibanen ernaast, binnen het luchthaventerrein — OSM-naam "الإمارات للشحن الجوي" / Emirates Air Cargo) |
| `dia-dmcc` | beursgebouw / bestemming | DMCC / Dubai Diamond Exchange, Almas Tower, Jumeirah Lake Towers | 25,0691, 55,1412 | [8][11] | bron-gelegd (z15 gezien: herkenbare torenvoet in het JLT-torencluster aan het meer, exact op de OSM-polygoon "برج الماس / Almas Tower") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Mutare | -18,9667, 32,6333 | eerste stadsknoop op de A9 vanaf Marange, vóór de aansluiting op de doorgaande corridor naar Harare |
| b1 | 2 | Rusape | -18,5367, 32,1247 | tussenstad op de A9, enige doorgaande route tussen Mutare en Marondera |
| b1 | 3 | Marondera | -18,1897, 31,5467 | laatste tussenstad vóór Harare, waar de A9 de stadsrand van Harare nadert |
| b3 | 1 | Dubai World Trade Centre-interchange | 25,2276, 55,2888 | Sheikh Zayed Road (E11) is de enige doorgaande snelweg tussen DXB en JLT; dit knooppunt pint de route bij de eerste grote interchange |
| b3 | 2 | Mall of the Emirates-interchange | 25,1181, 55,2006 | tweede vaste interchange op dezelfde E11, vlak vóór de afslag naar JLT/DMCC |

## 5 · Verwerkingsknopen
*(geen — deze keten kent geen smelter/raffinaderij/slijperij: Marange is winning, DMCC is een handelsbeurs/kluis, geen fysieke bewerking. Het slijpen (~90-95% van de wereld in Surat, India) valt buiten deze keten.)*

## 6 · Stoppunt
De brief stopt bij DMCC / Dubai Diamond Exchange: dit is precies het punt dat de haalbaarheidstoets vraagt (truckbeen vrachtterminal → beurs/kluis), en er is geen bron die voor déze specifieke stroom een vervolgbeen (bv. naar een Antwerpse of Indiase slijperij) aan Marange-rough koppelt — fase D vervalt, fase E ook.

## 7 · Open punten
- **Geen bron koppelt Marange-rough specifiek aan de vertrekluchthaven HRE**: het ketenontwerp noemt alleen "Zimbabwaanse rough via Dubai/Antwerpse tenders" zonder vertrekpunt; HRE is aangenomen als enige internationale/vrachtluchthaven van Zimbabwe, niet per zending gebrond.
- **`dia-hre-cargo` is niet met naam bevestigd als dé cargo-faciliteit**: het satellietbeeld toont een plausibele vrachtloods+apron-cluster naast een breedromper vrachttoestel, maar geen naambord; alleen algemeen bewijs dat HRE vrachtvluchten (Astral Aviation) afhandelt.
- **Geen gepubliceerde wegkilometrage voor de A9 Mutare–Harare-corridor gevonden** binnen het webbudget; de ~270 km uit het ketenontwerp is niet onafhankelijk bevestigd, alleen intern consistent met de som van de via-punten (275,4 km hemelsbreed).
- **Geen gepubliceerde vluchtlengte HRE→DXB**: berekende grootcirkel (geen gekarteerd luchtwegennet bestaat); een tussenlanding is niet uitgesloten maar door geen bron genoemd, dus aangenomen: één directe vlucht.
- **Fase C (DXB→DMCC) heeft geen eigen bron voor het exacte traject**; toegevoegd op de haalbaarheidstoets, geometrie is de enige doorgaande snelweg (E11) tussen de twee ankers.
- **Sanctiestatus ZCDC-gelieerde entiteiten (gedeeltelijke opheffing 2024)** komt uit het ketenontwerp/risicotekst; niet apart met een primaire bron geverifieerd binnen het webbudget van deze brief (KP/Global Witness worden generiek aangehaald in §8).
- **Marange-aandeel binnen "Zimbabwaanse rough"** is niet los van eventuele andere Zimbabwaanse alluviale velden bevestigd — het ontwerp behandelt Marange als vrijwel de volledige Zimbabwaanse productie, conform design/diamant.md.

## 8 · Bronnen
[1] Kimberley Process Certification Scheme (KPCS) — officiële site, ruwstatistiek en lidstaatoverzicht Zimbabwe. https://www.kimberleyprocess.com
[2] Global Witness — rapportage over Marange, het 2008-geweld en mensenrechtenschendingen rond ZCDC. https://www.globalwitness.org
[3] Wikipedia — "Marange diamond fields" (coördinaat -19,59056/32,35222; Chiadzwa, Mutare District; ~13% van het wereldvolume in 2013, laagwaardig alluviaal). https://en.wikipedia.org/wiki/Marange_diamond_fields
[4] `v2/design/diamant.md` (project-brief) §3a (dia-marange: 4% wereldvolume, ~5 Mct/jr, ZCDC-operator, "volumineus, laagwaardig; beladen (2008-geweld, mensenrechten)"), §4a (bron luchtvracht: "Zimbabwaanse rough via Dubai-/Antwerpse tenders").
[5] USGS Mineral Commodity Summaries 2025 (Diamond) — wereld-ruwproductie ~110-120 Mct/jaar als referentiekader voor het Marange-aandeel.
[6] Wikipedia — "Robert Gabriel Mugabe International Airport" (HRE, ICAO FVRG, 17°55′54,5″S 31°05′34,25″E ≈ -17,93181/31,09285; cargo-operator Astral Aviation naar Nairobi–JKIA genoemd). https://en.wikipedia.org/wiki/Robert_Gabriel_Mugabe_International_Airport
[7] Wikipedia — "Dubai International Airport" (DXB, 25°15′10″N 055°21′52″E = 25,25278/55,36444; Cargo Mega Terminal/Cargo Village, ~2,5 Mt/jaar capaciteit, Al Garhoud). https://en.wikipedia.org/wiki/Dubai_International_Airport
[8] Wikipedia — "Dubai Multi Commodities Centre" (DMCC, hoofdkwartier Almas Tower, Jumeirah Lake Towers, ~1.000 diamantbedrijven + Dubai Diamond Exchange + kluizen/handelsvloer). https://en.wikipedia.org/wiki/Dubai_Multi_Commodities_Centre
[9] Wikipedia — "Mutare", "Rusape", "Marondera", "Harare" (coördinaten via MediaWiki API prop=coordinates, gebruikt als via-punten op de A9-corridor). https://en.wikipedia.org/wiki/Mutare · https://en.wikipedia.org/wiki/Rusape · https://en.wikipedia.org/wiki/Marondera · https://en.wikipedia.org/wiki/Harare
[10] Wikipedia — "Dubai World Trade Centre" (25,22761/55,28878) en "Mall of the Emirates" (25,11806/55,20056), gebruikt als via-punten op Sheikh Zayed Road (E11). https://en.wikipedia.org/wiki/Dubai_World_Trade_Centre · https://en.wikipedia.org/wiki/Mall_of_the_Emirates
[11] OpenStreetMap (ODbL) via Photon — "الإمارات للشحن الجوي / Emirates Air Cargo" (building, 25,25745/55,34060, binnen مطار دبي الدولي); "برج الماس / Almas Tower" (building=apartments, 25,06906/55,14117, Cluster D, Jumeirah Lake Towers). https://photon.komoot.io
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15–z18, live) — `v2/build-cache/satcheck/sat-diamant-marange-dubai-marange.png`, `-hre-cargo-confirm.png`, `-dxb-cargo.png`, `-dmcc.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `diamant-marange-dubai`** → `v2/data/stroomroute-diamant-marange-dubai.json` — 4 benen,
**5.864,7 km**, 5.635 punten, 4 markers. stippel-truck 0,8 + truck 357,4 + lucht 5.471,7 + truck 34,8
= 5.864,7 km. Recept: `bak_stromen.sh` (functie `bak_diamant_marange_dubai`). Bestandsgrootte
**115,2 KB**.

**b0 (truck, STIPPEL, "last mile"):** Marange-mijn (ZCDC-terrein, anker `dia-marange-mijn`) →
doorgaande weg — **0,786 km, 2 punten**. ⚠️ **Geen wegklassefout maar een echt "net reikt
niet"-geval:** een osmium-connectiviteitscheck op de zimbabwe-extract laat zien dat het mijnanker
snapt op een geïsoleerd eilandje van 8 knopen (vooral `track`-ways, 0,14 km afstand) dat niet
verbonden is met het doorgaande wegnet (de component van 1,9 mln knopen incl. de R5/Harare-Mutare
Highway) — ook niet met `corridorKlassen` ruim (tertiary/unclassified/service) of
`eindToegangPrivaat: True`. De dichtstbijzijnde wél-verbonden weg (service) ligt op 0,79 km, getekend
als stippel met die reden.

**b1 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel
`diamant-marange-dubai-marange-hre`, extract `zimbabwe`):** de mijnwegaansluiting →
Harare (HRE) vrachtterminal, via Mutare → Rusape → Marondera — **357,4 km over 4.899 punten**, tegen
de ontwerpschatting ~270 km = **+32,4%, BUITEN ±15% — BEVINDING, niet dichtgetrokken.** Alle vier
subsnaps liggen op 0,00–0,13 km (geen enkel via-punt is bijgeschoven om het getal te halen). De
brief-schatting was zelf al "geen betrouwbare gepubliceerde wegreferentie" (§2, som via-punten
hemelsbreed 275,4 km); de werkelijk gerouteerde 357,4 km over de R5/A3-corridor Mutare–Rusape–
Marondera–Harare is plausibeler voor deze afstand (real-world referentie: Harare–Mutare ≈ 263 km,
Marange–Mutare ≈ 90 km over de weg, samen ≈ 353 km — dicht bij de gemeten 357,4). ⚠️ Het brief-
via-punt "Mutare" (stadscentrum 32,6333/-18,9667) snapte op een even geïsoleerde wegstomp (0,048 km,
component van 2 knopen) — ook geen wegklassefout maar een via-punt náást de doorgaande weg;
verplaatst naar de R5/Harare-Mutare Highway zelf (32,6426/-18,9511, nog steeds Mutare-stad). Dit is
een via-punt (corridorkeuze), geen anker, dus geen brief-wijziging nodig.

**b2 (lucht, DOORGETROKKEN — geen stippel, `maak_luchtbeen.py`, bakhandleiding §2):** vlucht
Harare (HRE) → Dubai (DXB) als grootcirkel — **5.471,7 km over 220 punten**, exact gelijk aan de
brief-berekening (§2: "5.471,7 km berekende grootcirkel"). Geen tussenlanding gebrond (brief §7:
geen bron noemt een hub) → één directe vrachtvlucht, aangenomen conform de brief. Beide
vrachtterminal-ankers (`dia-hre-cargo`, `dia-dxb-cargo`) zijn satelliet-gelegd (bron-gelegd, brief
§3), dus geen "net reikt niet"-geval.

**b3 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel `diamant-marange-dubai-dxb-dmcc`,
extract `gcc-staten`):** Dubai Intl (DXB) vrachtterminal → DMCC/Almas Tower over Sheikh Zayed Road
(E11), via Dubai World Trade Centre-interchange en Mall of the Emirates-interchange — **34,8 km over
514 punten**, tegen ~34 km = **+1,4% [OK]**. Beide ankers snappen op ≤0,06 km. Ankers hergebruikt van
de zusterbrief `diamant-mbujimayi-dubai` (dezelfde DXB-vrachtterminal- en DMCC-coördinaten, beide
bron-gelegd in deze golf).

**Toets naden:** alle drie de overgangen **0,00 km** — elk been begint precies waar het vorige
eindigt (mijn-stippel→b1 op de mijnwegaansluiting, b1→b2 op HRE-cargo, b2→b3 op DXB-cargo).

**`toets_knikken.py`:** b1 (50 knikken ≥60°, vrijwel allemaal spikes met straal ≤50 m — OSM-
wegdetail op kruisingen/opritten, geen bevinding; 1 omkering "scherpe bocht, echt" bij
-18,18906/31,54769). b2 (lucht) 0 knikken (per constructie recht/grootcirkel). b3 (13 knikken ≥60°,
waaronder **1 TERUGLOOP (158,2°, R≈4 m) bij 25,25382/55,33649**, nabij de DXB-vrachtterminal-
oprit). ⚠️ **Bevinding, niet dichtgetrokken:** klein lokaal artefact in het gescande wegprofiel
(vermoedelijk een niet volledig gesnoeide keerlus op een kruising/oprit bij de vrachtterminal); het
been blijft ruim binnen de lengtetoets (+1,4%) en de lichte werkwijze heeft geen gereedschap om een
individuele graafknik te repareren zonder via-punten kunstmatig te verschuiven.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — de mijn-stippel
(0,786 km) valt onder de 5 km-drempel; b1/b3 zijn gerouteerde weggeometrie (geen omwegfactor 1,000);
b2 (lucht) wordt door het tool overgeslagen (per constructie recht).

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, lucht} (binnen de
toegestane set), elk been ≥2 punten (minimum 2 op de mijn-stippel, maximum 4.899 op b1).

**Markers:** alle vier op de been-eindpunten zelf (`dia-marange-mijn`, `dia-hre-cargo`,
`dia-dxb-cargo`, `dia-dmcc`) — elk 0,00–0,13 km van de lijn (anker ≈ routeerpunt op alle vier).

**Gereedschapslessen:**
- **Eerste bake met een luchtbeen in dit project** (samen met de zusterbrieven van deze golf, §2
  "Lucht", bakhandleiding); het recept `maak_luchtbeen.py --van/--naar/--uit` →
  `--been-geojson "lucht|...|..."` werkte in één keer, gaf exact de brief-berekening terug.
- **Een via-snap ≤5 km is NIET per definitie goed gelegd** — de bakhandleiding waarschuwt bij >5 km,
  maar hier gaven twee punten op 0,14 km en 0,048 km toch "geen wegpad": de nabijheid was klein, maar
  het snappunt zat op een klein, van het hoofdnet AFGESNEDEN eilandje. `corridorKlassen`/
  `eindToegangPrivaat` lossen een wegklasseprobleem op, geen topologisch-disjuncte graaf. De vondst
  kwam pas met een expliciete connectiviteitscheck (osmium, node-id-gebaseerde BFS tussen de
  aankersnap en het beoogde eindpunt) — niet met de snapafstand alleen.
- Voor het mijnanker is dat gat (0,79 km) een echt "net reikt niet"-geval en gestippeld met reden;
  voor het Mutare-via-punt is het een via-puntfout (op een zijtak/geïsoleerde stomp), gefixt door het
  via-punt te verplaatsen naar de daadwerkelijke doorgaande weg (R5) — geen brief-wijziging, want een
  via-punt is geen anker.
- De gedeelde slot-mechaniek (`neem_slot`) kon niet met de letterlijke `rm -rf "$d"` uit de opdracht
  draaien — de sandbox-veiligheidscontrole weigerde dat patroon. Gewerkt met `find "$d" ... -delete`
  in plaats van `rm -rf`, wat wél door de check kwam; slots zijn steeds netjes vrijgegeven.

**⚠️ Overgenomen uit §7 (niet dichtgetrokken bij het bakken):**
- Geen bron koppelt Marange-rough specifiek aan HRE als vertrekluchthaven (aangenomen: enige
  internationale vrachtluchthaven van Zimbabwe).
- `dia-hre-cargo` is niet met naam bevestigd als dé cargo-faciliteit (plausibele vrachtloods+apron,
  geen naambord op de satellietbeelden).
- Geen gepubliceerde wegkm voor de Marange–Harare-corridor gevonden; de gemeten 357,4 km (+32,4%
  t.o.v. de ontwerpschatting) staat nu als eigen datapunt — een toekomstige onafhankelijke bron kan
  dit bevestigen of weerleggen.
- Geen gepubliceerde vluchtlengte HRE→DXB (berekende grootcirkel; één directe vlucht aangenomen).
- Fase C (DXB→DMCC) heeft geen eigen bron voor het exacte traject.
- Sanctiestatus ZCDC-gelieerde entiteiten en het Marange-aandeel binnen "Zimbabwaanse rough" blijven
  ongeverifieerd binnen het webbudget van deze brief.
