# Routebrief (licht) · uranium — Olympic Dam → Port Adelaide

**stroom-id:** `uranium-olympicdam-portadelaide` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** Uraanoxideconcentraat (yellowcake) van de Olympic Dam-mijn/metallurgische fabriek (BHP,
Roxby Downs, Zuid-Australië) per **truck** over de enige verharde doorgaande route (Stuart Highway →
Augusta/Princes Highway) naar Port Adelaide, Outer Harbor — stoppunt, geen bestemmingsland gedocumenteerd.
**Welke as van het verhaal:** *Australië (~9% van de wereldwinning), tot nu toe onvertegenwoordigd in v2.* BHP
(Olympic Dam EIS 2011): "all uranium oxide produced at Olympic Dam is exported" via Outer Harbor [1][2].
v1-checklist (`design/uranium.md`) noemt ≈5.000 tU/jaar (≈9% wereldwinning, WNA/USGS-indicatief, peiljaar
±2023/24) — geen recenter BHP-jaarcijfer gevonden binnen het webbudget.

## 1 · Ketenkaart
```
Olympic Dam-fabriek `u-olympicdam-plant` ──(b1 truck · Stuart Hwy → Augusta/Princes Hwy · ~700 km,
   aannemelijk: modaliteit/traject niet direct bevestigd voor UOC)──►
   Port Adelaide, Outer Harbor `u-portadelaide-outerharbor` ── stoppunt (geen bestemmingsland)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `u-olympicdam-plant` → `u-portadelaide-outerharbor` | Stuart Highway (Roxby Downs–Pimba–Port Augusta) → Augusta Highway/Princes Highway (Port Augusta–Adelaide) — enige verharde doorgaande route, aannemelijk: geen bron beschrijft het exacte traject of de modaliteit expliciet voor UOC | ~700 [webcheck, grootcirkel ~560 km × wegfactor] | maak_stroombeen_weg (extract australie) | nee — het hele tracé is gekarteerde hoofdweg; geen netgat |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-olympicdam-plant` | mijn / metallurgische fabriek (laadplek) | Olympic Dam Operations, BHP, Roxby Downs | -30.4400, 136.8731 | [3][4][sat] | bron-gelegd (z15 gezien: het volledige metallurgische complex — smelter/raffinaderij-gebouwen, tailingsdammen, de open pit ~1 km NW ervan; het Wikipedia-infoboxpunt bleek géén stads-/mijncentroïde maar de fabriek zelf) |
| `u-portadelaide-outerharbor` | overslag / losplek (stoppunt) | Outer Harbor container-/algemene-vrachtterminal, Port of Adelaide | -34.7694, 138.4920 | [5][6][sat] | aannemelijk (z15 gezien: reëel operationeel terminal met containerstapels, kranen en aangemeerd schip — géén havengebied-centroïde in open water; niet specifiek als BHP-koper/uranium-berth bevestigd — de eerdere claim "berths 18-20" bleek bij nameting Binnenhaven-berths voor meststof/schroot/staal/textiel/graan [8], dus verworpen) |

## 4 · Via-punten (junctiepunten op de enige doorgaande route — geen alternatieve corridor)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Pimba — kruising Olympic Dam Highway × Stuart Highway | -31.1756, 136.8264 | hier draait de route van de mijn-toegangsweg de Stuart Highway op (zuidwaarts); zonder dit punt kan de scanner een kortere maar niet-verharde binnendoor-route kiezen |
| b1 | 2 | Port Augusta — kruising Stuart Highway × Augusta Highway | -32.4925, 137.7663 | hier verlaat de route de Stuart Highway (die verder naar Adelaide via een andere, langere kustweg loopt) en gaat de Augusta Highway op naar het zuiden |
| b1 | 3 | Port Wakefield — overgang Augusta Highway → Princes Highway/Port Wakefield Road | -34.1936, 138.1497 | wegnummer- en naamwissel op hetzelfde doorgaande tracé richting Adelaide/Port Adelaide |

⚠️ Coördinaten van de drie via-punten zijn **algemene-kennis-schattingen van de plaatsnaam** (geen aparte bron
per punt binnen het webbudget geraadpleegd — de Wikipedia-coördinaten-API gaf tijdens dit werk herhaaldelijk
429's, gedeeld sessiebudget); de wegscanner snapt ze zelf op de dichtstbijzijnde doorgaande rijbaan. Snap > 5 km
op een van deze drie is een signaal om de coördinaat na te kijken vóór het getal te geloven (bakhandleiding §2/§6).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Olympic Dam-fabriek (Roxby Downs) | BHP | uraanerts (bijproduct van koper) → uraanoxideconcentraat (drums/containers) | ≈5.000 tU/jaar (WNA/USGS-indicatief, peiljaar ±2023/24, v1-checklist `design/uranium.md`) — geen recenter BHP-cijfer binnen het webbudget | [1][10] |

## 6 · Stoppunt
De brief stopt bij Port Adelaide/Outer Harbor (bindende keuze uit de haalbaarheidstoets, zoals
uranium-rossing-walvisbay): BHP noemt geen klanten of bestemmingslanden per zending — alleen "exported" — dus
elk zeebeen zou op een verzonnen loshaven landen. Geen fase B getekend.

## 7 · Open punten
- **Modaliteit is een aanname, niet hard bevestigd.** Wikipedia noemt alleen "exported through Port Adelaide"
  (modus niet genoemd) [3]. mining-technology.com bevestigt truck voor **koperkathodes**, maar zwijgt over
  uraniumoxide [4]. Een BHP-EIS-verwijzing (chapter-22-traffic.pdf, 403, alleen via het zoekresultaat geciteerd)
  beschrijft een bestaand "single daily general freight train" dat terugkeert met "copper cathodes and uranium
  oxide concentrate" — mogelijk (deels) spoor via de bestaande aansluiting Pimba/Manguri op de Tarcoola–
  Adelaide-lijn. Een ouder ABC-artikel (2004) bevestigt dat spoor toen een VOORSTEL was t.o.v. de toenmalige
  truck-praktijk [6], niets over nu. **Vóór het bakken:** bevestigt een gerichte bronronde spoor voor UOC, dan
  splitst b1 bij Pimba/Manguri in spoor (`toets_spoorroute.mjs`, `BAKE_SUFFIX=-raw`) + truck-restant — de
  `australie`-extract dekt beide, dit is een gereedschapskeuze, geen blokkade (haalbaarheidstoets, bindend).
- **Geen enkele gepubliceerde km-waarde voor dit specifieke traject** — ~700 km is een webcheck-schatting
  (grootcirkel ~560 km × gebruikelijke wegfactor voor Australische binnenlandroutes), geen citaat-bron. De
  via-puntcoördinaten zijn eveneens ongeverifieerde schattingen (zie §4). Bake-toets bepaalt de echte
  wegafstand en of ±15% wordt gehaald.
- **Welke terminal binnen Outer Harbor BHP werkelijk gebruikt is niet aanwijsbaar** — geen BHP-bron noemt een
  berthnummer; de eerder gecirculeerde claim "berths 18-20" bleek bij nameting onjuist (Binnenhaven, meststof/
  schroot/staal/textiel/graan) [8]. Het gelegde anker is de enige substantiële vracht-/containerterminal in het
  directe Outer Harbor-gebied; status blijft **aannemelijk**, niet bron-gelegd.
- **Geen gepubliceerde bestemmingslanden per zending** (net als uranium-rossing-walvisbay) — de keten stopt
  bindend bij de haven.
- **Haven-aanloop niet van toepassing**, want er is geen zeebeen getekend. Mocht een latere fase alsnog een
  zeebeen toevoegen: Outer Harbor ligt 16,6 km van de dichtstbijzijnde MARNET-zeeknoop (knoop 6042,
  -34.9107/138.4332) — >5 km, dus een haven-aanloop zou dan verplicht zijn (LAR-586, ook al valt het binnen de
  25 km) — overgenomen uit de haalbaarheidstoets, niet zelf herrekend.

## 8 · Bronnen
[1] BHP, Olympic Dam Expansion Draft EIS 2009, Chapter 26 "Radiation" (via de haalbaarheidstoets/ketenontwerp-
bronnenlijst) — "all uranium oxide produced at Olympic Dam is exported" via Port Adelaide/Outer Harbor.
https://www.bhp.com/-/media/bhp/regulatory-information-media/copper/olympic-dam/0000/supplementary-eis-main-report/chapter-26-radiation.pdf
[2] BHP, Olympic Dam Draft EIS 2009, Chapter 2 "Existing Operation" — beschrijft de geïntegreerde metallurgische
fabriek (concentrator, hydromet, smelter, raffinaderij); niet direct opvraagbaar (403 op WebFetch, zelfde
patroon als de traffic-PDF).
https://www.bhp.com/-/media/bhp/regulatory-information-media/copper/olympic-dam/0000/draft-eis-main-report/odxeischapter2existingoperation.pdf
[3] Wikipedia, "Olympic Dam mine" — coördinaat 30°26′24″S 136°52′23″E (=-30.4400,136.8731), "the copper and
uranium oxide are exported through Port Adelaide" (modus niet genoemd). https://en.wikipedia.org/wiki/Olympic_Dam_mine
[4] mining-technology.com, "Olympic Dam Copper-Uranium Mine, Adelaide, Australia" — "Copper cathode sheets are
transported by truck within Australia and to Port Adelaide for export" (uranium niet expliciet genoemd);
integrale fabrieksbeschrijving (concentrator, hydromet, smelter, sulfuurzuurfabriek, raffinaderijen).
https://www.mining-technology.com/projects/olympic-dam/
[5] Wikipedia, "Outer Harbor, South Australia" — plaatscoördinaat (suburb-centroïde, niet als anker gebruikt).
https://en.wikipedia.org/wiki/Outer_Harbor,_South_Australia
[6] ABC News, 2004-12-08, "Olympic Dam plans prompt uranium transport fears" — bevestigt dat omschakeling naar
spoor via de Adelaide–Darwin-lijn destijds een VOORSTEL was t.o.v. de toenmalige (truck-)praktijk.
https://www.abc.net.au/news/2004-12-08/olympic-dam-plans-prompt-uranium-transport-fears
[7] Friends of the Earth Adelaide, "Uranium oxide accident at Outer Harbor" — bevestigt dat yellowcake per
truck van Olympic Dam naar de dokken bij Outer Harbor gaat en daar per container wordt overgeslagen; geen
specifiek berth genoemd. https://adelaidefoe.org/uranium-oxide-accident-at-outer-harbor/
[8] Flinders Port Holdings, "Port Adelaide" — berth-overzicht Binnenhaven (ADL IH 18/19/20: meststof, schroot,
staal, textiel, graan; berth 29: mineraalzand/vee/zwavel/meststof) — weerlegt de eerdere "berths 18-20 = koper/
uranium"-claim. https://www.flindersportholdings.com.au/port-adelaide/
[9] OpenStreetMap via Nominatim/Photon — "Port of Adelaide" industrieel landgebruik-vlak, centroïde
-34.7694,138.4920 (gebruikt als anker, satelliet-bevestigd als reëel terminal, geen aparte OSM-bronclaim voor
BHP-specifieke berth).
[10] v1-checklist, `design/uranium.md` — Australië ≈9% van de wereldwinning (WNA/USGS-indicatief), niet apart
herbevestigd binnen het webbudget.
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15) —
`v2/build-cache/satcheck/sat-uranium-olympicdam-portadelaide-mine-wiki.png`,
`v2/build-cache/satcheck/sat-uranium-olympicdam-portadelaide-outerharbor.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Bestand:** `v2/data/stroomroute-uranium-olympicdam-portadelaide.json` · 81,9 KB · 1 been · 581,9 km · 3.815
punten · 2 markers. Recept: `v2/tools/bak_stromen.sh` functie `bak_uranium_olympicdam_portadelaide()`,
geometrie uit `v2/tools/maak_stroombeen_weg.py` profiel `uranium-olympicdam-portadelaide` (extract
`australie`, `--bron geofabrik`).

| # | modaliteit | km | naad | markers ≤ lijn |
|---|---|---|---|---|
| b1 | truck | 581,9 | 0,00 km (eerste been) | beide op 0,0 m (anker = routeerpunt) |

**Vóór het bakken gecheckt (webbudget):** een BHP-EIS-vondst over een dagelijkse vrachttrein met "copper
cathodes and uranium oxide concentrate" (chapter-22-traffic.pdf) bleek bij een gerichte zoekronde te horen
bij de **nooit gebouwde Olympic Dam Expansion** (2009-2011 EIS, spoorvoorstel Pimba→Olympic Dam met 14
treinen/week, geschrapt sinds 2012) — geen bron bevestigt spoor als de huidige praktijk. Friends of the
Earth Adelaide bevestigt onafhankelijk truckvervoer (brief §7[7]) voor de bestaande situatie. Conclusie:
géén spoorsplitsing, het hele been b1 is truck, zoals de bak-aanwijzing bij een niet-bevestigde bron
voorschreef.

**Modaliteit-/wegkeuze bij het bakken:**
- Het profiel snapte in eerste instantie niet: `eindToegangPrivaat: True` was nodig, want zowel de
  Olympic Dam-fabriekstoegangsweg als de wegen binnen Outer Harbor dragen `access=private` in OSM — zonder
  die vlag stonden beide ankers op een geïsoleerd wegfragment (2 resp. 24 knopen, geen pad naar het
  hoofdnet). `corridorKlassen: ["tertiary", "unclassified"]` was daarnaast nodig omdat Olympic Dam Highway
  (B97) over delen van zijn traject als `secondary`/`unclassified` gekarteerd staat, niet alleen `primary`.
- Geen via-punt snapte > 5 km (max 0,98 km bij Pimba); geen reden om `vensterKm` naar 75 te verruimen.
- `snoei_keerlussen` haalde 6 dubbel-gereden stukjes weg (584,2 → 581,8 km geometrie vóór afronding), o.a.
  bij Port Augusta en Port Wakefield — normale kruispuntartefacten, geen route-fout.

**Toelichting stippels:** geen. Het hele been is doorgetrokken gekarteerde hoofdweg, zoals de brief
voorschreef (b1 stippel = nee).

**Toelichting haven-aanloop:** niet van toepassing — geen zeebeen getekend (stoppunt bij de haven, zoals
uranium-rossing-walvisbay). Outer Harbor ligt weliswaar 16,6 km van zijn MARNET-zeeknoop (>5 km, LAR-586
zou een haven-aanloop verplichten zodra een zeebeen wordt toegevoegd), maar dat blijft theoretisch zolang
er geen bestemmingsland gedocumenteerd is (brief §7).

**Toets:** km binnen ±15% → **NEE**, 581,9 km tegen de brief-schatting ~700 km = **-16,9%**, buiten de norm.
Blijft staan als bevinding, niet dichtgetrokken: de brief zelf noemt de 700 km-referentiewaarde een zwakke
webcheck-schatting (grootcirkel × wegfactor, geen citaat-bron) en waarschuwt expliciet "geloof de
±15%-toets niet blind" (bak_aanwijzingen). Het gemeten getal (581,9 km, geroutet over de enige verharde
doorgaande corridor) is de sterkere waarde. Geen naad > 5 km (enig been). 0 omkeringen/terugloop
(`toets_knikken.py`: 19 knikken ≥60°, allemaal kruispunt-spikes met kleine boogstralen, 0 omkeringen ≥150°).
`toets_rechte_benen.py --min-km 5`: geen been gemeld (geen verdacht rechte lijn). Beide markers op 0,0 m
van de lijn. `json.load` slaagt, versie 2, punt_formaat lonlat, modaliteit `truck` ∈ toegestane set,
been ≥ 2 punten (3.815), bestandsgrootte 81,9 KB.

**Gereedschapslessen:**
- `eindToegangPrivaat: True` is niet alleen een Codelco-achtig mijnpoort-patroon: een reguliere
  havenoperator-terminal (Outer Harbor) kan dezelfde `access=private`-kartering dragen op zijn interne
  wegen. Bij een geïsoleerde snap (component van een paar knopen) eerst de wegklasse/access nakijken vóór
  je `vensterKm` ophoogt — hier zou een groter venster niets hebben opgelost, want het probleem was een
  filter, geen afstand.
- Diagnose van "geen wegpad tussen punt i en i+1" met een losse debug-replica van `_kies_profiel` +
  `_wegen_graaf`/`_dichtste_knoop`/component-BFS was sneller dan gokken met profielvlaggen: binnen twee
  Python-oproepen bleek de plant op een 2-knopencomponent te snappen en Outer Harbor op een 24-knopencomponent,
  beide losgekoppeld van het 493.759-knopen-hoofdnet.
